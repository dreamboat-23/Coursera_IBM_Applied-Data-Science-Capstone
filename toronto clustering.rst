
Data Wrangling
==============

The data was downloaded onto an excel table. I imported the excel table
to IBM Watson and I downloaded the required libraries to start cleaning
up the data.

.. code:: ipython3

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

.. code:: ipython3

    
    import types
    import pandas as pd
    from botocore.client import Config
    import ibm_boto3
    
    def __iter__(self): return 0
    
    # @hidden_cell
    
    client_24156fed339f42bba9c0707239ed37c4 = ibm_boto3.client(service_name='s3',
        ibm_api_key_id='kx0Kit5kvbbzMjIJ2fKCiKjjMt-ZRMIDeOTex9ANAgqX',
        ibm_auth_endpoint="https://iam.ng.bluemix.net/oidc/token",
        config=Config(signature_version='oauth'),
        endpoint_url='https://s3-api.us-geo.objectstorage.service.networklayer.com')
    
    body = client_24156fed339f42bba9c0707239ed37c4.get_object(Bucket='ibmcourseraapplieddatasciencecaps-donotdelete-pr-xgokqdp8xydy3q',Key='Canada neighborhood data (1).xlsx')['Body']
    # add missing __iter__ method, so pandas accepts body as file-like object
    if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )
    
    df = pd.read_excel(body)
    df.head()





.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Postcode</th>
          <th>Borough</th>
          <th>Neighbourhood</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>M1A</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>1</th>
          <td>M2A</td>
          <td>NaN</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>2</th>
          <td>M3A</td>
          <td>North York</td>
          <td>Parkwoods</td>
        </tr>
        <tr>
          <th>3</th>
          <td>M4A</td>
          <td>North York</td>
          <td>Victoria Village</td>
        </tr>
        <tr>
          <th>4</th>
          <td>M5A</td>
          <td>Downtown Toronto</td>
          <td>Harbourfront</td>
        </tr>
      </tbody>
    </table>
    </div>



Let us examine the missing data

.. code:: ipython3

    missing_data = df.isnull()
    missing_data.head(3)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Postcode</th>
          <th>Borough</th>
          <th>Neighbourhood</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>False</td>
          <td>True</td>
          <td>True</td>
        </tr>
        <tr>
          <th>1</th>
          <td>False</td>
          <td>True</td>
          <td>True</td>
        </tr>
        <tr>
          <th>2</th>
          <td>False</td>
          <td>False</td>
          <td>False</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    for column in missing_data.columns.values.tolist():
        print(column)
        print (missing_data[column].value_counts())
        print("")


.. parsed-literal::

    Postcode
    False    288
    Name: Postcode, dtype: int64
    
    Borough
    False    211
    True      77
    Name: Borough, dtype: int64
    
    Neighbourhood
    False    210
    True      78
    Name: Neighbourhood, dtype: int64
    


As we can see, there are 77 true values, indicating missing data, and
per prompt requirement, these will be dropped from the Borough column

.. code:: ipython3

    df.dropna(subset=["Borough"], axis=0, inplace=True)
    
    #reset the index
    
    df.reset_index(drop=True, inplace=True)
    
    df.head(12)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Postcode</th>
          <th>Borough</th>
          <th>Neighbourhood</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>M3A</td>
          <td>North York</td>
          <td>Parkwoods</td>
        </tr>
        <tr>
          <th>1</th>
          <td>M4A</td>
          <td>North York</td>
          <td>Victoria Village</td>
        </tr>
        <tr>
          <th>2</th>
          <td>M5A</td>
          <td>Downtown Toronto</td>
          <td>Harbourfront</td>
        </tr>
        <tr>
          <th>3</th>
          <td>M5A</td>
          <td>Downtown Toronto</td>
          <td>Regent Park</td>
        </tr>
        <tr>
          <th>4</th>
          <td>M6A</td>
          <td>North York</td>
          <td>Lawrence Heights</td>
        </tr>
        <tr>
          <th>5</th>
          <td>M6A</td>
          <td>North York</td>
          <td>Lawrence Manor</td>
        </tr>
        <tr>
          <th>6</th>
          <td>M7A</td>
          <td>Queen's Park</td>
          <td>NaN</td>
        </tr>
        <tr>
          <th>7</th>
          <td>M9A</td>
          <td>Etobicoke</td>
          <td>Islington Avenue</td>
        </tr>
        <tr>
          <th>8</th>
          <td>M1B</td>
          <td>Scarborough</td>
          <td>Rouge</td>
        </tr>
        <tr>
          <th>9</th>
          <td>M1B</td>
          <td>Scarborough</td>
          <td>Malvern</td>
        </tr>
        <tr>
          <th>10</th>
          <td>M3B</td>
          <td>North York</td>
          <td>Don Mills North</td>
        </tr>
        <tr>
          <th>11</th>
          <td>M4B</td>
          <td>East York</td>
          <td>Woodbine Gardens</td>
        </tr>
      </tbody>
    </table>
    </div>



We then assign missing neighborhoods to name of corresponding borough

.. code:: ipython3

    df['Neighbourhood'].replace(np.nan, df['Borough'], inplace=True)
    df.head(12)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Postcode</th>
          <th>Borough</th>
          <th>Neighbourhood</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>M3A</td>
          <td>North York</td>
          <td>Parkwoods</td>
        </tr>
        <tr>
          <th>1</th>
          <td>M4A</td>
          <td>North York</td>
          <td>Victoria Village</td>
        </tr>
        <tr>
          <th>2</th>
          <td>M5A</td>
          <td>Downtown Toronto</td>
          <td>Harbourfront</td>
        </tr>
        <tr>
          <th>3</th>
          <td>M5A</td>
          <td>Downtown Toronto</td>
          <td>Regent Park</td>
        </tr>
        <tr>
          <th>4</th>
          <td>M6A</td>
          <td>North York</td>
          <td>Lawrence Heights</td>
        </tr>
        <tr>
          <th>5</th>
          <td>M6A</td>
          <td>North York</td>
          <td>Lawrence Manor</td>
        </tr>
        <tr>
          <th>6</th>
          <td>M7A</td>
          <td>Queen's Park</td>
          <td>Queen's Park</td>
        </tr>
        <tr>
          <th>7</th>
          <td>M9A</td>
          <td>Etobicoke</td>
          <td>Islington Avenue</td>
        </tr>
        <tr>
          <th>8</th>
          <td>M1B</td>
          <td>Scarborough</td>
          <td>Rouge</td>
        </tr>
        <tr>
          <th>9</th>
          <td>M1B</td>
          <td>Scarborough</td>
          <td>Malvern</td>
        </tr>
        <tr>
          <th>10</th>
          <td>M3B</td>
          <td>North York</td>
          <td>Don Mills North</td>
        </tr>
        <tr>
          <th>11</th>
          <td>M4B</td>
          <td>East York</td>
          <td>Woodbine Gardens</td>
        </tr>
      </tbody>
    </table>
    </div>



Then concatenate by Postcode

.. code:: ipython3

    df_1= df.groupby('Postcode').agg(lambda x: ','.join(x))

.. code:: ipython3

    df_2=df_1.reset_index()

Within each Borough, there are multiple Postcodes and so we clean up the
data frame to remove any repeats, so that each line has only one
Postcode, one Borough, and all the Neighborhoods in that Borough and
Postcode.

.. code:: ipython3

    df_2['Borough']= df_2['Borough'].str.replace('[{}\s]','').str.split(',').apply(set).str.join(',').str.strip(',').str.replace(",{2,}",",")

.. code:: ipython3

    df_2.head(12)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Postcode</th>
          <th>Borough</th>
          <th>Neighbourhood</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>M1B</td>
          <td>Scarborough</td>
          <td>Rouge,Malvern</td>
        </tr>
        <tr>
          <th>1</th>
          <td>M1C</td>
          <td>Scarborough</td>
          <td>Highland Creek,Rouge Hill,Port Union</td>
        </tr>
        <tr>
          <th>2</th>
          <td>M1E</td>
          <td>Scarborough</td>
          <td>Guildwood,Morningside,West Hill</td>
        </tr>
        <tr>
          <th>3</th>
          <td>M1G</td>
          <td>Scarborough</td>
          <td>Woburn</td>
        </tr>
        <tr>
          <th>4</th>
          <td>M1H</td>
          <td>Scarborough</td>
          <td>Cedarbrae</td>
        </tr>
        <tr>
          <th>5</th>
          <td>M1J</td>
          <td>Scarborough</td>
          <td>Scarborough Village</td>
        </tr>
        <tr>
          <th>6</th>
          <td>M1K</td>
          <td>Scarborough</td>
          <td>East Birchmount Park,Ionview,Kennedy Park</td>
        </tr>
        <tr>
          <th>7</th>
          <td>M1L</td>
          <td>Scarborough</td>
          <td>Clairlea,Golden Mile,Oakridge</td>
        </tr>
        <tr>
          <th>8</th>
          <td>M1M</td>
          <td>Scarborough</td>
          <td>Cliffcrest,Cliffside,Scarborough Village West</td>
        </tr>
        <tr>
          <th>9</th>
          <td>M1N</td>
          <td>Scarborough</td>
          <td>Birch Cliff,Cliffside West</td>
        </tr>
        <tr>
          <th>10</th>
          <td>M1P</td>
          <td>Scarborough</td>
          <td>Dorset Park,Scarborough Town Centre,Wexford He...</td>
        </tr>
        <tr>
          <th>11</th>
          <td>M1R</td>
          <td>Scarborough</td>
          <td>Maryvale,Wexford</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    df_2.shape




.. parsed-literal::

    (103, 3)



The data frame has 3 rows and 103 columns

Geocoding
=========

Using the CSV data to merge it to the cleaned table from the previous
section. First examine what the data frame looks like

.. code:: ipython3

    filepath = "https://cocl.us/Geospatial_data"
    df_3 = pd.read_csv('https://cocl.us/Geospatial_data')
    df_3.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Postal Code</th>
          <th>Latitude</th>
          <th>Longitude</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>M1B</td>
          <td>43.806686</td>
          <td>-79.194353</td>
        </tr>
        <tr>
          <th>1</th>
          <td>M1C</td>
          <td>43.784535</td>
          <td>-79.160497</td>
        </tr>
        <tr>
          <th>2</th>
          <td>M1E</td>
          <td>43.763573</td>
          <td>-79.188711</td>
        </tr>
        <tr>
          <th>3</th>
          <td>M1G</td>
          <td>43.770992</td>
          <td>-79.216917</td>
        </tr>
        <tr>
          <th>4</th>
          <td>M1H</td>
          <td>43.773136</td>
          <td>-79.239476</td>
        </tr>
      </tbody>
    </table>
    </div>



Rename the field "Postal Code" to Postcode to match the previous
section, and merge the two data sets to get the required data frame.

.. code:: ipython3

    df_3.rename(columns={'Postal Code': 'Postcode'}, inplace=True)
    df_4 = pd.merge(df_3, df_2, how='inner', on=None, left_on=None, right_on=None,
             left_index=False, right_index=False, sort=True,
             suffixes=('_x', '_y'), copy=True, indicator=False,
             validate=None)
    
    df_4.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Postcode</th>
          <th>Latitude</th>
          <th>Longitude</th>
          <th>Borough</th>
          <th>Neighbourhood</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>M1B</td>
          <td>43.806686</td>
          <td>-79.194353</td>
          <td>Scarborough</td>
          <td>Rouge,Malvern</td>
        </tr>
        <tr>
          <th>1</th>
          <td>M1C</td>
          <td>43.784535</td>
          <td>-79.160497</td>
          <td>Scarborough</td>
          <td>Highland Creek,Rouge Hill,Port Union</td>
        </tr>
        <tr>
          <th>2</th>
          <td>M1E</td>
          <td>43.763573</td>
          <td>-79.188711</td>
          <td>Scarborough</td>
          <td>Guildwood,Morningside,West Hill</td>
        </tr>
        <tr>
          <th>3</th>
          <td>M1G</td>
          <td>43.770992</td>
          <td>-79.216917</td>
          <td>Scarborough</td>
          <td>Woburn</td>
        </tr>
        <tr>
          <th>4</th>
          <td>M1H</td>
          <td>43.773136</td>
          <td>-79.239476</td>
          <td>Scarborough</td>
          <td>Cedarbrae</td>
        </tr>
      </tbody>
    </table>
    </div>



Then we fix the column order to have Latitude and Longitude as the last
two columns, then assign them to the data frame.

.. code:: ipython3

    column_order = ['Postcode',
     'Borough',
     'Neighbourhood',
     'Latitude',
     'Longitude']
    df_5=df_4[column_order]
    df_5.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Postcode</th>
          <th>Borough</th>
          <th>Neighbourhood</th>
          <th>Latitude</th>
          <th>Longitude</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>M1B</td>
          <td>Scarborough</td>
          <td>Rouge,Malvern</td>
          <td>43.806686</td>
          <td>-79.194353</td>
        </tr>
        <tr>
          <th>1</th>
          <td>M1C</td>
          <td>Scarborough</td>
          <td>Highland Creek,Rouge Hill,Port Union</td>
          <td>43.784535</td>
          <td>-79.160497</td>
        </tr>
        <tr>
          <th>2</th>
          <td>M1E</td>
          <td>Scarborough</td>
          <td>Guildwood,Morningside,West Hill</td>
          <td>43.763573</td>
          <td>-79.188711</td>
        </tr>
        <tr>
          <th>3</th>
          <td>M1G</td>
          <td>Scarborough</td>
          <td>Woburn</td>
          <td>43.770992</td>
          <td>-79.216917</td>
        </tr>
        <tr>
          <th>4</th>
          <td>M1H</td>
          <td>Scarborough</td>
          <td>Cedarbrae</td>
          <td>43.773136</td>
          <td>-79.239476</td>
        </tr>
      </tbody>
    </table>
    </div>



Visualization and Clustering
============================

First we import some required libraries

.. code:: ipython3

    !conda install -c conda-forge geopy --yes
    from geopy.geocoders import Nominatim
    import requests
    import matplotlib.cm as cm
    import matplotlib.colors as colors
    from sklearn.cluster import KMeans
    !conda install -c conda-forge folium=0.5.0 --yes
    import folium
    print('Libraries imported.')


.. parsed-literal::

    Solving environment: done
    
    ## Package Plan ##
    
      environment location: /opt/conda/envs/Python36
    
      added / updated specs: 
        - geopy
    
    
    The following packages will be downloaded:
    
        package                    |            build
        ---------------------------|-----------------
        certifi-2019.9.11          |           py36_0         147 KB  conda-forge
        openssl-1.1.1c             |       h516909a_0         2.1 MB  conda-forge
        geopy-1.20.0               |             py_0          57 KB  conda-forge
        ca-certificates-2019.9.11  |       hecc5488_0         144 KB  conda-forge
        geographiclib-1.50         |             py_0          34 KB  conda-forge
        ------------------------------------------------------------
                                               Total:         2.5 MB
    
    The following NEW packages will be INSTALLED:
    
        geographiclib:   1.50-py_0         conda-forge
        geopy:           1.20.0-py_0       conda-forge
    
    The following packages will be UPDATED:
    
        ca-certificates: 2019.8.28-0                   --> 2019.9.11-hecc5488_0 conda-forge
        certifi:         2019.9.11-py36_0              --> 2019.9.11-py36_0     conda-forge
    
    The following packages will be DOWNGRADED:
    
        openssl:         1.1.1d-h7b6447c_2             --> 1.1.1c-h516909a_0    conda-forge
    
    
    Downloading and Extracting Packages
    certifi-2019.9.11    | 147 KB    | ##################################### | 100% 
    openssl-1.1.1c       | 2.1 MB    | ##################################### | 100% 
    geopy-1.20.0         | 57 KB     | ##################################### | 100% 
    ca-certificates-2019 | 144 KB    | ##################################### | 100% 
    geographiclib-1.50   | 34 KB     | ##################################### | 100% 
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    Solving environment: done
    
    ## Package Plan ##
    
      environment location: /opt/conda/envs/Python36
    
      added / updated specs: 
        - folium=0.5.0
    
    
    The following packages will be downloaded:
    
        package                    |            build
        ---------------------------|-----------------
        folium-0.5.0               |             py_0          45 KB  conda-forge
        vincent-0.4.4              |             py_1          28 KB  conda-forge
        altair-3.2.0               |           py36_0         770 KB  conda-forge
        branca-0.3.1               |             py_0          25 KB  conda-forge
        ------------------------------------------------------------
                                               Total:         868 KB
    
    The following NEW packages will be INSTALLED:
    
        altair:  3.2.0-py36_0 conda-forge
        branca:  0.3.1-py_0   conda-forge
        folium:  0.5.0-py_0   conda-forge
        vincent: 0.4.4-py_1   conda-forge
    
    
    Downloading and Extracting Packages
    folium-0.5.0         | 45 KB     | ##################################### | 100% 
    vincent-0.4.4        | 28 KB     | ##################################### | 100% 
    altair-3.2.0         | 770 KB    | ##################################### | 100% 
    branca-0.3.1         | 25 KB     | ##################################### | 100% 
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    Libraries imported.


Then we look for the coordinates of Toronto

.. code:: ipython3

    address = 'Toronto, Ontario'
    
    geolocator = Nominatim(user_agent="TO_explorer")
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    print('The geograpical coordinate of Toronto, Ontario are {}, {}.'.format(latitude, longitude))


.. parsed-literal::

    The geograpical coordinate of Toronto, Ontario are 43.653963, -79.387207.


Now we show the map of Toronto with the neighborhoods as markers

.. code:: ipython3

    map_toronto = folium.Map(location=[latitude, longitude], zoom_start=10)
    
    for lat, lng, borough, neighbourhood in zip(df_5['Latitude'], df_5['Longitude'], df_5['Borough'], df_5['Neighbourhood']):
        label = '{}, {}'.format(neighbourhood, borough)
        label = folium.Popup(label, parse_html=True)
        folium.CircleMarker(
            [lat, lng],
            radius=6,
            popup=label,
            color='magenta',
            fill=True,
            fill_color='#3186cc',
            fill_opacity=0.7,
            parse_html=False).add_to(map_toronto)  
        
    map_toronto




.. raw:: html

    <div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYycsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDMuNjUzOTYzLC03OS4zODcyMDddLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTAsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzc0ZWIzOTliNTFkMTQxOWU4M2Q1YzdkYWE5MjM5ZjhiID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICJtYXhab29tIjogMTgsCiAgIm1pblpvb20iOiAxLAogICJub1dyYXAiOiBmYWxzZSwKICAic3ViZG9tYWlucyI6ICJhYmMiCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNjU0Y2Y5ODVjZjg0M2NkODU1MmZjMjE3ODQ1NDdmMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjgwNjY4NjI5OTk5OTk5NiwtNzkuMTk0MzUzNDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjBkZWI4YWJjMzExNGNhNDllNjg3MDdiODEzMzE1OGMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjZiMzZhODRmZGU2NDEyZDlkYTliOTFiOGVhOWQ3M2UgPSAkKCc8ZGl2IGlkPSJodG1sXzY2YjM2YTg0ZmRlNjQxMmQ5ZGE5YjkxYjhlYTlkNzNlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3VnZSxNYWx2ZXJuLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjBkZWI4YWJjMzExNGNhNDllNjg3MDdiODEzMzE1OGMuc2V0Q29udGVudChodG1sXzY2YjM2YTg0ZmRlNjQxMmQ5ZGE5YjkxYjhlYTlkNzNlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q2NTRjZjk4NWNmODQzY2Q4NTUyZmMyMTc4NDU0N2YxLmJpbmRQb3B1cChwb3B1cF8yMGRlYjhhYmMzMTE0Y2E0OWU2ODcwN2I4MTMzMTU4Yyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xYzA4ZGY2MDE2MmU0NTZlOTE3OGI2NDU2MzVlYmQ4NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4NDUzNTEsLTc5LjE2MDQ5NzA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRlNWFjZjllMDJlYzRkYWJhYTBmN2IzYjAzYTlkNWQ4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2QwNjhjNGZiMDcwMzRhYjZhMmNjNzZiODdiZjU0YTU4ID0gJCgnPGRpdiBpZD0iaHRtbF9kMDY4YzRmYjA3MDM0YWI2YTJjYzc2Yjg3YmY1NGE1OCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaGxhbmQgQ3JlZWssUm91Z2UgSGlsbCxQb3J0IFVuaW9uLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNGU1YWNmOWUwMmVjNGRhYmFhMGY3YjNiMDNhOWQ1ZDguc2V0Q29udGVudChodG1sX2QwNjhjNGZiMDcwMzRhYjZhMmNjNzZiODdiZjU0YTU4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFjMDhkZjYwMTYyZTQ1NmU5MTc4YjY0NTYzNWViZDg0LmJpbmRQb3B1cChwb3B1cF80ZTVhY2Y5ZTAyZWM0ZGFiYWEwZjdiM2IwM2E5ZDVkOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85ODQ0NGJkOTVkYjk0Yzk1YTdmNDRjNzg0NzczYTFkMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc2MzU3MjYsLTc5LjE4ODcxMTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjQxNTQ5ZDRhYzYwNDg0OWJiZTFiNTMxMTQ5Yjg4ZjEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDE2MGQ4MTE4YTMwNDc2Y2I4ZWE5NjQ1NTA1MjZkNjMgPSAkKCc8ZGl2IGlkPSJodG1sX2QxNjBkODExOGEzMDQ3NmNiOGVhOTY0NTUwNTI2ZDYzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HdWlsZHdvb2QsTW9ybmluZ3NpZGUsV2VzdCBIaWxsLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjQxNTQ5ZDRhYzYwNDg0OWJiZTFiNTMxMTQ5Yjg4ZjEuc2V0Q29udGVudChodG1sX2QxNjBkODExOGEzMDQ3NmNiOGVhOTY0NTUwNTI2ZDYzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk4NDQ0YmQ5NWRiOTRjOTVhN2Y0NGM3ODQ3NzNhMWQxLmJpbmRQb3B1cChwb3B1cF9mNDE1NDlkNGFjNjA0ODQ5YmJlMWI1MzExNDliODhmMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hMjUxODg5OWMzZDg0ODI4YmZjZTg5MzFjMzYzODA0OSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MDk5MjEsLTc5LjIxNjkxNzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzkwYTc4ZmI3NjQzMDQzNzY4NDQ4NGRkYTI3Y2RjZTU2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzEwZTEyMWM2ZTE3NjRlNzY4ZWIyYWNkNTUzY2NjNTNmID0gJCgnPGRpdiBpZD0iaHRtbF8xMGUxMjFjNmUxNzY0ZTc2OGViMmFjZDU1M2NjYzUzZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V29idXJuLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTBhNzhmYjc2NDMwNDM3Njg0NDg0ZGRhMjdjZGNlNTYuc2V0Q29udGVudChodG1sXzEwZTEyMWM2ZTE3NjRlNzY4ZWIyYWNkNTUzY2NjNTNmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2EyNTE4ODk5YzNkODQ4MjhiZmNlODkzMWMzNjM4MDQ5LmJpbmRQb3B1cChwb3B1cF85MGE3OGZiNzY0MzA0Mzc2ODQ0ODRkZGEyN2NkY2U1Nik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83MWVmMzkzOGIxMmI0M2FkYWRmOGMyZTk2Y2VlMDNhZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MzEzNiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjE1OWU2NGViYzRiNDVkNjkyOTVlZDUzNTFlZGRiOTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGZkZWIzYTNiMTdkNDhkZTkwOGQwYzgzNGI4NDY3MjcgPSAkKCc8ZGl2IGlkPSJodG1sXzRmZGViM2EzYjE3ZDQ4ZGU5MDhkMGM4MzRiODQ2NzI3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZWRhcmJyYWUsIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82MTU5ZTY0ZWJjNGI0NWQ2OTI5NWVkNTM1MWVkZGI5Mi5zZXRDb250ZW50KGh0bWxfNGZkZWIzYTNiMTdkNDhkZTkwOGQwYzgzNGI4NDY3MjcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzFlZjM5MzhiMTJiNDNhZGFkZjhjMmU5NmNlZTAzYWQuYmluZFBvcHVwKHBvcHVwXzYxNTllNjRlYmM0YjQ1ZDY5Mjk1ZWQ1MzUxZWRkYjkyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UyODgwODE0ODdlZTQ0OWFhZjQzYTdhMGMzOTExNTY4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ0NzM0MiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmFkNTFhNGIyZDEyNDdhMDljZDViM2M5OGI2M2Q0Y2EgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGI2ZjU0YjM0OWQ2NDZmZDliMDQ3YTIzOTlmOWRhYzcgPSAkKCc8ZGl2IGlkPSJodG1sXzhiNmY1NGIzNDlkNjQ2ZmQ5YjA0N2EyMzk5ZjlkYWM3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TY2FyYm9yb3VnaCBWaWxsYWdlLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYmFkNTFhNGIyZDEyNDdhMDljZDViM2M5OGI2M2Q0Y2Euc2V0Q29udGVudChodG1sXzhiNmY1NGIzNDlkNjQ2ZmQ5YjA0N2EyMzk5ZjlkYWM3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UyODgwODE0ODdlZTQ0OWFhZjQzYTdhMGMzOTExNTY4LmJpbmRQb3B1cChwb3B1cF9iYWQ1MWE0YjJkMTI0N2EwOWNkNWIzYzk4YjYzZDRjYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lYjYxNWE4MWI4ZDc0NzFkYmJiNjFjNzQ3YjE1MjkxMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNzkyOTIsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzNmNDhlNDhjOGM0YjQxNDhiNDg3OWYwMGZmYjg4MTkzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2NiOWQ1YzIyMzMwNDRlNzZiYzY5MzFhY2VmMWMyYjM4ID0gJCgnPGRpdiBpZD0iaHRtbF9jYjlkNWMyMjMzMDQ0ZTc2YmM2OTMxYWNlZjFjMmIzOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdCBCaXJjaG1vdW50IFBhcmssSW9udmlldyxLZW5uZWR5IFBhcmssIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zZjQ4ZTQ4YzhjNGI0MTQ4YjQ4NzlmMDBmZmI4ODE5My5zZXRDb250ZW50KGh0bWxfY2I5ZDVjMjIzMzA0NGU3NmJjNjkzMWFjZWYxYzJiMzgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZWI2MTVhODFiOGQ3NDcxZGJiYjYxYzc0N2IxNTI5MTEuYmluZFBvcHVwKHBvcHVwXzNmNDhlNDhjOGM0YjQxNDhiNDg3OWYwMGZmYjg4MTkzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RiMTg1ZjY4Zjc5ZjQzYTM5NjAxYTI4YTE5ZmY2MGFlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzExMTExNzAwMDAwMDA0LC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzIyNTBlMGZjZTBkMTQ4MWI4NGM5ZmYxNmQ2ZDk1OGNlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2U0YTI0YTE1NjJjNDRhODdhMDVlYmFiZjYxYjZjMWVlID0gJCgnPGRpdiBpZD0iaHRtbF9lNGEyNGExNTYyYzQ0YTg3YTA1ZWJhYmY2MWI2YzFlZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2xhaXJsZWEsR29sZGVuIE1pbGUsT2FrcmlkZ2UsIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yMjUwZTBmY2UwZDE0ODFiODRjOWZmMTZkNmQ5NThjZS5zZXRDb250ZW50KGh0bWxfZTRhMjRhMTU2MmM0NGE4N2EwNWViYWJmNjFiNmMxZWUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGIxODVmNjhmNzlmNDNhMzk2MDFhMjhhMTlmZjYwYWUuYmluZFBvcHVwKHBvcHVwXzIyNTBlMGZjZTBkMTQ4MWI4NGM5ZmYxNmQ2ZDk1OGNlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIyZmExMzIwYmQ0NTQ4YjhhYTQwZDRiODVkYjAyN2FlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE2MzE2LC03OS4yMzk0NzYwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zYjBiNDJmMTQ1ODU0YTE1ODhlYmMxYjAwNTE4ODExZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lOTI2YTYwNjJhNWQ0ZWRjYTVlMWFlZWNiY2EyNDcxZCA9ICQoJzxkaXYgaWQ9Imh0bWxfZTkyNmE2MDYyYTVkNGVkY2E1ZTFhZWVjYmNhMjQ3MWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsaWZmY3Jlc3QsQ2xpZmZzaWRlLFNjYXJib3JvdWdoIFZpbGxhZ2UgV2VzdCwgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNiMGI0MmYxNDU4NTRhMTU4OGViYzFiMDA1MTg4MTFlLnNldENvbnRlbnQoaHRtbF9lOTI2YTYwNjJhNWQ0ZWRjYTVlMWFlZWNiY2EyNDcxZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yMmZhMTMyMGJkNDU0OGI4YWE0MGQ0Yjg1ZGIwMjdhZS5iaW5kUG9wdXAocG9wdXBfM2IwYjQyZjE0NTg1NGExNTg4ZWJjMWIwMDUxODgxMWUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODU3MzhjZjNhYTU2NDRhYmFiMTc2NGIwNjMxNWU5NmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTI2NTcwMDAwMDAwMDQsLTc5LjI2NDg0ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzZkZmY2MjU1NDUzNGI0ZTlmZGQyNDRiZDQxNDE1MWIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTI4YmViYjU1OGMyNGM0NzhkYzAyMWVhNzhiZGJiMmUgPSAkKCc8ZGl2IGlkPSJodG1sX2UyOGJlYmI1NThjMjRjNDc4ZGMwMjFlYTc4YmRiYjJlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CaXJjaCBDbGlmZixDbGlmZnNpZGUgV2VzdCwgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M2ZGZmNjI1NTQ1MzRiNGU5ZmRkMjQ0YmQ0MTQxNTFiLnNldENvbnRlbnQoaHRtbF9lMjhiZWJiNTU4YzI0YzQ3OGRjMDIxZWE3OGJkYmIyZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84NTczOGNmM2FhNTY0NGFiYWIxNzY0YjA2MzE1ZTk2Yi5iaW5kUG9wdXAocG9wdXBfYzZkZmY2MjU1NDUzNGI0ZTlmZGQyNDRiZDQxNDE1MWIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTYzZjBjYzE2Yjg3NDBkYmE3NDcxMmE4ZGIzYWU0NGMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTc0MDk2LC03OS4yNzMzMDQwMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yYmIwNDU0NmZjOGM0Nzk2ODI4Yjk1MjM0NjA0ZDUxYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84NjlmMGFlMjY1ZjE0MWIyODkwNzM5ZjNmOTc1NmVlOCA9ICQoJzxkaXYgaWQ9Imh0bWxfODY5ZjBhZTI2NWYxNDFiMjg5MDczOWYzZjk3NTZlZTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvcnNldCBQYXJrLFNjYXJib3JvdWdoIFRvd24gQ2VudHJlLFdleGZvcmQgSGVpZ2h0cywgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzJiYjA0NTQ2ZmM4YzQ3OTY4MjhiOTUyMzQ2MDRkNTFhLnNldENvbnRlbnQoaHRtbF84NjlmMGFlMjY1ZjE0MWIyODkwNzM5ZjNmOTc1NmVlOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85NjNmMGNjMTZiODc0MGRiYTc0NzEyYThkYjNhZTQ0Yy5iaW5kUG9wdXAocG9wdXBfMmJiMDQ1NDZmYzhjNDc5NjgyOGI5NTIzNDYwNGQ1MWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjNiMGE0ZTU0NWI2NDVkYTlhMjExNjgyZGVhYjljYzIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTAwNzE1MDAwMDAwMDQsLTc5LjI5NTg0OTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjMyZDZiMzdmODJlNGY4Y2EwZWJiZjAxOTUzMjAwODEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTkwYjcxOTc2YmE3NDJmNzlmMmJkOTFiZTY4OGM2MjkgPSAkKCc8ZGl2IGlkPSJodG1sXzE5MGI3MTk3NmJhNzQyZjc5ZjJiZDkxYmU2ODhjNjI5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJ5dmFsZSxXZXhmb3JkLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjMyZDZiMzdmODJlNGY4Y2EwZWJiZjAxOTUzMjAwODEuc2V0Q29udGVudChodG1sXzE5MGI3MTk3NmJhNzQyZjc5ZjJiZDkxYmU2ODhjNjI5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2IzYjBhNGU1NDViNjQ1ZGE5YTIxMTY4MmRlYWI5Y2MyLmJpbmRQb3B1cChwb3B1cF8yMzJkNmIzN2Y4MmU0ZjhjYTBlYmJmMDE5NTMyMDA4MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kM2QyMWViNDE4NDY0ODRmYjQyOWZiMjdkODA0ZjU4OCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5NDIwMDMsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U5ZmUxMTEwMTgyYjQ0ODA4ZDZhMWVkYTZhNzJlNDY0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2IyYjNkN2NiMzJjZjQ3ODQ5M2E1OTYzZTFlZDIyOWE5ID0gJCgnPGRpdiBpZD0iaHRtbF9iMmIzZDdjYjMyY2Y0Nzg0OTNhNTk2M2UxZWQyMjlhOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0LCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTlmZTExMTAxODJiNDQ4MDhkNmExZWRhNmE3MmU0NjQuc2V0Q29udGVudChodG1sX2IyYjNkN2NiMzJjZjQ3ODQ5M2E1OTYzZTFlZDIyOWE5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2QzZDIxZWI0MTg0NjQ4NGZiNDI5ZmIyN2Q4MDRmNTg4LmJpbmRQb3B1cChwb3B1cF9lOWZlMTExMDE4MmI0NDgwOGQ2YTFlZGE2YTcyZTQ2NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNWFlOTNiNTYyM2Y0YWExYTFlZTc4YmYzMWUzZWFkOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4MTYzNzUsLTc5LjMwNDMwMjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTY4MmQwMDJiZDAwNDYzMzkwZTRmNzJhNzBhOGZkZDQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2NkM2MwYWZmZDE2NDQ1ZThlMzMzYjU1ZWRiZDRmZmUgPSAkKCc8ZGl2IGlkPSJodG1sX2NjZDNjMGFmZmQxNjQ0NWU4ZTMzM2I1NWVkYmQ0ZmZlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGFya3MgQ29ybmVycyxTdWxsaXZhbixUYW0gTyYjMzk7U2hhbnRlciwgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzk2ODJkMDAyYmQwMDQ2MzM5MGU0ZjcyYTcwYThmZGQ0LnNldENvbnRlbnQoaHRtbF9jY2QzYzBhZmZkMTY0NDVlOGUzMzNiNTVlZGJkNGZmZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kNWFlOTNiNTYyM2Y0YWExYTFlZTc4YmYzMWUzZWFkOC5iaW5kUG9wdXAocG9wdXBfOTY4MmQwMDJiZDAwNDYzMzkwZTRmNzJhNzBhOGZkZDQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWZhOWMxMGQ2ZTNjNGZmZWEyZTlkZTFhODg4NzBiMGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My44MTUyNTIyLC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RhOWYxNWRkNjljMDQ0ODE4ZTkyYzJmZmUwODlmMjZmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzhkODQ0ZmZkYjAwYTQwODQ5YzUzMTU2MmUyNjMwM2MwID0gJCgnPGRpdiBpZD0iaHRtbF84ZDg0NGZmZGIwMGE0MDg0OWM1MzE1NjJlMjYzMDNjMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0IE5vcnRoLEwmIzM5O0Ftb3JlYXV4IEVhc3QsTWlsbGlrZW4sU3RlZWxlcyBFYXN0LCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGE5ZjE1ZGQ2OWMwNDQ4MThlOTJjMmZmZTA4OWYyNmYuc2V0Q29udGVudChodG1sXzhkODQ0ZmZkYjAwYTQwODQ5YzUzMTU2MmUyNjMwM2MwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2FmYTljMTBkNmUzYzRmZmVhMmU5ZGUxYTg4ODcwYjBiLmJpbmRQb3B1cChwb3B1cF9kYTlmMTVkZDY5YzA0NDgxOGU5MmMyZmZlMDg5ZjI2Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wMDE4Yjk2YzNkODA0NmY3YWQ1YThiZGY5OTQ1NGVhZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5OTUyNTIwMDAwMDAwNSwtNzkuMzE4Mzg4N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lM2ZmMmQyY2ZkMjE0ODdlOTBkNGFmZTI3MzM5MzY0YiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81ZjQ0NmFlYThmN2I0ZjdiYjNiODQzNjY0MzliYTk0MyA9ICQoJzxkaXYgaWQ9Imh0bWxfNWY0NDZhZWE4ZjdiNGY3YmIzYjg0MzY2NDM5YmE5NDMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkwmIzM5O0Ftb3JlYXV4IFdlc3QsIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lM2ZmMmQyY2ZkMjE0ODdlOTBkNGFmZTI3MzM5MzY0Yi5zZXRDb250ZW50KGh0bWxfNWY0NDZhZWE4ZjdiNGY3YmIzYjg0MzY2NDM5YmE5NDMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDAxOGI5NmMzZDgwNDZmN2FkNWE4YmRmOTk0NTRlYWUuYmluZFBvcHVwKHBvcHVwX2UzZmYyZDJjZmQyMTQ4N2U5MGQ0YWZlMjczMzkzNjRiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzYyNGYxNGIxMDMwMzRkYzk4MTUzZTRhMDY2N2E3YTkxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuODM2MTI0NzAwMDAwMDA2LC03OS4yMDU2MzYwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNzZlMDcwNWQzOTE0NWYzOWJlOGY0OGZhN2E2NTc2ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80NTYwM2RiMzZmNWI0MmZmODJhMTc3NmNhZGViNDUyYyA9ICQoJzxkaXYgaWQ9Imh0bWxfNDU2MDNkYjM2ZjViNDJmZjgyYTE3NzZjYWRlYjQ1MmMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlVwcGVyIFJvdWdlLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTc2ZTA3MDVkMzkxNDVmMzliZThmNDhmYTdhNjU3NmQuc2V0Q29udGVudChodG1sXzQ1NjAzZGIzNmY1YjQyZmY4MmExNzc2Y2FkZWI0NTJjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzYyNGYxNGIxMDMwMzRkYzk4MTUzZTRhMDY2N2E3YTkxLmJpbmRQb3B1cChwb3B1cF9hNzZlMDcwNWQzOTE0NWYzOWJlOGY0OGZhN2E2NTc2ZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85ZGQxMDMxNWY3MTA0ZmY5OWNhMDFmYjc4NmJkMjkzOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjgwMzc2MjIsLTc5LjM2MzQ1MTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTBlMmE2NGRkZmQ3NDk3ZmEyMzc5NzdhM2Y4N2Y3NWIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGNlMjlmOGU1MjFlNDFiMTg3MTdlZDVkN2JiMzY2NTEgPSAkKCc8ZGl2IGlkPSJodG1sX2RjZTI5ZjhlNTIxZTQxYjE4NzE3ZWQ1ZDdiYjM2NjUxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IaWxsY3Jlc3QgVmlsbGFnZSwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hMGUyYTY0ZGRmZDc0OTdmYTIzNzk3N2EzZjg3Zjc1Yi5zZXRDb250ZW50KGh0bWxfZGNlMjlmOGU1MjFlNDFiMTg3MTdlZDVkN2JiMzY2NTEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWRkMTAzMTVmNzEwNGZmOTljYTAxZmI3ODZiZDI5MzkuYmluZFBvcHVwKHBvcHVwX2EwZTJhNjRkZGZkNzQ5N2ZhMjM3OTc3YTNmODdmNzViKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2YyNWRkOWQ5MDBiYzRmNWQ4Yjk0NjE0NTdkMDU3NmZlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzc4NTE3NSwtNzkuMzQ2NTU1N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMGM5ZmZjOGNkYWY0Mjc0ODllNjIzNzU1OGJmMzM4MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jNjA0MDQ5MTQ5ODI0NjNlYWJhNzVjNWUzOGE0YTBjZCA9ICQoJzxkaXYgaWQ9Imh0bWxfYzYwNDA0OTE0OTgyNDYzZWFiYTc1YzVlMzhhNGEwY2QiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZhaXJ2aWV3LEhlbnJ5IEZhcm0sT3Jpb2xlLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2YwYzlmZmM4Y2RhZjQyNzQ4OWU2MjM3NTU4YmYzMzgwLnNldENvbnRlbnQoaHRtbF9jNjA0MDQ5MTQ5ODI0NjNlYWJhNzVjNWUzOGE0YTBjZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mMjVkZDlkOTAwYmM0ZjVkOGI5NDYxNDU3ZDA1NzZmZS5iaW5kUG9wdXAocG9wdXBfZjBjOWZmYzhjZGFmNDI3NDg5ZTYyMzc1NThiZjMzODApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGY3ZDU4ODRmZTE4NDk1MDgwZDZiODU2ODZmZDRiMWQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43ODY5NDczLC03OS4zODU5NzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWU5NjkyYjY5ODM1NGQyNzg3MWE5MmNjNTI4NDcyMzEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTY5OTM4ZmUyYTQ4NGIxOThjMzgzZGQwNGVkZmQzZmYgPSAkKCc8ZGl2IGlkPSJodG1sXzU2OTkzOGZlMmE0ODRiMTk4YzM4M2RkMDRlZGZkM2ZmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXl2aWV3IFZpbGxhZ2UsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWU5NjkyYjY5ODM1NGQyNzg3MWE5MmNjNTI4NDcyMzEuc2V0Q29udGVudChodG1sXzU2OTkzOGZlMmE0ODRiMTk4YzM4M2RkMDRlZGZkM2ZmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhmN2Q1ODg0ZmUxODQ5NTA4MGQ2Yjg1Njg2ZmQ0YjFkLmJpbmRQb3B1cChwb3B1cF85ZTk2OTJiNjk4MzU0ZDI3ODcxYTkyY2M1Mjg0NzIzMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iNjcxY2YxOTRiMjQ0NDJhOTRjNjdmMDk1MzY0ZjQ2NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1NzQ5MDIsLTc5LjM3NDcxNDA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2I2YmI4ZDQ1OGVjMjQ2Yzc4MzhiMDc5NDlhM2E3MmQ5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2E1NTc0NTdkMjFhNTQ3NTliMDdkYzkxNWYxODRmYzc4ID0gJCgnPGRpdiBpZD0iaHRtbF9hNTU3NDU3ZDIxYTU0NzU5YjA3ZGM5MTVmMTg0ZmM3OCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U2lsdmVyIEhpbGxzLFlvcmsgTWlsbHMsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjZiYjhkNDU4ZWMyNDZjNzgzOGIwNzk0OWEzYTcyZDkuc2V0Q29udGVudChodG1sX2E1NTc0NTdkMjFhNTQ3NTliMDdkYzkxNWYxODRmYzc4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2I2NzFjZjE5NGIyNDQ0MmE5NGM2N2YwOTUzNjRmNDY2LmJpbmRQb3B1cChwb3B1cF9iNmJiOGQ0NThlYzI0NmM3ODM4YjA3OTQ5YTNhNzJkOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81OTEwNjc5MTIzNjQ0NjNmYmRhYTQyZTBiZDJkNzZmZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4OTA1MywtNzkuNDA4NDkyNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGUyNjFhNTE0MTllNDUyMjljZGViNzFjZTg5MmY1YTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGU5OThkOGVlY2UyNDZkMmFjZmUyODI2MzUzNWFhODAgPSAkKCc8ZGl2IGlkPSJodG1sXzhlOTk4ZDhlZWNlMjQ2ZDJhY2ZlMjgyNjM1MzVhYTgwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5OZXd0b25icm9vayxXaWxsb3dkYWxlLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RlMjYxYTUxNDE5ZTQ1MjI5Y2RlYjcxY2U4OTJmNWEwLnNldENvbnRlbnQoaHRtbF84ZTk5OGQ4ZWVjZTI0NmQyYWNmZTI4MjYzNTM1YWE4MCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81OTEwNjc5MTIzNjQ0NjNmYmRhYTQyZTBiZDJkNzZmZi5iaW5kUG9wdXAocG9wdXBfZGUyNjFhNTE0MTllNDUyMjljZGViNzFjZTg5MmY1YTApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTMyYTk2YjgxMTc1NDg0MGI5MjVjZjZiNTczMjc4ODQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NzAxMTk5LC03OS40MDg0OTI3OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jNWVmMWI5YmU2M2M0YzRlOTQxNjRlYWFmZjE3ZDVkMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hNmZkNzU4ZDdkMGQ0ZGUzYTZlN2M5YTI4MmY1MWU2MSA9ICQoJzxkaXYgaWQ9Imh0bWxfYTZmZDc1OGQ3ZDBkNGRlM2E2ZTdjOWEyODJmNTFlNjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxvd2RhbGUgU291dGgsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzVlZjFiOWJlNjNjNGM0ZTk0MTY0ZWFhZmYxN2Q1ZDAuc2V0Q29udGVudChodG1sX2E2ZmQ3NThkN2QwZDRkZTNhNmU3YzlhMjgyZjUxZTYxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzUzMmE5NmI4MTE3NTQ4NDBiOTI1Y2Y2YjU3MzI3ODg0LmJpbmRQb3B1cChwb3B1cF9jNWVmMWI5YmU2M2M0YzRlOTQxNjRlYWFmZjE3ZDVkMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85NmIxMDhhNmY0NzI0OGU2YTY5ODY1NGU2YmIxOTMyMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1Mjc1ODI5OTk5OTk5NiwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83NDQ1Yjg3MGY5Yjg0NDI5OTY5NmJhMDQ3NzQ5YTQ5OCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80NDAwNzk3Y2YwOTE0NDk5YTMxZTZiMTNhYWE4YzExMiA9ICQoJzxkaXYgaWQ9Imh0bWxfNDQwMDc5N2NmMDkxNDQ5OWEzMWU2YjEzYWFhOGMxMTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPllvcmsgTWlsbHMgV2VzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83NDQ1Yjg3MGY5Yjg0NDI5OTY5NmJhMDQ3NzQ5YTQ5OC5zZXRDb250ZW50KGh0bWxfNDQwMDc5N2NmMDkxNDQ5OWEzMWU2YjEzYWFhOGMxMTIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTZiMTA4YTZmNDcyNDhlNmE2OTg2NTRlNmJiMTkzMjEuYmluZFBvcHVwKHBvcHVwXzc0NDViODcwZjliODQ0Mjk5Njk2YmEwNDc3NDlhNDk4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2JmNzljMjI3NzVlNTRlNzBiMTM3MDg0YmYwM2VlMjE1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzgyNzM2NCwtNzkuNDQyMjU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wMGYwMDk1MDgxODg0NmE2OTk1ZDgxMTlmODAxNmNkYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hOTQxNWEwNzM1Mjc0ZGRiYmNmNTQ4YmY4Yzc2MjYyMSA9ICQoJzxkaXYgaWQ9Imh0bWxfYTk0MTVhMDczNTI3NGRkYmJjZjU0OGJmOGM3NjI2MjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxvd2RhbGUgV2VzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wMGYwMDk1MDgxODg0NmE2OTk1ZDgxMTlmODAxNmNkYi5zZXRDb250ZW50KGh0bWxfYTk0MTVhMDczNTI3NGRkYmJjZjU0OGJmOGM3NjI2MjEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYmY3OWMyMjc3NWU1NGU3MGIxMzcwODRiZjAzZWUyMTUuYmluZFBvcHVwKHBvcHVwXzAwZjAwOTUwODE4ODQ2YTY5OTVkODExOWY4MDE2Y2RiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q4ZGE2MWJmZTcxNjQ2NzJhMDkzMGQ4MTJlMzY0ZjAwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzUzMjU4NiwtNzkuMzI5NjU2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kNmU2MzcwNzM4MDA0MjJhODMwMjcxMWJlNjAzNDY0NyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNWViMDhhMjU1MDM0YzlkOTc3NWRlZGM4Yzk3MDE2ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfMTVlYjA4YTI1NTAzNGM5ZDk3NzVkZWRjOGM5NzAxNmYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBhcmt3b29kcywgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kNmU2MzcwNzM4MDA0MjJhODMwMjcxMWJlNjAzNDY0Ny5zZXRDb250ZW50KGh0bWxfMTVlYjA4YTI1NTAzNGM5ZDk3NzVkZWRjOGM5NzAxNmYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDhkYTYxYmZlNzE2NDY3MmEwOTMwZDgxMmUzNjRmMDAuYmluZFBvcHVwKHBvcHVwX2Q2ZTYzNzA3MzgwMDQyMmE4MzAyNzExYmU2MDM0NjQ3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzEwMjFiN2JkMjBiOTRlZjBiN2NlN2UwZDU5MzhhOTFmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ1OTA1Nzk5OTk5OTk2LC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTQ1OTQ1M2E3ZTFlNGNiOTg4OWFlMjNiNjc0YWE5YzcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWJmZTZjMWJkMTk0NDk5MWEzNWYxODFhMDAxNTE1YzUgPSAkKCc8ZGl2IGlkPSJodG1sX2ViZmU2YzFiZDE5NDQ5OTFhMzVmMTgxYTAwMTUxNWM1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb24gTWlsbHMgTm9ydGgsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTQ1OTQ1M2E3ZTFlNGNiOTg4OWFlMjNiNjc0YWE5Yzcuc2V0Q29udGVudChodG1sX2ViZmU2YzFiZDE5NDQ5OTFhMzVmMTgxYTAwMTUxNWM1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzEwMjFiN2JkMjBiOTRlZjBiN2NlN2UwZDU5MzhhOTFmLmJpbmRQb3B1cChwb3B1cF9lNDU5NDUzYTdlMWU0Y2I5ODg5YWUyM2I2NzRhYTljNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MjAyNDIzOTFjMjk0N2FhODc1NTY3OTMwYjNiMzc3ZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNTg5OTcwMDAwMDAxLC03OS4zNDA5MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODJlYWU0YmI1OGFhNDU4Mjk5NjkxYTQxYjllZTVlNmQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2Y0NDcwY2JmOTM5NDU0OWFmODgyMzk2ZjA5MjU0MGIgPSAkKCc8ZGl2IGlkPSJodG1sX2NmNDQ3MGNiZjkzOTQ1NDlhZjg4MjM5NmYwOTI1NDBiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GbGVtaW5nZG9uIFBhcmssRG9uIE1pbGxzIFNvdXRoLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzgyZWFlNGJiNThhYTQ1ODI5OTY5MWE0MWI5ZWU1ZTZkLnNldENvbnRlbnQoaHRtbF9jZjQ0NzBjYmY5Mzk0NTQ5YWY4ODIzOTZmMDkyNTQwYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MjAyNDIzOTFjMjk0N2FhODc1NTY3OTMwYjNiMzc3Zi5iaW5kUG9wdXAocG9wdXBfODJlYWU0YmI1OGFhNDU4Mjk5NjkxYTQxYjllZTVlNmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmUyNWYwNmU3MzVlNDBlM2EwNGJlZTNjMjgxMGExZWEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTQzMjgzLC03OS40NDIyNTkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA1YTRjMzcyZTU0ZjQzNmY5MjI0MzI1NjkzNGQwNzIzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzlmMTBiMzNiZGY1ZDQ2MmFhN2JlNGI5ZmYyMzE4ZGQ3ID0gJCgnPGRpdiBpZD0iaHRtbF85ZjEwYjMzYmRmNWQ0NjJhYTdiZTRiOWZmMjMxOGRkNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmF0aHVyc3QgTWFub3IsRG93bnN2aWV3IE5vcnRoLFdpbHNvbiBIZWlnaHRzLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzA1YTRjMzcyZTU0ZjQzNmY5MjI0MzI1NjkzNGQwNzIzLnNldENvbnRlbnQoaHRtbF85ZjEwYjMzYmRmNWQ0NjJhYTdiZTRiOWZmMjMxOGRkNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mZTI1ZjA2ZTczNWU0MGUzYTA0YmVlM2MyODEwYTFlYS5iaW5kUG9wdXAocG9wdXBfMDVhNGMzNzJlNTRmNDM2ZjkyMjQzMjU2OTM0ZDA3MjMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWM2NzlmNmY1YzZiNDEzNjk5YWYyMTI5MWM5Y2M3YTUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Njc5ODAzLC03OS40ODcyNjE5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81MGRjYTE2MjI4NzQ0OWNmOTczOTExMTgyNGE4NDczYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jYjcyZjQ1MTRlZmI0MzI3YTljZTc0NGEyZDQ0YmM1ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfY2I3MmY0NTE0ZWZiNDMyN2E5Y2U3NDRhMmQ0NGJjNWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vcnRod29vZCBQYXJrLFlvcmsgVW5pdmVyc2l0eSwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81MGRjYTE2MjI4NzQ0OWNmOTczOTExMTgyNGE4NDczYS5zZXRDb250ZW50KGh0bWxfY2I3MmY0NTE0ZWZiNDMyN2E5Y2U3NDRhMmQ0NGJjNWYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWM2NzlmNmY1YzZiNDEzNjk5YWYyMTI5MWM5Y2M3YTUuYmluZFBvcHVwKHBvcHVwXzUwZGNhMTYyMjg3NDQ5Y2Y5NzM5MTExODI0YTg0NzNhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI1NDlmZTY5YzJhMDQ3NmZhYmI3ZjFkZTQ0OWVlMzY1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzM3NDczMjAwMDAwMDA0LC03OS40NjQ3NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lNDhhMmQzYzc3NDA0NDM5ODM1ZGRhZDNhM2IyNGQ3ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kM2Y2NDBhMDRjOTk0ZTE5OTk4ODRmMzc3ZjRjMTZmYiA9ICQoJzxkaXYgaWQ9Imh0bWxfZDNmNjQwYTA0Yzk5NGUxOTk5ODg0ZjM3N2Y0YzE2ZmIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNGQiBUb3JvbnRvLERvd25zdmlldyBFYXN0LCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2U0OGEyZDNjNzc0MDQ0Mzk4MzVkZGFkM2EzYjI0ZDdkLnNldENvbnRlbnQoaHRtbF9kM2Y2NDBhMDRjOTk0ZTE5OTk4ODRmMzc3ZjRjMTZmYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yNTQ5ZmU2OWMyYTA0NzZmYWJiN2YxZGU0NDllZTM2NS5iaW5kUG9wdXAocG9wdXBfZTQ4YTJkM2M3NzQwNDQzOTgzNWRkYWQzYTNiMjRkN2QpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmY1OTI1ODc3NGJkNDhhYzhkMDlhZDQ0MjE0MmMzZjAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MzkwMTQ2LC03OS41MDY5NDM2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M1YTMwZTBkZmM4OTQ3YzE5ZjIxYTdmZDFjMzY4ZWU0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNlYWZmNmQ3YmYwODQxYjU4Y2JhZDRlNGJhNWE2ZjM2ID0gJCgnPGRpdiBpZD0iaHRtbF8zZWFmZjZkN2JmMDg0MWI1OGNiYWQ0ZTRiYTVhNmYzNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IFdlc3QsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzVhMzBlMGRmYzg5NDdjMTlmMjFhN2ZkMWMzNjhlZTQuc2V0Q29udGVudChodG1sXzNlYWZmNmQ3YmYwODQxYjU4Y2JhZDRlNGJhNWE2ZjM2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZmNTkyNTg3NzRiZDQ4YWM4ZDA5YWQ0NDIxNDJjM2YwLmJpbmRQb3B1cChwb3B1cF9jNWEzMGUwZGZjODk0N2MxOWYyMWE3ZmQxYzM2OGVlNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85ODI5ODg5NGFmY2M0NTM2ODY2YTllODM3NGZkMmMzOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyODQ5NjQsLTc5LjQ5NTY5NzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzU1YTUwZjVlNWRkNDQ1NzM4MjRjNTI5YjIwY2UzMTMzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2M4YTYwZGEzM2RmZjQyM2Q5YTQwNTFjYzQxZThlZTFmID0gJCgnPGRpdiBpZD0iaHRtbF9jOGE2MGRhMzNkZmY0MjNkOWE0MDUxY2M0MWU4ZWUxZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IENlbnRyYWwsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNTVhNTBmNWU1ZGQ0NDU3MzgyNGM1MjliMjBjZTMxMzMuc2V0Q29udGVudChodG1sX2M4YTYwZGEzM2RmZjQyM2Q5YTQwNTFjYzQxZThlZTFmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk4Mjk4ODk0YWZjYzQ1MzY4NjZhOWU4Mzc0ZmQyYzM4LmJpbmRQb3B1cChwb3B1cF81NWE1MGY1ZTVkZDQ0NTczODI0YzUyOWIyMGNlMzEzMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MTAzM2MxNTdmYTg0ZTRhYWMyY2Q5ZTFhYTQ1YjBlNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc2MTYzMTMsLTc5LjUyMDk5OTQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2I1NjZiMDcyZWVmNzRmYmRiMTRkZmExOWI2ZDBjMGYzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzdkZWJjMzY0MDk2ZTQ2Yzg5NWFiNGFkN2IzODIyMzliID0gJCgnPGRpdiBpZD0iaHRtbF83ZGViYzM2NDA5NmU0NmM4OTVhYjRhZDdiMzgyMjM5YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IE5vcnRod2VzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iNTY2YjA3MmVlZjc0ZmJkYjE0ZGZhMTliNmQwYzBmMy5zZXRDb250ZW50KGh0bWxfN2RlYmMzNjQwOTZlNDZjODk1YWI0YWQ3YjM4MjIzOWIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDEwMzNjMTU3ZmE4NGU0YWFjMmNkOWUxYWE0NWIwZTcuYmluZFBvcHVwKHBvcHVwX2I1NjZiMDcyZWVmNzRmYmRiMTRkZmExOWI2ZDBjMGYzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQyN2Q1NWFjNzRhMzQ2ZDJiMmRjNDA2OGEzNmZlNDZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI1ODgyMjk5OTk5OTk1LC03OS4zMTU1NzE1OTk5OTk5OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82ZWQzNmE2OTZiZTY0NzIxYTQ5M2ZlMGI5ZmU4NWQ2ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84ZjM5MmRjNTJkYTk0MDUzYmI1YWY3MTViNGViZmZkNCA9ICQoJzxkaXYgaWQ9Imh0bWxfOGYzOTJkYzUyZGE5NDA1M2JiNWFmNzE1YjRlYmZmZDQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlZpY3RvcmlhIFZpbGxhZ2UsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmVkMzZhNjk2YmU2NDcyMWE0OTNmZTBiOWZlODVkNmYuc2V0Q29udGVudChodG1sXzhmMzkyZGM1MmRhOTQwNTNiYjVhZjcxNWI0ZWJmZmQ0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQyN2Q1NWFjNzRhMzQ2ZDJiMmRjNDA2OGEzNmZlNDZhLmJpbmRQb3B1cChwb3B1cF82ZWQzNmE2OTZiZTY0NzIxYTQ5M2ZlMGI5ZmU4NWQ2Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kZGE0NGVmZmU0MjE0YmY2YWY3NWY2M2M5NWEwYzE0MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcwNjM5NzIsLTc5LjMwOTkzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82MDllMGQ1MDVkNDY0MTRhOGY3NGI4MjY0MjA3ZjkwZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hOWMxY2ZhMmQxN2Q0ODAzOWMzMGIwYTIzNmE2ZDE0OSA9ICQoJzxkaXYgaWQ9Imh0bWxfYTljMWNmYTJkMTdkNDgwMzljMzBiMGEyMzZhNmQxNDkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldvb2RiaW5lIEdhcmRlbnMsUGFya3ZpZXcgSGlsbCwgRWFzdFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzYwOWUwZDUwNWQ0NjQxNGE4Zjc0YjgyNjQyMDdmOTBkLnNldENvbnRlbnQoaHRtbF9hOWMxY2ZhMmQxN2Q0ODAzOWMzMGIwYTIzNmE2ZDE0OSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kZGE0NGVmZmU0MjE0YmY2YWY3NWY2M2M5NWEwYzE0MS5iaW5kUG9wdXAocG9wdXBfNjA5ZTBkNTA1ZDQ2NDE0YThmNzRiODI2NDIwN2Y5MGQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmRmN2IyNDM0NjRkNDZhYTliMTk3OTgwN2FjYjFiYjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTUzNDM5MDAwMDAwMDUsLTc5LjMxODM4ODddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjU5NzY2NDkzMGMwNDIyZjlkYzYyZWQ0N2ViNTUzYTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYmZhNTk2ODhiMWFjNGVjOTg0NDdkZTNiMGIyY2E2MzkgPSAkKCc8ZGl2IGlkPSJodG1sX2JmYTU5Njg4YjFhYzRlYzk4NDQ3ZGUzYjBiMmNhNjM5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Xb29kYmluZSBIZWlnaHRzLCBFYXN0WW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjU5NzY2NDkzMGMwNDIyZjlkYzYyZWQ0N2ViNTUzYTYuc2V0Q29udGVudChodG1sX2JmYTU5Njg4YjFhYzRlYzk4NDQ3ZGUzYjBiMmNhNjM5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJkZjdiMjQzNDY0ZDQ2YWE5YjE5Nzk4MDdhY2IxYmI4LmJpbmRQb3B1cChwb3B1cF9mNTk3NjY0OTMwYzA0MjJmOWRjNjJlZDQ3ZWI1NTNhNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hNDAyYTk3YjE3NmE0ZTFjYjA4NjQxMGNlNjJlMDk0ZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY3NjM1NzM5OTk5OTk5LC03OS4yOTMwMzEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NkMmFlODNiMGQyMjQzMDRhN2M3NmUwOWUzNWUzYWRmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JlMjA4ZWE0MTQ2NTQwZDg4MjVlMmU4NWFmMTUyMzc2ID0gJCgnPGRpdiBpZD0iaHRtbF9iZTIwOGVhNDE0NjU0MGQ4ODI1ZTJlODVhZjE1MjM3NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhlIEJlYWNoZXMsIEVhc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jZDJhZTgzYjBkMjI0MzA0YTdjNzZlMDllMzVlM2FkZi5zZXRDb250ZW50KGh0bWxfYmUyMDhlYTQxNDY1NDBkODgyNWUyZTg1YWYxNTIzNzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTQwMmE5N2IxNzZhNGUxY2IwODY0MTBjZTYyZTA5NGYuYmluZFBvcHVwKHBvcHVwX2NkMmFlODNiMGQyMjQzMDRhN2M3NmUwOWUzNWUzYWRmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk5ZDIyZWJiNjM1ODQxMGM4OWU4MjUwMzM0YzJiYmEwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA5MDYwNCwtNzkuMzYzNDUxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zZjU3NmJiN2NmODU0ZWRiYTBlMGJiZWYzOTE5NmFmNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kYTEzNzQ4NWQ3NmY0ZmUxODdhZWI1M2Y5NDA2OWI0YyA9ICQoJzxkaXYgaWQ9Imh0bWxfZGExMzc0ODVkNzZmNGZlMTg3YWViNTNmOTQwNjliNGMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxlYXNpZGUsIEVhc3RZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zZjU3NmJiN2NmODU0ZWRiYTBlMGJiZWYzOTE5NmFmNy5zZXRDb250ZW50KGh0bWxfZGExMzc0ODVkNzZmNGZlMTg3YWViNTNmOTQwNjliNGMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTlkMjJlYmI2MzU4NDEwYzg5ZTgyNTAzMzRjMmJiYTAuYmluZFBvcHVwKHBvcHVwXzNmNTc2YmI3Y2Y4NTRlZGJhMGUwYmJlZjM5MTk2YWY3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI4NWY3ODZiZjFkNTQ3MzdiYWM4NmY1MmU0YTVhNmQ2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA1MzY4OSwtNzkuMzQ5MzcxOTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTA3M2U1NjlkM2JkNGU3NDk2Y2RiN2YwN2E0MmJiZDIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjU0ODU4ZWZiODc2NGE2MTg1NmZhODdmNmQ2ODA1YjcgPSAkKCc8ZGl2IGlkPSJodG1sX2Y1NDg1OGVmYjg3NjRhNjE4NTZmYTg3ZjZkNjgwNWI3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaG9ybmNsaWZmZSBQYXJrLCBFYXN0WW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTA3M2U1NjlkM2JkNGU3NDk2Y2RiN2YwN2E0MmJiZDIuc2V0Q29udGVudChodG1sX2Y1NDg1OGVmYjg3NjRhNjE4NTZmYTg3ZjZkNjgwNWI3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzI4NWY3ODZiZjFkNTQ3MzdiYWM4NmY1MmU0YTVhNmQ2LmJpbmRQb3B1cChwb3B1cF9lMDczZTU2OWQzYmQ0ZTc0OTZjZGI3ZjA3YTQyYmJkMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iN2FhYTFkMzM3Yjc0OTFkYTE0MDczYTJmMTI5Mjk0NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY4NTM0NywtNzkuMzM4MTA2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wMGVhMmI1Y2M2ZDE0ZWQ3YWIxOTMwMzYzMWU1MDcwMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xZjkwNjZkOGE0OWY0NTI2OGRlMzYwOThiZDZjZDExZSA9ICQoJzxkaXYgaWQ9Imh0bWxfMWY5MDY2ZDhhNDlmNDUyNjhkZTM2MDk4YmQ2Y2QxMWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgVG9yb250bywgRWFzdFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzAwZWEyYjVjYzZkMTRlZDdhYjE5MzAzNjMxZTUwNzAxLnNldENvbnRlbnQoaHRtbF8xZjkwNjZkOGE0OWY0NTI2OGRlMzYwOThiZDZjZDExZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iN2FhYTFkMzM3Yjc0OTFkYTE0MDczYTJmMTI5Mjk0Ni5iaW5kUG9wdXAocG9wdXBfMDBlYTJiNWNjNmQxNGVkN2FiMTkzMDM2MzFlNTA3MDEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmJmZWE0M2M0OTk1NDY1ZDg4MjcxYWJmMDIzMGQ2MWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Nzk1NTcxLC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODIyNTdhNGU1OTZiNGE3ODhmYmFjYzhhYzRkMDkwNmMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDY2MDMxYTY2Y2ExNDliNjgyN2ZlZWE2Zjc5NDczMjUgPSAkKCc8ZGl2IGlkPSJodG1sXzQ2NjAzMWE2NmNhMTQ5YjY4MjdmZWVhNmY3OTQ3MzI1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgRGFuZm9ydGggV2VzdCxSaXZlcmRhbGUsIEVhc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MjI1N2E0ZTU5NmI0YTc4OGZiYWNjOGFjNGQwOTA2Yy5zZXRDb250ZW50KGh0bWxfNDY2MDMxYTY2Y2ExNDliNjgyN2ZlZWE2Zjc5NDczMjUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYmJmZWE0M2M0OTk1NDY1ZDg4MjcxYWJmMDIzMGQ2MWIuYmluZFBvcHVwKHBvcHVwXzgyMjU3YTRlNTk2YjRhNzg4ZmJhY2M4YWM0ZDA5MDZjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZlY2FiY2FiOWRkZDQ3Yzg5ZTJmOWJjMDBmYTIxMzZkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY4OTk4NSwtNzkuMzE1NTcxNTk5OTk5OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmNlYTU1ZjQ4MDljNGE1N2I5ZmI5YjM5ZWRjMDQyOWUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzQ1MGY5YTBlODY5NDk4MDkwYzkzZTgxZGZmNjY5MGUgPSAkKCc8ZGl2IGlkPSJodG1sXzc0NTBmOWEwZTg2OTQ5ODA5MGM5M2U4MWRmZjY2OTBlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgQmVhY2hlcyBXZXN0LEluZGlhIEJhemFhciwgRWFzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2JjZWE1NWY0ODA5YzRhNTdiOWZiOWIzOWVkYzA0MjllLnNldENvbnRlbnQoaHRtbF83NDUwZjlhMGU4Njk0OTgwOTBjOTNlODFkZmY2NjkwZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82ZWNhYmNhYjlkZGQ0N2M4OWUyZjliYzAwZmEyMTM2ZC5iaW5kUG9wdXAocG9wdXBfYmNlYTU1ZjQ4MDljNGE1N2I5ZmI5YjM5ZWRjMDQyOWUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2QyNDY1MTQ1ZTRhNDU3NWFhODc2MTBkOTJmNzk4MzYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTk1MjU1LC03OS4zNDA5MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTE3ZWVlMjUwM2ZlNGYzYzg0Yjk4OTc2ZWM2NDFkZDIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYzgzOTk0NTkyMGI1NDNkZDhlMzU0MzlhZDFiMmM1OTIgPSAkKCc8ZGl2IGlkPSJodG1sX2M4Mzk5NDU5MjBiNTQzZGQ4ZTM1NDM5YWQxYjJjNTkyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdHVkaW8gRGlzdHJpY3QsIEVhc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lMTdlZWUyNTAzZmU0ZjNjODRiOTg5NzZlYzY0MWRkMi5zZXRDb250ZW50KGh0bWxfYzgzOTk0NTkyMGI1NDNkZDhlMzU0MzlhZDFiMmM1OTIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2QyNDY1MTQ1ZTRhNDU3NWFhODc2MTBkOTJmNzk4MzYuYmluZFBvcHVwKHBvcHVwX2UxN2VlZTI1MDNmZTRmM2M4NGI5ODk3NmVjNjQxZGQyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IyMDhiMDM5NzFkZDRhOTE5OTk4M2U4OGIxY2EwZWY4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI4MDIwNSwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jYTZkZjMxNTQ2Yzg0ODMxODMwOWY3MmRlNzMwODc3NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lMDUxMmI2ZGI1MjU0MTZlYTE3OTFjMzE2MDU3MGQ2MSA9ICQoJzxkaXYgaWQ9Imh0bWxfZTA1MTJiNmRiNTI1NDE2ZWExNzkxYzMxNjA1NzBkNjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIFBhcmssIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jYTZkZjMxNTQ2Yzg0ODMxODMwOWY3MmRlNzMwODc3NC5zZXRDb250ZW50KGh0bWxfZTA1MTJiNmRiNTI1NDE2ZWExNzkxYzMxNjA1NzBkNjEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjIwOGIwMzk3MWRkNGE5MTk5OTgzZTg4YjFjYTBlZjguYmluZFBvcHVwKHBvcHVwX2NhNmRmMzE1NDZjODQ4MzE4MzA5ZjcyZGU3MzA4Nzc0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZiZDNmODVlM2U5ODQ4ZjI5YzY0YzRkZTQzMjkwN2YwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzEyNzUxMSwtNzkuMzkwMTk3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81ODFkODZiN2ZjOTQ0NWM0ODFiMmIyMmY0ZGRkZDA0YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hMmMwZjc3NDk0YTQ0ZjNmYTBkN2QwZGFkNGFhMTBmNiA9ICQoJzxkaXYgaWQ9Imh0bWxfYTJjMGY3NzQ5NGE0NGYzZmEwZDdkMGRhZDRhYTEwZjYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUgTm9ydGgsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81ODFkODZiN2ZjOTQ0NWM0ODFiMmIyMmY0ZGRkZDA0YS5zZXRDb250ZW50KGh0bWxfYTJjMGY3NzQ5NGE0NGYzZmEwZDdkMGRhZDRhYTEwZjYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmJkM2Y4NWUzZTk4NDhmMjljNjRjNGRlNDMyOTA3ZjAuYmluZFBvcHVwKHBvcHVwXzU4MWQ4NmI3ZmM5NDQ1YzQ4MWIyYjIyZjRkZGRkMDRhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E1ZGI5ZThjMWY4MjQwNGU4NTMyMWI3ZTYxN2JmZjc4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE1MzgzNCwtNzkuNDA1Njc4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmE3NjlmYjg2MTMzNGNjMzk5OGYwNGFlZTRhYjU3MTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWVmMGQwYTU5Njg4NDIzNTk5MjIyYTBlNTkwYjgwOGUgPSAkKCc8ZGl2IGlkPSJodG1sXzVlZjBkMGE1OTY4ODQyMzU5OTIyMmEwZTU5MGI4MDhlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aCBUb3JvbnRvIFdlc3QsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mYTc2OWZiODYxMzM0Y2MzOTk4ZjA0YWVlNGFiNTcxMi5zZXRDb250ZW50KGh0bWxfNWVmMGQwYTU5Njg4NDIzNTk5MjIyYTBlNTkwYjgwOGUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTVkYjllOGMxZjgyNDA0ZTg1MzIxYjdlNjE3YmZmNzguYmluZFBvcHVwKHBvcHVwX2ZhNzY5ZmI4NjEzMzRjYzM5OThmMDRhZWU0YWI1NzEyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZmMmQyOWI0YmNkYTQxMTc5OGIwZmE0YmM1ZmYyNGE4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA0MzI0NCwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yZWZkZjVkNzEyYmQ0Y2QxOTQ2ZmZjNjg1M2FlZTI3YyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kNDVlZTliNzNjNGU0ZWVkYjA3Y2I2NmYzMDcxMDUxNyA9ICQoJzxkaXYgaWQ9Imh0bWxfZDQ1ZWU5YjczYzRlNGVlZGIwN2NiNjZmMzA3MTA1MTciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yZWZkZjVkNzEyYmQ0Y2QxOTQ2ZmZjNjg1M2FlZTI3Yy5zZXRDb250ZW50KGh0bWxfZDQ1ZWU5YjczYzRlNGVlZGIwN2NiNjZmMzA3MTA1MTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZmYyZDI5YjRiY2RhNDExNzk4YjBmYTRiYzVmZjI0YTguYmluZFBvcHVwKHBvcHVwXzJlZmRmNWQ3MTJiZDRjZDE5NDZmZmM2ODUzYWVlMjdjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2FiNTQxOTIyZGI2MzQyNjc5MGI3NTg5YjliZDU2OGEwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg5NTc0MywtNzkuMzgzMTU5OTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzYyZTc4YjllZWFkNGRkNDg5NzQxM2U4ZmIwMzI4NzQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYmEyMjU3ZjI4NGIyNDI5MjkwMDVkNDNjMDIyYzU0MDggPSAkKCc8ZGl2IGlkPSJodG1sX2JhMjI1N2YyODRiMjQyOTI5MDA1ZDQzYzAyMmM1NDA4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb29yZSBQYXJrLFN1bW1lcmhpbGwgRWFzdCwgQ2VudHJhbFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M2MmU3OGI5ZWVhZDRkZDQ4OTc0MTNlOGZiMDMyODc0LnNldENvbnRlbnQoaHRtbF9iYTIyNTdmMjg0YjI0MjkyOTAwNWQ0M2MwMjJjNTQwOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hYjU0MTkyMmRiNjM0MjY3OTBiNzU4OWI5YmQ1NjhhMC5iaW5kUG9wdXAocG9wdXBfYzYyZTc4YjllZWFkNGRkNDg5NzQxM2U4ZmIwMzI4NzQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTM3MzYyMGQ3NzZiNDQ4YWIwODIzNTdhNTRjOTgxYTYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42ODY0MTIyOTk5OTk5OSwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80MGIwNDJiZmFlN2M0M2ZkOGUwNWUzYmExYTYxZDZiOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNzExZThlMzVjZjk0NDc5OTNjN2E1MmY0NmIzNTA5ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfMzcxMWU4ZTM1Y2Y5NDQ3OTkzYzdhNTJmNDZiMzUwOWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRlZXIgUGFyayxGb3Jlc3QgSGlsbCBTRSxSYXRobmVsbHksU291dGggSGlsbCxTdW1tZXJoaWxsIFdlc3QsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80MGIwNDJiZmFlN2M0M2ZkOGUwNWUzYmExYTYxZDZiOC5zZXRDb250ZW50KGh0bWxfMzcxMWU4ZTM1Y2Y5NDQ3OTkzYzdhNTJmNDZiMzUwOWUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTM3MzYyMGQ3NzZiNDQ4YWIwODIzNTdhNTRjOTgxYTYuYmluZFBvcHVwKHBvcHVwXzQwYjA0MmJmYWU3YzQzZmQ4ZTA1ZTNiYTFhNjFkNmI4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIyZmM1MzU3NDU4MTQ2N2FhNDZjM2Y3ODczYjdiODIyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjc5NTYyNiwtNzkuMzc3NTI5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTgwM2I2YzgxNzY3NGJlMTgyNzdlZDA1M2ZjOTdjNGUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTA4ZWNjNjg4ODJkNGIxMzhmODU2ZjNlODM4NmVlY2YgPSAkKCc8ZGl2IGlkPSJodG1sX2EwOGVjYzY4ODgyZDRiMTM4Zjg1NmYzZTgzODZlZWNmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlZGFsZSwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lODAzYjZjODE3Njc0YmUxODI3N2VkMDUzZmM5N2M0ZS5zZXRDb250ZW50KGh0bWxfYTA4ZWNjNjg4ODJkNGIxMzhmODU2ZjNlODM4NmVlY2YpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjJmYzUzNTc0NTgxNDY3YWE0NmMzZjc4NzNiN2I4MjIuYmluZFBvcHVwKHBvcHVwX2U4MDNiNmM4MTc2NzRiZTE4Mjc3ZWQwNTNmYzk3YzRlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzAzNGU1MzI4OTczNDRjYjE4OGVkMmRkYmUzYWZiNjY2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY3OTY3LC03OS4zNjc2NzUzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzgzNDc1N2M1MjE5ZDRmM2Y4NGZjOGZlZDY0MDIyYjczID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzZlNjExNTdkODI5ZjQyMTJiZGNhM2VlMDk0NTlkZTc1ID0gJCgnPGRpdiBpZD0iaHRtbF82ZTYxMTU3ZDgyOWY0MjEyYmRjYTNlZTA5NDU5ZGU3NSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FiYmFnZXRvd24sU3QuIEphbWVzIFRvd24sIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODM0NzU3YzUyMTlkNGYzZjg0ZmM4ZmVkNjQwMjJiNzMuc2V0Q29udGVudChodG1sXzZlNjExNTdkODI5ZjQyMTJiZGNhM2VlMDk0NTlkZTc1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzAzNGU1MzI4OTczNDRjYjE4OGVkMmRkYmUzYWZiNjY2LmJpbmRQb3B1cChwb3B1cF84MzQ3NTdjNTIxOWQ0ZjNmODRmYzhmZWQ2NDAyMmI3Myk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83YWNmODIyODUwYTc0NTUxYTRmYzgzZmE3NDNiNGQwZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2NTg1OTksLTc5LjM4MzE1OTkwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk4YzgwMGU4MmU0ZjRmNzI5Mjg5MTYyZDE0NTA2MmNhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJhNmQ1NTgxOTVkMTQzZDI5NDNkNzc4ZWE4ZTRhMjg2ID0gJCgnPGRpdiBpZD0iaHRtbF8yYTZkNTU4MTk1ZDE0M2QyOTQzZDc3OGVhOGU0YTI4NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2h1cmNoIGFuZCBXZWxsZXNsZXksIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOThjODAwZTgyZTRmNGY3MjkyODkxNjJkMTQ1MDYyY2Euc2V0Q29udGVudChodG1sXzJhNmQ1NTgxOTVkMTQzZDI5NDNkNzc4ZWE4ZTRhMjg2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzdhY2Y4MjI4NTBhNzQ1NTFhNGZjODNmYTc0M2I0ZDBlLmJpbmRQb3B1cChwb3B1cF85OGM4MDBlODJlNGY0ZjcyOTI4OTE2MmQxNDUwNjJjYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jMjczZjVmOGFmNmY0MGY5YmQwZGY3MTUwZjI1YjlmMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1NDI1OTksLTc5LjM2MDYzNTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDcxMmMzMzkzNmFmNGExZjk1M2MzNzczZjI1MjgwY2EgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjJmODYyM2FlZDIzNDA4NWEwMWNhZjkyYjA5MWY4MWUgPSAkKCc8ZGl2IGlkPSJodG1sXzYyZjg2MjNhZWQyMzQwODVhMDFjYWY5MmIwOTFmODFlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQsUmVnZW50IFBhcmssIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDcxMmMzMzkzNmFmNGExZjk1M2MzNzczZjI1MjgwY2Euc2V0Q29udGVudChodG1sXzYyZjg2MjNhZWQyMzQwODVhMDFjYWY5MmIwOTFmODFlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2MyNzNmNWY4YWY2ZjQwZjliZDBkZjcxNTBmMjViOWYwLmJpbmRQb3B1cChwb3B1cF80NzEyYzMzOTM2YWY0YTFmOTUzYzM3NzNmMjUyODBjYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZDRiNmYzM2Y2Mjg0YTcxYThlNTRiYjMxZmQxZTg1OCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1NzE2MTgsLTc5LjM3ODkzNzA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzYxMzA1ZjQ3MWZhNDQ1ODZiMjQxMzA0MDU1OTk5YjI0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZhNGU2MDM0MzZkNTQ2MGNiMThkYjAxMGIyMTZhMThmID0gJCgnPGRpdiBpZD0iaHRtbF9mYTRlNjAzNDM2ZDU0NjBjYjE4ZGIwMTBiMjE2YTE4ZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UnllcnNvbixHYXJkZW4gRGlzdHJpY3QsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjEzMDVmNDcxZmE0NDU4NmIyNDEzMDQwNTU5OTliMjQuc2V0Q29udGVudChodG1sX2ZhNGU2MDM0MzZkNTQ2MGNiMThkYjAxMGIyMTZhMThmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzdkNGI2ZjMzZjYyODRhNzFhOGU1NGJiMzFmZDFlODU4LmJpbmRQb3B1cChwb3B1cF82MTMwNWY0NzFmYTQ0NTg2YjI0MTMwNDA1NTk5OWIyNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zNzhjNzgzMmE5MDg0YTljYjk5MGFlZDMxMWJkMmRmZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1MTQ5MzksLTc5LjM3NTQxNzldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYThhNWRmMGRiYTgzNDlhOGIwODI4M2I5OGMwM2I3ODUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTRhNDAwZTcwNDlmNDQ1Mjk5ZmI3YTQ0NGZhMzZiMjUgPSAkKCc8ZGl2IGlkPSJodG1sXzU0YTQwMGU3MDQ5ZjQ0NTI5OWZiN2E0NDRmYTM2YjI1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdC4gSmFtZXMgVG93biwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hOGE1ZGYwZGJhODM0OWE4YjA4MjgzYjk4YzAzYjc4NS5zZXRDb250ZW50KGh0bWxfNTRhNDAwZTcwNDlmNDQ1Mjk5ZmI3YTQ0NGZhMzZiMjUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzc4Yzc4MzJhOTA4NGE5Y2I5OTBhZWQzMTFiZDJkZmYuYmluZFBvcHVwKHBvcHVwX2E4YTVkZjBkYmE4MzQ5YThiMDgyODNiOThjMDNiNzg1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIwMzYwNTI2NzVhZDRjNjBhN2JmM2NkNGUzN2NiZTFjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ0NzcwNzk5OTk5OTk2LC03OS4zNzMzMDY0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA1NzlhN2Y3MGFlMTQ5MWQ5MmQxYTg4N2ZlZTgyMzhhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJlOWUxNzhkNGQxNjQyZGM4NTljMTZmNDc2ZTdlODljID0gJCgnPGRpdiBpZD0iaHRtbF8yZTllMTc4ZDRkMTY0MmRjODU5YzE2ZjQ3NmU3ZTg5YyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVyY3p5IFBhcmssIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDU3OWE3ZjcwYWUxNDkxZDkyZDFhODg3ZmVlODIzOGEuc2V0Q29udGVudChodG1sXzJlOWUxNzhkNGQxNjQyZGM4NTljMTZmNDc2ZTdlODljKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzIwMzYwNTI2NzVhZDRjNjBhN2JmM2NkNGUzN2NiZTFjLmJpbmRQb3B1cChwb3B1cF8wNTc5YTdmNzBhZTE0OTFkOTJkMWE4ODdmZWU4MjM4YSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kOTExYzIyYjM0MDI0MDJkYTQ2ZmU0YzkzMDZiZDVjNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1Nzk1MjQsLTc5LjM4NzM4MjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTU5OTJlOGVlYmExNGQyODhjNThjNDQ5NjMyNzBhYTUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNmNlNzhkMzNhZjc2NGE2MWI5MDU3YTBhYmJmYTgwOTEgPSAkKCc8ZGl2IGlkPSJodG1sXzZjZTc4ZDMzYWY3NjRhNjFiOTA1N2EwYWJiZmE4MDkxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZW50cmFsIEJheSBTdHJlZXQsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTU5OTJlOGVlYmExNGQyODhjNThjNDQ5NjMyNzBhYTUuc2V0Q29udGVudChodG1sXzZjZTc4ZDMzYWY3NjRhNjFiOTA1N2EwYWJiZmE4MDkxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q5MTFjMjJiMzQwMjQwMmRhNDZmZTRjOTMwNmJkNWM1LmJpbmRQb3B1cChwb3B1cF9hNTk5MmU4ZWViYTE0ZDI4OGM1OGM0NDk2MzI3MGFhNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zYzJlMmNlM2M2N2I0YzVhYjhjODlkMTQ1NzlkNDUyZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1MDU3MTIwMDAwMDAxLC03OS4zODQ1Njc1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE5Y2JmYWYwOWVmYTQ4YzJhMDRmM2M2ZWE2ZGYzZmVkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzhmZGM4NDJhMzQ1MDQ3OWY4ZTJjNWJiMGRkMzVlMDkyID0gJCgnPGRpdiBpZD0iaHRtbF84ZmRjODQyYTM0NTA0NzlmOGUyYzViYjBkZDM1ZTA5MiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWRlbGFpZGUsS2luZyxSaWNobW9uZCwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xOWNiZmFmMDllZmE0OGMyYTA0ZjNjNmVhNmRmM2ZlZC5zZXRDb250ZW50KGh0bWxfOGZkYzg0MmEzNDUwNDc5ZjhlMmM1YmIwZGQzNWUwOTIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2MyZTJjZTNjNjdiNGM1YWI4Yzg5ZDE0NTc5ZDQ1MmUuYmluZFBvcHVwKHBvcHVwXzE5Y2JmYWYwOWVmYTQ4YzJhMDRmM2M2ZWE2ZGYzZmVkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U5NzNhY2ExYTIzZDQ5OTJhYmM4MmQ2NThjM2UyMjNiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQwODE1NywtNzkuMzgxNzUyMjk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTFhZDExMzFmY2JjNGM2Y2JjMDEwYTFkM2Y5NzU1ZGEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODU5YTkxZDQ5NDdmNDRmMjlmODRjMmUwMWEzZmJhMTAgPSAkKCc8ZGl2IGlkPSJodG1sXzg1OWE5MWQ0OTQ3ZjQ0ZjI5Zjg0YzJlMDFhM2ZiYTEwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQgRWFzdCxUb3JvbnRvIElzbGFuZHMsVW5pb24gU3RhdGlvbiwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85MWFkMTEzMWZjYmM0YzZjYmMwMTBhMWQzZjk3NTVkYS5zZXRDb250ZW50KGh0bWxfODU5YTkxZDQ5NDdmNDRmMjlmODRjMmUwMWEzZmJhMTApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTk3M2FjYTFhMjNkNDk5MmFiYzgyZDY1OGMzZTIyM2IuYmluZFBvcHVwKHBvcHVwXzkxYWQxMTMxZmNiYzRjNmNiYzAxMGExZDNmOTc1NWRhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzAyMTk3ZWY5NmY4MzQ3M2M5MzczMDc0YTJiNDJjZGI4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ3MTc2OCwtNzkuMzgxNTc2NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmM1ZDNhZGQ3Mjk4NDJlOTkxOTNlODQwMWEwYjM5YjkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWQxYWVhNjFkMjgxNDA1ZThmZmI0MjAzZTJlM2E4ODcgPSAkKCc8ZGl2IGlkPSJodG1sXzVkMWFlYTYxZDI4MTQwNWU4ZmZiNDIwM2UyZTNhODg3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5EZXNpZ24gRXhjaGFuZ2UsVG9yb250byBEb21pbmlvbiBDZW50cmUsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmM1ZDNhZGQ3Mjk4NDJlOTkxOTNlODQwMWEwYjM5Yjkuc2V0Q29udGVudChodG1sXzVkMWFlYTYxZDI4MTQwNWU4ZmZiNDIwM2UyZTNhODg3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzAyMTk3ZWY5NmY4MzQ3M2M5MzczMDc0YTJiNDJjZGI4LmJpbmRQb3B1cChwb3B1cF9mYzVkM2FkZDcyOTg0MmU5OTE5M2U4NDAxYTBiMzliOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kMjhjNTMyZTZiYzQ0MDllYWMzODdlMDBhNzhiNWY1MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY0ODE5ODUsLTc5LjM3OTgxNjkwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2FmNzUzMDZlYjExZTRkNmU4MTMxYjllZTY3MGI2NzEyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI3ZmZlNjMwN2M2YzQ4MzhhY2FjNDMxNDdkN2E2NGYzID0gJCgnPGRpdiBpZD0iaHRtbF8yN2ZmZTYzMDdjNmM0ODM4YWNhYzQzMTQ3ZDdhNjRmMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q29tbWVyY2UgQ291cnQsVmljdG9yaWEgSG90ZWwsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWY3NTMwNmViMTFlNGQ2ZTgxMzFiOWVlNjcwYjY3MTIuc2V0Q29udGVudChodG1sXzI3ZmZlNjMwN2M2YzQ4MzhhY2FjNDMxNDdkN2E2NGYzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2QyOGM1MzJlNmJjNDQwOWVhYzM4N2UwMGE3OGI1ZjUxLmJpbmRQb3B1cChwb3B1cF9hZjc1MzA2ZWIxMWU0ZDZlODEzMWI5ZWU2NzBiNjcxMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNjJhNzVjNTQ0MGQ0ZGM4YmQ5NmNjYzRlNTNlZDcyNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjczMzI4MjUsLTc5LjQxOTc0OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmRhNWUwMmZmNTE0NGJhYWI5ZjZiZDY3ZmI5YTE2N2QgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTc0MzEzMjg4MDdjNDc1MGI5YjJjZTk4ZGMyZGNlNGYgPSAkKCc8ZGl2IGlkPSJodG1sX2U3NDMxMzI4ODA3YzQ3NTBiOWIyY2U5OGRjMmRjZTRmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWRmb3JkIFBhcmssTGF3cmVuY2UgTWFub3IgRWFzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yZGE1ZTAyZmY1MTQ0YmFhYjlmNmJkNjdmYjlhMTY3ZC5zZXRDb250ZW50KGh0bWxfZTc0MzEzMjg4MDdjNDc1MGI5YjJjZTk4ZGMyZGNlNGYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTYyYTc1YzU0NDBkNGRjOGJkOTZjY2M0ZTUzZWQ3MjcuYmluZFBvcHVwKHBvcHVwXzJkYTVlMDJmZjUxNDRiYWFiOWY2YmQ2N2ZiOWExNjdkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI1MTI5YTBkYWVjYzQyY2RiMzFjOTA4NzM3ZWVlNzQ2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzExNjk0OCwtNzkuNDE2OTM1NTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmQxOTc5YjcyYmEzNDhiNjk0M2U4M2YyMWVhNzNiM2QgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDg0NTBjZjg2NzQyNDJjODgwMjIzN2RjZWViZmJiZTEgPSAkKCc8ZGl2IGlkPSJodG1sXzQ4NDUwY2Y4Njc0MjQyYzg4MDIyMzdkY2VlYmZiYmUxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlbGF3biwgQ2VudHJhbFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZkMTk3OWI3MmJhMzQ4YjY5NDNlODNmMjFlYTczYjNkLnNldENvbnRlbnQoaHRtbF80ODQ1MGNmODY3NDI0MmM4ODAyMjM3ZGNlZWJmYmJlMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yNTEyOWEwZGFlY2M0MmNkYjMxYzkwODczN2VlZTc0Ni5iaW5kUG9wdXAocG9wdXBfZmQxOTc5YjcyYmEzNDhiNjk0M2U4M2YyMWVhNzNiM2QpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDdlZWI2MmI0ZmI3NGIwZTgzYzQ4OThjMGQ4NTY5NWYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTY5NDc2LC03OS40MTEzMDcyMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85NDIxYmMyMjlmNDU0YWEwYmQzNTllYjhlMjYyMTdmOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNTA3MWRmMDM1ZjQ0N2I3OWQyM2UwOTRlYjY2OGNkYyA9ICQoJzxkaXYgaWQ9Imh0bWxfMTUwNzFkZjAzNWY0NDdiNzlkMjNlMDk0ZWI2NjhjZGMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZvcmVzdCBIaWxsIE5vcnRoLEZvcmVzdCBIaWxsIFdlc3QsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85NDIxYmMyMjlmNDU0YWEwYmQzNTllYjhlMjYyMTdmOC5zZXRDb250ZW50KGh0bWxfMTUwNzFkZjAzNWY0NDdiNzlkMjNlMDk0ZWI2NjhjZGMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDdlZWI2MmI0ZmI3NGIwZTgzYzQ4OThjMGQ4NTY5NWYuYmluZFBvcHVwKHBvcHVwXzk0MjFiYzIyOWY0NTRhYTBiZDM1OWViOGUyNjIxN2Y4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2JmNGZkYTBhZjg4NTQ5YmZhYTMxOTM3YjlhMmQ1ZTYxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjcyNzA5NywtNzkuNDA1Njc4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGEzYWFkNWU5OGM1NGQzMzlhYjJkMjkwY2Q2M2Q2YmQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDQxNzUyYzE4NWMyNGI3YzhjNjMwMGFmZDI5NTlmMmQgPSAkKCc8ZGl2IGlkPSJodG1sXzQ0MTc1MmMxODVjMjRiN2M4YzYzMDBhZmQyOTU5ZjJkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgQW5uZXgsTm9ydGggTWlkdG93bixZb3JrdmlsbGUsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kYTNhYWQ1ZTk4YzU0ZDMzOWFiMmQyOTBjZDYzZDZiZC5zZXRDb250ZW50KGh0bWxfNDQxNzUyYzE4NWMyNGI3YzhjNjMwMGFmZDI5NTlmMmQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYmY0ZmRhMGFmODg1NDliZmFhMzE5MzdiOWEyZDVlNjEuYmluZFBvcHVwKHBvcHVwX2RhM2FhZDVlOThjNTRkMzM5YWIyZDI5MGNkNjNkNmJkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2FjYjU5YmRlZjMxYjQ2YjE5ZjFjMjU0MWIwZWJhM2ExID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjYyNjk1NiwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80MWVjOWIzZjE1OWY0MzFiYmE5ODlhMDJiMzJjYzk5NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80NGE2NmRiMjRlZDE0NmZiYWNjMjY0Mzc5NGQ4NmFkYiA9ICQoJzxkaXYgaWQ9Imh0bWxfNDRhNjZkYjI0ZWQxNDZmYmFjYzI2NDM3OTRkODZhZGIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhhcmJvcmQsVW5pdmVyc2l0eSBvZiBUb3JvbnRvLCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQxZWM5YjNmMTU5ZjQzMWJiYTk4OWEwMmIzMmNjOTk0LnNldENvbnRlbnQoaHRtbF80NGE2NmRiMjRlZDE0NmZiYWNjMjY0Mzc5NGQ4NmFkYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hY2I1OWJkZWYzMWI0NmIxOWYxYzI1NDFiMGViYTNhMS5iaW5kUG9wdXAocG9wdXBfNDFlYzliM2YxNTlmNDMxYmJhOTg5YTAyYjMyY2M5OTQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmRiOTI2Mzc0NjgzNDk5NWI3ODRlNDk0ZWZmZTAxZDMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTMyMDU3LC03OS40MDAwNDkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE1ODc4MzJhODhjMjQ4OWNhNmZmNWVkNzJmNmE1ZGVmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRmMTk1YmJmMWRjMDRjYWFiNGM3ZDY4NDI1MDA1ZTQ1ID0gJCgnPGRpdiBpZD0iaHRtbF80ZjE5NWJiZjFkYzA0Y2FhYjRjN2Q2ODQyNTAwNWU0NSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2hpbmF0b3duLEdyYW5nZSBQYXJrLEtlbnNpbmd0b24gTWFya2V0LCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzE1ODc4MzJhODhjMjQ4OWNhNmZmNWVkNzJmNmE1ZGVmLnNldENvbnRlbnQoaHRtbF80ZjE5NWJiZjFkYzA0Y2FhYjRjN2Q2ODQyNTAwNWU0NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iZGI5MjYzNzQ2ODM0OTk1Yjc4NGU0OTRlZmZlMDFkMy5iaW5kUG9wdXAocG9wdXBfMTU4NzgzMmE4OGMyNDg5Y2E2ZmY1ZWQ3MmY2YTVkZWYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDg2YTcwMzY4Njk5NDAwMmFlYjg4MTFkNmU2NjQwYzUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Mjg5NDY3LC03OS4zOTQ0MTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzY3ZTYwNjZlNjlhNjQwNmVhNmEzZjU1MWQ1ZjI0MTYyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Q4ZTlkNTU0MjgxYzQzOThhNTVlNjZkYzBlZWZiM2ZiID0gJCgnPGRpdiBpZD0iaHRtbF9kOGU5ZDU1NDI4MWM0Mzk4YTU1ZTY2ZGMwZWVmYjNmYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q04gVG93ZXIsQmF0aHVyc3QgUXVheSxJc2xhbmQgYWlycG9ydCxIYXJib3VyZnJvbnQgV2VzdCxLaW5nIGFuZCBTcGFkaW5hLFJhaWx3YXkgTGFuZHMsU291dGggTmlhZ2FyYSwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82N2U2MDY2ZTY5YTY0MDZlYTZhM2Y1NTFkNWYyNDE2Mi5zZXRDb250ZW50KGh0bWxfZDhlOWQ1NTQyODFjNDM5OGE1NWU2NmRjMGVlZmIzZmIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDg2YTcwMzY4Njk5NDAwMmFlYjg4MTFkNmU2NjQwYzUuYmluZFBvcHVwKHBvcHVwXzY3ZTYwNjZlNjlhNjQwNmVhNmEzZjU1MWQ1ZjI0MTYyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzllOWYwYjlkYzIwNjQ3NWFiZWI1M2NiNzJlY2NjMzdmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ2NDM1MiwtNzkuMzc0ODQ1OTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWQ1MmNiMDQzZTIyNGM3YTgwMDRiMGVjYjlhNDc2NWYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzc4ZGQ2YmY4ZmMyNGE3ZjhiNjliNjU3MzEwY2YzOGYgPSAkKCc8ZGl2IGlkPSJodG1sXzM3OGRkNmJmOGZjMjRhN2Y4YjY5YjY1NzMxMGNmMzhmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdG4gQSBQTyBCb3hlcyAyNSBUaGUgRXNwbGFuYWRlLCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVkNTJjYjA0M2UyMjRjN2E4MDA0YjBlY2I5YTQ3NjVmLnNldENvbnRlbnQoaHRtbF8zNzhkZDZiZjhmYzI0YTdmOGI2OWI2NTczMTBjZjM4Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85ZTlmMGI5ZGMyMDY0NzVhYmViNTNjYjcyZWNjYzM3Zi5iaW5kUG9wdXAocG9wdXBfNWQ1MmNiMDQzZTIyNGM3YTgwMDRiMGVjYjlhNDc2NWYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDJlMDRmZGVlMDkzNDJlYTkxNDFlY2U1MDMxZjQyYTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDg0MjkyLC03OS4zODIyODAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2UyM2VlYzE4NmFhZDQ0MDRiYmQyM2IxYWI2OWFlY2I4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2QzOTVhYjQ5NDIwODQ0YTRhN2NkMmU4NjA1ZDAyOGY4ID0gJCgnPGRpdiBpZD0iaHRtbF9kMzk1YWI0OTQyMDg0NGE0YTdjZDJlODYwNWQwMjhmOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rmlyc3QgQ2FuYWRpYW4gUGxhY2UsVW5kZXJncm91bmQgY2l0eSwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lMjNlZWMxODZhYWQ0NDA0YmJkMjNiMWFiNjlhZWNiOC5zZXRDb250ZW50KGh0bWxfZDM5NWFiNDk0MjA4NDRhNGE3Y2QyZTg2MDVkMDI4ZjgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDJlMDRmZGVlMDkzNDJlYTkxNDFlY2U1MDMxZjQyYTEuYmluZFBvcHVwKHBvcHVwX2UyM2VlYzE4NmFhZDQ0MDRiYmQyM2IxYWI2OWFlY2I4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZlY2UzMmRhMmVjYTQzZTNiN2UxYWIyM2Q4M2Q5MGVlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE4NTE3OTk5OTk5OTk2LC03OS40NjQ3NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iMzI0MTBlZWJiOWQ0NjVkOTgzMTE2OWUwYTdkMTBlYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mOGE1MDE0ZDdjMzU0MjY5YmRlMjYxMGZjYzVhOGE3NiA9ICQoJzxkaXYgaWQ9Imh0bWxfZjhhNTAxNGQ3YzM1NDI2OWJkZTI2MTBmY2M1YThhNzYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIEhlaWdodHMsTGF3cmVuY2UgTWFub3IsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjMyNDEwZWViYjlkNDY1ZDk4MzExNjllMGE3ZDEwZWEuc2V0Q29udGVudChodG1sX2Y4YTUwMTRkN2MzNTQyNjliZGUyNjEwZmNjNWE4YTc2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZlY2UzMmRhMmVjYTQzZTNiN2UxYWIyM2Q4M2Q5MGVlLmJpbmRQb3B1cChwb3B1cF9iMzI0MTBlZWJiOWQ0NjVkOTgzMTE2OWUwYTdkMTBlYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80NzQ4ODYyYTQ1ZTI0MzUxYTM3M2QxNzFmMDc2N2Y0MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcwOTU3NywtNzkuNDQ1MDcyNTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDhkMzE4ZWRmMzI4NGMxMWE2OGU1ODRhMmY1NjExYzAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjZhOGE1ZGVjNGZmNDA0MWIyZTY1ZWJiZmQ1OWRhNDMgPSAkKCc8ZGl2IGlkPSJodG1sX2I2YThhNWRlYzRmZjQwNDFiMmU2NWViYmZkNTlkYTQzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HbGVuY2Fpcm4sIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDhkMzE4ZWRmMzI4NGMxMWE2OGU1ODRhMmY1NjExYzAuc2V0Q29udGVudChodG1sX2I2YThhNWRlYzRmZjQwNDFiMmU2NWViYmZkNTlkYTQzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQ3NDg4NjJhNDVlMjQzNTFhMzczZDE3MWYwNzY3ZjQyLmJpbmRQb3B1cChwb3B1cF8wOGQzMThlZGYzMjg0YzExYTY4ZTU4NGEyZjU2MTFjMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lMDVlNmMyZDM1ZGI0NDE3OTc0Yzc5MDMxOGU5MjI0YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5Mzc4MTMsLTc5LjQyODE5MTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzljMWI4YjlkZTZkNjRjYWY5YmEzMjE2Zjg3YjYyMGY0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2I0N2QxZWQ4ZmMyZjRjMDNiZDQ5YTYyZjgwYWJkNTk1ID0gJCgnPGRpdiBpZD0iaHRtbF9iNDdkMWVkOGZjMmY0YzAzYmQ0OWE2MmY4MGFiZDU5NSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtZXdvb2QtQ2VkYXJ2YWxlLCBZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85YzFiOGI5ZGU2ZDY0Y2FmOWJhMzIxNmY4N2I2MjBmNC5zZXRDb250ZW50KGh0bWxfYjQ3ZDFlZDhmYzJmNGMwM2JkNDlhNjJmODBhYmQ1OTUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTA1ZTZjMmQzNWRiNDQxNzk3NGM3OTAzMThlOTIyNGEuYmluZFBvcHVwKHBvcHVwXzljMWI4YjlkZTZkNjRjYWY5YmEzMjE2Zjg3YjYyMGY0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdjN2U2ODY2NGU1ODQwMDU4YmQ2ODczZDM0N2E4ODg5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg5MDI1NiwtNzkuNDUzNTEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg3OWY4ZDY4NTJlYzRiYWQ4NTEwNGE1NzZmZmNjM2I1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2I5MTVhZTllNDRjMTQ3MmNhMDlkZGY3MTk2ODE2MTAzID0gJCgnPGRpdiBpZD0iaHRtbF9iOTE1YWU5ZTQ0YzE0NzJjYTA5ZGRmNzE5NjgxNjEwMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FsZWRvbmlhLUZhaXJiYW5rcywgWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODc5ZjhkNjg1MmVjNGJhZDg1MTA0YTU3NmZmY2MzYjUuc2V0Q29udGVudChodG1sX2I5MTVhZTllNDRjMTQ3MmNhMDlkZGY3MTk2ODE2MTAzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzdjN2U2ODY2NGU1ODQwMDU4YmQ2ODczZDM0N2E4ODg5LmJpbmRQb3B1cChwb3B1cF84NzlmOGQ2ODUyZWM0YmFkODUxMDRhNTc2ZmZjYzNiNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lYzE5YzI2N2YzMjg0MmE0OWNiMDE2ODc2NWMwZGVmNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2OTU0MiwtNzkuNDIyNTYzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ZGUyM2I5YjJjMjA0ZTY1ODRmZmRhODZiMzFjNDdkNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81M2FkNDgxMGJkNWM0MmZkYWZhOTU1OGNkMTlkNGJlYyA9ICQoJzxkaXYgaWQ9Imh0bWxfNTNhZDQ4MTBiZDVjNDJmZGFmYTk1NThjZDE5ZDRiZWMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNocmlzdGllLCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdkZTIzYjliMmMyMDRlNjU4NGZmZGE4NmIzMWM0N2Q3LnNldENvbnRlbnQoaHRtbF81M2FkNDgxMGJkNWM0MmZkYWZhOTU1OGNkMTlkNGJlYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lYzE5YzI2N2YzMjg0MmE0OWNiMDE2ODc2NWMwZGVmNy5iaW5kUG9wdXAocG9wdXBfN2RlMjNiOWIyYzIwNGU2NTg0ZmZkYTg2YjMxYzQ3ZDcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDY4ODFhN2Y4ZGE5NDdkNzhmMzFmYmQxYmQ1YWEwODAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjkwMDUxMDAwMDAwMSwtNzkuNDQyMjU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83MDM5MDI1ZGYxNjU0MDJlYWJhZmQyMzllOWUxZTc2MSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85M2VhZTA3NjI3ZDE0MzEzYjY0Yzc3Y2E5YjdjZTEyOSA9ICQoJzxkaXYgaWQ9Imh0bWxfOTNlYWUwNzYyN2QxNDMxM2I2NGM3N2NhOWI3Y2UxMjkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvdmVyY291cnQgVmlsbGFnZSxEdWZmZXJpbiwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzcwMzkwMjVkZjE2NTQwMmVhYmFmZDIzOWU5ZTFlNzYxLnNldENvbnRlbnQoaHRtbF85M2VhZTA3NjI3ZDE0MzEzYjY0Yzc3Y2E5YjdjZTEyOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wNjg4MWE3ZjhkYTk0N2Q3OGYzMWZiZDFiZDVhYTA4MC5iaW5kUG9wdXAocG9wdXBfNzAzOTAyNWRmMTY1NDAyZWFiYWZkMjM5ZTllMWU3NjEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZThmYWMwYmIxNzVkNDdlYWE0ODIyZjk5OWUxZjE5YTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDc5MjY3MDAwMDAwMDYsLTc5LjQxOTc0OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmVjN2Y2YjE3ZGY0NDFkOGJiODhiMzE1NjA2ZmE1OWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDdkMDUzM2NjY2NlNDM1MGFhNmUxZmJkNTljZTljNmMgPSAkKCc8ZGl2IGlkPSJodG1sXzQ3ZDA1MzNjY2NjZTQzNTBhYTZlMWZiZDU5Y2U5YzZjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5MaXR0bGUgUG9ydHVnYWwsVHJpbml0eSwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2JlYzdmNmIxN2RmNDQxZDhiYjg4YjMxNTYwNmZhNTljLnNldENvbnRlbnQoaHRtbF80N2QwNTMzY2NjY2U0MzUwYWE2ZTFmYmQ1OWNlOWM2Yyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lOGZhYzBiYjE3NWQ0N2VhYTQ4MjJmOTk5ZTFmMTlhOC5iaW5kUG9wdXAocG9wdXBfYmVjN2Y2YjE3ZGY0NDFkOGJiODhiMzE1NjA2ZmE1OWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmI0YjM1ODA1YzNhNDY2OWE4OTM5YzE5MjIwYjJkNDEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MzY4NDcyLC03OS40MjgxOTE0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mY2Q1OWQ3NjBkZDg0MjhmOGFkZmIzZjUxOWE2Mzk3ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lZjkyOWVkNDkwMzI0NmY5YWI5MGZiOGE4NzM1ZWNkYSA9ICQoJzxkaXYgaWQ9Imh0bWxfZWY5MjllZDQ5MDMyNDZmOWFiOTBmYjhhODczNWVjZGEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJyb2NrdG9uLEV4aGliaXRpb24gUGxhY2UsUGFya2RhbGUgVmlsbGFnZSwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZjZDU5ZDc2MGRkODQyOGY4YWRmYjNmNTE5YTYzOTdmLnNldENvbnRlbnQoaHRtbF9lZjkyOWVkNDkwMzI0NmY5YWI5MGZiOGE4NzM1ZWNkYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yYjRiMzU4MDVjM2E0NjY5YTg5MzljMTkyMjBiMmQ0MS5iaW5kUG9wdXAocG9wdXBfZmNkNTlkNzYwZGQ4NDI4ZjhhZGZiM2Y1MTlhNjM5N2YpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODI3ZDY1YTcwNmQxNDRjM2I5YTIzMGJmMjRlNjg5NmQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MTM3NTYyMDAwMDAwMDYsLTc5LjQ5MDA3MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGQ5MWQyYTVhZjYzNDMyNzllOGYwM2VjZjg5NzhlNzAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMWVhYTE4YTJlZjZhNGMwN2E1NWE5MzM0NTY1NWIxMzcgPSAkKCc8ZGl2IGlkPSJodG1sXzFlYWExOGEyZWY2YTRjMDdhNTVhOTMzNDU2NTViMTM3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb3duc3ZpZXcsTm9ydGggUGFyayxVcHdvb2QgUGFyaywgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kZDkxZDJhNWFmNjM0MzI3OWU4ZjAzZWNmODk3OGU3MC5zZXRDb250ZW50KGh0bWxfMWVhYTE4YTJlZjZhNGMwN2E1NWE5MzM0NTY1NWIxMzcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODI3ZDY1YTcwNmQxNDRjM2I5YTIzMGJmMjRlNjg5NmQuYmluZFBvcHVwKHBvcHVwX2RkOTFkMmE1YWY2MzQzMjc5ZThmMDNlY2Y4OTc4ZTcwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y1ZDNlMTk0Y2M2YzRmMGI4NTcyNGQwNTc3YmEwZGQ2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjkxMTE1OCwtNzkuNDc2MDEzMjk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfY2YwZjk1NDk3ODMwNGY5MWFmOGYyNGU2ZmZkZDc3MTMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjk4YWMyYmZkYzIxNDU0MGFhYjQxZTc1YzM5ZWIyN2MgPSAkKCc8ZGl2IGlkPSJodG1sX2I5OGFjMmJmZGMyMTQ1NDBhYWI0MWU3NWMzOWViMjdjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5EZWwgUmF5LEtlZWxlc2RhbGUsTW91bnQgRGVubmlzLFNpbHZlcnRob3JuLCBZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jZjBmOTU0OTc4MzA0ZjkxYWY4ZjI0ZTZmZmRkNzcxMy5zZXRDb250ZW50KGh0bWxfYjk4YWMyYmZkYzIxNDU0MGFhYjQxZTc1YzM5ZWIyN2MpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjVkM2UxOTRjYzZjNGYwYjg1NzI0ZDA1NzdiYTBkZDYuYmluZFBvcHVwKHBvcHVwX2NmMGY5NTQ5NzgzMDRmOTFhZjhmMjRlNmZmZGQ3NzEzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZmYWVmNmJhNmI4NjQzYzQ5MWU1Mzg0YzY5OTMwYTZjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjczMTg1Mjk5OTk5OTksLTc5LjQ4NzI2MTkwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M5NjM3ZmFkMmU3ZDRiOGU5MTkzZWFlZmYxNzVkOGFlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Y5MGYwYmE0ZTgzZDRiODI5YTFkMDI0ZDQxODU4OGMyID0gJCgnPGRpdiBpZD0iaHRtbF9mOTBmMGJhNGU4M2Q0YjgyOWExZDAyNGQ0MTg1ODhjMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhlIEp1bmN0aW9uIE5vcnRoLFJ1bm55bWVkZSwgWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzk2MzdmYWQyZTdkNGI4ZTkxOTNlYWVmZjE3NWQ4YWUuc2V0Q29udGVudChodG1sX2Y5MGYwYmE0ZTgzZDRiODI5YTFkMDI0ZDQxODU4OGMyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZmYWVmNmJhNmI4NjQzYzQ5MWU1Mzg0YzY5OTMwYTZjLmJpbmRQb3B1cChwb3B1cF9jOTYzN2ZhZDJlN2Q0YjhlOTE5M2VhZWZmMTc1ZDhhZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNGNjZjM3ZDkxMzQ0ZmNmOTM2YzU4ZWU4NGQ3MDIwMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MTYwODMsLTc5LjQ2NDc2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2JjNGM0ZThiNDhlNzQ1NzNiMTA2NTY4OGQxMDMyMDg4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzBkODAxNjU1YzkwYjQ1YmE5MjY5N2MyMDg1NmUzNTIwID0gJCgnPGRpdiBpZD0iaHRtbF8wZDgwMTY1NWM5MGI0NWJhOTI2OTdjMjA4NTZlMzUyMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaCBQYXJrLFRoZSBKdW5jdGlvbiBTb3V0aCwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2JjNGM0ZThiNDhlNzQ1NzNiMTA2NTY4OGQxMDMyMDg4LnNldENvbnRlbnQoaHRtbF8wZDgwMTY1NWM5MGI0NWJhOTI2OTdjMjA4NTZlMzUyMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kNGNjZjM3ZDkxMzQ0ZmNmOTM2YzU4ZWU4NGQ3MDIwMS5iaW5kUG9wdXAocG9wdXBfYmM0YzRlOGI0OGU3NDU3M2IxMDY1Njg4ZDEwMzIwODgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZWY2YjQ5N2ZkNzI0NDBiM2FhY2NjZTkwMmI2Y2FmNzQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDg5NTk3LC03OS40NTYzMjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmQ1ZmMwNzUwNmIyNGE1ZDllZjEwZGQ0ZTJjNDVlMGQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMmY4MWJhNTZkNDViNDlmNDliYzRkMzk0NTU1NTI1NDMgPSAkKCc8ZGl2IGlkPSJodG1sXzJmODFiYTU2ZDQ1YjQ5ZjQ5YmM0ZDM5NDU1NTUyNTQzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrZGFsZSxSb25jZXN2YWxsZXMsIFdlc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iZDVmYzA3NTA2YjI0YTVkOWVmMTBkZDRlMmM0NWUwZC5zZXRDb250ZW50KGh0bWxfMmY4MWJhNTZkNDViNDlmNDliYzRkMzk0NTU1NTI1NDMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZWY2YjQ5N2ZkNzI0NDBiM2FhY2NjZTkwMmI2Y2FmNzQuYmluZFBvcHVwKHBvcHVwX2JkNWZjMDc1MDZiMjRhNWQ5ZWYxMGRkNGUyYzQ1ZTBkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhiMGFjZTY1MGU0MzRkMjVhZTE4NDZjZWE5YmRlZTUzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUxNTcwNiwtNzkuNDg0NDQ5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iYmJjY2U1MzNiODM0MmZiODM5Y2M5NTZlNmJiMzA1MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83ZWM4MzFmYmQ5NzY0MjJhODk2ZTdiNjVkNDFjMTkxZSA9ICQoJzxkaXYgaWQ9Imh0bWxfN2VjODMxZmJkOTc2NDIyYTg5NmU3YjY1ZDQxYzE5MWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJ1bm55bWVkZSxTd2Fuc2VhLCBXZXN0VG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYmJiY2NlNTMzYjgzNDJmYjgzOWNjOTU2ZTZiYjMwNTIuc2V0Q29udGVudChodG1sXzdlYzgzMWZiZDk3NjQyMmE4OTZlN2I2NWQ0MWMxOTFlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhiMGFjZTY1MGU0MzRkMjVhZTE4NDZjZWE5YmRlZTUzLmJpbmRQb3B1cChwb3B1cF9iYmJjY2U1MzNiODM0MmZiODM5Y2M5NTZlNmJiMzA1Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jZGNhYjQ2Yjc3NDI0YWY5ODMwODI0ZWI0MTc5NmJjZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MjMwMTUsLTc5LjM4OTQ5MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjNiODEzMmFjYjM5NDkyNWFlZmJiNzZjNTk3ZWY5ZDIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmY3NWIxZjlhNjAzNGQ3NjhhOWFjMDlmNjk5YmRkOTkgPSAkKCc8ZGl2IGlkPSJodG1sX2ZmNzViMWY5YTYwMzRkNzY4YTlhYzA5ZjY5OWJkZDk5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5RdWVlbiYjMzk7cyBQYXJrLCBRdWVlbiYjMzk7c1Bhcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2YzYjgxMzJhY2IzOTQ5MjVhZWZiYjc2YzU5N2VmOWQyLnNldENvbnRlbnQoaHRtbF9mZjc1YjFmOWE2MDM0ZDc2OGE5YWMwOWY2OTliZGQ5OSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jZGNhYjQ2Yjc3NDI0YWY5ODMwODI0ZWI0MTc5NmJjZS5iaW5kUG9wdXAocG9wdXBfZjNiODEzMmFjYjM5NDkyNWFlZmJiNzZjNTk3ZWY5ZDIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfM2I1ODk1NDgyNzEzNDM5Mjg0OTEwYzljODA0NTI1NjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MzY5NjU2LC03OS42MTU4MTg5OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80NTMzMzRhOGVhMzI0ZDg2OGE3M2JhNjE3ZGZmNDlhMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83MWViMTRmYzJlNjg0ODkzYWJlY2M5ZDUzMzgyOWY3MyA9ICQoJzxkaXYgaWQ9Imh0bWxfNzFlYjE0ZmMyZTY4NDg5M2FiZWNjOWQ1MzM4MjlmNzMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNhbmFkYSBQb3N0IEdhdGV3YXkgUHJvY2Vzc2luZyBDZW50cmUsIE1pc3Npc3NhdWdhPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80NTMzMzRhOGVhMzI0ZDg2OGE3M2JhNjE3ZGZmNDlhMS5zZXRDb250ZW50KGh0bWxfNzFlYjE0ZmMyZTY4NDg5M2FiZWNjOWQ1MzM4MjlmNzMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2I1ODk1NDgyNzEzNDM5Mjg0OTEwYzljODA0NTI1NjcuYmluZFBvcHVwKHBvcHVwXzQ1MzMzNGE4ZWEzMjRkODY4YTczYmE2MTdkZmY0OWExKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdiZjQ5ZWVjY2EyZjQ3NzQ5OWY3MzUyYjRlMDUzMGIzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjYyNzQzOSwtNzkuMzIxNTU4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzVjZDZlZDRhNDMyOTQ3MTdiZTg1M2NiNGQzNWY4YzEwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzcwN2M3Y2M1YTlkYjQyOGI4OTQ0YmVlNzE3OTg2YTcxID0gJCgnPGRpdiBpZD0iaHRtbF83MDdjN2NjNWE5ZGI0MjhiODk0NGJlZTcxNzk4NmE3MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnVzaW5lc3MgUmVwbHkgTWFpbCBQcm9jZXNzaW5nIENlbnRyZSA5NjkgRWFzdGVybiwgRWFzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVjZDZlZDRhNDMyOTQ3MTdiZTg1M2NiNGQzNWY4YzEwLnNldENvbnRlbnQoaHRtbF83MDdjN2NjNWE5ZGI0MjhiODk0NGJlZTcxNzk4NmE3MSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83YmY0OWVlY2NhMmY0Nzc0OTlmNzM1MmI0ZTA1MzBiMy5iaW5kUG9wdXAocG9wdXBfNWNkNmVkNGE0MzI5NDcxN2JlODUzY2I0ZDM1ZjhjMTApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWI3MmRlZTYzYzBjNGVkMDk1ZmM2ZGRiZDM2MDYwZGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MDU2NDY2LC03OS41MDEzMjA3MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82NmU1NWYzOThiMDM0YzQ3YTU4YWQ1N2I0MzBiMmI0YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zMTM5NzI4OGZkMjE0ZjhlYTJmNGEwZjBiYWE2OTY2NiA9ICQoJzxkaXYgaWQ9Imh0bWxfMzEzOTcyODhmZDIxNGY4ZWEyZjRhMGYwYmFhNjk2NjYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWJlciBCYXkgU2hvcmVzLE1pbWljbyBTb3V0aCxOZXcgVG9yb250bywgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82NmU1NWYzOThiMDM0YzQ3YTU4YWQ1N2I0MzBiMmI0YS5zZXRDb250ZW50KGh0bWxfMzEzOTcyODhmZDIxNGY4ZWEyZjRhMGYwYmFhNjk2NjYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMWI3MmRlZTYzYzBjNGVkMDk1ZmM2ZGRiZDM2MDYwZGYuYmluZFBvcHVwKHBvcHVwXzY2ZTU1ZjM5OGIwMzRjNDdhNThhZDU3YjQzMGIyYjRhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RiMzA1Mzk5OGZiNTQ0YWFhZWI3NzJkNWQwMzJmNzk2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjAyNDEzNzAwMDAwMDEsLTc5LjU0MzQ4NDA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRiZDFmZTA4YmU2OTQ0NjRiZGUzMDIyMWI3NTM1ZWI1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzMyZTljMmVmYThiYjQyZDliMTIxZjY2YWRkM2Y0YTdhID0gJCgnPGRpdiBpZD0iaHRtbF8zMmU5YzJlZmE4YmI0MmQ5YjEyMWY2NmFkZDNmNGE3YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWxkZXJ3b29kLExvbmcgQnJhbmNoLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRiZDFmZTA4YmU2OTQ0NjRiZGUzMDIyMWI3NTM1ZWI1LnNldENvbnRlbnQoaHRtbF8zMmU5YzJlZmE4YmI0MmQ5YjEyMWY2NmFkZDNmNGE3YSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kYjMwNTM5OThmYjU0NGFhYWViNzcyZDVkMDMyZjc5Ni5iaW5kUG9wdXAocG9wdXBfNGJkMWZlMDhiZTY5NDQ2NGJkZTMwMjIxYjc1MzVlYjUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDk4M2JjZjRkOWNmNGQ3OWEyZDc5ZWQzOWQ4NzU0NTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTM2NTM2MDAwMDAwMDUsLTc5LjUwNjk0MzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzljMjMyMGI5YzQ2NDQxN2FkMGIxNDQ2NmU5NzNiY2QgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYmUyNTBlNmNhMWVjNDRlNmJmYjFmMTBlODc0OTNiMmYgPSAkKCc8ZGl2IGlkPSJodG1sX2JlMjUwZTZjYTFlYzQ0ZTZiZmIxZjEwZTg3NDkzYjJmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgS2luZ3N3YXksTW9udGdvbWVyeSBSb2FkLE9sZCBNaWxsIE5vcnRoLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzM5YzIzMjBiOWM0NjQ0MTdhZDBiMTQ0NjZlOTczYmNkLnNldENvbnRlbnQoaHRtbF9iZTI1MGU2Y2ExZWM0NGU2YmZiMWYxMGU4NzQ5M2IyZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80OTgzYmNmNGQ5Y2Y0ZDc5YTJkNzllZDM5ZDg3NTQ1MS5iaW5kUG9wdXAocG9wdXBfMzljMjMyMGI5YzQ2NDQxN2FkMGIxNDQ2NmU5NzNiY2QpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmNjODBhMjRjNTEyNGY2Nzg0MjU0Njk4YWYzMTdhYjkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MzYyNTc5LC03OS40OTg1MDkwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yN2M1YmVmOTkyMzE0ZGQ0YmE5Mzk0ZjNiZmQ4NWFmZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83ZmFmMDA3N2IzMGM0MmU0ODYzNGUwMjMwMDk1OTkxMSA9ICQoJzxkaXYgaWQ9Imh0bWxfN2ZhZjAwNzdiMzBjNDJlNDg2MzRlMDIzMDA5NTk5MTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWJlciBCYXksS2luZyYjMzk7cyBNaWxsIFBhcmssS2luZ3N3YXkgUGFyayBTb3V0aCBFYXN0LE1pbWljbyBORSxPbGQgTWlsbCBTb3V0aCxUaGUgUXVlZW5zd2F5IEVhc3QsUm95YWwgWW9yayBTb3V0aCBFYXN0LFN1bm55bGVhLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI3YzViZWY5OTIzMTRkZDRiYTkzOTRmM2JmZDg1YWZkLnNldENvbnRlbnQoaHRtbF83ZmFmMDA3N2IzMGM0MmU0ODYzNGUwMjMwMDk1OTkxMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mY2M4MGEyNGM1MTI0ZjY3ODQyNTQ2OThhZjMxN2FiOS5iaW5kUG9wdXAocG9wdXBfMjdjNWJlZjk5MjMxNGRkNGJhOTM5NGYzYmZkODVhZmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzZiYTA5OWUxY2U5NGI3OGE3Y2M5NWZjYjVkNzFmNmEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Mjg4NDA4LC03OS41MjA5OTk0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84MmE5Y2VlODk4ODI0YTAyYjQ3YmUzNDE3NGMyZjRkYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mMmZlNjg4MTg0ZDc0ZmEzYTU0NmVmZTllMTA4MDg5ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfZjJmZTY4ODE4NGQ3NGZhM2E1NDZlZmU5ZTEwODA4OWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPktpbmdzd2F5IFBhcmsgU291dGggV2VzdCxNaW1pY28gTlcsVGhlIFF1ZWVuc3dheSBXZXN0LFJveWFsIFlvcmsgU291dGggV2VzdCxTb3V0aCBvZiBCbG9vciwgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MmE5Y2VlODk4ODI0YTAyYjQ3YmUzNDE3NGMyZjRkYS5zZXRDb250ZW50KGh0bWxfZjJmZTY4ODE4NGQ3NGZhM2E1NDZlZmU5ZTEwODA4OWUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzZiYTA5OWUxY2U5NGI3OGE3Y2M5NWZjYjVkNzFmNmEuYmluZFBvcHVwKHBvcHVwXzgyYTljZWU4OTg4MjRhMDJiNDdiZTM0MTc0YzJmNGRhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZmYTdiODU2NGEzMTQ0YzNiNTg5ZGVmMzU0YjJmNWRlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY3ODU1NiwtNzkuNTMyMjQyNDAwMDAwMDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWY1NWE2ZTU0NTVhNGQyZmE1ODRjNTRjM2JiZmU4YTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjdkZTFlZWNhZTU5NDM2N2JlNzJjNGFmYTY2OGZjMWMgPSAkKCc8ZGl2IGlkPSJodG1sX2Y3ZGUxZWVjYWU1OTQzNjdiZTcyYzRhZmE2NjhmYzFjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Jc2xpbmd0b24gQXZlbnVlLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVmNTVhNmU1NDU1YTRkMmZhNTg0YzU0YzNiYmZlOGE2LnNldENvbnRlbnQoaHRtbF9mN2RlMWVlY2FlNTk0MzY3YmU3MmM0YWZhNjY4ZmMxYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82ZmE3Yjg1NjRhMzE0NGMzYjU4OWRlZjM1NGIyZjVkZS5iaW5kUG9wdXAocG9wdXBfNWY1NWE2ZTU0NTVhNGQyZmE1ODRjNTRjM2JiZmU4YTYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2MxYjcxOWFlYTQ5NGIyMWJjMmI2NWNkMWMwYzczOTYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTA5NDMyLC03OS41NTQ3MjQ0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lOTA5ZDU2YTJhNDc0NmVkYjgyOWEzMjcxM2U2NmEzMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wZTVkMDFhMmQxMzE0NzhjOWJlOTc1ZjcwZTM2MTIxZSA9ICQoJzxkaXYgaWQ9Imh0bWxfMGU1ZDAxYTJkMTMxNDc4YzliZTk3NWY3MGUzNjEyMWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsb3ZlcmRhbGUsSXNsaW5ndG9uLE1hcnRpbiBHcm92ZSxQcmluY2VzcyBHYXJkZW5zLFdlc3QgRGVhbmUgUGFyaywgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lOTA5ZDU2YTJhNDc0NmVkYjgyOWEzMjcxM2U2NmEzMy5zZXRDb250ZW50KGh0bWxfMGU1ZDAxYTJkMTMxNDc4YzliZTk3NWY3MGUzNjEyMWUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfY2MxYjcxOWFlYTQ5NGIyMWJjMmI2NWNkMWMwYzczOTYuYmluZFBvcHVwKHBvcHVwX2U5MDlkNTZhMmE0NzQ2ZWRiODI5YTMyNzEzZTY2YTMzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzYzMzkwMjNmOWQ4MTQwMDk5MDlkNzdlMjU3NzQzNTU0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQzNTE1MiwtNzkuNTc3MjAwNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDg3MjAzZTQ4OTMwNDdjNDgxZDkxOTMzMDY0MTNjMGYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMmNjMTBhNTYyODY4NGY4OWE4MTdmZGMyMjI3ZDU2M2UgPSAkKCc8ZGl2IGlkPSJodG1sXzJjYzEwYTU2Mjg2ODRmODlhODE3ZmRjMjIyN2Q1NjNlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CbG9vcmRhbGUgR2FyZGVucyxFcmluZ2F0ZSxNYXJrbGFuZCBXb29kLE9sZCBCdXJuaGFtdGhvcnBlLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzA4NzIwM2U0ODkzMDQ3YzQ4MWQ5MTkzMzA2NDEzYzBmLnNldENvbnRlbnQoaHRtbF8yY2MxMGE1NjI4Njg0Zjg5YTgxN2ZkYzIyMjdkNTYzZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82MzM5MDIzZjlkODE0MDA5OTA5ZDc3ZTI1Nzc0MzU1NC5iaW5kUG9wdXAocG9wdXBfMDg3MjAzZTQ4OTMwNDdjNDgxZDkxOTMzMDY0MTNjMGYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTE5N2M1MDg5YWQ1NDZkNWEwZGY1NWQyMDU4NmMzZjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTYzMDMzLC03OS41NjU5NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kNDMwZGFlZTc2Nzc0ZTAwYWFiZDM4Y2Y3NjhlODEzMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81ZWM5ODJjYTZmMTI0NjkyOThmOWQ4NDE3ZjFmZTA3ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfNWVjOTgyY2E2ZjEyNDY5Mjk4ZjlkODQxN2YxZmUwN2YiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWJlciBTdW1taXQsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDQzMGRhZWU3Njc3NGUwMGFhYmQzOGNmNzY4ZTgxMzAuc2V0Q29udGVudChodG1sXzVlYzk4MmNhNmYxMjQ2OTI5OGY5ZDg0MTdmMWZlMDdmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ExOTdjNTA4OWFkNTQ2ZDVhMGRmNTVkMjA1ODZjM2Y4LmJpbmRQb3B1cChwb3B1cF9kNDMwZGFlZTc2Nzc0ZTAwYWFiZDM4Y2Y3NjhlODEzMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kZjg1YzBiZTA4OGI0NTFjYjBjMGY5MDU1NGQ2OTIyNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNDc2NTksLTc5LjUzMjI0MjQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzEwMTI2ODE3MTFhYjQ3ZTRhNjQwOGY5NDg4MzlhOWM5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNhOTJmODNkNjA5ZDQxNjVhYzBiMzNhZTAyYjUxNjRlID0gJCgnPGRpdiBpZD0iaHRtbF8zYTkyZjgzZDYwOWQ0MTY1YWMwYjMzYWUwMmI1MTY0ZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RW1lcnksSHVtYmVybGVhLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzEwMTI2ODE3MTFhYjQ3ZTRhNjQwOGY5NDg4MzlhOWM5LnNldENvbnRlbnQoaHRtbF8zYTkyZjgzZDYwOWQ0MTY1YWMwYjMzYWUwMmI1MTY0ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kZjg1YzBiZTA4OGI0NTFjYjBjMGY5MDU1NGQ2OTIyNC5iaW5kUG9wdXAocG9wdXBfMTAxMjY4MTcxMWFiNDdlNGE2NDA4Zjk0ODgzOWE5YzkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjA0NjI5ZDc0YjVlNGY4OWE3ZmFjNDFiNzY2NjJjM2IgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MDY4NzYsLTc5LjUxODE4ODQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA3YjkyOGUxZDNkYTRhNzY4ZTk3NGJlOGI4Y2I5NmU0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzA4NGFjOGMxZTNjYjQ0ODk5NGMxMWM2ODU3YjQ1ZmUzID0gJCgnPGRpdiBpZD0iaHRtbF8wODRhYzhjMWUzY2I0NDg5OTRjMTFjNjg1N2I0NWZlMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2VzdG9uLCBZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wN2I5MjhlMWQzZGE0YTc2OGU5NzRiZThiOGNiOTZlNC5zZXRDb250ZW50KGh0bWxfMDg0YWM4YzFlM2NiNDQ4OTk0YzExYzY4NTdiNDVmZTMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjA0NjI5ZDc0YjVlNGY4OWE3ZmFjNDFiNzY2NjJjM2IuYmluZFBvcHVwKHBvcHVwXzA3YjkyOGUxZDNkYTRhNzY4ZTk3NGJlOGI4Y2I5NmU0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M2NDQ1YWZkYTAxYjQ3NjVhNGQ0YmQ1NGYzYTNhNzgxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjk2MzE5LC03OS41MzIyNDI0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNiwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8wMTE5M2MxNDgxNzY0YTc5ODFmZjQxMjk0MjczZDhmYyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kMzBiYmY5OTZkNTk0ZDVhOWFkZjY5ZTViMzgyOTc1MyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83ODU3NDMzMmI2NGI0MjIzYThkOGVlYmVjNGQ5YjBmMyA9ICQoJzxkaXYgaWQ9Imh0bWxfNzg1NzQzMzJiNjRiNDIyM2E4ZDhlZWJlYzRkOWIwZjMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldlc3Rtb3VudCwgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kMzBiYmY5OTZkNTk0ZDVhOWFkZjY5ZTViMzgyOTc1My5zZXRDb250ZW50KGh0bWxfNzg1NzQzMzJiNjRiNDIyM2E4ZDhlZWJlYzRkOWIwZjMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzY0NDVhZmRhMDFiNDc2NWE0ZDRiZDU0ZjNhM2E3ODEuYmluZFBvcHVwKHBvcHVwX2QzMGJiZjk5NmQ1OTRkNWE5YWRmNjllNWIzODI5NzUzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNhN2UyNWIxYzkwZjRlYjk5YzU0MWZjMmE3NDlhYjZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg4OTA1NCwtNzkuNTU0NzI0NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTIxZWJhOGJkYTFmNDEwYmE3Y2M0NmE1NDZjYzYxZGUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGVlODc0MDU5OGE2NDY1NmIyNjlmMTNiZDdkYzlkOWUgPSAkKCc8ZGl2IGlkPSJodG1sXzRlZTg3NDA1OThhNjQ2NTZiMjY5ZjEzYmQ3ZGM5ZDllIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc3ZpZXcgVmlsbGFnZSxNYXJ0aW4gR3JvdmUgR2FyZGVucyxSaWNodmlldyBHYXJkZW5zLFN0LiBQaGlsbGlwcywgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81MjFlYmE4YmRhMWY0MTBiYTdjYzQ2YTU0NmNjNjFkZS5zZXRDb250ZW50KGh0bWxfNGVlODc0MDU5OGE2NDY1NmIyNjlmMTNiZDdkYzlkOWUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2E3ZTI1YjFjOTBmNGViOTljNTQxZmMyYTc0OWFiNmEuYmluZFBvcHVwKHBvcHVwXzUyMWViYThiZGExZjQxMGJhN2NjNDZhNTQ2Y2M2MWRlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzA1YTY1YWY0NWFiZjQxMjQ5MjA4MjQ0NmI0N2VkMWE3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzM5NDE2Mzk5OTk5OTk2LC03OS41ODg0MzY5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA2LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzAxMTkzYzE0ODE3NjRhNzk4MWZmNDEyOTQyNzNkOGZjKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M1ZjA2YzJiZTFlYjRkOGE4MDJhYmZlMzRhM2E5YjI3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQyOThlMTM1YTA0YjQ4NDRiZWI3MTlmZDRiMTFkNTExID0gJCgnPGRpdiBpZD0iaHRtbF80Mjk4ZTEzNWEwNGI0ODQ0YmViNzE5ZmQ0YjExZDUxMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWxiaW9uIEdhcmRlbnMsQmVhdW1vbmQgSGVpZ2h0cyxIdW1iZXJnYXRlLEphbWVzdG93bixNb3VudCBPbGl2ZSxTaWx2ZXJzdG9uZSxTb3V0aCBTdGVlbGVzLFRoaXN0bGV0b3duLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M1ZjA2YzJiZTFlYjRkOGE4MDJhYmZlMzRhM2E5YjI3LnNldENvbnRlbnQoaHRtbF80Mjk4ZTEzNWEwNGI0ODQ0YmViNzE5ZmQ0YjExZDUxMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wNWE2NWFmNDVhYmY0MTI0OTIwODI0NDZiNDdlZDFhNy5iaW5kUG9wdXAocG9wdXBfYzVmMDZjMmJlMWViNGQ4YTgwMmFiZmUzNGEzYTliMjcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjcxY2E5MDM5OWEyNGVkZGI1YzhmZTViNjhmNjg1ODMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MDY3NDgyOTk5OTk5OTQsLTc5LjU5NDA1NDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDYsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMDExOTNjMTQ4MTc2NGE3OTgxZmY0MTI5NDI3M2Q4ZmMpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzIxOTgwMDYwNmZiNDM5YmI0MmI2NDRjNDJhMjg3Y2MgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODRiNjFhNTU4YTg4NGQxODk3MjQ2NmVhYTAxYzhkMTAgPSAkKCc8ZGl2IGlkPSJodG1sXzg0YjYxYTU1OGE4ODRkMTg5NzI0NjZlYWEwMWM4ZDEwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aHdlc3QsIEV0b2JpY29rZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzIxOTgwMDYwNmZiNDM5YmI0MmI2NDRjNDJhMjg3Y2Muc2V0Q29udGVudChodG1sXzg0YjYxYTU1OGE4ODRkMTg5NzI0NjZlYWEwMWM4ZDEwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2I3MWNhOTAzOTlhMjRlZGRiNWM4ZmU1YjY4ZjY4NTgzLmJpbmRQb3B1cChwb3B1cF9jMjE5ODAwNjA2ZmI0MzliYjQyYjY0NGM0MmEyODdjYyk7CgogICAgICAgICAgICAKICAgICAgICAKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



Using Foursquare API to explore the neighborhoods
=================================================

.. code:: ipython3

    # @hidden_cell
    CLIENT_ID = 'XMCICN4YC1PQCMXSJEA2YVR5PRAC4N22MLOUV115WCWNA1HW' 
    CLIENT_SECRET = '2VYYN4JX2SG1NTZUOGDOCKY1MRM12V40FV5KYFBMQUBLWRFY'
    VERSION = '20180605'
    radius=500
    url = 'https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&ll={},{}&v={}&radius={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, radius)
    results = requests.get(url).json()

Define a function to get the category

.. code:: ipython3

    def get_category_type(row):
        try:
            categories_list = row['categories']
        except:
            categories_list = row['venue.categories']
            
        if len(categories_list) == 0:
            return None
        else:
            return categories_list[0]['name']

Using the get\_category\_type function, we clean up the json and turn it
into a pandas DF. Before we start we need to import certain libraries.

.. code:: ipython3

    import json
    from pandas.io.json import json_normalize 

.. code:: ipython3

    venues = results['response']['groups'][0]['items']
       
    nearby_venues = json_normalize(venues) # flatten JSON
    
    filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
    nearby_venues =nearby_venues.loc[:, filtered_columns]
    
    nearby_venues['venue.categories'] = nearby_venues.apply(get_category_type, axis=1)
    
    nearby_venues.columns = [col.split(".")[-1] for col in nearby_venues.columns]
    
    nearby_venues.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>name</th>
          <th>categories</th>
          <th>lat</th>
          <th>lng</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Downtown Toronto</td>
          <td>Neighborhood</td>
          <td>43.653232</td>
          <td>-79.385296</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Japango</td>
          <td>Sushi Restaurant</td>
          <td>43.655268</td>
          <td>-79.385165</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Cafe Plenty</td>
          <td>Café</td>
          <td>43.654571</td>
          <td>-79.389450</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Sansotei Ramen 三草亭</td>
          <td>Ramen Restaurant</td>
          <td>43.655157</td>
          <td>-79.386501</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Rolltation</td>
          <td>Japanese Restaurant</td>
          <td>43.654918</td>
          <td>-79.387424</td>
        </tr>
      </tbody>
    </table>
    </div>



Now we explore the nearby venues!

.. code:: ipython3

    def getNearbyVenues(names, latitudes, longitudes, radius=500):
        
        venues_list=[]
        for name, lat, lng in zip(names, latitudes, longitudes):
            print(name)
          
            url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}'.format(
                CLIENT_ID, 
                CLIENT_SECRET, 
                VERSION, 
                lat, 
                lng, 
                radius)
                
            results = requests.get(url).json()["response"]['groups'][0]['items']
            
            # return only relevant information for each nearby venue
            venues_list.append([(
                name, 
                lat, 
                lng, 
                v['venue']['name'], 
                v['venue']['location']['lat'], 
                v['venue']['location']['lng'],  
                v['venue']['categories'][0]['name']) for v in results])
    
        nearby_venues = pd.DataFrame([item for venue_list in venues_list for item in venue_list])
        nearby_venues.columns = ['Neighborhood', 
                      'Neighborhood Latitude', 
                      'Neighborhood Longitude', 
                      'Venue', 
                      'Venue Latitude', 
                      'Venue Longitude', 
                      'Venue Category']
        
        return(nearby_venues)

.. code:: ipython3

    toronto_venues = getNearbyVenues(names=df_5['Neighbourhood'],
                                       latitudes=df_5['Latitude'],
                                       longitudes=df_5['Longitude']
                                      )


.. parsed-literal::

    Rouge,Malvern
    Highland Creek,Rouge Hill,Port Union
    Guildwood,Morningside,West Hill
    Woburn
    Cedarbrae
    Scarborough Village
    East Birchmount Park,Ionview,Kennedy Park
    Clairlea,Golden Mile,Oakridge
    Cliffcrest,Cliffside,Scarborough Village West
    Birch Cliff,Cliffside West
    Dorset Park,Scarborough Town Centre,Wexford Heights
    Maryvale,Wexford
    Agincourt
    Clarks Corners,Sullivan,Tam O'Shanter
    Agincourt North,L'Amoreaux East,Milliken,Steeles East
    L'Amoreaux West
    Upper Rouge
    Hillcrest Village
    Fairview,Henry Farm,Oriole
    Bayview Village
    Silver Hills,York Mills
    Newtonbrook,Willowdale
    Willowdale South
    York Mills West
    Willowdale West
    Parkwoods
    Don Mills North
    Flemingdon Park,Don Mills South
    Bathurst Manor,Downsview North,Wilson Heights
    Northwood Park,York University
    CFB Toronto,Downsview East
    Downsview West
    Downsview Central
    Downsview Northwest
    Victoria Village
    Woodbine Gardens,Parkview Hill
    Woodbine Heights
    The Beaches
    Leaside
    Thorncliffe Park
    East Toronto
    The Danforth West,Riverdale
    The Beaches West,India Bazaar
    Studio District
    Lawrence Park
    Davisville North
    North Toronto West
    Davisville
    Moore Park,Summerhill East
    Deer Park,Forest Hill SE,Rathnelly,South Hill,Summerhill West
    Rosedale
    Cabbagetown,St. James Town
    Church and Wellesley
    Harbourfront,Regent Park
    Ryerson,Garden District
    St. James Town
    Berczy Park
    Central Bay Street
    Adelaide,King,Richmond
    Harbourfront East,Toronto Islands,Union Station
    Design Exchange,Toronto Dominion Centre
    Commerce Court,Victoria Hotel
    Bedford Park,Lawrence Manor East
    Roselawn
    Forest Hill North,Forest Hill West
    The Annex,North Midtown,Yorkville
    Harbord,University of Toronto
    Chinatown,Grange Park,Kensington Market
    CN Tower,Bathurst Quay,Island airport,Harbourfront West,King and Spadina,Railway Lands,South Niagara
    Stn A PO Boxes 25 The Esplanade
    First Canadian Place,Underground city
    Lawrence Heights,Lawrence Manor
    Glencairn
    Humewood-Cedarvale
    Caledonia-Fairbanks
    Christie
    Dovercourt Village,Dufferin
    Little Portugal,Trinity
    Brockton,Exhibition Place,Parkdale Village
    Downsview,North Park,Upwood Park
    Del Ray,Keelesdale,Mount Dennis,Silverthorn
    The Junction North,Runnymede
    High Park,The Junction South
    Parkdale,Roncesvalles
    Runnymede,Swansea
    Queen's Park
    Canada Post Gateway Processing Centre
    Business Reply Mail Processing Centre 969 Eastern
    Humber Bay Shores,Mimico South,New Toronto
    Alderwood,Long Branch
    The Kingsway,Montgomery Road,Old Mill North
    Humber Bay,King's Mill Park,Kingsway Park South East,Mimico NE,Old Mill South,The Queensway East,Royal York South East,Sunnylea
    Kingsway Park South West,Mimico NW,The Queensway West,Royal York South West,South of Bloor
    Islington Avenue
    Cloverdale,Islington,Martin Grove,Princess Gardens,West Deane Park
    Bloordale Gardens,Eringate,Markland Wood,Old Burnhamthorpe
    Humber Summit
    Emery,Humberlea
    Weston
    Westmount
    Kingsview Village,Martin Grove Gardens,Richview Gardens,St. Phillips
    Albion Gardens,Beaumond Heights,Humbergate,Jamestown,Mount Olive,Silverstone,South Steeles,Thistletown
    Northwest


.. code:: ipython3

    print(toronto_venues.shape)
    toronto_venues.head()


.. parsed-literal::

    (1333, 7)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Neighborhood</th>
          <th>Neighborhood Latitude</th>
          <th>Neighborhood Longitude</th>
          <th>Venue</th>
          <th>Venue Latitude</th>
          <th>Venue Longitude</th>
          <th>Venue Category</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Rouge,Malvern</td>
          <td>43.806686</td>
          <td>-79.194353</td>
          <td>Wendy's</td>
          <td>43.807448</td>
          <td>-79.199056</td>
          <td>Fast Food Restaurant</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Highland Creek,Rouge Hill,Port Union</td>
          <td>43.784535</td>
          <td>-79.160497</td>
          <td>Royal Canadian Legion</td>
          <td>43.782533</td>
          <td>-79.163085</td>
          <td>Bar</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Guildwood,Morningside,West Hill</td>
          <td>43.763573</td>
          <td>-79.188711</td>
          <td>Swiss Chalet Rotisserie &amp; Grill</td>
          <td>43.767697</td>
          <td>-79.189914</td>
          <td>Pizza Place</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Guildwood,Morningside,West Hill</td>
          <td>43.763573</td>
          <td>-79.188711</td>
          <td>G &amp; G Electronics</td>
          <td>43.765309</td>
          <td>-79.191537</td>
          <td>Electronics Store</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Guildwood,Morningside,West Hill</td>
          <td>43.763573</td>
          <td>-79.188711</td>
          <td>Marina Spa</td>
          <td>43.766000</td>
          <td>-79.191000</td>
          <td>Spa</td>
        </tr>
      </tbody>
    </table>
    </div>



Then group the venues by "Neighborhood"

.. code:: ipython3

    toronto_venues.groupby('Neighborhood').count()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Neighborhood Latitude</th>
          <th>Neighborhood Longitude</th>
          <th>Venue</th>
          <th>Venue Latitude</th>
          <th>Venue Longitude</th>
          <th>Venue Category</th>
        </tr>
        <tr>
          <th>Neighborhood</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Adelaide,King,Richmond</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Agincourt</th>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
        </tr>
        <tr>
          <th>Agincourt North,L'Amoreaux East,Milliken,Steeles East</th>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
        </tr>
        <tr>
          <th>Albion Gardens,Beaumond Heights,Humbergate,Jamestown,Mount Olive,Silverstone,South Steeles,Thistletown</th>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
        </tr>
        <tr>
          <th>Alderwood,Long Branch</th>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
        </tr>
        <tr>
          <th>Bathurst Manor,Downsview North,Wilson Heights</th>
          <td>19</td>
          <td>19</td>
          <td>19</td>
          <td>19</td>
          <td>19</td>
          <td>19</td>
        </tr>
        <tr>
          <th>Bayview Village</th>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
        </tr>
        <tr>
          <th>Bedford Park,Lawrence Manor East</th>
          <td>23</td>
          <td>23</td>
          <td>23</td>
          <td>23</td>
          <td>23</td>
          <td>23</td>
        </tr>
        <tr>
          <th>Berczy Park</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Birch Cliff,Cliffside West</th>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
        </tr>
        <tr>
          <th>Bloordale Gardens,Eringate,Markland Wood,Old Burnhamthorpe</th>
          <td>7</td>
          <td>7</td>
          <td>7</td>
          <td>7</td>
          <td>7</td>
          <td>7</td>
        </tr>
        <tr>
          <th>Brockton,Exhibition Place,Parkdale Village</th>
          <td>24</td>
          <td>24</td>
          <td>24</td>
          <td>24</td>
          <td>24</td>
          <td>24</td>
        </tr>
        <tr>
          <th>Business Reply Mail Processing Centre 969 Eastern</th>
          <td>15</td>
          <td>15</td>
          <td>15</td>
          <td>15</td>
          <td>15</td>
          <td>15</td>
        </tr>
        <tr>
          <th>CFB Toronto,Downsview East</th>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
        </tr>
        <tr>
          <th>CN Tower,Bathurst Quay,Island airport,Harbourfront West,King and Spadina,Railway Lands,South Niagara</th>
          <td>17</td>
          <td>17</td>
          <td>17</td>
          <td>17</td>
          <td>17</td>
          <td>17</td>
        </tr>
        <tr>
          <th>Cabbagetown,St. James Town</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Caledonia-Fairbanks</th>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Canada Post Gateway Processing Centre</th>
          <td>11</td>
          <td>11</td>
          <td>11</td>
          <td>11</td>
          <td>11</td>
          <td>11</td>
        </tr>
        <tr>
          <th>Cedarbrae</th>
          <td>7</td>
          <td>7</td>
          <td>7</td>
          <td>7</td>
          <td>7</td>
          <td>7</td>
        </tr>
        <tr>
          <th>Central Bay Street</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Chinatown,Grange Park,Kensington Market</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Christie</th>
          <td>16</td>
          <td>16</td>
          <td>16</td>
          <td>16</td>
          <td>16</td>
          <td>16</td>
        </tr>
        <tr>
          <th>Church and Wellesley</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Clairlea,Golden Mile,Oakridge</th>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
        </tr>
        <tr>
          <th>Clarks Corners,Sullivan,Tam O'Shanter</th>
          <td>12</td>
          <td>12</td>
          <td>12</td>
          <td>12</td>
          <td>12</td>
          <td>12</td>
        </tr>
        <tr>
          <th>Cliffcrest,Cliffside,Scarborough Village West</th>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
        </tr>
        <tr>
          <th>Commerce Court,Victoria Hotel</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Davisville</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Davisville North</th>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
        </tr>
        <tr>
          <th>Deer Park,Forest Hill SE,Rathnelly,South Hill,Summerhill West</th>
          <td>16</td>
          <td>16</td>
          <td>16</td>
          <td>16</td>
          <td>16</td>
          <td>16</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>Northwest</th>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
        </tr>
        <tr>
          <th>Northwood Park,York University</th>
          <td>6</td>
          <td>6</td>
          <td>6</td>
          <td>6</td>
          <td>6</td>
          <td>6</td>
        </tr>
        <tr>
          <th>Parkdale,Roncesvalles</th>
          <td>15</td>
          <td>15</td>
          <td>15</td>
          <td>15</td>
          <td>15</td>
          <td>15</td>
        </tr>
        <tr>
          <th>Parkwoods</th>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
        </tr>
        <tr>
          <th>Queen's Park</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Rosedale</th>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
          <td>5</td>
        </tr>
        <tr>
          <th>Roselawn</th>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
          <td>2</td>
        </tr>
        <tr>
          <th>Rouge,Malvern</th>
          <td>1</td>
          <td>1</td>
          <td>1</td>
          <td>1</td>
          <td>1</td>
          <td>1</td>
        </tr>
        <tr>
          <th>Runnymede,Swansea</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Ryerson,Garden District</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Scarborough Village</th>
          <td>1</td>
          <td>1</td>
          <td>1</td>
          <td>1</td>
          <td>1</td>
          <td>1</td>
        </tr>
        <tr>
          <th>St. James Town</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Stn A PO Boxes 25 The Esplanade</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Studio District</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>The Annex,North Midtown,Yorkville</th>
          <td>22</td>
          <td>22</td>
          <td>22</td>
          <td>22</td>
          <td>22</td>
          <td>22</td>
        </tr>
        <tr>
          <th>The Beaches</th>
          <td>6</td>
          <td>6</td>
          <td>6</td>
          <td>6</td>
          <td>6</td>
          <td>6</td>
        </tr>
        <tr>
          <th>The Beaches West,India Bazaar</th>
          <td>20</td>
          <td>20</td>
          <td>20</td>
          <td>20</td>
          <td>20</td>
          <td>20</td>
        </tr>
        <tr>
          <th>The Danforth West,Riverdale</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>The Junction North,Runnymede</th>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
        </tr>
        <tr>
          <th>The Kingsway,Montgomery Road,Old Mill North</th>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
        </tr>
        <tr>
          <th>Thorncliffe Park</th>
          <td>17</td>
          <td>17</td>
          <td>17</td>
          <td>17</td>
          <td>17</td>
          <td>17</td>
        </tr>
        <tr>
          <th>Victoria Village</th>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
          <td>4</td>
        </tr>
        <tr>
          <th>Westmount</th>
          <td>8</td>
          <td>8</td>
          <td>8</td>
          <td>8</td>
          <td>8</td>
          <td>8</td>
        </tr>
        <tr>
          <th>Weston</th>
          <td>1</td>
          <td>1</td>
          <td>1</td>
          <td>1</td>
          <td>1</td>
          <td>1</td>
        </tr>
        <tr>
          <th>Willowdale South</th>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
          <td>30</td>
        </tr>
        <tr>
          <th>Willowdale West</th>
          <td>6</td>
          <td>6</td>
          <td>6</td>
          <td>6</td>
          <td>6</td>
          <td>6</td>
        </tr>
        <tr>
          <th>Woburn</th>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
        </tr>
        <tr>
          <th>Woodbine Gardens,Parkview Hill</th>
          <td>12</td>
          <td>12</td>
          <td>12</td>
          <td>12</td>
          <td>12</td>
          <td>12</td>
        </tr>
        <tr>
          <th>Woodbine Heights</th>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
          <td>9</td>
        </tr>
        <tr>
          <th>York Mills West</th>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
          <td>3</td>
        </tr>
      </tbody>
    </table>
    <p>99 rows × 6 columns</p>
    </div>



We then check to see how many unique categories of venues there are in
the Toronto

.. code:: ipython3

    print('There are {} uniques categories.'.format(len(toronto_venues['Venue Category'].unique())))


.. parsed-literal::

    There are 237 uniques categories.


We check to see which places are most visited by neighborhood

.. code:: ipython3

    toronto_onehot = pd.get_dummies(toronto_venues[['Venue Category']], prefix="", prefix_sep="")
    
    toronto_onehot['Neighborhood'] = toronto_venues['Neighborhood'] 
    
    fixed_columns = [toronto_onehot.columns[-1]] + list(toronto_onehot.columns[:-1])
    toronto_onehot = toronto_onehot[fixed_columns]

.. code:: ipython3

    toronto_grouped = toronto_onehot.groupby('Neighborhood').mean().reset_index()
    toronto_grouped




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Neighborhood</th>
          <th>Yoga Studio</th>
          <th>Accessories Store</th>
          <th>Airport</th>
          <th>Airport Food Court</th>
          <th>Airport Gate</th>
          <th>Airport Lounge</th>
          <th>Airport Service</th>
          <th>Airport Terminal</th>
          <th>American Restaurant</th>
          <th>...</th>
          <th>Train Station</th>
          <th>Turkish Restaurant</th>
          <th>Vegetarian / Vegan Restaurant</th>
          <th>Video Game Store</th>
          <th>Video Store</th>
          <th>Vietnamese Restaurant</th>
          <th>Warehouse Store</th>
          <th>Wine Bar</th>
          <th>Wings Joint</th>
          <th>Women's Store</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Adelaide,King,Richmond</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.033333</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.033333</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Agincourt</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Agincourt North,L'Amoreaux East,Milliken,Steel...</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Albion Gardens,Beaumond Heights,Humbergate,Jam...</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Alderwood,Long Branch</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>5</th>
          <td>Bathurst Manor,Downsview North,Wilson Heights</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.052632</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>6</th>
          <td>Bayview Village</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>7</th>
          <td>Bedford Park,Lawrence Manor East</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.043478</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>8</th>
          <td>Berczy Park</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.033333</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>9</th>
          <td>Birch Cliff,Cliffside West</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>10</th>
          <td>Bloordale Gardens,Eringate,Markland Wood,Old B...</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>11</th>
          <td>Brockton,Exhibition Place,Parkdale Village</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>12</th>
          <td>Business Reply Mail Processing Centre 969 Eastern</td>
          <td>0.066667</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>13</th>
          <td>CFB Toronto,Downsview East</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.500000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>14</th>
          <td>CN Tower,Bathurst Quay,Island airport,Harbourf...</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.058824</td>
          <td>0.058824</td>
          <td>0.058824</td>
          <td>0.117647</td>
          <td>0.176471</td>
          <td>0.117647</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>15</th>
          <td>Cabbagetown,St. James Town</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>16</th>
          <td>Caledonia-Fairbanks</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.2</td>
        </tr>
        <tr>
          <th>17</th>
          <td>Canada Post Gateway Processing Centre</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.090909</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>18</th>
          <td>Cedarbrae</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>19</th>
          <td>Central Bay Street</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.033333</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>20</th>
          <td>Chinatown,Grange Park,Kensington Market</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.033333</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.066667</td>
          <td>0.000000</td>
          <td>0.033333</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>21</th>
          <td>Christie</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>22</th>
          <td>Church and Wellesley</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>23</th>
          <td>Clairlea,Golden Mile,Oakridge</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>24</th>
          <td>Clarks Corners,Sullivan,Tam O'Shanter</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>25</th>
          <td>Cliffcrest,Cliffside,Scarborough Village West</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.333333</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>26</th>
          <td>Commerce Court,Victoria Hotel</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.033333</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>27</th>
          <td>Davisville</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>28</th>
          <td>Davisville North</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>29</th>
          <td>Deer Park,Forest Hill SE,Rathnelly,South Hill,...</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.062500</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.062500</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>69</th>
          <td>Northwest</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>70</th>
          <td>Northwood Park,York University</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>71</th>
          <td>Parkdale,Roncesvalles</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>72</th>
          <td>Parkwoods</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>73</th>
          <td>Queen's Park</td>
          <td>0.033333</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.033333</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>74</th>
          <td>Rosedale</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>75</th>
          <td>Roselawn</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>76</th>
          <td>Rouge,Malvern</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>77</th>
          <td>Runnymede,Swansea</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.033333</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>78</th>
          <td>Ryerson,Garden District</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.033333</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.033333</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>79</th>
          <td>Scarborough Village</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>80</th>
          <td>St. James Town</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.033333</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>81</th>
          <td>Stn A PO Boxes 25 The Esplanade</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.033333</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>82</th>
          <td>Studio District</td>
          <td>0.033333</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.033333</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>83</th>
          <td>The Annex,North Midtown,Yorkville</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.045455</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.045455</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>84</th>
          <td>The Beaches</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>85</th>
          <td>The Beaches West,India Bazaar</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>86</th>
          <td>The Danforth West,Riverdale</td>
          <td>0.033333</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>87</th>
          <td>The Junction North,Runnymede</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>88</th>
          <td>The Kingsway,Montgomery Road,Old Mill North</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>89</th>
          <td>Thorncliffe Park</td>
          <td>0.058824</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.058824</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>90</th>
          <td>Victoria Village</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>91</th>
          <td>Westmount</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>92</th>
          <td>Weston</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>93</th>
          <td>Willowdale South</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.033333</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>94</th>
          <td>Willowdale West</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>95</th>
          <td>Woburn</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>96</th>
          <td>Woodbine Gardens,Parkview Hill</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>97</th>
          <td>Woodbine Heights</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.111111</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>98</th>
          <td>York Mills West</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>...</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
        </tr>
      </tbody>
    </table>
    <p>99 rows × 237 columns</p>
    </div>



We see the top 3 most visited venues in each neigborhood

.. code:: ipython3

    num_top_venues = 3
    
    for hood in toronto_grouped['Neighborhood']:
        print("----"+hood+"----")
        temp = toronto_grouped[toronto_grouped['Neighborhood'] == hood].T.reset_index()
        temp.columns = ['venue','freq']
        temp = temp.iloc[1:]
        temp['freq'] = temp['freq'].astype(float)
        temp = temp.round({'freq': 2})
        print(temp.sort_values('freq', ascending=False).reset_index(drop=True).head(num_top_venues))
        print('\n')


.. parsed-literal::

    ----Adelaide,King,Richmond----
            venue  freq
    0        Café  0.10
    1  Steakhouse  0.10
    2       Hotel  0.07
    
    
    ----Agincourt----
                venue  freq
    0          Lounge  0.25
    1  Breakfast Spot  0.25
    2  Clothing Store  0.25
    
    
    ----Agincourt North,L'Amoreaux East,Milliken,Steeles East----
               venue  freq
    0     Playground   0.5
    1           Park   0.5
    2  Movie Theater   0.0
    
    
    ----Albion Gardens,Beaumond Heights,Humbergate,Jamestown,Mount Olive,Silverstone,South Steeles,Thistletown----
                      venue  freq
    0         Grocery Store  0.22
    1           Pizza Place  0.22
    2  Fast Food Restaurant  0.11
    
    
    ----Alderwood,Long Branch----
              venue  freq
    0   Pizza Place  0.22
    1   Coffee Shop  0.11
    2  Dance Studio  0.11
    
    
    ----Bathurst Manor,Downsview North,Wilson Heights----
             venue  freq
    0  Coffee Shop  0.11
    1     Pharmacy  0.05
    2        Diner  0.05
    
    
    ----Bayview Village----
                    venue  freq
    0                Café  0.25
    1  Chinese Restaurant  0.25
    2                Bank  0.25
    
    
    ----Bedford Park,Lawrence Manor East----
                      venue  freq
    0  Fast Food Restaurant  0.09
    1    Italian Restaurant  0.09
    2           Coffee Shop  0.09
    
    
    ----Berczy Park----
                venue  freq
    0  Farmers Market  0.07
    1            Café  0.07
    2        Beer Bar  0.07
    
    
    ----Birch Cliff,Cliffside West----
                       venue  freq
    0                   Café  0.25
    1  General Entertainment  0.25
    2           Skating Rink  0.25
    
    
    ----Bloordale Gardens,Eringate,Markland Wood,Old Burnhamthorpe----
                   venue  freq
    0        Pizza Place  0.14
    1  Convenience Store  0.14
    2       Liquor Store  0.14
    
    
    ----Brockton,Exhibition Place,Parkdale Village----
                       venue  freq
    0                   Café  0.12
    1         Breakfast Spot  0.08
    2  Performing Arts Venue  0.08
    
    
    ----Business Reply Mail Processing Centre 969 Eastern----
               venue  freq
    0    Yoga Studio  0.07
    1  Auto Workshop  0.07
    2     Comic Shop  0.07
    
    
    ----CFB Toronto,Downsview East----
             venue  freq
    0      Airport   0.5
    1         Park   0.5
    2  Yoga Studio   0.0
    
    
    ----CN Tower,Bathurst Quay,Island airport,Harbourfront West,King and Spadina,Railway Lands,South Niagara----
                  venue  freq
    0   Airport Service  0.18
    1    Airport Lounge  0.12
    2  Airport Terminal  0.12
    
    
    ----Cabbagetown,St. James Town----
             venue  freq
    0         Café  0.07
    1   Restaurant  0.07
    2  Coffee Shop  0.07
    
    
    ----Caledonia-Fairbanks----
               venue  freq
    0           Park   0.4
    1  Women's Store   0.2
    2         Market   0.2
    
    
    ----Canada Post Gateway Processing Centre----
                      venue  freq
    0                 Hotel  0.18
    1           Coffee Shop  0.18
    2  Gym / Fitness Center  0.09
    
    
    ----Cedarbrae----
                      venue  freq
    0       Thai Restaurant  0.14
    1                Bakery  0.14
    2  Caribbean Restaurant  0.14
    
    
    ----Central Bay Street----
                 venue  freq
    0      Coffee Shop  0.20
    1  Bubble Tea Shop  0.07
    2              Spa  0.07
    
    
    ----Chinatown,Grange Park,Kensington Market----
                      venue  freq
    0                  Café  0.13
    1    Mexican Restaurant  0.07
    2  Caribbean Restaurant  0.07
    
    
    ----Christie----
               venue  freq
    0           Café  0.19
    1  Grocery Store  0.19
    2           Park  0.12
    
    
    ----Church and Wellesley----
              venue  freq
    0       Gay Bar  0.07
    1  Burger Joint  0.07
    2    Hobby Shop  0.03
    
    
    ----Clairlea,Golden Mile,Oakridge----
              venue  freq
    0        Bakery  0.22
    1      Bus Line  0.22
    2  Intersection  0.11
    
    
    ----Clarks Corners,Sullivan,Tam O'Shanter----
              venue  freq
    0   Pizza Place  0.17
    1      Pharmacy  0.17
    2  Noodle House  0.08
    
    
    ----Cliffcrest,Cliffside,Scarborough Village West----
                     venue  freq
    0        Movie Theater  0.33
    1  American Restaurant  0.33
    2                Motel  0.33
    
    
    ----Commerce Court,Victoria Hotel----
             venue  freq
    0         Café  0.17
    1  Coffee Shop  0.13
    2   Restaurant  0.10
    
    
    ----Davisville----
                    venue  freq
    0        Dessert Shop  0.10
    1  Italian Restaurant  0.07
    2         Pizza Place  0.07
    
    
    ----Davisville North----
                   venue  freq
    0              Hotel  0.22
    1  Convenience Store  0.11
    2  Food & Drink Shop  0.11
    
    
    ----Deer Park,Forest Hill SE,Rathnelly,South Hill,Summerhill West----
                    venue  freq
    0         Coffee Shop  0.12
    1                 Pub  0.12
    2  Light Rail Station  0.06
    
    
    ----Del Ray,Keelesdale,Mount Dennis,Silverthorn----
                    venue  freq
    0        Skating Rink   0.2
    1  Turkish Restaurant   0.2
    2          Restaurant   0.2
    
    
    ----Design Exchange,Toronto Dominion Centre----
             venue  freq
    0  Coffee Shop  0.17
    1   Restaurant  0.10
    2         Café  0.10
    
    
    ----Don Mills North----
                      venue  freq
    0  Gym / Fitness Center   0.2
    1  Caribbean Restaurant   0.2
    2      Basketball Court   0.2
    
    
    ----Dorset Park,Scarborough Town Centre,Wexford Heights----
                        venue  freq
    0       Indian Restaurant  0.22
    1             Gaming Cafe  0.11
    2  Furniture / Home Store  0.11
    
    
    ----Dovercourt Village,Dufferin----
             venue  freq
    0  Supermarket  0.13
    1     Pharmacy  0.13
    2       Bakery  0.13
    
    
    ----Downsview Central----
                   venue  freq
    0  Korean Restaurant  0.33
    1     Baseball Field  0.33
    2         Food Truck  0.33
    
    
    ----Downsview Northwest----
                      venue  freq
    0  Gym / Fitness Center   0.2
    1          Liquor Store   0.2
    2         Grocery Store   0.2
    
    
    ----Downsview West----
               venue  freq
    0  Grocery Store   0.4
    1           Park   0.2
    2           Bank   0.2
    
    
    ----Downsview,North Park,Upwood Park----
                            venue  freq
    0  Construction & Landscaping  0.25
    1                        Park  0.25
    2            Basketball Court  0.25
    
    
    ----East Birchmount Park,Ionview,Kennedy Park----
                  venue  freq
    0  Department Store   0.2
    1       Coffee Shop   0.2
    2        Hobby Shop   0.2
    
    
    ----East Toronto----
                   venue  freq
    0        Coffee Shop  0.33
    1  Convenience Store  0.33
    2               Park  0.33
    
    
    ----Emery,Humberlea----
                venue  freq
    0  Baseball Field   1.0
    1     Yoga Studio   0.0
    2          Lounge   0.0
    
    
    ----Fairview,Henry Farm,Oriole----
                venue  freq
    0  Clothing Store  0.13
    1     Coffee Shop  0.13
    2            Bank  0.03
    
    
    ----First Canadian Place,Underground city----
             venue  freq
    0         Café  0.13
    1  Coffee Shop  0.10
    2   Steakhouse  0.07
    
    
    ----Flemingdon Park,Don Mills South----
                  venue  freq
    0  Asian Restaurant  0.09
    1        Beer Store  0.09
    2               Gym  0.09
    
    
    ----Forest Hill North,Forest Hill West----
                    venue  freq
    0    Sushi Restaurant  0.25
    1       Jewelry Store  0.25
    2  Mexican Restaurant  0.25
    
    
    ----Glencairn----
                  venue  freq
    0       Pizza Place  0.25
    1               Pub  0.25
    2  Asian Restaurant  0.25
    
    
    ----Guildwood,Morningside,West Hill----
                venue  freq
    0     Pizza Place  0.12
    1  Medical Center  0.12
    2  Breakfast Spot  0.12
    
    
    ----Harbord,University of Toronto----
           venue  freq
    0       Café  0.13
    1     Bakery  0.07
    2  Bookstore  0.07
    
    
    ----Harbourfront East,Toronto Islands,Union Station----
       venue  freq
    0  Plaza  0.07
    1   Park  0.07
    2  Hotel  0.07
    
    
    ----Harbourfront,Regent Park----
             venue  freq
    0  Coffee Shop   0.2
    1         Park   0.1
    2       Bakery   0.1
    
    
    ----High Park,The Junction South----
                    venue  freq
    0  Mexican Restaurant  0.08
    1                Café  0.08
    2       Grocery Store  0.08
    
    
    ----Highland Creek,Rouge Hill,Port Union----
             venue  freq
    0          Bar   1.0
    1  Yoga Studio   0.0
    2       Lounge   0.0
    
    
    ----Hillcrest Village----
                          venue  freq
    0                      Pool   0.2
    1  Mediterranean Restaurant   0.2
    2               Golf Course   0.2
    
    
    ----Humber Bay Shores,Mimico South,New Toronto----
                      venue  freq
    0                  Café  0.12
    1  Fast Food Restaurant  0.06
    2           Coffee Shop  0.06
    
    
    ----Humber Bay,King's Mill Park,Kingsway Park South East,Mimico NE,Old Mill South,The Queensway East,Royal York South East,Sunnylea----
                  venue  freq
    0  Business Service  0.33
    1              Park  0.33
    2    Baseball Field  0.33
    
    
    ----Humber Summit----
                     venue  freq
    0          Pizza Place   0.5
    1  Empanada Restaurant   0.5
    2        Movie Theater   0.0
    
    
    ----Humewood-Cedarvale----
              venue  freq
    0         Field  0.25
    1          Park  0.25
    2  Hockey Arena  0.25
    
    
    ----Kingsview Village,Martin Grove Gardens,Richview Gardens,St. Phillips----
                   venue  freq
    0        Pizza Place  0.25
    1               Park  0.25
    2  Mobile Phone Shop  0.25
    
    
    ----Kingsway Park South West,Mimico NW,The Queensway West,Royal York South West,South of Bloor----
                   venue  freq
    0  Convenience Store  0.07
    1     Discount Store  0.07
    2       Burger Joint  0.07
    
    
    ----L'Amoreaux West----
                      venue  freq
    0  Fast Food Restaurant  0.15
    1    Chinese Restaurant  0.15
    2        Breakfast Spot  0.08
    
    
    ----Lawrence Heights,Lawrence Manor----
                        venue  freq
    0  Furniture / Home Store  0.25
    1                Boutique  0.08
    2      Miscellaneous Shop  0.08
    
    
    ----Lawrence Park----
             venue  freq
    0         Park  0.33
    1  Swim School  0.33
    2     Bus Line  0.33
    
    
    ----Leaside----
                     venue  freq
    0  Sporting Goods Shop  0.10
    1          Coffee Shop  0.10
    2         Burger Joint  0.07
    
    
    ----Little Portugal,Trinity----
                       venue  freq
    0                    Bar  0.13
    1       Asian Restaurant  0.10
    2  Vietnamese Restaurant  0.07
    
    
    ----Maryvale,Wexford----
                           venue  freq
    0  Middle Eastern Restaurant  0.12
    1                     Bakery  0.12
    2             Breakfast Spot  0.12
    
    
    ----Moore Park,Summerhill East----
              venue  freq
    0    Playground  0.33
    1   Summer Camp  0.33
    2  Tennis Court  0.33
    
    
    ----Newtonbrook,Willowdale----
               venue  freq
    0      Piano Bar   1.0
    1    Yoga Studio   0.0
    2  Movie Theater   0.0
    
    
    ----North Toronto West----
                     venue  freq
    0  Sporting Goods Shop  0.10
    1          Coffee Shop  0.10
    2          Yoga Studio  0.05
    
    
    ----Northwest----
                     venue  freq
    0            Drugstore   0.5
    1  Rental Car Location   0.5
    2          Yoga Studio   0.0
    
    
    ----Northwood Park,York University----
                    venue  freq
    0      Massage Studio  0.17
    1         Coffee Shop  0.17
    2  Falafel Restaurant  0.17
    
    
    ----Parkdale,Roncesvalles----
                venue  freq
    0       Gift Shop  0.13
    1  Breakfast Spot  0.13
    2       Bookstore  0.07
    
    
    ----Parkwoods----
                   venue  freq
    0          BBQ Joint  0.33
    1               Park  0.33
    2  Food & Drink Shop  0.33
    
    
    ----Queen's Park----
             venue  freq
    0  Coffee Shop  0.17
    1         Park  0.07
    2        Diner  0.07
    
    
    ----Rosedale----
            venue  freq
    0        Park   0.4
    1  Playground   0.2
    2    Building   0.2
    
    
    ----Roselawn----
             venue  freq
    0       Garden   0.5
    1  Music Venue   0.5
    2  Yoga Studio   0.0
    
    
    ----Rouge,Malvern----
                      venue  freq
    0  Fast Food Restaurant   1.0
    1         Movie Theater   0.0
    2                Market   0.0
    
    
    ----Runnymede,Swansea----
                    venue  freq
    0                Café  0.10
    1         Pizza Place  0.07
    2  Italian Restaurant  0.07
    
    
    ----Ryerson,Garden District----
                venue  freq
    0            Café  0.10
    1  Clothing Store  0.07
    2             Spa  0.03
    
    
    ----Scarborough Village----
               venue  freq
    0     Playground   1.0
    1  Movie Theater   0.0
    2         Market   0.0
    
    
    ----St. James Town----
                    venue  freq
    0         Coffee Shop  0.13
    1           Gastropub  0.10
    2  Italian Restaurant  0.10
    
    
    ----Stn A PO Boxes 25 The Esplanade----
                    venue  freq
    0                Café  0.10
    1      Farmers Market  0.07
    2  Seafood Restaurant  0.07
    
    
    ----Studio District----
                    venue  freq
    0                Café  0.13
    1         Coffee Shop  0.10
    2  Italian Restaurant  0.07
    
    
    ----The Annex,North Midtown,Yorkville----
                venue  freq
    0  Sandwich Place  0.14
    1            Café  0.14
    2     Coffee Shop  0.09
    
    
    ----The Beaches----
                   venue  freq
    0              Trail  0.17
    1  Health Food Store  0.17
    2               Park  0.17
    
    
    ----The Beaches West,India Bazaar----
                      venue  freq
    0        Sandwich Place  0.10
    1                  Park  0.10
    2  Fast Food Restaurant  0.05
    
    
    ----The Danforth West,Riverdale----
                    venue  freq
    0    Greek Restaurant  0.27
    1      Ice Cream Shop  0.07
    2  Italian Restaurant  0.07
    
    
    ----The Junction North,Runnymede----
                   venue  freq
    0        Pizza Place  0.25
    1      Grocery Store  0.25
    2  Convenience Store  0.25
    
    
    ----The Kingsway,Montgomery Road,Old Mill North----
            venue  freq
    0        Park  0.33
    1  Smoke Shop  0.33
    2       River  0.33
    
    
    ----Thorncliffe Park----
                   venue  freq
    0       Burger Joint  0.12
    1  Indian Restaurant  0.12
    2        Yoga Studio  0.06
    
    
    ----Victoria Village----
                       venue  freq
    0           Hockey Arena  0.25
    1            Coffee Shop  0.25
    2  Portuguese Restaurant  0.25
    
    
    ----Westmount----
                           venue  freq
    0                Pizza Place  0.25
    1  Middle Eastern Restaurant  0.12
    2             Sandwich Place  0.12
    
    
    ----Weston----
                   venue  freq
    0  Convenience Store   1.0
    1        Yoga Studio   0.0
    2             Museum   0.0
    
    
    ----Willowdale South----
                  venue  freq
    0  Ramen Restaurant  0.10
    1              Café  0.07
    2       Coffee Shop  0.07
    
    
    ----Willowdale West----
               venue  freq
    0    Pizza Place  0.17
    1    Coffee Shop  0.17
    2  Grocery Store  0.17
    
    
    ----Woburn----
                    venue  freq
    0         Coffee Shop  0.67
    1   Korean Restaurant  0.33
    2  Mac & Cheese Joint  0.00
    
    
    ----Woodbine Gardens,Parkview Hill----
                      venue  freq
    0           Pizza Place  0.17
    1  Fast Food Restaurant  0.17
    2             Gastropub  0.08
    
    
    ----Woodbine Heights----
                    venue  freq
    0  Athletics & Sports  0.11
    1            Pharmacy  0.11
    2      Cosmetics Shop  0.11
    
    
    ----York Mills West----
                   venue  freq
    0  Convenience Store  0.33
    1               Park  0.33
    2               Bank  0.33
    
    


Even better, we can see in a Pandas data frame the top ten common venues
in each neighborhood

.. code:: ipython3

    def _most_common_venues(row, num_top_venues):
        row_categories = row.iloc[1:]
        row_categories_sorted = row_categories.sort_values(ascending=False)
        
        return row_categories_sorted.index.values[0:num_top_venues]

.. code:: ipython3

    num_top_venues = 10
    
    indicators = ['st', 'nd', 'rd']
    
    # create columns according to number of top venues
    columns = ['Neighborhood']
    for ind in np.arange(num_top_venues):
        try:
            columns.append('{}{} Most Common Venue'.format(ind+1, indicators[ind]))
        except:
            columns.append('{}th Most Common Venue'.format(ind+1))
    
    # create a new dataframe
    sorted_neighborhoods_venues = pd.DataFrame(columns=columns)
    sorted_neighborhoods_venues['Neighborhood'] = toronto_grouped['Neighborhood']
    
    for ind in np.arange(toronto_grouped.shape[0]):
        sorted_neighborhoods_venues.iloc[ind, 1:] = _most_common_venues(toronto_grouped.iloc[ind, :], num_top_venues)
    
    sorted_neighborhoods_venues.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Neighborhood</th>
          <th>1st Most Common Venue</th>
          <th>2nd Most Common Venue</th>
          <th>3rd Most Common Venue</th>
          <th>4th Most Common Venue</th>
          <th>5th Most Common Venue</th>
          <th>6th Most Common Venue</th>
          <th>7th Most Common Venue</th>
          <th>8th Most Common Venue</th>
          <th>9th Most Common Venue</th>
          <th>10th Most Common Venue</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Adelaide,King,Richmond</td>
          <td>Café</td>
          <td>Steakhouse</td>
          <td>Asian Restaurant</td>
          <td>Hotel</td>
          <td>Lounge</td>
          <td>Bar</td>
          <td>Speakeasy</td>
          <td>Smoke Shop</td>
          <td>Seafood Restaurant</td>
          <td>Gastropub</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Agincourt</td>
          <td>Lounge</td>
          <td>Clothing Store</td>
          <td>Breakfast Spot</td>
          <td>Skating Rink</td>
          <td>Department Store</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Agincourt North,L'Amoreaux East,Milliken,Steel...</td>
          <td>Playground</td>
          <td>Park</td>
          <td>Women's Store</td>
          <td>Dance Studio</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Albion Gardens,Beaumond Heights,Humbergate,Jam...</td>
          <td>Grocery Store</td>
          <td>Pizza Place</td>
          <td>Fried Chicken Joint</td>
          <td>Sandwich Place</td>
          <td>Fast Food Restaurant</td>
          <td>Beer Store</td>
          <td>Pharmacy</td>
          <td>Gay Bar</td>
          <td>Cuban Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Alderwood,Long Branch</td>
          <td>Pizza Place</td>
          <td>Gym</td>
          <td>Skating Rink</td>
          <td>Coffee Shop</td>
          <td>Pub</td>
          <td>Dance Studio</td>
          <td>Sandwich Place</td>
          <td>Pharmacy</td>
          <td>Garden</td>
          <td>Coworking Space</td>
        </tr>
      </tbody>
    </table>
    </div>



Clustering
==========

.. code:: ipython3

    kclusters = 5
    
    toronto_grouped_clustering = toronto_grouped.drop('Neighborhood', 1)
    
    kmeans = KMeans(n_clusters=kclusters, random_state=0).fit(toronto_grouped_clustering)
    
    kmeans.labels_[0:98]




.. parsed-literal::

    array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0,
           0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 3, 0, 4, 4, 0, 4, 3, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 4, 0, 0, 0, 4, 0, 0, 0,
           1, 2, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 4, 0, 0, 4,
           4, 0, 0, 0, 4, 0, 0, 0, 0, 0], dtype=int32)



.. code:: ipython3

    #sorted_neighborhoods_venues.drop(['Cluster Labels'],axis=1,inplace=True)
    sorted_neighborhoods_venues.insert(0, 'Cluster Labels', kmeans.labels_)
    toronto_merged = df_5
    # merge toronto_grouped with toronto_data to add latitude/longitude for each neighborhood
    toronto_merged = toronto_merged.join(sorted_neighborhoods_venues.set_index('Neighborhood'), on='Neighbourhood')
    toronto_merged.dropna(subset=["Cluster Labels"], axis=0, inplace=True)
    toronto_merged.reset_index(drop=True, inplace=True)
    toronto_merged['Cluster Labels'].astype(int)
    toronto_merged.head()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Postcode</th>
          <th>Borough</th>
          <th>Neighbourhood</th>
          <th>Latitude</th>
          <th>Longitude</th>
          <th>Cluster Labels</th>
          <th>1st Most Common Venue</th>
          <th>2nd Most Common Venue</th>
          <th>3rd Most Common Venue</th>
          <th>4th Most Common Venue</th>
          <th>5th Most Common Venue</th>
          <th>6th Most Common Venue</th>
          <th>7th Most Common Venue</th>
          <th>8th Most Common Venue</th>
          <th>9th Most Common Venue</th>
          <th>10th Most Common Venue</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>M1B</td>
          <td>Scarborough</td>
          <td>Rouge,Malvern</td>
          <td>43.806686</td>
          <td>-79.194353</td>
          <td>0.0</td>
          <td>Fast Food Restaurant</td>
          <td>Women's Store</td>
          <td>Falafel Restaurant</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>1</th>
          <td>M1C</td>
          <td>Scarborough</td>
          <td>Highland Creek,Rouge Hill,Port Union</td>
          <td>43.784535</td>
          <td>-79.160497</td>
          <td>0.0</td>
          <td>Bar</td>
          <td>Women's Store</td>
          <td>Farmers Market</td>
          <td>Event Space</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>2</th>
          <td>M1E</td>
          <td>Scarborough</td>
          <td>Guildwood,Morningside,West Hill</td>
          <td>43.763573</td>
          <td>-79.188711</td>
          <td>0.0</td>
          <td>Spa</td>
          <td>Intersection</td>
          <td>Electronics Store</td>
          <td>Pizza Place</td>
          <td>Mexican Restaurant</td>
          <td>Breakfast Spot</td>
          <td>Rental Car Location</td>
          <td>Medical Center</td>
          <td>Dim Sum Restaurant</td>
          <td>Diner</td>
        </tr>
        <tr>
          <th>3</th>
          <td>M1G</td>
          <td>Scarborough</td>
          <td>Woburn</td>
          <td>43.770992</td>
          <td>-79.216917</td>
          <td>0.0</td>
          <td>Coffee Shop</td>
          <td>Korean Restaurant</td>
          <td>Falafel Restaurant</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>4</th>
          <td>M1H</td>
          <td>Scarborough</td>
          <td>Cedarbrae</td>
          <td>43.773136</td>
          <td>-79.239476</td>
          <td>0.0</td>
          <td>Fried Chicken Joint</td>
          <td>Bakery</td>
          <td>Hakka Restaurant</td>
          <td>Bank</td>
          <td>Thai Restaurant</td>
          <td>Athletics &amp; Sports</td>
          <td>Caribbean Restaurant</td>
          <td>Discount Store</td>
          <td>Dim Sum Restaurant</td>
          <td>Diner</td>
        </tr>
      </tbody>
    </table>
    </div>



We visualize the clusters in a map

.. code:: ipython3

    map_clusters = folium.Map(location=[latitude, longitude], zoom_start=11)
    
    # set color scheme for the clusters
    x = np.arange(kclusters)
    ys = [i + x + (i*x)**2 for i in range(kclusters)]
    colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
    rainbow = [colors.rgb2hex(i) for i in colors_array]
    
    # add markers to the map
    markers_colors = []
    for lat, lon, poi, cluster in zip(toronto_merged['Latitude'], toronto_merged['Longitude'], toronto_merged['Neighbourhood'], toronto_merged['Cluster Labels'].astype(int)):
        label = folium.Popup(str(poi) + ' Cluster ' + str(cluster), parse_html=True)
        folium.CircleMarker(
            [lat, lon],
            radius=5,
            popup=label,
            color=rainbow[cluster-1],
            fill=True,
            fill_color=rainbow[cluster-1],
            fill_opacity=0.7).add_to(map_clusters)   
    map_clusters




.. raw:: html

    <div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzggewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4IiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCcsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDMuNjUzOTYzLC03OS4zODcyMDddLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTEsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzMxN2Y0YTQ1NjA5ZTRkMTBiYWEwYjhlMDFkMWQ3OGQ5ID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICJtYXhab29tIjogMTgsCiAgIm1pblpvb20iOiAxLAogICJub1dyYXAiOiBmYWxzZSwKICAic3ViZG9tYWlucyI6ICJhYmMiCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MGU5ZDdjNzYwOTU0NTg2OWE3NjI2ZTEwZDEzZjcxMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjgwNjY4NjI5OTk5OTk5NiwtNzkuMTk0MzUzNDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmQwZjBmYmMxZGM5NGZmMDhlNmU0NWFhZWU0YTZiNTEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmFlZDNiZTUwZTkwNGY1N2I3OTcwOTJlNjY5ZDFjZWQgPSAkKCc8ZGl2IGlkPSJodG1sX2ZhZWQzYmU1MGU5MDRmNTdiNzk3MDkyZTY2OWQxY2VkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3VnZSxNYWx2ZXJuIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmQwZjBmYmMxZGM5NGZmMDhlNmU0NWFhZWU0YTZiNTEuc2V0Q29udGVudChodG1sX2ZhZWQzYmU1MGU5MDRmNTdiNzk3MDkyZTY2OWQxY2VkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQwZTlkN2M3NjA5NTQ1ODY5YTc2MjZlMTBkMTNmNzEyLmJpbmRQb3B1cChwb3B1cF9mZDBmMGZiYzFkYzk0ZmYwOGU2ZTQ1YWFlZTRhNmI1MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hNGVmYWJkYjYyZWU0YTAxODEyNGYyMTc4ZWQ5ZDdjOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4NDUzNTEsLTc5LjE2MDQ5NzA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2UzYWUxNjAwOGFhNDQ4YTFhN2IzZWQ1N2M3M2E4NDVkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2RjZTI1MWU3Njc2MDRiMmU4YjllYWMyNzY5MzRiMzE5ID0gJCgnPGRpdiBpZD0iaHRtbF9kY2UyNTFlNzY3NjA0YjJlOGI5ZWFjMjc2OTM0YjMxOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaGxhbmQgQ3JlZWssUm91Z2UgSGlsbCxQb3J0IFVuaW9uIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTNhZTE2MDA4YWE0NDhhMWE3YjNlZDU3YzczYTg0NWQuc2V0Q29udGVudChodG1sX2RjZTI1MWU3Njc2MDRiMmU4YjllYWMyNzY5MzRiMzE5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2E0ZWZhYmRiNjJlZTRhMDE4MTI0ZjIxNzhlZDlkN2M5LmJpbmRQb3B1cChwb3B1cF9lM2FlMTYwMDhhYTQ0OGExYTdiM2VkNTdjNzNhODQ1ZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82Mzc5YzcyNjA2MGE0YWM3YjMwOWFjYjkxNTYwNmY4MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc2MzU3MjYsLTc5LjE4ODcxMTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzdhODBiYzg1OTMwNGMzZTgwZjY0N2ZjMTg3MjQwNDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWEyOGMyZWJjMWMwNDhlYWJhYzMxYTc0NmI3Yjc1MjIgPSAkKCc8ZGl2IGlkPSJodG1sX2VhMjhjMmViYzFjMDQ4ZWFiYWMzMWE3NDZiN2I3NTIyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HdWlsZHdvb2QsTW9ybmluZ3NpZGUsV2VzdCBIaWxsIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzdhODBiYzg1OTMwNGMzZTgwZjY0N2ZjMTg3MjQwNDkuc2V0Q29udGVudChodG1sX2VhMjhjMmViYzFjMDQ4ZWFiYWMzMWE3NDZiN2I3NTIyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzYzNzljNzI2MDYwYTRhYzdiMzA5YWNiOTE1NjA2ZjgwLmJpbmRQb3B1cChwb3B1cF83N2E4MGJjODU5MzA0YzNlODBmNjQ3ZmMxODcyNDA0OSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wNGUwOWI0NTA0YTk0M2VkYmY3NjRjYTU2YmI1YmUxNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MDk5MjEsLTc5LjIxNjkxNzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2UwZTE5MTNlZjY5NjQyNmQ4MmViMjkxYjJiNGU2ODcxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFiZTJkMDRjZTg5YjQyOWM4MGVhMzcyZjI0MmE5OTIwID0gJCgnPGRpdiBpZD0iaHRtbF8xYmUyZDA0Y2U4OWI0MjljODBlYTM3MmYyNDJhOTkyMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V29idXJuIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTBlMTkxM2VmNjk2NDI2ZDgyZWIyOTFiMmI0ZTY4NzEuc2V0Q29udGVudChodG1sXzFiZTJkMDRjZTg5YjQyOWM4MGVhMzcyZjI0MmE5OTIwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzA0ZTA5YjQ1MDRhOTQzZWRiZjc2NGNhNTZiYjViZTE1LmJpbmRQb3B1cChwb3B1cF9lMGUxOTEzZWY2OTY0MjZkODJlYjI5MWIyYjRlNjg3MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hZjk2NjBhOTUzYjA0MTVmYWUyMjJmMzc1ZDM5YTdhZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MzEzNiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjY3NDc2ZTI5ZGU1NDIwZjgzYTlkNzBmMWIyZWRlNzQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYzQxZWFkODZiYTcwNDg0OWI3MjVmN2Y2NWMyZDFmNmEgPSAkKCc8ZGl2IGlkPSJodG1sX2M0MWVhZDg2YmE3MDQ4NDliNzI1ZjdmNjVjMmQxZjZhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZWRhcmJyYWUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82Njc0NzZlMjlkZTU0MjBmODNhOWQ3MGYxYjJlZGU3NC5zZXRDb250ZW50KGh0bWxfYzQxZWFkODZiYTcwNDg0OWI3MjVmN2Y2NWMyZDFmNmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWY5NjYwYTk1M2IwNDE1ZmFlMjIyZjM3NWQzOWE3YWUuYmluZFBvcHVwKHBvcHVwXzY2NzQ3NmUyOWRlNTQyMGY4M2E5ZDcwZjFiMmVkZTc0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzVlODVmNDEzOWRhZDRiMjI5ZmNjMTNjMTg5OGFhZjgyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ0NzM0MiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjUzYTZmNjc4ZjhiNGI2YzljNWE5ZTQyMWJhZDI2MzAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWI0NWUyYmMwYjk5NGI4N2FlZTVhMDQ3ZjE5YjE2ODIgPSAkKCc8ZGl2IGlkPSJodG1sXzViNDVlMmJjMGI5OTRiODdhZWU1YTA0N2YxOWIxNjgyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TY2FyYm9yb3VnaCBWaWxsYWdlIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjUzYTZmNjc4ZjhiNGI2YzljNWE5ZTQyMWJhZDI2MzAuc2V0Q29udGVudChodG1sXzViNDVlMmJjMGI5OTRiODdhZWU1YTA0N2YxOWIxNjgyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzVlODVmNDEzOWRhZDRiMjI5ZmNjMTNjMTg5OGFhZjgyLmJpbmRQb3B1cChwb3B1cF8yNTNhNmY2NzhmOGI0YjZjOWM1YTllNDIxYmFkMjYzMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNDMwMTA1YmZlMGU0ZTYwYWUyNTJiZTQwZjExMzM3MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNzkyOTIsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2QyZDdkYjViZjIxZTRhMjk4ZjMzMGU1YTJkY2RkZGNkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzZmOWI1NGM3ZjM4NjQ5YjVhY2RmYWM1YmEzMzJkYmVlID0gJCgnPGRpdiBpZD0iaHRtbF82ZjliNTRjN2YzODY0OWI1YWNkZmFjNWJhMzMyZGJlZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdCBCaXJjaG1vdW50IFBhcmssSW9udmlldyxLZW5uZWR5IFBhcmsgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kMmQ3ZGI1YmYyMWU0YTI5OGYzMzBlNWEyZGNkZGRjZC5zZXRDb250ZW50KGh0bWxfNmY5YjU0YzdmMzg2NDliNWFjZGZhYzViYTMzMmRiZWUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTQzMDEwNWJmZTBlNGU2MGFlMjUyYmU0MGYxMTMzNzAuYmluZFBvcHVwKHBvcHVwX2QyZDdkYjViZjIxZTRhMjk4ZjMzMGU1YTJkY2RkZGNkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBiYzdlMDdlOWE4NzRmNjNhODE1N2JjYmM0NWMxZjMyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzExMTExNzAwMDAwMDA0LC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzJiN2FiOTUyMjU1YzQyZDJhMjFmMTAwYWI4NzQ3OWMyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI3ZDUxMjNmZWRkNzRjNjI4ZDRhNGRhOTBhYjdkYjQwID0gJCgnPGRpdiBpZD0iaHRtbF8yN2Q1MTIzZmVkZDc0YzYyOGQ0YTRkYTkwYWI3ZGI0MCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2xhaXJsZWEsR29sZGVuIE1pbGUsT2FrcmlkZ2UgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yYjdhYjk1MjI1NWM0MmQyYTIxZjEwMGFiODc0NzljMi5zZXRDb250ZW50KGh0bWxfMjdkNTEyM2ZlZGQ3NGM2MjhkNGE0ZGE5MGFiN2RiNDApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMGJjN2UwN2U5YTg3NGY2M2E4MTU3YmNiYzQ1YzFmMzIuYmluZFBvcHVwKHBvcHVwXzJiN2FiOTUyMjU1YzQyZDJhMjFmMTAwYWI4NzQ3OWMyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBlYjlmNjdmN2UxOTQzMWY4MWVlOTgxZTQ5MzY2ZTQyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE2MzE2LC03OS4yMzk0NzYwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hODljNDkwZmVmNjY0OWJhODQ5MjBjZWM0MjRjOTA2OSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mNWE0MjlmNjViZDk0MmZlOGYxNDNjYjE0MDViNDY0NCA9ICQoJzxkaXYgaWQ9Imh0bWxfZjVhNDI5ZjY1YmQ5NDJmZThmMTQzY2IxNDA1YjQ2NDQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsaWZmY3Jlc3QsQ2xpZmZzaWRlLFNjYXJib3JvdWdoIFZpbGxhZ2UgV2VzdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2E4OWM0OTBmZWY2NjQ5YmE4NDkyMGNlYzQyNGM5MDY5LnNldENvbnRlbnQoaHRtbF9mNWE0MjlmNjViZDk0MmZlOGYxNDNjYjE0MDViNDY0NCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wZWI5ZjY3ZjdlMTk0MzFmODFlZTk4MWU0OTM2NmU0Mi5iaW5kUG9wdXAocG9wdXBfYTg5YzQ5MGZlZjY2NDliYTg0OTIwY2VjNDI0YzkwNjkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGI3YjIzOGUxNmZiNDA3OTk1NTJmZDM4MDQ5MWNlNzIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTI2NTcwMDAwMDAwMDQsLTc5LjI2NDg0ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDBkMGVhNTRiOWZjNGYwNDliY2UyZTZkNmZiYmZhMzIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODhjODZmYjM2NGViNGNmNmI5ZWIxNzI5NDI5YTdjN2QgPSAkKCc8ZGl2IGlkPSJodG1sXzg4Yzg2ZmIzNjRlYjRjZjZiOWViMTcyOTQyOWE3YzdkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CaXJjaCBDbGlmZixDbGlmZnNpZGUgV2VzdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzAwZDBlYTU0YjlmYzRmMDQ5YmNlMmU2ZDZmYmJmYTMyLnNldENvbnRlbnQoaHRtbF84OGM4NmZiMzY0ZWI0Y2Y2YjllYjE3Mjk0MjlhN2M3ZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80YjdiMjM4ZTE2ZmI0MDc5OTU1MmZkMzgwNDkxY2U3Mi5iaW5kUG9wdXAocG9wdXBfMDBkMGVhNTRiOWZjNGYwNDliY2UyZTZkNmZiYmZhMzIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTQ0ZmRkYzRkOWFmNDhkNWJjZmM2OTM4OGZjNDg3NjkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTc0MDk2LC03OS4yNzMzMDQwMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mZmI5NDE3NWU5YzA0NjA4ODQ0MTExMzIzNjRkZDVjOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wMDg5ZmY0ZjBmODQ0M2M0YmY3NDM0ODczM2JiYzdjMyA9ICQoJzxkaXYgaWQ9Imh0bWxfMDA4OWZmNGYwZjg0NDNjNGJmNzQzNDg3MzNiYmM3YzMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvcnNldCBQYXJrLFNjYXJib3JvdWdoIFRvd24gQ2VudHJlLFdleGZvcmQgSGVpZ2h0cyBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZmYjk0MTc1ZTljMDQ2MDg4NDQxMTEzMjM2NGRkNWM5LnNldENvbnRlbnQoaHRtbF8wMDg5ZmY0ZjBmODQ0M2M0YmY3NDM0ODczM2JiYzdjMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNDRmZGRjNGQ5YWY0OGQ1YmNmYzY5Mzg4ZmM0ODc2OS5iaW5kUG9wdXAocG9wdXBfZmZiOTQxNzVlOWMwNDYwODg0NDExMTMyMzY0ZGQ1YzkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTZmNWIzY2Q1NjAxNDVkYTgyODdlOGViMjMyMjVhYmQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTAwNzE1MDAwMDAwMDQsLTc5LjI5NTg0OTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmZiNWUyOWUxZWNmNDYyYzg2ZDlhZWU4OWQyYzY1ODcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDZhYTc2ZWQzYjZiNDg1YzllMThkNDQ5Nzc2ZWNjMjcgPSAkKCc8ZGl2IGlkPSJodG1sX2Q2YWE3NmVkM2I2YjQ4NWM5ZTE4ZDQ0OTc3NmVjYzI3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJ5dmFsZSxXZXhmb3JkIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmZiNWUyOWUxZWNmNDYyYzg2ZDlhZWU4OWQyYzY1ODcuc2V0Q29udGVudChodG1sX2Q2YWE3NmVkM2I2YjQ4NWM5ZTE4ZDQ0OTc3NmVjYzI3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk2ZjViM2NkNTYwMTQ1ZGE4Mjg3ZThlYjIzMjI1YWJkLmJpbmRQb3B1cChwb3B1cF8yZmI1ZTI5ZTFlY2Y0NjJjODZkOWFlZTg5ZDJjNjU4Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MDkwNDBiZjJlMzk0OTk5OTUyMmU4YjBlOTA2Mzc3ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5NDIwMDMsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2I1YmFiYmI5YzUyYjRlZDRiNTIzZDhiZTZhMGRhNGVhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJiZjI2MmJiZWZlMjRmN2M5MmRmMDQ5NmY4ZDM0ZTRmID0gJCgnPGRpdiBpZD0iaHRtbF8yYmYyNjJiYmVmZTI0ZjdjOTJkZjA0OTZmOGQzNGU0ZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjViYWJiYjljNTJiNGVkNGI1MjNkOGJlNmEwZGE0ZWEuc2V0Q29udGVudChodG1sXzJiZjI2MmJiZWZlMjRmN2M5MmRmMDQ5NmY4ZDM0ZTRmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkwOTA0MGJmMmUzOTQ5OTk5NTIyZThiMGU5MDYzNzdlLmJpbmRQb3B1cChwb3B1cF9iNWJhYmJiOWM1MmI0ZWQ0YjUyM2Q4YmU2YTBkYTRlYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83MDMzODI1NGE1ZGU0ODEyOWE0NDQ2M2UwOGVkM2I5NSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4MTYzNzUsLTc5LjMwNDMwMjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDU0NmQ0MDcwNDczNDc5OGFlNDM4N2YyNTY4YmE5YjAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2VjNTg0MTY4MjAwNDYyOWI1NDYxMTZkMGYzODI0MmIgPSAkKCc8ZGl2IGlkPSJodG1sXzNlYzU4NDE2ODIwMDQ2MjliNTQ2MTE2ZDBmMzgyNDJiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGFya3MgQ29ybmVycyxTdWxsaXZhbixUYW0gTyYjMzk7U2hhbnRlciBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q1NDZkNDA3MDQ3MzQ3OThhZTQzODdmMjU2OGJhOWIwLnNldENvbnRlbnQoaHRtbF8zZWM1ODQxNjgyMDA0NjI5YjU0NjExNmQwZjM4MjQyYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83MDMzODI1NGE1ZGU0ODEyOWE0NDQ2M2UwOGVkM2I5NS5iaW5kUG9wdXAocG9wdXBfZDU0NmQ0MDcwNDczNDc5OGFlNDM4N2YyNTY4YmE5YjApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGU3NzA3MGY4MmM2NGQ5Njg3NmNkYTgxNGRjN2Y0M2UgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My44MTUyNTIyLC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y2OWQxMDljYWNhYjQ2NDQ4ZmY1MTNmMmNhYTYwNDVkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzk5ZGI4YzdmNDA2YjQ0MzA5MTU2ZTY1YzZhYjQ3Y2MzID0gJCgnPGRpdiBpZD0iaHRtbF85OWRiOGM3ZjQwNmI0NDMwOTE1NmU2NWM2YWI0N2NjMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0IE5vcnRoLEwmIzM5O0Ftb3JlYXV4IEVhc3QsTWlsbGlrZW4sU3RlZWxlcyBFYXN0IENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjY5ZDEwOWNhY2FiNDY0NDhmZjUxM2YyY2FhNjA0NWQuc2V0Q29udGVudChodG1sXzk5ZGI4YzdmNDA2YjQ0MzA5MTU2ZTY1YzZhYjQ3Y2MzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhlNzcwNzBmODJjNjRkOTY4NzZjZGE4MTRkYzdmNDNlLmJpbmRQb3B1cChwb3B1cF9mNjlkMTA5Y2FjYWI0NjQ0OGZmNTEzZjJjYWE2MDQ1ZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zMzUxMTJiMmVjYjc0MTUxYTlhODg1MjExMTEyNjU4NSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5OTUyNTIwMDAwMDAwNSwtNzkuMzE4Mzg4N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNzk3ZDU4ZjMwNDk0OWY0OWYxNGJhZmMxNjg0ZmMyZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yZTdlYmZmNzNjNjU0YmRkYjVhZWIwM2IxN2E2MjZkNyA9ICQoJzxkaXYgaWQ9Imh0bWxfMmU3ZWJmZjczYzY1NGJkZGI1YWViMDNiMTdhNjI2ZDciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkwmIzM5O0Ftb3JlYXV4IFdlc3QgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hNzk3ZDU4ZjMwNDk0OWY0OWYxNGJhZmMxNjg0ZmMyZS5zZXRDb250ZW50KGh0bWxfMmU3ZWJmZjczYzY1NGJkZGI1YWViMDNiMTdhNjI2ZDcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzM1MTEyYjJlY2I3NDE1MWE5YTg4NTIxMTExMjY1ODUuYmluZFBvcHVwKHBvcHVwX2E3OTdkNThmMzA0OTQ5ZjQ5ZjE0YmFmYzE2ODRmYzJlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzVjNDA5YzFkNDNmOTRiOWFiMzE3MGZjYmY5Y2I3MmNkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuODAzNzYyMiwtNzkuMzYzNDUxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82YzNjNTgwYTJlMzU0MmYxYjdkMjUxYTE3Y2JlMTQzYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83MTMxOTFlYzMxMDc0MmVjYjRiODVkYmQ5NjA2YTAwOCA9ICQoJzxkaXYgaWQ9Imh0bWxfNzEzMTkxZWMzMTA3NDJlY2I0Yjg1ZGJkOTYwNmEwMDgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhpbGxjcmVzdCBWaWxsYWdlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmMzYzU4MGEyZTM1NDJmMWI3ZDI1MWExN2NiZTE0M2Euc2V0Q29udGVudChodG1sXzcxMzE5MWVjMzEwNzQyZWNiNGI4NWRiZDk2MDZhMDA4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzVjNDA5YzFkNDNmOTRiOWFiMzE3MGZjYmY5Y2I3MmNkLmJpbmRQb3B1cChwb3B1cF82YzNjNTgwYTJlMzU0MmYxYjdkMjUxYTE3Y2JlMTQzYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81YTI5OTYyMDlhZjg0MTY0OTNiMmUxMzZmMTlhOGVkYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3ODUxNzUsLTc5LjM0NjU1NTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzY2MzBkZWVkNzk5NDUxMGE1MjdhMDVhNTIyZmY0ZTQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2I4MjkzNjc2YTM3NDEwNWFiZmY3OTY0NTFhY2Y2MjIgPSAkKCc8ZGl2IGlkPSJodG1sXzNiODI5MzY3NmEzNzQxMDVhYmZmNzk2NDUxYWNmNjIyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GYWlydmlldyxIZW5yeSBGYXJtLE9yaW9sZSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M2NjMwZGVlZDc5OTQ1MTBhNTI3YTA1YTUyMmZmNGU0LnNldENvbnRlbnQoaHRtbF8zYjgyOTM2NzZhMzc0MTA1YWJmZjc5NjQ1MWFjZjYyMik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81YTI5OTYyMDlhZjg0MTY0OTNiMmUxMzZmMTlhOGVkYS5iaW5kUG9wdXAocG9wdXBfYzY2MzBkZWVkNzk5NDUxMGE1MjdhMDVhNTIyZmY0ZTQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNWIxZDliYzUwYjAyNDcwMGJlZDg4YTBhMDJhMGJkY2IgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43ODY5NDczLC03OS4zODU5NzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmVkZTJlM2M5YmFhNDQ3NDk0YTFjYzI0ZDA1ZjUzMDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzY4MzA3OWYzYWY3NDliMWE3MTFmYWI1Y2JhYTJiYWIgPSAkKCc8ZGl2IGlkPSJodG1sXzM2ODMwNzlmM2FmNzQ5YjFhNzExZmFiNWNiYWEyYmFiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXl2aWV3IFZpbGxhZ2UgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mZWRlMmUzYzliYWE0NDc0OTRhMWNjMjRkMDVmNTMwOS5zZXRDb250ZW50KGh0bWxfMzY4MzA3OWYzYWY3NDliMWE3MTFmYWI1Y2JhYTJiYWIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNWIxZDliYzUwYjAyNDcwMGJlZDg4YTBhMDJhMGJkY2IuYmluZFBvcHVwKHBvcHVwX2ZlZGUyZTNjOWJhYTQ0NzQ5NGExY2MyNGQwNWY1MzA5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IxYjA5NjhmNDUyNDQ1NWZhZjBhMTE4ZTU3NTdmODM0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzg5MDUzLC03OS40MDg0OTI3OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84MjkzMGM4MDRlN2Y0MDZhOWJkNzZhMzczOWUxMGY5MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wZjk4MmU2ZTZjMjA0ZDExODdkNzFmMmE4Zjg2YzFmMiA9ICQoJzxkaXYgaWQ9Imh0bWxfMGY5ODJlNmU2YzIwNGQxMTg3ZDcxZjJhOGY4NmMxZjIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5ld3RvbmJyb29rLFdpbGxvd2RhbGUgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MjkzMGM4MDRlN2Y0MDZhOWJkNzZhMzczOWUxMGY5MC5zZXRDb250ZW50KGh0bWxfMGY5ODJlNmU2YzIwNGQxMTg3ZDcxZjJhOGY4NmMxZjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjFiMDk2OGY0NTI0NDU1ZmFmMGExMThlNTc1N2Y4MzQuYmluZFBvcHVwKHBvcHVwXzgyOTMwYzgwNGU3ZjQwNmE5YmQ3NmEzNzM5ZTEwZjkwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzcyMWNiOGVkZjUzNjQwZDc5MDczYjBkNzkyZmI0ZDI2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzcwMTE5OSwtNzkuNDA4NDkyNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGUyMDMzMjA0OTY1NDg1NDgxN2U3NDJiMWY1ZGJjZGIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzBjZGUyMGIwMzBmNGI0YzhkNzc4MTNmOTMyZGJkOWMgPSAkKCc8ZGl2IGlkPSJodG1sXzMwY2RlMjBiMDMwZjRiNGM4ZDc3ODEzZjkzMmRiZDljIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XaWxsb3dkYWxlIFNvdXRoIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGUyMDMzMjA0OTY1NDg1NDgxN2U3NDJiMWY1ZGJjZGIuc2V0Q29udGVudChodG1sXzMwY2RlMjBiMDMwZjRiNGM4ZDc3ODEzZjkzMmRiZDljKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzcyMWNiOGVkZjUzNjQwZDc5MDczYjBkNzkyZmI0ZDI2LmJpbmRQb3B1cChwb3B1cF84ZTIwMzMyMDQ5NjU0ODU0ODE3ZTc0MmIxZjVkYmNkYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jMTYzZWUyMmY0Yjg0MTRkYTU0ODc0YzY3YTcyMjEwYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1Mjc1ODI5OTk5OTk5NiwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84N2I0NDMzYzk5ZTE0ZjkyYTA0YTZmZjUxMjhlNWY5ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iOTI4NjIxZWM5ZGQ0NjYyOWFjNTc4ZjQxNmM0ZjU1NSA9ICQoJzxkaXYgaWQ9Imh0bWxfYjkyODYyMWVjOWRkNDY2MjlhYzU3OGY0MTZjNGY1NTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPllvcmsgTWlsbHMgV2VzdCBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg3YjQ0MzNjOTllMTRmOTJhMDRhNmZmNTEyOGU1ZjlmLnNldENvbnRlbnQoaHRtbF9iOTI4NjIxZWM5ZGQ0NjYyOWFjNTc4ZjQxNmM0ZjU1NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jMTYzZWUyMmY0Yjg0MTRkYTU0ODc0YzY3YTcyMjEwYS5iaW5kUG9wdXAocG9wdXBfODdiNDQzM2M5OWUxNGY5MmEwNGE2ZmY1MTI4ZTVmOWYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWIwMWM1ZGNlNjA3NDYzMGIxNjBmYzAwNGRmNzYzOTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43ODI3MzY0LC03OS40NDIyNTkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzZjMzZkZmFkMGM1MzQzYmU4OWJjNWE1N2ViNTVlMGMzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JiNThhZDg4NGI0NzQxNGZhYmViMTlhNDU5M2M0MzhjID0gJCgnPGRpdiBpZD0iaHRtbF9iYjU4YWQ4ODRiNDc0MTRmYWJlYjE5YTQ1OTNjNDM4YyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2lsbG93ZGFsZSBXZXN0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmMzNmRmYWQwYzUzNDNiZTg5YmM1YTU3ZWI1NWUwYzMuc2V0Q29udGVudChodG1sX2JiNThhZDg4NGI0NzQxNGZhYmViMTlhNDU5M2M0MzhjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2FiMDFjNWRjZTYwNzQ2MzBiMTYwZmMwMDRkZjc2Mzk4LmJpbmRQb3B1cChwb3B1cF82YzM2ZGZhZDBjNTM0M2JlODliYzVhNTdlYjU1ZTBjMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80ODg4MmYxZDU1NWU0MDExYWE5MGE4ZjczNjM4MDhjZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1MzI1ODYsLTc5LjMyOTY1NjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWMyOThkODliNDI4NGYzZGIwNTQ2YmEzZWZjM2VhYmUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOWVmZjlhYjg5YjI0NDAxZjlmYWQwNzhkZDFjYTUwOTAgPSAkKCc8ZGl2IGlkPSJodG1sXzllZmY5YWI4OWIyNDQwMWY5ZmFkMDc4ZGQxY2E1MDkwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrd29vZHMgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hYzI5OGQ4OWI0Mjg0ZjNkYjA1NDZiYTNlZmMzZWFiZS5zZXRDb250ZW50KGh0bWxfOWVmZjlhYjg5YjI0NDAxZjlmYWQwNzhkZDFjYTUwOTApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDg4ODJmMWQ1NTVlNDAxMWFhOTBhOGY3MzYzODA4Y2YuYmluZFBvcHVwKHBvcHVwX2FjMjk4ZDg5YjQyODRmM2RiMDU0NmJhM2VmYzNlYWJlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzUzOWQxOWFkMTRhYjRiODhhZGE4MjhlNzQyYWE0OTE3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ1OTA1Nzk5OTk5OTk2LC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmE4OTEwNTc1NzRhNGMwZGI2ZGQ2NzczZTU5M2M2NWYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGI0MmZkM2QxZjMyNDQ2NTg1NTI2MmEyN2JmZjk3MWUgPSAkKCc8ZGl2IGlkPSJodG1sX2RiNDJmZDNkMWYzMjQ0NjU4NTUyNjJhMjdiZmY5NzFlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb24gTWlsbHMgTm9ydGggQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iYTg5MTA1NzU3NGE0YzBkYjZkZDY3NzNlNTkzYzY1Zi5zZXRDb250ZW50KGh0bWxfZGI0MmZkM2QxZjMyNDQ2NTg1NTI2MmEyN2JmZjk3MWUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTM5ZDE5YWQxNGFiNGI4OGFkYTgyOGU3NDJhYTQ5MTcuYmluZFBvcHVwKHBvcHVwX2JhODkxMDU3NTc0YTRjMGRiNmRkNjc3M2U1OTNjNjVmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJjZDBjNjE4MWUxMjRiMjdiNWQ0ODZmN2U1OTcyNDc5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI1ODk5NzAwMDAwMDEsLTc5LjM0MDkyM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85MmM3ZWM0YTJiMjc0ZjRiOGRkY2IxYWViNjViMTc4NyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xMGQxYWUwNzBiZDA0ZmY2ODNmMDM5NjY2ZTcwZmYwOSA9ICQoJzxkaXYgaWQ9Imh0bWxfMTBkMWFlMDcwYmQwNGZmNjgzZjAzOTY2NmU3MGZmMDkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZsZW1pbmdkb24gUGFyayxEb24gTWlsbHMgU291dGggQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85MmM3ZWM0YTJiMjc0ZjRiOGRkY2IxYWViNjViMTc4Ny5zZXRDb250ZW50KGh0bWxfMTBkMWFlMDcwYmQwNGZmNjgzZjAzOTY2NmU3MGZmMDkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmNkMGM2MTgxZTEyNGIyN2I1ZDQ4NmY3ZTU5NzI0NzkuYmluZFBvcHVwKHBvcHVwXzkyYzdlYzRhMmIyNzRmNGI4ZGRjYjFhZWI2NWIxNzg3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMzNjlmODVjNzdmODQwOWY4MmI4NjdmMGI0N2FlYzViID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzU0MzI4MywtNzkuNDQyMjU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84ZDViZTkzMmIzNGQ0OTRmOGMwOGIzNjg2NTY5MjJmYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iYjg4NDI2YzkwNGE0YTRlYTBkNDJiNjZlNjQ3OWE0ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfYmI4ODQyNmM5MDRhNGE0ZWEwZDQyYjY2ZTY0NzlhNGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJhdGh1cnN0IE1hbm9yLERvd25zdmlldyBOb3J0aCxXaWxzb24gSGVpZ2h0cyBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhkNWJlOTMyYjM0ZDQ5NGY4YzA4YjM2ODY1NjkyMmZhLnNldENvbnRlbnQoaHRtbF9iYjg4NDI2YzkwNGE0YTRlYTBkNDJiNjZlNjQ3OWE0Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMzY5Zjg1Yzc3Zjg0MDlmODJiODY3ZjBiNDdhZWM1Yi5iaW5kUG9wdXAocG9wdXBfOGQ1YmU5MzJiMzRkNDk0ZjhjMDhiMzY4NjU2OTIyZmEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTZiNTdlYTFmODc0NDVkZWJkNWZmNWFiYmYxYzZiZjUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Njc5ODAzLC03OS40ODcyNjE5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zM2UwOGZmOTYyNGY0MWU3YTJhM2VmMWQyNTE2NWJkYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84YzhhNGEyNzAxY2Q0MTFiYmI4YzBiN2FjYzcyOTllMyA9ICQoJzxkaXYgaWQ9Imh0bWxfOGM4YTRhMjcwMWNkNDExYmJiOGMwYjdhY2M3Mjk5ZTMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vcnRod29vZCBQYXJrLFlvcmsgVW5pdmVyc2l0eSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzMzZTA4ZmY5NjI0ZjQxZTdhMmEzZWYxZDI1MTY1YmRhLnNldENvbnRlbnQoaHRtbF84YzhhNGEyNzAxY2Q0MTFiYmI4YzBiN2FjYzcyOTllMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85NmI1N2VhMWY4NzQ0NWRlYmQ1ZmY1YWJiZjFjNmJmNS5iaW5kUG9wdXAocG9wdXBfMzNlMDhmZjk2MjRmNDFlN2EyYTNlZjFkMjUxNjViZGEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGQyOTQzMjA5MjljNDVkZjg5OTVmMmIzMzZiOWQyZDcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Mzc0NzMyMDAwMDAwMDQsLTc5LjQ2NDc2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2ZjYjcxNjA4MDgxYzQ4Nzg5NTE2NmU3ZTgzMzJmOGM0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzA5NDQzMmUxYzY2NTQ1MWZiMTc5OTk0MGNmZDc3ZjdmID0gJCgnPGRpdiBpZD0iaHRtbF8wOTQ0MzJlMWM2NjU0NTFmYjE3OTk5NDBjZmQ3N2Y3ZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q0ZCIFRvcm9udG8sRG93bnN2aWV3IEVhc3QgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mY2I3MTYwODA4MWM0ODc4OTUxNjZlN2U4MzMyZjhjNC5zZXRDb250ZW50KGh0bWxfMDk0NDMyZTFjNjY1NDUxZmIxNzk5OTQwY2ZkNzdmN2YpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGQyOTQzMjA5MjljNDVkZjg5OTVmMmIzMzZiOWQyZDcuYmluZFBvcHVwKHBvcHVwX2ZjYjcxNjA4MDgxYzQ4Nzg5NTE2NmU3ZTgzMzJmOGM0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc3NmFlMWEzZTk1NzQ4OWU5Y2EwNGMyYTVkNzcwZmZkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzM5MDE0NiwtNzkuNTA2OTQzNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lMzM3YmIzYTUyOGU0OWQwYjc4ZDVkMTc5YmQ5OWUxNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hMjk1Y2Y0Y2VhYTQ0YTg2YWQxYWZhNzhhYzY2MTRhYiA9ICQoJzxkaXYgaWQ9Imh0bWxfYTI5NWNmNGNlYWE0NGE4NmFkMWFmYTc4YWM2NjE0YWIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvd25zdmlldyBXZXN0IENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTMzN2JiM2E1MjhlNDlkMGI3OGQ1ZDE3OWJkOTllMTQuc2V0Q29udGVudChodG1sX2EyOTVjZjRjZWFhNDRhODZhZDFhZmE3OGFjNjYxNGFiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc3NmFlMWEzZTk1NzQ4OWU5Y2EwNGMyYTVkNzcwZmZkLmJpbmRQb3B1cChwb3B1cF9lMzM3YmIzYTUyOGU0OWQwYjc4ZDVkMTc5YmQ5OWUxNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZTdjZjg3MTRiNzI0Mjg4ODg2ZjAzMjVlZmQ2Y2UwNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyODQ5NjQsLTc5LjQ5NTY5NzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MGZmYjQiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODBmZmI0IiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2E4YzI3Mzk0ODhlNjQ3MTZiY2U5NjY4ZTdlYzVkYzBhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQxY2RiZDg1YWQzNzRlMzE4MTE3M2MwMGQxNTRiZDg1ID0gJCgnPGRpdiBpZD0iaHRtbF80MWNkYmQ4NWFkMzc0ZTMxODExNzNjMDBkMTU0YmQ4NSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IENlbnRyYWwgQ2x1c3RlciAzPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hOGMyNzM5NDg4ZTY0NzE2YmNlOTY2OGU3ZWM1ZGMwYS5zZXRDb250ZW50KGh0bWxfNDFjZGJkODVhZDM3NGUzMTgxMTczYzAwZDE1NGJkODUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2U3Y2Y4NzE0YjcyNDI4ODg4NmYwMzI1ZWZkNmNlMDcuYmluZFBvcHVwKHBvcHVwX2E4YzI3Mzk0ODhlNjQ3MTZiY2U5NjY4ZTdlYzVkYzBhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRlNTM0OTE0NWI0NDQ1MDFhMzRjYjhkYjk4OTM2MGJjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzYxNjMxMywtNzkuNTIwOTk5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmZiM2FiZGEzMThkNGFmN2EwMjU1NDc4NzllMjAzMjggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjkzN2M2YjlkYjY0NDVkMWFhOTljYjExODFmMDI2YTYgPSAkKCc8ZGl2IGlkPSJodG1sXzI5MzdjNmI5ZGI2NDQ1ZDFhYTk5Y2IxMTgxZjAyNmE2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb3duc3ZpZXcgTm9ydGh3ZXN0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYmZiM2FiZGEzMThkNGFmN2EwMjU1NDc4NzllMjAzMjguc2V0Q29udGVudChodG1sXzI5MzdjNmI5ZGI2NDQ1ZDFhYTk5Y2IxMTgxZjAyNmE2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzRlNTM0OTE0NWI0NDQ1MDFhMzRjYjhkYjk4OTM2MGJjLmJpbmRQb3B1cChwb3B1cF9iZmIzYWJkYTMxOGQ0YWY3YTAyNTU0Nzg3OWUyMDMyOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zYzM5NGJjMjVkOTI0MjlkYmI5ODA1YzMzYzljOWNhYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNTg4MjI5OTk5OTk5NSwtNzkuMzE1NTcxNTk5OTk5OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGNkMTYwZDI2YzY4NDRiOThiNjVlY2Y3ZTMyNzg1M2UgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYWY3NzhmZDFmMjI2NDE0MWI4MzlhNWM0MTI4MTczNWMgPSAkKCc8ZGl2IGlkPSJodG1sX2FmNzc4ZmQxZjIyNjQxNDFiODM5YTVjNDEyODE3MzVjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5WaWN0b3JpYSBWaWxsYWdlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGNkMTYwZDI2YzY4NDRiOThiNjVlY2Y3ZTMyNzg1M2Uuc2V0Q29udGVudChodG1sX2FmNzc4ZmQxZjIyNjQxNDFiODM5YTVjNDEyODE3MzVjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNjMzk0YmMyNWQ5MjQyOWRiYjk4MDVjMzNjOWM5Y2FiLmJpbmRQb3B1cChwb3B1cF84Y2QxNjBkMjZjNjg0NGI5OGI2NWVjZjdlMzI3ODUzZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85YmVhOWUwZDkyYTA0OGM3OTI2ZGYxNWJmOTNiNjUwNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcwNjM5NzIsLTc5LjMwOTkzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNmEzY2NlYTVmYjA0OWNlOTViNjQwNTlhMThmN2MxNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hZWQwN2E3NDBlZWI0ZDQwYTc4NzdjNTYwZTllNmI1MyA9ICQoJzxkaXYgaWQ9Imh0bWxfYWVkMDdhNzQwZWViNGQ0MGE3ODc3YzU2MGU5ZTZiNTMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldvb2RiaW5lIEdhcmRlbnMsUGFya3ZpZXcgSGlsbCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2E2YTNjY2VhNWZiMDQ5Y2U5NWI2NDA1OWExOGY3YzE3LnNldENvbnRlbnQoaHRtbF9hZWQwN2E3NDBlZWI0ZDQwYTc4NzdjNTYwZTllNmI1Myk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85YmVhOWUwZDkyYTA0OGM3OTI2ZGYxNWJmOTNiNjUwNC5iaW5kUG9wdXAocG9wdXBfYTZhM2NjZWE1ZmIwNDljZTk1YjY0MDU5YTE4ZjdjMTcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2Q1OTllNmZmOTQyNDdkOThmOGVkZTNkZjc0MjcwOGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTUzNDM5MDAwMDAwMDUsLTc5LjMxODM4ODddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjE3NTllMDU1M2M0NGRiYWJmMWM1Y2U4ZTI5ZTZkMGUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDhkODIyMjZkMDY0NDQ2ZTliMDJiMzk3ZTc3ODQ2NWUgPSAkKCc8ZGl2IGlkPSJodG1sXzQ4ZDgyMjI2ZDA2NDQ0NmU5YjAyYjM5N2U3Nzg0NjVlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Xb29kYmluZSBIZWlnaHRzIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjE3NTllMDU1M2M0NGRiYWJmMWM1Y2U4ZTI5ZTZkMGUuc2V0Q29udGVudChodG1sXzQ4ZDgyMjI2ZDA2NDQ0NmU5YjAyYjM5N2U3Nzg0NjVlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NkNTk5ZTZmZjk0MjQ3ZDk4ZjhlZGUzZGY3NDI3MDhmLmJpbmRQb3B1cChwb3B1cF8yMTc1OWUwNTUzYzQ0ZGJhYmYxYzVjZThlMjllNmQwZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jMWE1YWU2MmRhYzU0YTA3YTc0ZDg4OTRhMjQ2YTkzMyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY3NjM1NzM5OTk5OTk5LC03OS4yOTMwMzEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzhhZmM2MjllMzQ1YTQ5ZDA5ZDVjMThiYmM2Y2M5MzRjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzc3YzI1MjI0MWJkZTQyMDBiMzhjNjE4NTdkMjJlNmUzID0gJCgnPGRpdiBpZD0iaHRtbF83N2MyNTIyNDFiZGU0MjAwYjM4YzYxODU3ZDIyZTZlMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhlIEJlYWNoZXMgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84YWZjNjI5ZTM0NWE0OWQwOWQ1YzE4YmJjNmNjOTM0Yy5zZXRDb250ZW50KGh0bWxfNzdjMjUyMjQxYmRlNDIwMGIzOGM2MTg1N2QyMmU2ZTMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzFhNWFlNjJkYWM1NGEwN2E3NGQ4ODk0YTI0NmE5MzMuYmluZFBvcHVwKHBvcHVwXzhhZmM2MjllMzQ1YTQ5ZDA5ZDVjMThiYmM2Y2M5MzRjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJmZWM5OGI4OWMzNDRiYTNhMDhiZDQ4MzY1MWYxM2MwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA5MDYwNCwtNzkuMzYzNDUxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMTNkYTNlMGIzNmE0YmMyODRmMjFmYTM0NTIyMjgyOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNTZmMjA2NjJhMzk0NmFiOGQwNzRlYzdmYmI4YjZhYiA9ICQoJzxkaXYgaWQ9Imh0bWxfMTU2ZjIwNjYyYTM5NDZhYjhkMDc0ZWM3ZmJiOGI2YWIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxlYXNpZGUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMTNkYTNlMGIzNmE0YmMyODRmMjFmYTM0NTIyMjgyOS5zZXRDb250ZW50KGh0bWxfMTU2ZjIwNjYyYTM5NDZhYjhkMDc0ZWM3ZmJiOGI2YWIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmZlYzk4Yjg5YzM0NGJhM2EwOGJkNDgzNjUxZjEzYzAuYmluZFBvcHVwKHBvcHVwX2MxM2RhM2UwYjM2YTRiYzI4NGYyMWZhMzQ1MjIyODI5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzkyNzg2ZDJkNGFiMDQwYzQ5MDVhMmZkOWFjY2YxZjRhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA1MzY4OSwtNzkuMzQ5MzcxOTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjViZTIyMmNiZjk3NDI0MThmMDI0MDNiNGJiMmY2Y2YgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGQ3MTk1YjIxZTEwNDgwN2FmODRmY2M4ZTdhNjk3NjEgPSAkKCc8ZGl2IGlkPSJodG1sX2RkNzE5NWIyMWUxMDQ4MDdhZjg0ZmNjOGU3YTY5NzYxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaG9ybmNsaWZmZSBQYXJrIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjViZTIyMmNiZjk3NDI0MThmMDI0MDNiNGJiMmY2Y2Yuc2V0Q29udGVudChodG1sX2RkNzE5NWIyMWUxMDQ4MDdhZjg0ZmNjOGU3YTY5NzYxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkyNzg2ZDJkNGFiMDQwYzQ5MDVhMmZkOWFjY2YxZjRhLmJpbmRQb3B1cChwb3B1cF9iNWJlMjIyY2JmOTc0MjQxOGYwMjQwM2I0YmIyZjZjZik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hZjk4MjQ5NDJmMjY0MjQxYTI5M2NmMmE4OWNlMTJiZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY4NTM0NywtNzkuMzM4MTA2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lMmViOTQxNTI3Yjk0MWMzYTQ2NWJlM2U1NDNjZmFjMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83MGRiY2Q3YmMzNWE0ZmVkODYyNmFmNDQ3YjY4MWY4NCA9ICQoJzxkaXYgaWQ9Imh0bWxfNzBkYmNkN2JjMzVhNGZlZDg2MjZhZjQ0N2I2ODFmODQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgVG9yb250byBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2UyZWI5NDE1MjdiOTQxYzNhNDY1YmUzZTU0M2NmYWMxLnNldENvbnRlbnQoaHRtbF83MGRiY2Q3YmMzNWE0ZmVkODYyNmFmNDQ3YjY4MWY4NCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hZjk4MjQ5NDJmMjY0MjQxYTI5M2NmMmE4OWNlMTJiZi5iaW5kUG9wdXAocG9wdXBfZTJlYjk0MTUyN2I5NDFjM2E0NjViZTNlNTQzY2ZhYzEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOThlMmMxNTQxZDA5NDBiNjhiMmEwNDUxYWQzOGVlNmUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Nzk1NTcxLC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmQxMjBkZjhjYTYzNDRjOWJhMjAzYWEyYzQzNTVjOGMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTUyNTkyM2FmMTE0NGNlOWE2NTJkYTVhNGRkZGIzMzMgPSAkKCc8ZGl2IGlkPSJodG1sX2U1MjU5MjNhZjExNDRjZTlhNjUyZGE1YTRkZGRiMzMzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgRGFuZm9ydGggV2VzdCxSaXZlcmRhbGUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mZDEyMGRmOGNhNjM0NGM5YmEyMDNhYTJjNDM1NWM4Yy5zZXRDb250ZW50KGh0bWxfZTUyNTkyM2FmMTE0NGNlOWE2NTJkYTVhNGRkZGIzMzMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOThlMmMxNTQxZDA5NDBiNjhiMmEwNDUxYWQzOGVlNmUuYmluZFBvcHVwKHBvcHVwX2ZkMTIwZGY4Y2E2MzQ0YzliYTIwM2FhMmM0MzU1YzhjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzVjZjM0ZjZiODE0NDRlNWRiNzY4MmFiYzNhYjhmOTViID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY4OTk4NSwtNzkuMzE1NTcxNTk5OTk5OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmNmZGZiYTdhMDYxNDRhMmE3Y2M4YzZjMDQzNzYyNDEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTkwY2YxMDZmYzUzNDZiMWI5ZjlkYTcyZWFiMmYwYjAgPSAkKCc8ZGl2IGlkPSJodG1sX2U5MGNmMTA2ZmM1MzQ2YjFiOWY5ZGE3MmVhYjJmMGIwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgQmVhY2hlcyBXZXN0LEluZGlhIEJhemFhciBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZjZmRmYmE3YTA2MTQ0YTJhN2NjOGM2YzA0Mzc2MjQxLnNldENvbnRlbnQoaHRtbF9lOTBjZjEwNmZjNTM0NmIxYjlmOWRhNzJlYWIyZjBiMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81Y2YzNGY2YjgxNDQ0ZTVkYjc2ODJhYmMzYWI4Zjk1Yi5iaW5kUG9wdXAocG9wdXBfZmNmZGZiYTdhMDYxNDRhMmE3Y2M4YzZjMDQzNzYyNDEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjY2M2ZiMzQ1MTkxNDAyOGI3YTQ3NjY1MTRhMDg0ZmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTk1MjU1LC03OS4zNDA5MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWIwMjZkY2IxOWE4NDRiOTlkY2RkMDNkNjdjNTZkMzYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2MwZTY3OWQ2ZTQ4NDZjNmFmODk2MDM3MTZhN2ExYzcgPSAkKCc8ZGl2IGlkPSJodG1sXzdjMGU2NzlkNmU0ODQ2YzZhZjg5NjAzNzE2YTdhMWM3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdHVkaW8gRGlzdHJpY3QgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81YjAyNmRjYjE5YTg0NGI5OWRjZGQwM2Q2N2M1NmQzNi5zZXRDb250ZW50KGh0bWxfN2MwZTY3OWQ2ZTQ4NDZjNmFmODk2MDM3MTZhN2ExYzcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjY2M2ZiMzQ1MTkxNDAyOGI3YTQ3NjY1MTRhMDg0ZmIuYmluZFBvcHVwKHBvcHVwXzViMDI2ZGNiMTlhODQ0Yjk5ZGNkZDAzZDY3YzU2ZDM2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzVhMWIwMTI3M2FkOTQ0NzlhMTQwOWYxZjY3MzQ0MDVkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI4MDIwNSwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ZDc0MWRhZDUzZjI0YmEyOGI0NTUwZGM0ZjcxNWY2OCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81OGMxZmRkNWNlMzU0ZDkxYTNmNTk3NDY3YmY4OWZiYSA9ICQoJzxkaXYgaWQ9Imh0bWxfNThjMWZkZDVjZTM1NGQ5MWEzZjU5NzQ2N2JmODlmYmEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIFBhcmsgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80ZDc0MWRhZDUzZjI0YmEyOGI0NTUwZGM0ZjcxNWY2OC5zZXRDb250ZW50KGh0bWxfNThjMWZkZDVjZTM1NGQ5MWEzZjU5NzQ2N2JmODlmYmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNWExYjAxMjczYWQ5NDQ3OWExNDA5ZjFmNjczNDQwNWQuYmluZFBvcHVwKHBvcHVwXzRkNzQxZGFkNTNmMjRiYTI4YjQ1NTBkYzRmNzE1ZjY4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzUwNGE1YzBhZjg2NzQ0MWY5OTYxMzk1YjI1Nzk0NjkzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzEyNzUxMSwtNzkuMzkwMTk3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xZjdjNmQwOTg3MjQ0N2I2YTliOTY4YTIyZGY1ZjQ3YiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mZDRhOTczZmQyY2I0MDhkOGM2Y2FkNjJkNmM0NzNiZCA9ICQoJzxkaXYgaWQ9Imh0bWxfZmQ0YTk3M2ZkMmNiNDA4ZDhjNmNhZDYyZDZjNDczYmQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUgTm9ydGggQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xZjdjNmQwOTg3MjQ0N2I2YTliOTY4YTIyZGY1ZjQ3Yi5zZXRDb250ZW50KGh0bWxfZmQ0YTk3M2ZkMmNiNDA4ZDhjNmNhZDYyZDZjNDczYmQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTA0YTVjMGFmODY3NDQxZjk5NjEzOTViMjU3OTQ2OTMuYmluZFBvcHVwKHBvcHVwXzFmN2M2ZDA5ODcyNDQ3YjZhOWI5NjhhMjJkZjVmNDdiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I1YWQ4M2JjYTg1OTRlMGE4OWM4NzQzYjZmOGMyMWZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE1MzgzNCwtNzkuNDA1Njc4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGI4Y2IyMmVhODJmNGUzNWIzZTZmMWJiZTZmYmJmN2UgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjZmZjI5MWIzZTIzNDMwNDgyZWY2YTFmMTE4OWNlNjMgPSAkKCc8ZGl2IGlkPSJodG1sXzI2ZmYyOTFiM2UyMzQzMDQ4MmVmNmExZjExODljZTYzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aCBUb3JvbnRvIFdlc3QgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84YjhjYjIyZWE4MmY0ZTM1YjNlNmYxYmJlNmZiYmY3ZS5zZXRDb250ZW50KGh0bWxfMjZmZjI5MWIzZTIzNDMwNDgyZWY2YTFmMTE4OWNlNjMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjVhZDgzYmNhODU5NGUwYTg5Yzg3NDNiNmY4YzIxZmEuYmluZFBvcHVwKHBvcHVwXzhiOGNiMjJlYTgyZjRlMzViM2U2ZjFiYmU2ZmJiZjdlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2YyYmY1YjNhNjA0NTQwNjM4YTRmNDJjNzk0ZTQxMDdkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA0MzI0NCwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMTU0ODY1ZGQ2ZDk0YmU3YmY4YWExNjQ0YzE4ODk4NyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hZmM4Y2I0MDdmODk0YTA5YTQxNzE3M2RhMzE4ZDRiNyA9ICQoJzxkaXYgaWQ9Imh0bWxfYWZjOGNiNDA3Zjg5NGEwOWE0MTcxNzNkYTMxOGQ0YjciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMTU0ODY1ZGQ2ZDk0YmU3YmY4YWExNjQ0YzE4ODk4Ny5zZXRDb250ZW50KGh0bWxfYWZjOGNiNDA3Zjg5NGEwOWE0MTcxNzNkYTMxOGQ0YjcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjJiZjViM2E2MDQ1NDA2MzhhNGY0MmM3OTRlNDEwN2QuYmluZFBvcHVwKHBvcHVwX2MxNTQ4NjVkZDZkOTRiZTdiZjhhYTE2NDRjMTg4OTg3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJjMGRiNGNkYjE0NzQzODU4YzI4ZmEyMTAxOWVhZTI4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg5NTc0MywtNzkuMzgzMTU5OTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjhmNjRlYWIyYzU1NGNhYjg1NTgyMGVlYzQ4NDY5NTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjEzYTBhOTFiOWIzNGY2NjhlMjA1MjQ2YzlkYTg3N2YgPSAkKCc8ZGl2IGlkPSJodG1sX2YxM2EwYTkxYjliMzRmNjY4ZTIwNTI0NmM5ZGE4NzdmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb29yZSBQYXJrLFN1bW1lcmhpbGwgRWFzdCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y4ZjY0ZWFiMmM1NTRjYWI4NTU4MjBlZWM0ODQ2OTU4LnNldENvbnRlbnQoaHRtbF9mMTNhMGE5MWI5YjM0ZjY2OGUyMDUyNDZjOWRhODc3Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yYzBkYjRjZGIxNDc0Mzg1OGMyOGZhMjEwMTllYWUyOC5iaW5kUG9wdXAocG9wdXBfZjhmNjRlYWIyYzU1NGNhYjg1NTgyMGVlYzQ4NDY5NTgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDgwMWNjZjAxODM1NGU1Y2FkYWJkYjE4MWIyMDc5MzcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42ODY0MTIyOTk5OTk5OSwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wODEwNThiNzRlN2Q0YzFlOWNlYWY0ZjZkM2ZjMzgwOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82MWEyMGM4MDE1MjI0YWY3OWFkMzg2YjAyNzg5MzdjNiA9ICQoJzxkaXYgaWQ9Imh0bWxfNjFhMjBjODAxNTIyNGFmNzlhZDM4NmIwMjc4OTM3YzYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRlZXIgUGFyayxGb3Jlc3QgSGlsbCBTRSxSYXRobmVsbHksU291dGggSGlsbCxTdW1tZXJoaWxsIFdlc3QgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wODEwNThiNzRlN2Q0YzFlOWNlYWY0ZjZkM2ZjMzgwOC5zZXRDb250ZW50KGh0bWxfNjFhMjBjODAxNTIyNGFmNzlhZDM4NmIwMjc4OTM3YzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDgwMWNjZjAxODM1NGU1Y2FkYWJkYjE4MWIyMDc5MzcuYmluZFBvcHVwKHBvcHVwXzA4MTA1OGI3NGU3ZDRjMWU5Y2VhZjRmNmQzZmMzODA4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q5NDI2NThmZDgwNTQ1ZmRiZmI4NDM5ZWEwZWFmZTMyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjc5NTYyNiwtNzkuMzc3NTI5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZWI2NTI0NjQxNGZjNDk0NThhOWQxNmUwYTc0NDE4NGIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2E2MTRhMzRiZjY1NDc0ZWFlZjE4OGEzYTk1NTVlMGUgPSAkKCc8ZGl2IGlkPSJodG1sXzNhNjE0YTM0YmY2NTQ3NGVhZWYxODhhM2E5NTU1ZTBlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlZGFsZSBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ViNjUyNDY0MTRmYzQ5NDU4YTlkMTZlMGE3NDQxODRiLnNldENvbnRlbnQoaHRtbF8zYTYxNGEzNGJmNjU0NzRlYWVmMTg4YTNhOTU1NWUwZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kOTQyNjU4ZmQ4MDU0NWZkYmZiODQzOWVhMGVhZmUzMi5iaW5kUG9wdXAocG9wdXBfZWI2NTI0NjQxNGZjNDk0NThhOWQxNmUwYTc0NDE4NGIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTBhZDRjY2ZhNjVjNDFiNmEyY2NhMTkyYWYwYTYwMDkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Njc5NjcsLTc5LjM2NzY3NTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGY3Mjc1Y2E0ZTM4NGU5NWExNTExMmY1YTkxMTNiNDEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTVjYzk2MDA1OWZiNGFjM2FlYWU0NjZiZjhkYmJkNTggPSAkKCc8ZGl2IGlkPSJodG1sXzk1Y2M5NjAwNTlmYjRhYzNhZWFlNDY2YmY4ZGJiZDU4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYWJiYWdldG93bixTdC4gSmFtZXMgVG93biBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhmNzI3NWNhNGUzODRlOTVhMTUxMTJmNWE5MTEzYjQxLnNldENvbnRlbnQoaHRtbF85NWNjOTYwMDU5ZmI0YWMzYWVhZTQ2NmJmOGRiYmQ1OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xMGFkNGNjZmE2NWM0MWI2YTJjY2ExOTJhZjBhNjAwOS5iaW5kUG9wdXAocG9wdXBfOGY3Mjc1Y2E0ZTM4NGU5NWExNTExMmY1YTkxMTNiNDEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjYwYTRmZmQ4Y2Q5NDJjYTljODNiY2Y5ZjE5MzBjZjEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjU4NTk5LC03OS4zODMxNTk5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jOTkyMDUwOWE0ZTA0MjJmOTU4MDc0MDFkZmI2NjFmYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mYzI2ZTgyMWMzZDk0MGU0OGQzNGMwNjZhNjI1ZjI4MiA9ICQoJzxkaXYgaWQ9Imh0bWxfZmMyNmU4MjFjM2Q5NDBlNDhkMzRjMDY2YTYyNWYyODIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNodXJjaCBhbmQgV2VsbGVzbGV5IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzk5MjA1MDlhNGUwNDIyZjk1ODA3NDAxZGZiNjYxZmMuc2V0Q29udGVudChodG1sX2ZjMjZlODIxYzNkOTQwZTQ4ZDM0YzA2NmE2MjVmMjgyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzY2MGE0ZmZkOGNkOTQyY2E5YzgzYmNmOWYxOTMwY2YxLmJpbmRQb3B1cChwb3B1cF9jOTkyMDUwOWE0ZTA0MjJmOTU4MDc0MDFkZmI2NjFmYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80ZDZiOTk0YjM1ZTE0YWMzYTkxYmIxNmZhNTlkOGUxMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1NDI1OTksLTc5LjM2MDYzNTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGI0MjI1MWE1YmMwNDk0N2JlYmE5ZGJjYTkxMTY4MzkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDFlMGI5MGU0MGMwNGMyMDliYjk4OTY2ZDRmZmUzNDAgPSAkKCc8ZGl2IGlkPSJodG1sX2QxZTBiOTBlNDBjMDRjMjA5YmI5ODk2NmQ0ZmZlMzQwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQsUmVnZW50IFBhcmsgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kYjQyMjUxYTViYzA0OTQ3YmViYTlkYmNhOTExNjgzOS5zZXRDb250ZW50KGh0bWxfZDFlMGI5MGU0MGMwNGMyMDliYjk4OTY2ZDRmZmUzNDApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNGQ2Yjk5NGIzNWUxNGFjM2E5MWJiMTZmYTU5ZDhlMTAuYmluZFBvcHVwKHBvcHVwX2RiNDIyNTFhNWJjMDQ5NDdiZWJhOWRiY2E5MTE2ODM5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzUwODM2YTdiNTQ2ZDQ0MzE5ODk5Y2Q1NDlhYTBhMWQ1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjU3MTYxOCwtNzkuMzc4OTM3MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjRlM2Q4ODhmN2Q5NDFiZDgxZDg3YmY1ZTM1MTU1ZWYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTBiYTU1ZjU2MGJhNGE5NDhmNjcyZWU1ZTI0NDEzZGUgPSAkKCc8ZGl2IGlkPSJodG1sXzkwYmE1NWY1NjBiYTRhOTQ4ZjY3MmVlNWUyNDQxM2RlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SeWVyc29uLEdhcmRlbiBEaXN0cmljdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y0ZTNkODg4ZjdkOTQxYmQ4MWQ4N2JmNWUzNTE1NWVmLnNldENvbnRlbnQoaHRtbF85MGJhNTVmNTYwYmE0YTk0OGY2NzJlZTVlMjQ0MTNkZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81MDgzNmE3YjU0NmQ0NDMxOTg5OWNkNTQ5YWEwYTFkNS5iaW5kUG9wdXAocG9wdXBfZjRlM2Q4ODhmN2Q5NDFiZDgxZDg3YmY1ZTM1MTU1ZWYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTc5NjUwNGMzOThjNGM1OGI3NjNkYTgwNWQxYzRmNTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTE0OTM5LC03OS4zNzU0MTc5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2VjNjgxNzM5NTIyOTRmNzQ5OTUwY2EwODJjZTYwZGQ0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU0MWE2MjBjNzdkODRiNmE5OTBjYmQ0MDMwYmRhZmY3ID0gJCgnPGRpdiBpZD0iaHRtbF81NDFhNjIwYzc3ZDg0YjZhOTkwY2JkNDAzMGJkYWZmNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3QuIEphbWVzIFRvd24gQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lYzY4MTczOTUyMjk0Zjc0OTk1MGNhMDgyY2U2MGRkNC5zZXRDb250ZW50KGh0bWxfNTQxYTYyMGM3N2Q4NGI2YTk5MGNiZDQwMzBiZGFmZjcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTc5NjUwNGMzOThjNGM1OGI3NjNkYTgwNWQxYzRmNTAuYmluZFBvcHVwKHBvcHVwX2VjNjgxNzM5NTIyOTRmNzQ5OTUwY2EwODJjZTYwZGQ0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzllZDVjZTM2YjA5MjQ4NWNiNzlhOGU5YTllY2Q2ZmUzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ0NzcwNzk5OTk5OTk2LC03OS4zNzMzMDY0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzQ4ZWFhMzNiZjQzMzQ5NjRiZjc4MjUyZmE1MTdjZDQ5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzExNzJiNGExYTgwZDQxYjU5NmYwNGZhNmU5ODUxYTVkID0gJCgnPGRpdiBpZD0iaHRtbF8xMTcyYjRhMWE4MGQ0MWI1OTZmMDRmYTZlOTg1MWE1ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVyY3p5IFBhcmsgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80OGVhYTMzYmY0MzM0OTY0YmY3ODI1MmZhNTE3Y2Q0OS5zZXRDb250ZW50KGh0bWxfMTE3MmI0YTFhODBkNDFiNTk2ZjA0ZmE2ZTk4NTFhNWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWVkNWNlMzZiMDkyNDg1Y2I3OWE4ZTlhOWVjZDZmZTMuYmluZFBvcHVwKHBvcHVwXzQ4ZWFhMzNiZjQzMzQ5NjRiZjc4MjUyZmE1MTdjZDQ5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2JkOWViZmQ2MTczNjQzOTJiOGFiNWVjOGJiNzRiZTk1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjU3OTUyNCwtNzkuMzg3MzgyNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80YjIxZTEzOGQxODk0NDc0OTE2NmZjZTIwZjJkMjdmMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jZmI1Y2Q0YjE4YTU0Yjc1YmUxMjU1ZjA1MTdmMzNkOSA9ICQoJzxkaXYgaWQ9Imh0bWxfY2ZiNWNkNGIxOGE1NGI3NWJlMTI1NWYwNTE3ZjMzZDkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNlbnRyYWwgQmF5IFN0cmVldCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRiMjFlMTM4ZDE4OTQ0NzQ5MTY2ZmNlMjBmMmQyN2YxLnNldENvbnRlbnQoaHRtbF9jZmI1Y2Q0YjE4YTU0Yjc1YmUxMjU1ZjA1MTdmMzNkOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iZDllYmZkNjE3MzY0MzkyYjhhYjVlYzhiYjc0YmU5NS5iaW5kUG9wdXAocG9wdXBfNGIyMWUxMzhkMTg5NDQ3NDkxNjZmY2UyMGYyZDI3ZjEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjA2YTU4Y2M1MDhiNDY1OTk5YTA2MjNhNWM4YmY5MjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTA1NzEyMDAwMDAwMSwtNzkuMzg0NTY3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81MWMxYmVkMjJiNWY0NDA2YmQ1OWFjNzY3ZjQ5OWRlNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yYjQ0NmRlNGE1YzA0MjVlOTc3Njk3MjM5MzYzMzExMSA9ICQoJzxkaXYgaWQ9Imh0bWxfMmI0NDZkZTRhNWMwNDI1ZTk3NzY5NzIzOTM2MzMxMTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZWxhaWRlLEtpbmcsUmljaG1vbmQgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81MWMxYmVkMjJiNWY0NDA2YmQ1OWFjNzY3ZjQ5OWRlNC5zZXRDb250ZW50KGh0bWxfMmI0NDZkZTRhNWMwNDI1ZTk3NzY5NzIzOTM2MzMxMTEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjA2YTU4Y2M1MDhiNDY1OTk5YTA2MjNhNWM4YmY5MjcuYmluZFBvcHVwKHBvcHVwXzUxYzFiZWQyMmI1ZjQ0MDZiZDU5YWM3NjdmNDk5ZGU0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzU5MjNjZjlkNmZjNzRhOTFhODhiNTg2Nzc1ZGQwZmIxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQwODE1NywtNzkuMzgxNzUyMjk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjI5NjMyOTZmNDBkNDI5ZmI4MWI5YTBiNzYyNmE2OWYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYWIwNTQ3OWU3ZWYzNDc4Njg5ZDkyODY5MGQ5OTQ3ZTAgPSAkKCc8ZGl2IGlkPSJodG1sX2FiMDU0NzllN2VmMzQ3ODY4OWQ5Mjg2OTBkOTk0N2UwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQgRWFzdCxUb3JvbnRvIElzbGFuZHMsVW5pb24gU3RhdGlvbiBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzYyOTYzMjk2ZjQwZDQyOWZiODFiOWEwYjc2MjZhNjlmLnNldENvbnRlbnQoaHRtbF9hYjA1NDc5ZTdlZjM0Nzg2ODlkOTI4NjkwZDk5NDdlMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81OTIzY2Y5ZDZmYzc0YTkxYTg4YjU4Njc3NWRkMGZiMS5iaW5kUG9wdXAocG9wdXBfNjI5NjMyOTZmNDBkNDI5ZmI4MWI5YTBiNzYyNmE2OWYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjBhMDFlOTcxZjQ1NGUzNmIyMjQ1ZGUzMTJlMTgxNjMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDcxNzY4LC03OS4zODE1NzY0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84NGRiNDY0ZTkwZDY0MGY1OWE3ZmZkYmM4N2IxMTg5MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81YzZiODNjODk2MTk0YTIyOTUxYzZjOGY1ODg3MjJiNiA9ICQoJzxkaXYgaWQ9Imh0bWxfNWM2YjgzYzg5NjE5NGEyMjk1MWM2YzhmNTg4NzIyYjYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRlc2lnbiBFeGNoYW5nZSxUb3JvbnRvIERvbWluaW9uIENlbnRyZSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg0ZGI0NjRlOTBkNjQwZjU5YTdmZmRiYzg3YjExODkwLnNldENvbnRlbnQoaHRtbF81YzZiODNjODk2MTk0YTIyOTUxYzZjOGY1ODg3MjJiNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iMGEwMWU5NzFmNDU0ZTM2YjIyNDVkZTMxMmUxODE2My5iaW5kUG9wdXAocG9wdXBfODRkYjQ2NGU5MGQ2NDBmNTlhN2ZmZGJjODdiMTE4OTApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmUwMWQzYjVlMmZkNGNiOGJiNTA5Y2YwYThmNDNjNmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDgxOTg1LC03OS4zNzk4MTY5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zZGM1ZjEzODIzMDc0YzY3OWIzNzM5NzliODgwMWY5NSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wZDljZDY5YzA3ODU0MDE3ODYwY2ZhNTYwYmFmYWYzZiA9ICQoJzxkaXYgaWQ9Imh0bWxfMGQ5Y2Q2OWMwNzg1NDAxNzg2MGNmYTU2MGJhZmFmM2YiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvbW1lcmNlIENvdXJ0LFZpY3RvcmlhIEhvdGVsIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfM2RjNWYxMzgyMzA3NGM2NzliMzczOTc5Yjg4MDFmOTUuc2V0Q29udGVudChodG1sXzBkOWNkNjljMDc4NTQwMTc4NjBjZmE1NjBiYWZhZjNmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2JlMDFkM2I1ZTJmZDRjYjhiYjUwOWNmMGE4ZjQzYzZiLmJpbmRQb3B1cChwb3B1cF8zZGM1ZjEzODIzMDc0YzY3OWIzNzM5NzliODgwMWY5NSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83Njc3Y2I1ODRlODk0NmFmYmM5MWQ0YTJiM2FiOWQ0YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjczMzI4MjUsLTc5LjQxOTc0OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGI2N2VhNTUxOWZmNDRiMDhmOGZkNjBmZmE1YmZkMGQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjZiODYxZDMzOGFiNDVhMmI0ZGZlZThmMTQxNTg5MzYgPSAkKCc8ZGl2IGlkPSJodG1sX2Y2Yjg2MWQzMzhhYjQ1YTJiNGRmZWU4ZjE0MTU4OTM2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWRmb3JkIFBhcmssTGF3cmVuY2UgTWFub3IgRWFzdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhiNjdlYTU1MTlmZjQ0YjA4ZjhmZDYwZmZhNWJmZDBkLnNldENvbnRlbnQoaHRtbF9mNmI4NjFkMzM4YWI0NWEyYjRkZmVlOGYxNDE1ODkzNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83Njc3Y2I1ODRlODk0NmFmYmM5MWQ0YTJiM2FiOWQ0Yy5iaW5kUG9wdXAocG9wdXBfOGI2N2VhNTUxOWZmNDRiMDhmOGZkNjBmZmE1YmZkMGQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmQ2MWZmYjRkZGNjNDhjNWFmMTllMjdkMWZkM2JlOTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MTE2OTQ4LC03OS40MTY5MzU1OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80NWRkMjlmNzBiMmE0MjA2YTlhMzEwNmI0NTkxZjQ2ZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84YzJjNjc0YWU5YTA0M2MwOGZmNmE4ZDU4M2MwMjQ4MyA9ICQoJzxkaXYgaWQ9Imh0bWxfOGMyYzY3NGFlOWEwNDNjMDhmZjZhOGQ1ODNjMDI0ODMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJvc2VsYXduIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDVkZDI5ZjcwYjJhNDIwNmE5YTMxMDZiNDU5MWY0NmUuc2V0Q29udGVudChodG1sXzhjMmM2NzRhZTlhMDQzYzA4ZmY2YThkNTgzYzAyNDgzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2JkNjFmZmI0ZGRjYzQ4YzVhZjE5ZTI3ZDFmZDNiZTk4LmJpbmRQb3B1cChwb3B1cF80NWRkMjlmNzBiMmE0MjA2YTlhMzEwNmI0NTkxZjQ2ZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kYWNlY2IzYTc4ZmQ0MGQzOGU3OTU3NGMzZDcxYmE5ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5Njk0NzYsLTc5LjQxMTMwNzIwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U2MjY4ZTI1NDdjODQxOGFiNDIzYTU0YmI1MWE2OWZjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzg0NGZiNjFlMGUwNTQ2YzA4MTgyMDgxMjIzYjRkNTNkID0gJCgnPGRpdiBpZD0iaHRtbF84NDRmYjYxZTBlMDU0NmMwODE4MjA4MTIyM2I0ZDUzZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rm9yZXN0IEhpbGwgTm9ydGgsRm9yZXN0IEhpbGwgV2VzdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2U2MjY4ZTI1NDdjODQxOGFiNDIzYTU0YmI1MWE2OWZjLnNldENvbnRlbnQoaHRtbF84NDRmYjYxZTBlMDU0NmMwODE4MjA4MTIyM2I0ZDUzZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kYWNlY2IzYTc4ZmQ0MGQzOGU3OTU3NGMzZDcxYmE5ZS5iaW5kUG9wdXAocG9wdXBfZTYyNjhlMjU0N2M4NDE4YWI0MjNhNTRiYjUxYTY5ZmMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzQ3M2FmNmQ3YjlkNGNiOTkxOWJlYzRiZmE1N2I5ZjQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NzI3MDk3LC03OS40MDU2Nzg0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85NTg2MzZlODdiNDE0YWRiODJkNjM0YTgzZDU0YjlmMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83OGQ4ZjA0MWJjOWQ0MjI2YTlmMWYxMWZiZDRjYTQzOSA9ICQoJzxkaXYgaWQ9Imh0bWxfNzhkOGYwNDFiYzlkNDIyNmE5ZjFmMTFmYmQ0Y2E0MzkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRoZSBBbm5leCxOb3J0aCBNaWR0b3duLFlvcmt2aWxsZSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzk1ODYzNmU4N2I0MTRhZGI4MmQ2MzRhODNkNTRiOWYyLnNldENvbnRlbnQoaHRtbF83OGQ4ZjA0MWJjOWQ0MjI2YTlmMWYxMWZiZDRjYTQzOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zNDczYWY2ZDdiOWQ0Y2I5OTE5YmVjNGJmYTU3YjlmNC5iaW5kUG9wdXAocG9wdXBfOTU4NjM2ZTg3YjQxNGFkYjgyZDYzNGE4M2Q1NGI5ZjIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmMyOThjZDA1OTYzNDIyMWFmNDcxNzc1ZGIxZDBkYTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjI2OTU2LC03OS40MDAwNDkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzU4YmM2OWQ3M2E3MjQ1MDI4M2IxYTViNGE0ZWYyOWUwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzM5NjkyOGRmZjRjZTQ0NTg4ZDdmNTRkZTAyZWMxMDY2ID0gJCgnPGRpdiBpZD0iaHRtbF8zOTY5MjhkZmY0Y2U0NDU4OGQ3ZjU0ZGUwMmVjMTA2NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGFyYm9yZCxVbml2ZXJzaXR5IG9mIFRvcm9udG8gQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81OGJjNjlkNzNhNzI0NTAyODNiMWE1YjRhNGVmMjllMC5zZXRDb250ZW50KGh0bWxfMzk2OTI4ZGZmNGNlNDQ1ODhkN2Y1NGRlMDJlYzEwNjYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZmMyOThjZDA1OTYzNDIyMWFmNDcxNzc1ZGIxZDBkYTMuYmluZFBvcHVwKHBvcHVwXzU4YmM2OWQ3M2E3MjQ1MDI4M2IxYTViNGE0ZWYyOWUwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzExZGI2ZmU4NzczYTQ4MzU5M2IwMGZhMjY2ZmU1MjkyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUzMjA1NywtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80NmZiM2I1MDBmOGY0MWRiYjQzM2RjYzE3OGIzMDAwMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85NDVlYjE2YjE3OGQ0ZjRlOTJiOTE1ZWMwYjBhODk2MSA9ICQoJzxkaXYgaWQ9Imh0bWxfOTQ1ZWIxNmIxNzhkNGY0ZTkyYjkxNWVjMGIwYTg5NjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNoaW5hdG93bixHcmFuZ2UgUGFyayxLZW5zaW5ndG9uIE1hcmtldCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQ2ZmIzYjUwMGY4ZjQxZGJiNDMzZGNjMTc4YjMwMDAwLnNldENvbnRlbnQoaHRtbF85NDVlYjE2YjE3OGQ0ZjRlOTJiOTE1ZWMwYjBhODk2MSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xMWRiNmZlODc3M2E0ODM1OTNiMDBmYTI2NmZlNTI5Mi5iaW5kUG9wdXAocG9wdXBfNDZmYjNiNTAwZjhmNDFkYmI0MzNkY2MxNzhiMzAwMDApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmIwNWRmZGI4MzZjNDlkN2IwMjBkZmRiMmQyNDY1MzIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Mjg5NDY3LC03OS4zOTQ0MTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzdkMzkxNzE1ZjI1YTQ1YTVhYjYzOWFiZTcyN2U3ZjNmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzgzYzFmNmQzNGU5MzQzZjA4ZjYwZWE3MjRmMzM1NGY5ID0gJCgnPGRpdiBpZD0iaHRtbF84M2MxZjZkMzRlOTM0M2YwOGY2MGVhNzI0ZjMzNTRmOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q04gVG93ZXIsQmF0aHVyc3QgUXVheSxJc2xhbmQgYWlycG9ydCxIYXJib3VyZnJvbnQgV2VzdCxLaW5nIGFuZCBTcGFkaW5hLFJhaWx3YXkgTGFuZHMsU291dGggTmlhZ2FyYSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdkMzkxNzE1ZjI1YTQ1YTVhYjYzOWFiZTcyN2U3ZjNmLnNldENvbnRlbnQoaHRtbF84M2MxZjZkMzRlOTM0M2YwOGY2MGVhNzI0ZjMzNTRmOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iYjA1ZGZkYjgzNmM0OWQ3YjAyMGRmZGIyZDI0NjUzMi5iaW5kUG9wdXAocG9wdXBfN2QzOTE3MTVmMjVhNDVhNWFiNjM5YWJlNzI3ZTdmM2YpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjdlNGE2YjdiOWI2NDhiZTg4NzUxMTMxMzMzMmM5NmQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDY0MzUyLC03OS4zNzQ4NDU5OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85YWVjNzI5MTNkMDI0NGRjYjQxNWVjZDUxOTdiM2JiZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yZDY2Y2U0ZGRhYjQ0NWQwODQzNzRmZmIwNjM2MTM0NSA9ICQoJzxkaXYgaWQ9Imh0bWxfMmQ2NmNlNGRkYWI0NDVkMDg0Mzc0ZmZiMDYzNjEzNDUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlN0biBBIFBPIEJveGVzIDI1IFRoZSBFc3BsYW5hZGUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85YWVjNzI5MTNkMDI0NGRjYjQxNWVjZDUxOTdiM2JiZS5zZXRDb250ZW50KGh0bWxfMmQ2NmNlNGRkYWI0NDVkMDg0Mzc0ZmZiMDYzNjEzNDUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjdlNGE2YjdiOWI2NDhiZTg4NzUxMTMxMzMzMmM5NmQuYmluZFBvcHVwKHBvcHVwXzlhZWM3MjkxM2QwMjQ0ZGNiNDE1ZWNkNTE5N2IzYmJlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzEzYTQ4MjFjMmI2ZDRlMDc4ZTc0NTY1OGIyMTk5Mjc5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ4NDI5MiwtNzkuMzgyMjgwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iOGFmMjhmOTkzZDk0ZTUxYjE1YjY4ZWEzMTZhMWZkYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84ODM5Nzc1YjlmMDA0YjI3OWI2ZDZkZmQ4NTQ5MWE3MyA9ICQoJzxkaXYgaWQ9Imh0bWxfODgzOTc3NWI5ZjAwNGIyNzliNmQ2ZGZkODU0OTFhNzMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZpcnN0IENhbmFkaWFuIFBsYWNlLFVuZGVyZ3JvdW5kIGNpdHkgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iOGFmMjhmOTkzZDk0ZTUxYjE1YjY4ZWEzMTZhMWZkYS5zZXRDb250ZW50KGh0bWxfODgzOTc3NWI5ZjAwNGIyNzliNmQ2ZGZkODU0OTFhNzMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTNhNDgyMWMyYjZkNGUwNzhlNzQ1NjU4YjIxOTkyNzkuYmluZFBvcHVwKHBvcHVwX2I4YWYyOGY5OTNkOTRlNTFiMTViNjhlYTMxNmExZmRhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U0MmFhYTY3NjdlZjRhNDI5NDI5ZDU5Y2MzZTFhOWRiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE4NTE3OTk5OTk5OTk2LC03OS40NjQ3NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yZTc4ZjMxZDBjYzk0YWYyYWU4ZTYwMWYzMWExNWNlNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wOTBhNDFmMDNhYmY0ZWIxOGE5Yzg2NDJlZGEwNGZmOSA9ICQoJzxkaXYgaWQ9Imh0bWxfMDkwYTQxZjAzYWJmNGViMThhOWM4NjQyZWRhMDRmZjkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIEhlaWdodHMsTGF3cmVuY2UgTWFub3IgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yZTc4ZjMxZDBjYzk0YWYyYWU4ZTYwMWYzMWExNWNlNC5zZXRDb250ZW50KGh0bWxfMDkwYTQxZjAzYWJmNGViMThhOWM4NjQyZWRhMDRmZjkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTQyYWFhNjc2N2VmNGE0Mjk0MjlkNTljYzNlMWE5ZGIuYmluZFBvcHVwKHBvcHVwXzJlNzhmMzFkMGNjOTRhZjJhZThlNjAxZjMxYTE1Y2U0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY0NWQ0MGU0YjNkODRkNDViYzY1YWYzYmJkM2I0NTAzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA5NTc3LC03OS40NDUwNzI1OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yMzljZDJjN2MzNmU0NWMwOGM2YTI5ZTQwOTI1M2E0OCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kODUzYzZiYWQzNzU0NjQxYmFlOGRkZTQ1MGE1NmFiYyA9ICQoJzxkaXYgaWQ9Imh0bWxfZDg1M2M2YmFkMzc1NDY0MWJhZThkZGU0NTBhNTZhYmMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdsZW5jYWlybiBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzIzOWNkMmM3YzM2ZTQ1YzA4YzZhMjllNDA5MjUzYTQ4LnNldENvbnRlbnQoaHRtbF9kODUzYzZiYWQzNzU0NjQxYmFlOGRkZTQ1MGE1NmFiYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82NDVkNDBlNGIzZDg0ZDQ1YmM2NWFmM2JiZDNiNDUwMy5iaW5kUG9wdXAocG9wdXBfMjM5Y2QyYzdjMzZlNDVjMDhjNmEyOWU0MDkyNTNhNDgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTkyYzc0MDM1MzRlNGQzMjg4NzA4ZmQyNDJjNjQ0MGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTM3ODEzLC03OS40MjgxOTE0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lOWU0M2Y0OTA1NDg0ODVlODc2MjExYzNmZjdkMzM2ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hZTc5YzYzNWY5MjY0ODk0YTAwYWI1MDY5ODk4ZTNmZSA9ICQoJzxkaXYgaWQ9Imh0bWxfYWU3OWM2MzVmOTI2NDg5NGEwMGFiNTA2OTg5OGUzZmUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWV3b29kLUNlZGFydmFsZSBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2U5ZTQzZjQ5MDU0ODQ4NWU4NzYyMTFjM2ZmN2QzMzZkLnNldENvbnRlbnQoaHRtbF9hZTc5YzYzNWY5MjY0ODk0YTAwYWI1MDY5ODk4ZTNmZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lOTJjNzQwMzUzNGU0ZDMyODg3MDhmZDI0MmM2NDQwZi5iaW5kUG9wdXAocG9wdXBfZTllNDNmNDkwNTQ4NDg1ZTg3NjIxMWMzZmY3ZDMzNmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmQ4ZDhhOGY2NzRiNGY0MGJlYWRjNGNlMDQ3ZTc5MTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42ODkwMjU2LC03OS40NTM1MTJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDkxZjY4Mzk3MGJkNDA5NWE5Y2M3OGIxNjEwYjNiNTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGY5M2ZhYTJmMTYyNDM2ZGIwNzE0YWRkMGFhZTI1NzggPSAkKCc8ZGl2IGlkPSJodG1sXzhmOTNmYWEyZjE2MjQzNmRiMDcxNGFkZDBhYWUyNTc4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYWxlZG9uaWEtRmFpcmJhbmtzIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDkxZjY4Mzk3MGJkNDA5NWE5Y2M3OGIxNjEwYjNiNTcuc2V0Q29udGVudChodG1sXzhmOTNmYWEyZjE2MjQzNmRiMDcxNGFkZDBhYWUyNTc4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJkOGQ4YThmNjc0YjRmNDBiZWFkYzRjZTA0N2U3OTEwLmJpbmRQb3B1cChwb3B1cF9kOTFmNjgzOTcwYmQ0MDk1YTljYzc4YjE2MTBiM2I1Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zOGFiNDZlMGZmZTA0MDA0OTg2MDk2OWIyN2NhMzNlMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2OTU0MiwtNzkuNDIyNTYzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80NTNiODM0MTVkZmQ0ODdhYjE5NzNkODg1ZDBhMGVlZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hYmRmYjlmYWJhOTg0MjQyYjk1NzI4NDYyNDhiYzViMSA9ICQoJzxkaXYgaWQ9Imh0bWxfYWJkZmI5ZmFiYTk4NDI0MmI5NTcyODQ2MjQ4YmM1YjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNocmlzdGllIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDUzYjgzNDE1ZGZkNDg3YWIxOTczZDg4NWQwYTBlZWUuc2V0Q29udGVudChodG1sX2FiZGZiOWZhYmE5ODQyNDJiOTU3Mjg0NjI0OGJjNWIxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzM4YWI0NmUwZmZlMDQwMDQ5ODYwOTY5YjI3Y2EzM2UwLmJpbmRQb3B1cChwb3B1cF80NTNiODM0MTVkZmQ0ODdhYjE5NzNkODg1ZDBhMGVlZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNzg0NjZkNDI3OGQ0NjcwODU5NDE3OWZmNWYzNWMwOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2OTAwNTEwMDAwMDAxLC03OS40NDIyNTkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzBlZDIwZmEzOWQ2NTQzM2I5NmYzYzJiZmMzYThmYzYxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY0YTM4ZGE5YWQyZTRmNWJhNWZkNTM3ZWU4NGMwYTVmID0gJCgnPGRpdiBpZD0iaHRtbF82NGEzOGRhOWFkMmU0ZjViYTVmZDUzN2VlODRjMGE1ZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG92ZXJjb3VydCBWaWxsYWdlLER1ZmZlcmluIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMGVkMjBmYTM5ZDY1NDMzYjk2ZjNjMmJmYzNhOGZjNjEuc2V0Q29udGVudChodG1sXzY0YTM4ZGE5YWQyZTRmNWJhNWZkNTM3ZWU4NGMwYTVmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2U3ODQ2NmQ0Mjc4ZDQ2NzA4NTk0MTc5ZmY1ZjM1YzA4LmJpbmRQb3B1cChwb3B1cF8wZWQyMGZhMzlkNjU0MzNiOTZmM2MyYmZjM2E4ZmM2MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jMzk4ZDc2MmE3MGE0NDJjODZkY2QxMzA0MTY1MzRmMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY0NzkyNjcwMDAwMDAwNiwtNzkuNDE5NzQ5N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83Y2YzODY2NmU4YzI0NjMyYTYyMjc0ODIxNzRlNTlhYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xY2FkMzM4ZGI2YjM0YzJhYjU4YzlhMGRmOGFhYzM1MSA9ICQoJzxkaXYgaWQ9Imh0bWxfMWNhZDMzOGRiNmIzNGMyYWI1OGM5YTBkZjhhYWMzNTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxpdHRsZSBQb3J0dWdhbCxUcmluaXR5IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfN2NmMzg2NjZlOGMyNDYzMmE2MjI3NDgyMTc0ZTU5YWMuc2V0Q29udGVudChodG1sXzFjYWQzMzhkYjZiMzRjMmFiNThjOWEwZGY4YWFjMzUxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2MzOThkNzYyYTcwYTQ0MmM4NmRjZDEzMDQxNjUzNGYwLmJpbmRQb3B1cChwb3B1cF83Y2YzODY2NmU4YzI0NjMyYTYyMjc0ODIxNzRlNTlhYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mOWE3MmNhZTAzZjU0ZGE4YTMwZTY3ZDk1NGFhYWFlYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYzNjg0NzIsLTc5LjQyODE5MTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzhhZTM5NTJjNzFiNjRjYjZhYmRhMDI1ZjAxMjYwOTJmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY0ZTg2NzU2Y2M5NzQ3YzM5MWVmNzcxMDg3YjljMzk3ID0gJCgnPGRpdiBpZD0iaHRtbF82NGU4Njc1NmNjOTc0N2MzOTFlZjc3MTA4N2I5YzM5NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnJvY2t0b24sRXhoaWJpdGlvbiBQbGFjZSxQYXJrZGFsZSBWaWxsYWdlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGFlMzk1MmM3MWI2NGNiNmFiZGEwMjVmMDEyNjA5MmYuc2V0Q29udGVudChodG1sXzY0ZTg2NzU2Y2M5NzQ3YzM5MWVmNzcxMDg3YjljMzk3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y5YTcyY2FlMDNmNTRkYThhMzBlNjdkOTU0YWFhYWVjLmJpbmRQb3B1cChwb3B1cF84YWUzOTUyYzcxYjY0Y2I2YWJkYTAyNWYwMTI2MDkyZik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81NWQ0MjRlOTE1OTY0NGZhYjMzNWFlYzMwODE0YWI3ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcxMzc1NjIwMDAwMDAwNiwtNzkuNDkwMDczOF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mOWUwMTlkZGY1Y2Q0M2UzOWU2N2RlMzZhOGMxZjI2NyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MDk2NTY3YzRjYmI0YzVhOTVlNjIwMWUzMmQyMWYzNCA9ICQoJzxkaXYgaWQ9Imh0bWxfNTA5NjU2N2M0Y2JiNGM1YTk1ZTYyMDFlMzJkMjFmMzQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvd25zdmlldyxOb3J0aCBQYXJrLFVwd29vZCBQYXJrIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjllMDE5ZGRmNWNkNDNlMzllNjdkZTM2YThjMWYyNjcuc2V0Q29udGVudChodG1sXzUwOTY1NjdjNGNiYjRjNWE5NWU2MjAxZTMyZDIxZjM0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzU1ZDQyNGU5MTU5NjQ0ZmFiMzM1YWVjMzA4MTRhYjdlLmJpbmRQb3B1cChwb3B1cF9mOWUwMTlkZGY1Y2Q0M2UzOWU2N2RlMzZhOGMxZjI2Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iNDc5MGZmMWRjMTI0OTdhODgwYjkyODRkMDJmNjRhNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5MTExNTgsLTc5LjQ3NjAxMzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2EyNDdjMTU1MDkxYzRmMThiMjkxNmJmMGU0ZWJiNDEzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRmODlkZGRlZTZmYTQ2ZmY4NWJhNzVmNGFmOTRkODNkID0gJCgnPGRpdiBpZD0iaHRtbF80Zjg5ZGRkZWU2ZmE0NmZmODViYTc1ZjRhZjk0ZDgzZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RGVsIFJheSxLZWVsZXNkYWxlLE1vdW50IERlbm5pcyxTaWx2ZXJ0aG9ybiBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2EyNDdjMTU1MDkxYzRmMThiMjkxNmJmMGU0ZWJiNDEzLnNldENvbnRlbnQoaHRtbF80Zjg5ZGRkZWU2ZmE0NmZmODViYTc1ZjRhZjk0ZDgzZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iNDc5MGZmMWRjMTI0OTdhODgwYjkyODRkMDJmNjRhNS5iaW5kUG9wdXAocG9wdXBfYTI0N2MxNTUwOTFjNGYxOGIyOTE2YmYwZTRlYmI0MTMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzBkYzE0NzU5NjZhNDRjZThhYTQ3MjMwYWZjZDM5OTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NzMxODUyOTk5OTk5OSwtNzkuNDg3MjYxOTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDExOWNkZTVlOWYwNDE4NjgyMGFlMzllYTY0ODg4YWIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOWI2N2RiMzYyY2U1NDUzMzkzYTI3NmQzZTcxYjI0NTEgPSAkKCc8ZGl2IGlkPSJodG1sXzliNjdkYjM2MmNlNTQ1MzM5M2EyNzZkM2U3MWIyNDUxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgSnVuY3Rpb24gTm9ydGgsUnVubnltZWRlIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDExOWNkZTVlOWYwNDE4NjgyMGFlMzllYTY0ODg4YWIuc2V0Q29udGVudChodG1sXzliNjdkYjM2MmNlNTQ1MzM5M2EyNzZkM2U3MWIyNDUxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzcwZGMxNDc1OTY2YTQ0Y2U4YWE0NzIzMGFmY2QzOTkzLmJpbmRQb3B1cChwb3B1cF8wMTE5Y2RlNWU5ZjA0MTg2ODIwYWUzOWVhNjQ4ODhhYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zZDdjMDU0ZjVmMmY0MTVlOTM3ZjQzZDhmNGE5NDcwNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MTYwODMsLTc5LjQ2NDc2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzgzMTcxOTIwNzZlMDQzMjc4Y2JjYzk4MjZjOTdhNGQwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2QyYzdkZWFlYjU2NTQ3N2M4OWNkZGI2YTcwOGNkMmU4ID0gJCgnPGRpdiBpZD0iaHRtbF9kMmM3ZGVhZWI1NjU0NzdjODljZGRiNmE3MDhjZDJlOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaCBQYXJrLFRoZSBKdW5jdGlvbiBTb3V0aCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzgzMTcxOTIwNzZlMDQzMjc4Y2JjYzk4MjZjOTdhNGQwLnNldENvbnRlbnQoaHRtbF9kMmM3ZGVhZWI1NjU0NzdjODljZGRiNmE3MDhjZDJlOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zZDdjMDU0ZjVmMmY0MTVlOTM3ZjQzZDhmNGE5NDcwNi5iaW5kUG9wdXAocG9wdXBfODMxNzE5MjA3NmUwNDMyNzhjYmNjOTgyNmM5N2E0ZDApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2E3MzgxOGJiMTMzNGNlMDk2ZDgzNzJkM2ZlMjliYzAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDg5NTk3LC03OS40NTYzMjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTI1MWY5ZTc1ZDRiNDRiNDk1NzBjZjg5ODY4NTk1YWUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzc1NjEyYTIxMmU0NGY1Mjg0MzZiNWMyYTFlM2ZjZGYgPSAkKCc8ZGl2IGlkPSJodG1sXzc3NTYxMmEyMTJlNDRmNTI4NDM2YjVjMmExZTNmY2RmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrZGFsZSxSb25jZXN2YWxsZXMgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85MjUxZjllNzVkNGI0NGI0OTU3MGNmODk4Njg1OTVhZS5zZXRDb250ZW50KGh0bWxfNzc1NjEyYTIxMmU0NGY1Mjg0MzZiNWMyYTFlM2ZjZGYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2E3MzgxOGJiMTMzNGNlMDk2ZDgzNzJkM2ZlMjliYzAuYmluZFBvcHVwKHBvcHVwXzkyNTFmOWU3NWQ0YjQ0YjQ5NTcwY2Y4OTg2ODU5NWFlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E5OTNlMDRkMjI4MTRjMWZiY2ZmZGEwZWFmYzkwMTFhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUxNTcwNiwtNzkuNDg0NDQ5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNDFhYTIzY2ZmOTY0M2U3OGFiM2Q1ODY4MGM4YjlkNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85MmQ2MWUxODc0MWI0YWNiYTI1YTE5NWJjNTI1NjE1MSA9ICQoJzxkaXYgaWQ9Imh0bWxfOTJkNjFlMTg3NDFiNGFjYmEyNWExOTViYzUyNTYxNTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJ1bm55bWVkZSxTd2Fuc2VhIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTQxYWEyM2NmZjk2NDNlNzhhYjNkNTg2ODBjOGI5ZDUuc2V0Q29udGVudChodG1sXzkyZDYxZTE4NzQxYjRhY2JhMjVhMTk1YmM1MjU2MTUxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2E5OTNlMDRkMjI4MTRjMWZiY2ZmZGEwZWFmYzkwMTFhLmJpbmRQb3B1cChwb3B1cF9hNDFhYTIzY2ZmOTY0M2U3OGFiM2Q1ODY4MGM4YjlkNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85NmU0YWYwMzMyYmU0Y2M4OWE2NTUzNzM0M2Q1Yjg3MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MjMwMTUsLTc5LjM4OTQ5MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjAyYzQ0OWI5MjgxNDhlZGFhYWE1ZWI0NWU5ZmZjMGMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzNmMTU5ZmQyMzFkNGZhZWE0MmJlNmMwODY0YTkzZjAgPSAkKCc8ZGl2IGlkPSJodG1sXzczZjE1OWZkMjMxZDRmYWVhNDJiZTZjMDg2NGE5M2YwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5RdWVlbiYjMzk7cyBQYXJrIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjAyYzQ0OWI5MjgxNDhlZGFhYWE1ZWI0NWU5ZmZjMGMuc2V0Q29udGVudChodG1sXzczZjE1OWZkMjMxZDRmYWVhNDJiZTZjMDg2NGE5M2YwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk2ZTRhZjAzMzJiZTRjYzg5YTY1NTM3MzQzZDViODcyLmJpbmRQb3B1cChwb3B1cF9mMDJjNDQ5YjkyODE0OGVkYWFhYTVlYjQ1ZTlmZmMwYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82ZDhkNDRkZGJlODM0YWQ5OWNhNGFmMzdjODljNThiZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYzNjk2NTYsLTc5LjYxNTgxODk5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE0MzE4M2ZmMGMyNzQyNDhhZWVhZWYwYTNkNTg3MTAzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzE2ODkzNDI4ZWFlMjRjZWFhNjZhNDM5MWFlOTczODk5ID0gJCgnPGRpdiBpZD0iaHRtbF8xNjg5MzQyOGVhZTI0Y2VhYTY2YTQzOTFhZTk3Mzg5OSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FuYWRhIFBvc3QgR2F0ZXdheSBQcm9jZXNzaW5nIENlbnRyZSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzE0MzE4M2ZmMGMyNzQyNDhhZWVhZWYwYTNkNTg3MTAzLnNldENvbnRlbnQoaHRtbF8xNjg5MzQyOGVhZTI0Y2VhYTY2YTQzOTFhZTk3Mzg5OSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82ZDhkNDRkZGJlODM0YWQ5OWNhNGFmMzdjODljNThiZS5iaW5kUG9wdXAocG9wdXBfMTQzMTgzZmYwYzI3NDI0OGFlZWFlZjBhM2Q1ODcxMDMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzhhZDhhYmU2ODdlNDFlZDhmYWIyYzcxYzhlZjYwZWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjI3NDM5LC03OS4zMjE1NThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmZkMGY1ODUxMDFhNDZkY2I5YTVhMWU3NGRhNjAxYTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTJmMjdlOTdkZWJmNDg2ZmEzNmIwMDQxMDJkZTZjNzcgPSAkKCc8ZGl2IGlkPSJodG1sXzUyZjI3ZTk3ZGViZjQ4NmZhMzZiMDA0MTAyZGU2Yzc3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CdXNpbmVzcyBSZXBseSBNYWlsIFByb2Nlc3NpbmcgQ2VudHJlIDk2OSBFYXN0ZXJuIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmZkMGY1ODUxMDFhNDZkY2I5YTVhMWU3NGRhNjAxYTYuc2V0Q29udGVudChodG1sXzUyZjI3ZTk3ZGViZjQ4NmZhMzZiMDA0MTAyZGU2Yzc3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc4YWQ4YWJlNjg3ZTQxZWQ4ZmFiMmM3MWM4ZWY2MGVlLmJpbmRQb3B1cChwb3B1cF9mZmQwZjU4NTEwMWE0NmRjYjlhNWExZTc0ZGE2MDFhNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZDE1Y2E3Mjc2NDM0ODEwODU5N2JhN2Y4MDVmNTY4OCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYwNTY0NjYsLTc5LjUwMTMyMDcwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2IwZjllMmVhZDk4NzRhNGE4Zjc2NjA5NmY1YjA1MGMzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JmMWFhNmRjMWVjZDQ5NTI5NmRiYjQ5NGI0NTJmNmIyID0gJCgnPGRpdiBpZD0iaHRtbF9iZjFhYTZkYzFlY2Q0OTUyOTZkYmI0OTRiNDUyZjZiMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtYmVyIEJheSBTaG9yZXMsTWltaWNvIFNvdXRoLE5ldyBUb3JvbnRvIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjBmOWUyZWFkOTg3NGE0YThmNzY2MDk2ZjViMDUwYzMuc2V0Q29udGVudChodG1sX2JmMWFhNmRjMWVjZDQ5NTI5NmRiYjQ5NGI0NTJmNmIyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzdkMTVjYTcyNzY0MzQ4MTA4NTk3YmE3ZjgwNWY1Njg4LmJpbmRQb3B1cChwb3B1cF9iMGY5ZTJlYWQ5ODc0YTRhOGY3NjYwOTZmNWIwNTBjMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lYjZlODg0ZWVhYzM0ZGYyODQyNmQ3ZWYzZWVkMDg0ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYwMjQxMzcwMDAwMDAxLC03OS41NDM0ODQwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84MjhlODc2Y2U5Yzk0OTllYTlmMTI5ZjgxZjFmODRhZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MTI0N2ZjOTk0YWU0NTQxODA3YzkzNTIzYzRiZjg4NiA9ICQoJzxkaXYgaWQ9Imh0bWxfNTEyNDdmYzk5NGFlNDU0MTgwN2M5MzUyM2M0YmY4ODYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFsZGVyd29vZCxMb25nIEJyYW5jaCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzgyOGU4NzZjZTljOTQ5OWVhOWYxMjlmODFmMWY4NGFlLnNldENvbnRlbnQoaHRtbF81MTI0N2ZjOTk0YWU0NTQxODA3YzkzNTIzYzRiZjg4Nik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lYjZlODg0ZWVhYzM0ZGYyODQyNmQ3ZWYzZWVkMDg0ZC5iaW5kUG9wdXAocG9wdXBfODI4ZTg3NmNlOWM5NDk5ZWE5ZjEyOWY4MWYxZjg0YWUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNWEyMjFiNzFkMWYyNGRkN2ExNzZmYzUzMDFlYTVlYjAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTM2NTM2MDAwMDAwMDUsLTc5LjUwNjk0MzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzg2NjM0ZWYyOTk3NDIxNzllYmY0YmIzMDQyNzUxODYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGVjZDY5NTUzNDg3NDYxMWFhZTAzODk4MDk4N2ViZjcgPSAkKCc8ZGl2IGlkPSJodG1sXzhlY2Q2OTU1MzQ4NzQ2MTFhYWUwMzg5ODA5ODdlYmY3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgS2luZ3N3YXksTW9udGdvbWVyeSBSb2FkLE9sZCBNaWxsIE5vcnRoIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzg2NjM0ZWYyOTk3NDIxNzllYmY0YmIzMDQyNzUxODYuc2V0Q29udGVudChodG1sXzhlY2Q2OTU1MzQ4NzQ2MTFhYWUwMzg5ODA5ODdlYmY3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzVhMjIxYjcxZDFmMjRkZDdhMTc2ZmM1MzAxZWE1ZWIwLmJpbmRQb3B1cChwb3B1cF9jODY2MzRlZjI5OTc0MjE3OWViZjRiYjMwNDI3NTE4Nik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zYzY4ZjIzZTMwZGY0MGRkOTE2NGZkYTUyNTNhZDI2ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYzNjI1NzksLTc5LjQ5ODUwOTA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzBjZWRiYzRjMTdkODQ3NmE4NTEyNTZhNjY3Mjk1ZDJiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzIwMGRhYTY3ZjMyOTQ5MWFhNTAwZmRhMmI2YmJjNzQzID0gJCgnPGRpdiBpZD0iaHRtbF8yMDBkYWE2N2YzMjk0OTFhYTUwMGZkYTJiNmJiYzc0MyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtYmVyIEJheSxLaW5nJiMzOTtzIE1pbGwgUGFyayxLaW5nc3dheSBQYXJrIFNvdXRoIEVhc3QsTWltaWNvIE5FLE9sZCBNaWxsIFNvdXRoLFRoZSBRdWVlbnN3YXkgRWFzdCxSb3lhbCBZb3JrIFNvdXRoIEVhc3QsU3VubnlsZWEgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wY2VkYmM0YzE3ZDg0NzZhODUxMjU2YTY2NzI5NWQyYi5zZXRDb250ZW50KGh0bWxfMjAwZGFhNjdmMzI5NDkxYWE1MDBmZGEyYjZiYmM3NDMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2M2OGYyM2UzMGRmNDBkZDkxNjRmZGE1MjUzYWQyNmQuYmluZFBvcHVwKHBvcHVwXzBjZWRiYzRjMTdkODQ3NmE4NTEyNTZhNjY3Mjk1ZDJiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdhYWU2ZGJlZDhiOTRhZjhhZDgyYjUwMDUxN2FlZWI5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjI4ODQwOCwtNzkuNTIwOTk5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODkxMjQ0MzJjY2FmNDJiOTk3ZmYzNTM2N2MyMDVmNTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzZmNDhiNTc2ODJhNDY2MTliZWQ1YzNiY2RhZWVmOTcgPSAkKCc8ZGl2IGlkPSJodG1sXzM2ZjQ4YjU3NjgyYTQ2NjE5YmVkNWMzYmNkYWVlZjk3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc3dheSBQYXJrIFNvdXRoIFdlc3QsTWltaWNvIE5XLFRoZSBRdWVlbnN3YXkgV2VzdCxSb3lhbCBZb3JrIFNvdXRoIFdlc3QsU291dGggb2YgQmxvb3IgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84OTEyNDQzMmNjYWY0MmI5OTdmZjM1MzY3YzIwNWY1Ny5zZXRDb250ZW50KGh0bWxfMzZmNDhiNTc2ODJhNDY2MTliZWQ1YzNiY2RhZWVmOTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2FhZTZkYmVkOGI5NGFmOGFkODJiNTAwNTE3YWVlYjkuYmluZFBvcHVwKHBvcHVwXzg5MTI0NDMyY2NhZjQyYjk5N2ZmMzUzNjdjMjA1ZjU3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzM4MmYyYmRmZjk1NzQ4YWE5YzZkMzAyNTAxYjk3MGJhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQzNTE1MiwtNzkuNTc3MjAwNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTYyNTk5OWEzNWQxNGNjMzllOGI0ZmEzM2VmOGRlMGIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYWE5MjY0MjIzNjdkNGY1YzgzYjdmY2Y2MDU3NzczN2QgPSAkKCc8ZGl2IGlkPSJodG1sX2FhOTI2NDIyMzY3ZDRmNWM4M2I3ZmNmNjA1Nzc3MzdkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CbG9vcmRhbGUgR2FyZGVucyxFcmluZ2F0ZSxNYXJrbGFuZCBXb29kLE9sZCBCdXJuaGFtdGhvcnBlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTYyNTk5OWEzNWQxNGNjMzllOGI0ZmEzM2VmOGRlMGIuc2V0Q29udGVudChodG1sX2FhOTI2NDIyMzY3ZDRmNWM4M2I3ZmNmNjA1Nzc3MzdkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzM4MmYyYmRmZjk1NzQ4YWE5YzZkMzAyNTAxYjk3MGJhLmJpbmRQb3B1cChwb3B1cF9lNjI1OTk5YTM1ZDE0Y2MzOWU4YjRmYTMzZWY4ZGUwYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iM2NiYTUzYTcxNGI0MjI3YjgyODlkYWRlNjVkYzAwMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1NjMwMzMsLTc5LjU2NTk2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRiNTVjNTAzYzNmMjQ1NzhiNDg2MGViMTYyOGNlN2ViID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2UwNDY1ZGI4ZDEwZDQ4OTliYjdmNjk0ZWY4NjNhZTMwID0gJCgnPGRpdiBpZD0iaHRtbF9lMDQ2NWRiOGQxMGQ0ODk5YmI3ZjY5NGVmODYzYWUzMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtYmVyIFN1bW1pdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRiNTVjNTAzYzNmMjQ1NzhiNDg2MGViMTYyOGNlN2ViLnNldENvbnRlbnQoaHRtbF9lMDQ2NWRiOGQxMGQ0ODk5YmI3ZjY5NGVmODYzYWUzMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iM2NiYTUzYTcxNGI0MjI3YjgyODlkYWRlNjVkYzAwMS5iaW5kUG9wdXAocG9wdXBfNGI1NWM1MDNjM2YyNDU3OGI0ODYwZWIxNjI4Y2U3ZWIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODA2ZGY5NGFiMjM1NDY4ZmFhNDg4YTY3NWRiZjU1MjIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MjQ3NjU5LC03OS41MzIyNDI0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODBmZmI0IiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwZmZiNCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF8yNTAwYTMwMDA2NDc0MjM5OTlmODA5MzU1MTQxYTRjOCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lZGFiZGM3YmIwYTg0OTBmYWYxMDg2ZmQ2N2JlOWRhYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yNDY2MDQ3ZTg5ZWM0ZmI4YTc2ZDIzYmVjYjg2ZmI4YSA9ICQoJzxkaXYgaWQ9Imh0bWxfMjQ2NjA0N2U4OWVjNGZiOGE3NmQyM2JlY2I4NmZiOGEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVtZXJ5LEh1bWJlcmxlYSBDbHVzdGVyIDM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2VkYWJkYzdiYjBhODQ5MGZhZjEwODZmZDY3YmU5ZGFhLnNldENvbnRlbnQoaHRtbF8yNDY2MDQ3ZTg5ZWM0ZmI4YTc2ZDIzYmVjYjg2ZmI4YSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84MDZkZjk0YWIyMzU0NjhmYWE0ODhhNjc1ZGJmNTUyMi5iaW5kUG9wdXAocG9wdXBfZWRhYmRjN2JiMGE4NDkwZmFmMTA4NmZkNjdiZTlkYWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzFmODMzZTQwMzU2NGJmZjhkMWNiYzgyMDQ1YmNlN2UgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MDY4NzYsLTc5LjUxODE4ODQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzAxNzQ4MjhiZGY5NjQ1M2NhZmRmOWY3MzZkM2MzMGQyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzg5NTI3NDNkNDM0MDQ1Nzk4NzUwNjc0NjIzMjVjYjlhID0gJCgnPGRpdiBpZD0iaHRtbF84OTUyNzQzZDQzNDA0NTc5ODc1MDY3NDYyMzI1Y2I5YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2VzdG9uIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDE3NDgyOGJkZjk2NDUzY2FmZGY5ZjczNmQzYzMwZDIuc2V0Q29udGVudChodG1sXzg5NTI3NDNkNDM0MDQ1Nzk4NzUwNjc0NjIzMjVjYjlhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2MxZjgzM2U0MDM1NjRiZmY4ZDFjYmM4MjA0NWJjZTdlLmJpbmRQb3B1cChwb3B1cF8wMTc0ODI4YmRmOTY0NTNjYWZkZjlmNzM2ZDNjMzBkMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MjAzNTRmMjY0YTI0OTBhYjU5MzViYzgzNjE1YjMzNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5NjMxOSwtNzkuNTMyMjQyNDAwMDAwMDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWJkMmY0MmU5MGU2NGYyNDkwOThhYWI1M2FmYzgwMzIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjcxMDRmZTVlMzFlNDU4Y2I0YmVkYTU0NWZjYmRjYmIgPSAkKCc8ZGl2IGlkPSJodG1sX2Y3MTA0ZmU1ZTMxZTQ1OGNiNGJlZGE1NDVmY2JkY2JiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0bW91bnQgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85YmQyZjQyZTkwZTY0ZjI0OTA5OGFhYjUzYWZjODAzMi5zZXRDb250ZW50KGh0bWxfZjcxMDRmZTVlMzFlNDU4Y2I0YmVkYTU0NWZjYmRjYmIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODIwMzU0ZjI2NGEyNDkwYWI1OTM1YmM4MzYxNWIzMzcuYmluZFBvcHVwKHBvcHVwXzliZDJmNDJlOTBlNjRmMjQ5MDk4YWFiNTNhZmM4MDMyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZkY2YxOTdhNTVhNzQwNjZiYmE0MDM3NDAwNzk4NzU0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg4OTA1NCwtNzkuNTU0NzI0NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzI3ZjExODA4MzZjNDRjYTk5YWIyY2NkODRmNzczMmYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOWZhYWRhODkzMjdmNDVjYmE5N2MwNjA5NDRmMzU4MTEgPSAkKCc8ZGl2IGlkPSJodG1sXzlmYWFkYTg5MzI3ZjQ1Y2JhOTdjMDYwOTQ0ZjM1ODExIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc3ZpZXcgVmlsbGFnZSxNYXJ0aW4gR3JvdmUgR2FyZGVucyxSaWNodmlldyBHYXJkZW5zLFN0LiBQaGlsbGlwcyBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzMyN2YxMTgwODM2YzQ0Y2E5OWFiMmNjZDg0Zjc3MzJmLnNldENvbnRlbnQoaHRtbF85ZmFhZGE4OTMyN2Y0NWNiYTk3YzA2MDk0NGYzNTgxMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82ZGNmMTk3YTU1YTc0MDY2YmJhNDAzNzQwMDc5ODc1NC5iaW5kUG9wdXAocG9wdXBfMzI3ZjExODA4MzZjNDRjYTk5YWIyY2NkODRmNzczMmYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjU5ZDMzNWJiNzJmNDlhNDg2M2UwODI4MTczMGJiMzIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Mzk0MTYzOTk5OTk5OTYsLTc5LjU4ODQzNjldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfMjUwMGEzMDAwNjQ3NDIzOTk5ZjgwOTM1NTE0MWE0YzgpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDVjZjYxMGZiYWUxNGJkYzkxN2JjMWE0NWI3NWRjNDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTVlMmQ4M2QyNTZhNDJmZGE0NjNhZTAyZTM4MWJkYTIgPSAkKCc8ZGl2IGlkPSJodG1sXzU1ZTJkODNkMjU2YTQyZmRhNDYzYWUwMmUzODFiZGEyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BbGJpb24gR2FyZGVucyxCZWF1bW9uZCBIZWlnaHRzLEh1bWJlcmdhdGUsSmFtZXN0b3duLE1vdW50IE9saXZlLFNpbHZlcnN0b25lLFNvdXRoIFN0ZWVsZXMsVGhpc3RsZXRvd24gQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80NWNmNjEwZmJhZTE0YmRjOTE3YmMxYTQ1Yjc1ZGM0OS5zZXRDb250ZW50KGh0bWxfNTVlMmQ4M2QyNTZhNDJmZGE0NjNhZTAyZTM4MWJkYTIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjU5ZDMzNWJiNzJmNDlhNDg2M2UwODI4MTczMGJiMzIuYmluZFBvcHVwKHBvcHVwXzQ1Y2Y2MTBmYmFlMTRiZGM5MTdiYzFhNDViNzVkYzQ5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRiMmQwNWY0N2I1NDRkMTE4NmJhYzkxYTNlOTEzYjQ5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA2NzQ4Mjk5OTk5OTk0LC03OS41OTQwNTQ0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzI1MDBhMzAwMDY0NzQyMzk5OWY4MDkzNTUxNDFhNGM4KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzAwNWMxYjQzOTA0YjQyMTliYzI4YzJiYWJhYTIyYmI4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZmNjQ4MjhhMmI0ODQwMjJhNTZhNGNlOTBhNTkyYWUxID0gJCgnPGRpdiBpZD0iaHRtbF9mZjY0ODI4YTJiNDg0MDIyYTU2YTRjZTkwYTU5MmFlMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Tm9ydGh3ZXN0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDA1YzFiNDM5MDRiNDIxOWJjMjhjMmJhYmFhMjJiYjguc2V0Q29udGVudChodG1sX2ZmNjQ4MjhhMmI0ODQwMjJhNTZhNGNlOTBhNTkyYWUxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzRiMmQwNWY0N2I1NDRkMTE4NmJhYzkxYTNlOTEzYjQ5LmJpbmRQb3B1cChwb3B1cF8wMDVjMWI0MzkwNGI0MjE5YmMyOGMyYmFiYWEyMmJiOCk7CgogICAgICAgICAgICAKICAgICAgICAKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



Now we examine the clusters to see the distinguishing venues

.. code:: ipython3

    toronto_merged.loc[toronto_merged['Cluster Labels'] == 0, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Borough</th>
          <th>Cluster Labels</th>
          <th>1st Most Common Venue</th>
          <th>2nd Most Common Venue</th>
          <th>3rd Most Common Venue</th>
          <th>4th Most Common Venue</th>
          <th>5th Most Common Venue</th>
          <th>6th Most Common Venue</th>
          <th>7th Most Common Venue</th>
          <th>8th Most Common Venue</th>
          <th>9th Most Common Venue</th>
          <th>10th Most Common Venue</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>Fast Food Restaurant</td>
          <td>Women's Store</td>
          <td>Falafel Restaurant</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>1</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>Bar</td>
          <td>Women's Store</td>
          <td>Farmers Market</td>
          <td>Event Space</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>2</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>Spa</td>
          <td>Intersection</td>
          <td>Electronics Store</td>
          <td>Pizza Place</td>
          <td>Mexican Restaurant</td>
          <td>Breakfast Spot</td>
          <td>Rental Car Location</td>
          <td>Medical Center</td>
          <td>Dim Sum Restaurant</td>
          <td>Diner</td>
        </tr>
        <tr>
          <th>3</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>Coffee Shop</td>
          <td>Korean Restaurant</td>
          <td>Falafel Restaurant</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>4</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>Fried Chicken Joint</td>
          <td>Bakery</td>
          <td>Hakka Restaurant</td>
          <td>Bank</td>
          <td>Thai Restaurant</td>
          <td>Athletics &amp; Sports</td>
          <td>Caribbean Restaurant</td>
          <td>Discount Store</td>
          <td>Dim Sum Restaurant</td>
          <td>Diner</td>
        </tr>
        <tr>
          <th>6</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>Coffee Shop</td>
          <td>Convenience Store</td>
          <td>Hobby Shop</td>
          <td>Discount Store</td>
          <td>Department Store</td>
          <td>Deli / Bodega</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
        </tr>
        <tr>
          <th>8</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>Motel</td>
          <td>American Restaurant</td>
          <td>Movie Theater</td>
          <td>Dance Studio</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>9</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>College Stadium</td>
          <td>General Entertainment</td>
          <td>Skating Rink</td>
          <td>Café</td>
          <td>Women's Store</td>
          <td>Deli / Bodega</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>10</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>Indian Restaurant</td>
          <td>Latin American Restaurant</td>
          <td>Vietnamese Restaurant</td>
          <td>Pet Store</td>
          <td>Chinese Restaurant</td>
          <td>Gaming Cafe</td>
          <td>Furniture / Home Store</td>
          <td>Thrift / Vintage Store</td>
          <td>Women's Store</td>
          <td>Diner</td>
        </tr>
        <tr>
          <th>11</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>Auto Garage</td>
          <td>Middle Eastern Restaurant</td>
          <td>Bakery</td>
          <td>Sandwich Place</td>
          <td>Shopping Mall</td>
          <td>Vietnamese Restaurant</td>
          <td>Breakfast Spot</td>
          <td>Accessories Store</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
        </tr>
        <tr>
          <th>12</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>Lounge</td>
          <td>Clothing Store</td>
          <td>Breakfast Spot</td>
          <td>Skating Rink</td>
          <td>Department Store</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>13</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>Pharmacy</td>
          <td>Pizza Place</td>
          <td>Fast Food Restaurant</td>
          <td>Fried Chicken Joint</td>
          <td>Breakfast Spot</td>
          <td>Bank</td>
          <td>Noodle House</td>
          <td>Italian Restaurant</td>
          <td>Chinese Restaurant</td>
          <td>Thai Restaurant</td>
        </tr>
        <tr>
          <th>15</th>
          <td>Scarborough</td>
          <td>0.0</td>
          <td>Fast Food Restaurant</td>
          <td>Chinese Restaurant</td>
          <td>Coffee Shop</td>
          <td>Bubble Tea Shop</td>
          <td>Sandwich Place</td>
          <td>Thrift / Vintage Store</td>
          <td>Nail Salon</td>
          <td>Pizza Place</td>
          <td>Pharmacy</td>
          <td>Breakfast Spot</td>
        </tr>
        <tr>
          <th>16</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Dog Run</td>
          <td>Golf Course</td>
          <td>Athletics &amp; Sports</td>
          <td>Pool</td>
          <td>Mediterranean Restaurant</td>
          <td>Women's Store</td>
          <td>Dessert Shop</td>
          <td>Dim Sum Restaurant</td>
          <td>Diner</td>
          <td>Discount Store</td>
        </tr>
        <tr>
          <th>17</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Coffee Shop</td>
          <td>Clothing Store</td>
          <td>Shopping Mall</td>
          <td>Theater</td>
          <td>Department Store</td>
          <td>Bank</td>
          <td>Bakery</td>
          <td>Burger Joint</td>
          <td>Liquor Store</td>
          <td>Japanese Restaurant</td>
        </tr>
        <tr>
          <th>18</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Chinese Restaurant</td>
          <td>Japanese Restaurant</td>
          <td>Bank</td>
          <td>Café</td>
          <td>Women's Store</td>
          <td>Dessert Shop</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
        </tr>
        <tr>
          <th>20</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Ramen Restaurant</td>
          <td>Coffee Shop</td>
          <td>Sandwich Place</td>
          <td>Café</td>
          <td>Juice Bar</td>
          <td>Japanese Restaurant</td>
          <td>Electronics Store</td>
          <td>Indonesian Restaurant</td>
          <td>Plaza</td>
          <td>Restaurant</td>
        </tr>
        <tr>
          <th>22</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Pizza Place</td>
          <td>Pharmacy</td>
          <td>Grocery Store</td>
          <td>Butcher</td>
          <td>Discount Store</td>
          <td>Coffee Shop</td>
          <td>General Entertainment</td>
          <td>Cuban Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>24</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Basketball Court</td>
          <td>Gym / Fitness Center</td>
          <td>Café</td>
          <td>Caribbean Restaurant</td>
          <td>Japanese Restaurant</td>
          <td>Women's Store</td>
          <td>Diner</td>
          <td>Discount Store</td>
          <td>Dog Run</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>25</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Gym</td>
          <td>Coffee Shop</td>
          <td>Beer Store</td>
          <td>Asian Restaurant</td>
          <td>Fast Food Restaurant</td>
          <td>Italian Restaurant</td>
          <td>Restaurant</td>
          <td>Supermarket</td>
          <td>Japanese Restaurant</td>
          <td>Sandwich Place</td>
        </tr>
        <tr>
          <th>26</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Coffee Shop</td>
          <td>Pharmacy</td>
          <td>Bank</td>
          <td>Frozen Yogurt Shop</td>
          <td>Fried Chicken Joint</td>
          <td>Fast Food Restaurant</td>
          <td>Diner</td>
          <td>Deli / Bodega</td>
          <td>Middle Eastern Restaurant</td>
          <td>Pizza Place</td>
        </tr>
        <tr>
          <th>27</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Coffee Shop</td>
          <td>Bar</td>
          <td>Caribbean Restaurant</td>
          <td>Miscellaneous Shop</td>
          <td>Massage Studio</td>
          <td>Falafel Restaurant</td>
          <td>General Entertainment</td>
          <td>Deli / Bodega</td>
          <td>Eastern European Restaurant</td>
          <td>Gluten-free Restaurant</td>
        </tr>
        <tr>
          <th>31</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Grocery Store</td>
          <td>Athletics &amp; Sports</td>
          <td>Discount Store</td>
          <td>Liquor Store</td>
          <td>Gym / Fitness Center</td>
          <td>Comfort Food Restaurant</td>
          <td>Dessert Shop</td>
          <td>Event Space</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
        </tr>
        <tr>
          <th>32</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Coffee Shop</td>
          <td>Portuguese Restaurant</td>
          <td>Hockey Arena</td>
          <td>Intersection</td>
          <td>Deli / Bodega</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>33</th>
          <td>EastYork</td>
          <td>0.0</td>
          <td>Pizza Place</td>
          <td>Fast Food Restaurant</td>
          <td>Pet Store</td>
          <td>Gastropub</td>
          <td>Bank</td>
          <td>Intersection</td>
          <td>Athletics &amp; Sports</td>
          <td>Café</td>
          <td>Gym / Fitness Center</td>
          <td>Pharmacy</td>
        </tr>
        <tr>
          <th>34</th>
          <td>EastYork</td>
          <td>0.0</td>
          <td>Park</td>
          <td>Pharmacy</td>
          <td>Curling Ice</td>
          <td>Video Store</td>
          <td>Skating Rink</td>
          <td>Beer Store</td>
          <td>Athletics &amp; Sports</td>
          <td>Asian Restaurant</td>
          <td>Cosmetics Shop</td>
          <td>Discount Store</td>
        </tr>
        <tr>
          <th>36</th>
          <td>EastYork</td>
          <td>0.0</td>
          <td>Sporting Goods Shop</td>
          <td>Coffee Shop</td>
          <td>Burger Joint</td>
          <td>Furniture / Home Store</td>
          <td>Gym</td>
          <td>Beer Store</td>
          <td>Sports Bar</td>
          <td>Bike Shop</td>
          <td>Smoothie Shop</td>
          <td>Shopping Mall</td>
        </tr>
        <tr>
          <th>37</th>
          <td>EastYork</td>
          <td>0.0</td>
          <td>Burger Joint</td>
          <td>Indian Restaurant</td>
          <td>Gym</td>
          <td>Supermarket</td>
          <td>Bank</td>
          <td>Coffee Shop</td>
          <td>Grocery Store</td>
          <td>Housing Development</td>
          <td>Liquor Store</td>
          <td>Park</td>
        </tr>
        <tr>
          <th>39</th>
          <td>EastToronto</td>
          <td>0.0</td>
          <td>Greek Restaurant</td>
          <td>Ice Cream Shop</td>
          <td>Italian Restaurant</td>
          <td>Yoga Studio</td>
          <td>Coffee Shop</td>
          <td>Pizza Place</td>
          <td>Cosmetics Shop</td>
          <td>Pub</td>
          <td>Restaurant</td>
          <td>Dessert Shop</td>
        </tr>
        <tr>
          <th>40</th>
          <td>EastToronto</td>
          <td>0.0</td>
          <td>Park</td>
          <td>Sandwich Place</td>
          <td>Gym</td>
          <td>Ice Cream Shop</td>
          <td>Pet Store</td>
          <td>Movie Theater</td>
          <td>Pub</td>
          <td>Burrito Place</td>
          <td>Burger Joint</td>
          <td>Liquor Store</td>
        </tr>
        <tr>
          <th>...</th>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
          <td>...</td>
        </tr>
        <tr>
          <th>60</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Coffee Shop</td>
          <td>Fast Food Restaurant</td>
          <td>Italian Restaurant</td>
          <td>Toy / Game Store</td>
          <td>Sushi Restaurant</td>
          <td>Butcher</td>
          <td>Pub</td>
          <td>Café</td>
          <td>Thai Restaurant</td>
          <td>Pizza Place</td>
        </tr>
        <tr>
          <th>61</th>
          <td>CentralToronto</td>
          <td>0.0</td>
          <td>Garden</td>
          <td>Music Venue</td>
          <td>Women's Store</td>
          <td>Dance Studio</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>62</th>
          <td>CentralToronto</td>
          <td>0.0</td>
          <td>Jewelry Store</td>
          <td>Sushi Restaurant</td>
          <td>Trail</td>
          <td>Mexican Restaurant</td>
          <td>Women's Store</td>
          <td>Department Store</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
        </tr>
        <tr>
          <th>63</th>
          <td>CentralToronto</td>
          <td>0.0</td>
          <td>Café</td>
          <td>Sandwich Place</td>
          <td>Coffee Shop</td>
          <td>History Museum</td>
          <td>Park</td>
          <td>Pizza Place</td>
          <td>Cosmetics Shop</td>
          <td>Pub</td>
          <td>Burger Joint</td>
          <td>Liquor Store</td>
        </tr>
        <tr>
          <th>64</th>
          <td>DowntownToronto</td>
          <td>0.0</td>
          <td>Café</td>
          <td>Bakery</td>
          <td>Restaurant</td>
          <td>Sandwich Place</td>
          <td>Bookstore</td>
          <td>Japanese Restaurant</td>
          <td>Italian Restaurant</td>
          <td>Bar</td>
          <td>Gym</td>
          <td>College Gym</td>
        </tr>
        <tr>
          <th>65</th>
          <td>DowntownToronto</td>
          <td>0.0</td>
          <td>Café</td>
          <td>Mexican Restaurant</td>
          <td>Vietnamese Restaurant</td>
          <td>Comfort Food Restaurant</td>
          <td>Caribbean Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Fish &amp; Chips Shop</td>
          <td>Belgian Restaurant</td>
          <td>Farmers Market</td>
          <td>Snack Place</td>
        </tr>
        <tr>
          <th>66</th>
          <td>DowntownToronto</td>
          <td>0.0</td>
          <td>Airport Service</td>
          <td>Airport Terminal</td>
          <td>Airport Lounge</td>
          <td>Boat or Ferry</td>
          <td>Sculpture Garden</td>
          <td>Plane</td>
          <td>Harbor / Marina</td>
          <td>Boutique</td>
          <td>Coffee Shop</td>
          <td>Airport Gate</td>
        </tr>
        <tr>
          <th>67</th>
          <td>DowntownToronto</td>
          <td>0.0</td>
          <td>Café</td>
          <td>Seafood Restaurant</td>
          <td>Beer Bar</td>
          <td>Farmers Market</td>
          <td>Cocktail Bar</td>
          <td>Clothing Store</td>
          <td>Food Truck</td>
          <td>Pub</td>
          <td>Steakhouse</td>
          <td>Bakery</td>
        </tr>
        <tr>
          <th>68</th>
          <td>DowntownToronto</td>
          <td>0.0</td>
          <td>Café</td>
          <td>Coffee Shop</td>
          <td>Steakhouse</td>
          <td>Restaurant</td>
          <td>Deli / Bodega</td>
          <td>Pizza Place</td>
          <td>Speakeasy</td>
          <td>Seafood Restaurant</td>
          <td>Pub</td>
          <td>Gym</td>
        </tr>
        <tr>
          <th>69</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Furniture / Home Store</td>
          <td>Event Space</td>
          <td>Clothing Store</td>
          <td>Athletics &amp; Sports</td>
          <td>Gift Shop</td>
          <td>Miscellaneous Shop</td>
          <td>Boutique</td>
          <td>Vietnamese Restaurant</td>
          <td>Coffee Shop</td>
          <td>Accessories Store</td>
        </tr>
        <tr>
          <th>70</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Pizza Place</td>
          <td>Pub</td>
          <td>Japanese Restaurant</td>
          <td>Asian Restaurant</td>
          <td>Deli / Bodega</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>73</th>
          <td>DowntownToronto</td>
          <td>0.0</td>
          <td>Grocery Store</td>
          <td>Café</td>
          <td>Park</td>
          <td>Athletics &amp; Sports</td>
          <td>Italian Restaurant</td>
          <td>Diner</td>
          <td>Convenience Store</td>
          <td>Nightclub</td>
          <td>Restaurant</td>
          <td>Baby Store</td>
        </tr>
        <tr>
          <th>74</th>
          <td>WestToronto</td>
          <td>0.0</td>
          <td>Supermarket</td>
          <td>Pharmacy</td>
          <td>Bakery</td>
          <td>Park</td>
          <td>Café</td>
          <td>Brewery</td>
          <td>Bus Stop</td>
          <td>Bar</td>
          <td>Bank</td>
          <td>Middle Eastern Restaurant</td>
        </tr>
        <tr>
          <th>75</th>
          <td>WestToronto</td>
          <td>0.0</td>
          <td>Bar</td>
          <td>Asian Restaurant</td>
          <td>Vietnamese Restaurant</td>
          <td>Pizza Place</td>
          <td>Salon / Barbershop</td>
          <td>Ice Cream Shop</td>
          <td>New American Restaurant</td>
          <td>Brewery</td>
          <td>Korean Restaurant</td>
          <td>Yoga Studio</td>
        </tr>
        <tr>
          <th>76</th>
          <td>WestToronto</td>
          <td>0.0</td>
          <td>Café</td>
          <td>Breakfast Spot</td>
          <td>Coffee Shop</td>
          <td>Performing Arts Venue</td>
          <td>Caribbean Restaurant</td>
          <td>Burrito Place</td>
          <td>Sandwich Place</td>
          <td>Stadium</td>
          <td>Italian Restaurant</td>
          <td>Intersection</td>
        </tr>
        <tr>
          <th>78</th>
          <td>York</td>
          <td>0.0</td>
          <td>Restaurant</td>
          <td>Skating Rink</td>
          <td>Check Cashing Service</td>
          <td>Turkish Restaurant</td>
          <td>Sandwich Place</td>
          <td>Dance Studio</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>80</th>
          <td>WestToronto</td>
          <td>0.0</td>
          <td>Thai Restaurant</td>
          <td>Grocery Store</td>
          <td>Café</td>
          <td>Mexican Restaurant</td>
          <td>Speakeasy</td>
          <td>Music Venue</td>
          <td>Cajun / Creole Restaurant</td>
          <td>Diner</td>
          <td>Discount Store</td>
          <td>Bookstore</td>
        </tr>
        <tr>
          <th>81</th>
          <td>WestToronto</td>
          <td>0.0</td>
          <td>Breakfast Spot</td>
          <td>Gift Shop</td>
          <td>Dog Run</td>
          <td>Cuban Restaurant</td>
          <td>Dessert Shop</td>
          <td>Bar</td>
          <td>Bookstore</td>
          <td>Restaurant</td>
          <td>Italian Restaurant</td>
          <td>Movie Theater</td>
        </tr>
        <tr>
          <th>82</th>
          <td>WestToronto</td>
          <td>0.0</td>
          <td>Café</td>
          <td>Pizza Place</td>
          <td>Italian Restaurant</td>
          <td>Sushi Restaurant</td>
          <td>Coffee Shop</td>
          <td>Gourmet Shop</td>
          <td>Food</td>
          <td>Sandwich Place</td>
          <td>Bookstore</td>
          <td>Smoothie Shop</td>
        </tr>
        <tr>
          <th>83</th>
          <td>Queen'sPark</td>
          <td>0.0</td>
          <td>Coffee Shop</td>
          <td>Gym</td>
          <td>Park</td>
          <td>Diner</td>
          <td>Hobby Shop</td>
          <td>Seafood Restaurant</td>
          <td>Sandwich Place</td>
          <td>Portuguese Restaurant</td>
          <td>Nightclub</td>
          <td>Mexican Restaurant</td>
        </tr>
        <tr>
          <th>84</th>
          <td>Mississauga</td>
          <td>0.0</td>
          <td>Coffee Shop</td>
          <td>Hotel</td>
          <td>American Restaurant</td>
          <td>Mediterranean Restaurant</td>
          <td>Burrito Place</td>
          <td>Sandwich Place</td>
          <td>Middle Eastern Restaurant</td>
          <td>Fried Chicken Joint</td>
          <td>Gym / Fitness Center</td>
          <td>Cosmetics Shop</td>
        </tr>
        <tr>
          <th>85</th>
          <td>EastToronto</td>
          <td>0.0</td>
          <td>Yoga Studio</td>
          <td>Auto Workshop</td>
          <td>Spa</td>
          <td>Smoke Shop</td>
          <td>Brewery</td>
          <td>Skate Park</td>
          <td>Farmers Market</td>
          <td>Fast Food Restaurant</td>
          <td>Burrito Place</td>
          <td>Restaurant</td>
        </tr>
        <tr>
          <th>86</th>
          <td>Etobicoke</td>
          <td>0.0</td>
          <td>Café</td>
          <td>Gym</td>
          <td>Bakery</td>
          <td>Pharmacy</td>
          <td>Pizza Place</td>
          <td>Restaurant</td>
          <td>Business Service</td>
          <td>Mexican Restaurant</td>
          <td>Sandwich Place</td>
          <td>Seafood Restaurant</td>
        </tr>
        <tr>
          <th>87</th>
          <td>Etobicoke</td>
          <td>0.0</td>
          <td>Pizza Place</td>
          <td>Gym</td>
          <td>Skating Rink</td>
          <td>Coffee Shop</td>
          <td>Pub</td>
          <td>Dance Studio</td>
          <td>Sandwich Place</td>
          <td>Pharmacy</td>
          <td>Garden</td>
          <td>Coworking Space</td>
        </tr>
        <tr>
          <th>90</th>
          <td>Etobicoke</td>
          <td>0.0</td>
          <td>Gym</td>
          <td>Tanning Salon</td>
          <td>Convenience Store</td>
          <td>Discount Store</td>
          <td>Burrito Place</td>
          <td>Sandwich Place</td>
          <td>Burger Joint</td>
          <td>Flower Shop</td>
          <td>Supplement Shop</td>
          <td>Bakery</td>
        </tr>
        <tr>
          <th>91</th>
          <td>Etobicoke</td>
          <td>0.0</td>
          <td>Pizza Place</td>
          <td>Beer Store</td>
          <td>Convenience Store</td>
          <td>Café</td>
          <td>Liquor Store</td>
          <td>Pharmacy</td>
          <td>Coffee Shop</td>
          <td>Gastropub</td>
          <td>Gluten-free Restaurant</td>
          <td>Dumpling Restaurant</td>
        </tr>
        <tr>
          <th>92</th>
          <td>NorthYork</td>
          <td>0.0</td>
          <td>Pizza Place</td>
          <td>Empanada Restaurant</td>
          <td>Dance Studio</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
          <td>Discount Store</td>
          <td>Diner</td>
        </tr>
        <tr>
          <th>95</th>
          <td>Etobicoke</td>
          <td>0.0</td>
          <td>Pizza Place</td>
          <td>Coffee Shop</td>
          <td>Discount Store</td>
          <td>Chinese Restaurant</td>
          <td>Middle Eastern Restaurant</td>
          <td>Intersection</td>
          <td>Sandwich Place</td>
          <td>Deli / Bodega</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
        </tr>
        <tr>
          <th>97</th>
          <td>Etobicoke</td>
          <td>0.0</td>
          <td>Grocery Store</td>
          <td>Pizza Place</td>
          <td>Fried Chicken Joint</td>
          <td>Sandwich Place</td>
          <td>Fast Food Restaurant</td>
          <td>Beer Store</td>
          <td>Pharmacy</td>
          <td>Gay Bar</td>
          <td>Cuban Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>98</th>
          <td>Etobicoke</td>
          <td>0.0</td>
          <td>Drugstore</td>
          <td>Rental Car Location</td>
          <td>Women's Store</td>
          <td>Dance Studio</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Dog Run</td>
          <td>Discount Store</td>
        </tr>
      </tbody>
    </table>
    <p>75 rows × 12 columns</p>
    </div>



.. code:: ipython3

    toronto_merged.loc[toronto_merged['Cluster Labels'] == 1, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Borough</th>
          <th>Cluster Labels</th>
          <th>1st Most Common Venue</th>
          <th>2nd Most Common Venue</th>
          <th>3rd Most Common Venue</th>
          <th>4th Most Common Venue</th>
          <th>5th Most Common Venue</th>
          <th>6th Most Common Venue</th>
          <th>7th Most Common Venue</th>
          <th>8th Most Common Venue</th>
          <th>9th Most Common Venue</th>
          <th>10th Most Common Venue</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>5</th>
          <td>Scarborough</td>
          <td>1.0</td>
          <td>Playground</td>
          <td>Women's Store</td>
          <td>Dance Studio</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
          <td>Discount Store</td>
        </tr>
        <tr>
          <th>14</th>
          <td>Scarborough</td>
          <td>1.0</td>
          <td>Playground</td>
          <td>Park</td>
          <td>Women's Store</td>
          <td>Dance Studio</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>46</th>
          <td>CentralToronto</td>
          <td>1.0</td>
          <td>Tennis Court</td>
          <td>Playground</td>
          <td>Summer Camp</td>
          <td>Women's Store</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
          <td>Discount Store</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    toronto_merged.loc[toronto_merged['Cluster Labels'] == 2, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Borough</th>
          <th>Cluster Labels</th>
          <th>1st Most Common Venue</th>
          <th>2nd Most Common Venue</th>
          <th>3rd Most Common Venue</th>
          <th>4th Most Common Venue</th>
          <th>5th Most Common Venue</th>
          <th>6th Most Common Venue</th>
          <th>7th Most Common Venue</th>
          <th>8th Most Common Venue</th>
          <th>9th Most Common Venue</th>
          <th>10th Most Common Venue</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>19</th>
          <td>NorthYork</td>
          <td>2.0</td>
          <td>Piano Bar</td>
          <td>Dance Studio</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
          <td>Discount Store</td>
          <td>Diner</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    toronto_merged.loc[toronto_merged['Cluster Labels'] == 3, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Borough</th>
          <th>Cluster Labels</th>
          <th>1st Most Common Venue</th>
          <th>2nd Most Common Venue</th>
          <th>3rd Most Common Venue</th>
          <th>4th Most Common Venue</th>
          <th>5th Most Common Venue</th>
          <th>6th Most Common Venue</th>
          <th>7th Most Common Venue</th>
          <th>8th Most Common Venue</th>
          <th>9th Most Common Venue</th>
          <th>10th Most Common Venue</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>30</th>
          <td>NorthYork</td>
          <td>3.0</td>
          <td>Korean Restaurant</td>
          <td>Baseball Field</td>
          <td>Food Truck</td>
          <td>Women's Store</td>
          <td>Dessert Shop</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
        </tr>
        <tr>
          <th>93</th>
          <td>NorthYork</td>
          <td>3.0</td>
          <td>Baseball Field</td>
          <td>Women's Store</td>
          <td>Farmers Market</td>
          <td>Event Space</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    toronto_merged.loc[toronto_merged['Cluster Labels'] == 4, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Borough</th>
          <th>Cluster Labels</th>
          <th>1st Most Common Venue</th>
          <th>2nd Most Common Venue</th>
          <th>3rd Most Common Venue</th>
          <th>4th Most Common Venue</th>
          <th>5th Most Common Venue</th>
          <th>6th Most Common Venue</th>
          <th>7th Most Common Venue</th>
          <th>8th Most Common Venue</th>
          <th>9th Most Common Venue</th>
          <th>10th Most Common Venue</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>7</th>
          <td>Scarborough</td>
          <td>4.0</td>
          <td>Bakery</td>
          <td>Bus Line</td>
          <td>Bus Station</td>
          <td>Park</td>
          <td>Soccer Field</td>
          <td>Fast Food Restaurant</td>
          <td>Intersection</td>
          <td>Women's Store</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
        </tr>
        <tr>
          <th>21</th>
          <td>NorthYork</td>
          <td>4.0</td>
          <td>Park</td>
          <td>Convenience Store</td>
          <td>Bank</td>
          <td>Women's Store</td>
          <td>Department Store</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
        </tr>
        <tr>
          <th>23</th>
          <td>NorthYork</td>
          <td>4.0</td>
          <td>Park</td>
          <td>Food &amp; Drink Shop</td>
          <td>BBQ Joint</td>
          <td>Women's Store</td>
          <td>Department Store</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>28</th>
          <td>NorthYork</td>
          <td>4.0</td>
          <td>Airport</td>
          <td>Park</td>
          <td>Women's Store</td>
          <td>Deli / Bodega</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>29</th>
          <td>NorthYork</td>
          <td>4.0</td>
          <td>Grocery Store</td>
          <td>Park</td>
          <td>Shopping Mall</td>
          <td>Bank</td>
          <td>Women's Store</td>
          <td>Department Store</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
        </tr>
        <tr>
          <th>35</th>
          <td>EastToronto</td>
          <td>4.0</td>
          <td>Trail</td>
          <td>Park</td>
          <td>Asian Restaurant</td>
          <td>Health Food Store</td>
          <td>Pub</td>
          <td>Women's Store</td>
          <td>Dessert Shop</td>
          <td>Dim Sum Restaurant</td>
          <td>Diner</td>
          <td>Discount Store</td>
        </tr>
        <tr>
          <th>38</th>
          <td>EastYork</td>
          <td>4.0</td>
          <td>Coffee Shop</td>
          <td>Park</td>
          <td>Convenience Store</td>
          <td>Deli / Bodega</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>42</th>
          <td>CentralToronto</td>
          <td>4.0</td>
          <td>Park</td>
          <td>Swim School</td>
          <td>Bus Line</td>
          <td>Women's Store</td>
          <td>Department Store</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>43</th>
          <td>CentralToronto</td>
          <td>4.0</td>
          <td>Hotel</td>
          <td>Gym</td>
          <td>Breakfast Spot</td>
          <td>Food &amp; Drink Shop</td>
          <td>Convenience Store</td>
          <td>Sandwich Place</td>
          <td>Park</td>
          <td>Clothing Store</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>48</th>
          <td>DowntownToronto</td>
          <td>4.0</td>
          <td>Park</td>
          <td>Trail</td>
          <td>Playground</td>
          <td>Building</td>
          <td>Women's Store</td>
          <td>Department Store</td>
          <td>Dessert Shop</td>
          <td>Dim Sum Restaurant</td>
          <td>Diner</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>71</th>
          <td>York</td>
          <td>4.0</td>
          <td>Trail</td>
          <td>Park</td>
          <td>Field</td>
          <td>Hockey Arena</td>
          <td>Women's Store</td>
          <td>Department Store</td>
          <td>Dessert Shop</td>
          <td>Dim Sum Restaurant</td>
          <td>Diner</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>72</th>
          <td>York</td>
          <td>4.0</td>
          <td>Park</td>
          <td>Women's Store</td>
          <td>Fast Food Restaurant</td>
          <td>Market</td>
          <td>Department Store</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
        </tr>
        <tr>
          <th>77</th>
          <td>NorthYork</td>
          <td>4.0</td>
          <td>Park</td>
          <td>Construction &amp; Landscaping</td>
          <td>Basketball Court</td>
          <td>Bakery</td>
          <td>Women's Store</td>
          <td>Dessert Shop</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
        </tr>
        <tr>
          <th>79</th>
          <td>York</td>
          <td>4.0</td>
          <td>Pizza Place</td>
          <td>Bus Line</td>
          <td>Convenience Store</td>
          <td>Grocery Store</td>
          <td>Gluten-free Restaurant</td>
          <td>Gift Shop</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>88</th>
          <td>Etobicoke</td>
          <td>4.0</td>
          <td>Park</td>
          <td>Smoke Shop</td>
          <td>River</td>
          <td>Women's Store</td>
          <td>Dance Studio</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>89</th>
          <td>Etobicoke</td>
          <td>4.0</td>
          <td>Business Service</td>
          <td>Park</td>
          <td>Baseball Field</td>
          <td>Deli / Bodega</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>94</th>
          <td>York</td>
          <td>4.0</td>
          <td>Convenience Store</td>
          <td>Women's Store</td>
          <td>Deli / Bodega</td>
          <td>Ethiopian Restaurant</td>
          <td>Empanada Restaurant</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
        <tr>
          <th>96</th>
          <td>Etobicoke</td>
          <td>4.0</td>
          <td>Pizza Place</td>
          <td>Park</td>
          <td>Bus Line</td>
          <td>Mobile Phone Shop</td>
          <td>Deli / Bodega</td>
          <td>Electronics Store</td>
          <td>Eastern European Restaurant</td>
          <td>Dumpling Restaurant</td>
          <td>Drugstore</td>
          <td>Dog Run</td>
        </tr>
      </tbody>
    </table>
    </div>



The segmentation and clustering is achieved
