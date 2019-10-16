
# Data Wrangling
The data was downloaded onto an excel table. I imported the excel table to IBM Watson and I downloaded the required libraries to start cleaning up the data.


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python

import types
import pandas as pd
from botocore.client import Config
import ibm_boto3

def __iter__(self): return 0

#@hidden_cell
# The following code accesses a file in your IBM Cloud Object Storage. It includes your credentials.
# You might want to remove those credentials before you share the notebook.
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

```




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


```python
missing_data = df.isnull()
missing_data.head(3)
```




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




```python
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")
```

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
    


As we can see, there are 77 true values, indicating missing data, and per prompt requirement, these will be dropped from the Borough column


```python
df.dropna(subset=["Borough"], axis=0, inplace=True)

#reset the index

df.reset_index(drop=True, inplace=True)

df.head(12)
```




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


```python
df['Neighbourhood'].replace(np.nan, df['Borough'], inplace=True)
df.head(12)
```




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


```python
df_1= df.groupby('Postcode').agg(lambda x: ','.join(x))
```


```python
df_2=df_1.reset_index()
```

Within each Borough, there are multiple Postcodes and so we clean up the data frame to remove any repeats, so that each line has only one Postcode, one Borough, and all the Neighborhoods in that Borough and Postcode.


```python
df_2['Borough']= df_2['Borough'].str.replace('[{}\s]','').str.split(',').apply(set).str.join(',').str.strip(',').str.replace(",{2,}",",")
```


```python
df_2.head(12)
```




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




```python
df_2.shape
```




    (103, 3)



The data frame has 3 rows and 103 columns

# Geocoding
Using the CSV data to merge it to the cleaned table from the previous section. First examine what the data frame looks like


```python
filepath = "https://cocl.us/Geospatial_data"
df_3 = pd.read_csv('https://cocl.us/Geospatial_data')
df_3.head()
```




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



Rename the field "Postal Code" to Postcode to match the previous section, and merge the two data sets to get the required data frame.


```python
df_3.rename(columns={'Postal Code': 'Postcode'}, inplace=True)
df_4 = pd.merge(df_3, df_2, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)

df_4.head()
```




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



Then we fix the column order to have Latitude and Longitude as the last two columns, then assign them to the data frame.


```python
column_order = ['Postcode',
 'Borough',
 'Neighbourhood',
 'Latitude',
 'Longitude']
df_5=df_4[column_order]
df_5.head()
```




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



# Visualization and Clustering
First we import some required libraries


```python
!conda install -c conda-forge geopy --yes
from geopy.geocoders import Nominatim
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.cluster import KMeans
!conda install -c conda-forge folium=0.5.0 --yes
import folium
print('Libraries imported.')
```

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


```python
address = 'Toronto, Ontario'

geolocator = Nominatim(user_agent="TO_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Toronto, Ontario are {}, {}.'.format(latitude, longitude))
```

    The geograpical coordinate of Toronto, Ontario are 43.653963, -79.387207.


Now we show the map of Toronto with the neighborhoods as markers


```python
map_toronto = folium.Map(location=[latitude, longitude], zoom_start=10)

for lat, lng, borough, neighbourhood in zip(df_5['Latitude'], df_5['Longitude'], df_5['Borough'], df_5['Neighbourhood']):
    label = '{}, {}'.format(neighbourhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=4,
        popup=label,
        color='magenta',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)  
    
map_toronto
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMiA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMicsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDMuNjUzOTYzLC03OS4zODcyMDddLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTAsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzAzZDRmMjgzMjg2NTQyNTU4N2VjMjU3NWM1ZGY2ZTgzID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICJtYXhab29tIjogMTgsCiAgIm1pblpvb20iOiAxLAogICJub1dyYXAiOiBmYWxzZSwKICAic3ViZG9tYWlucyI6ICJhYmMiCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82NzE5ZTA1NjZjMjQ0YzAwYWNiMjZiMTZmYzg1MTkxYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjgwNjY4NjI5OTk5OTk5NiwtNzkuMTk0MzUzNDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjJhOWQwYmUyODhkNDRhNjgxZjRiOWRjZWMzOTRhNTUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzZlY2Q5YjA5ZmNkNGZlMmIxMDA4YzQ4YTJhY2Y0Y2YgPSAkKCc8ZGl2IGlkPSJodG1sXzc2ZWNkOWIwOWZjZDRmZTJiMTAwOGM0OGEyYWNmNGNmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3VnZSxNYWx2ZXJuLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjJhOWQwYmUyODhkNDRhNjgxZjRiOWRjZWMzOTRhNTUuc2V0Q29udGVudChodG1sXzc2ZWNkOWIwOWZjZDRmZTJiMTAwOGM0OGEyYWNmNGNmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzY3MTllMDU2NmMyNDRjMDBhY2IyNmIxNmZjODUxOTFjLmJpbmRQb3B1cChwb3B1cF82MmE5ZDBiZTI4OGQ0NGE2ODFmNGI5ZGNlYzM5NGE1NSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mZGQ1OWQyNWU4OWE0MzI3YmFjZTVjMmZhODJkNDM3NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4NDUzNTEsLTc5LjE2MDQ5NzA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NjODU0NzdjM2I5ZTRjOTlhMGMyZGQ1YzBmOTkzNThiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JhYTAwOWU0YzZjYjQ3ZjQ5NGQ0YzJiZmM2ZjNmMTI0ID0gJCgnPGRpdiBpZD0iaHRtbF9iYWEwMDllNGM2Y2I0N2Y0OTRkNGMyYmZjNmYzZjEyNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaGxhbmQgQ3JlZWssUm91Z2UgSGlsbCxQb3J0IFVuaW9uLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfY2M4NTQ3N2MzYjllNGM5OWEwYzJkZDVjMGY5OTM1OGIuc2V0Q29udGVudChodG1sX2JhYTAwOWU0YzZjYjQ3ZjQ5NGQ0YzJiZmM2ZjNmMTI0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZkZDU5ZDI1ZTg5YTQzMjdiYWNlNWMyZmE4MmQ0Mzc3LmJpbmRQb3B1cChwb3B1cF9jYzg1NDc3YzNiOWU0Yzk5YTBjMmRkNWMwZjk5MzU4Yik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82YTJjNDY2NzU5MDY0ZDViODQ5OGE0OGZjMDI5Nzg2YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc2MzU3MjYsLTc5LjE4ODcxMTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNGRiNzg5Nzk4ZWFkNGY5OWFiYWZmNGUyYTZkMTMxYTUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTRlNWQxZjlhNTYwNDYwMjk2MGM0YThiNzg1NTEzZjYgPSAkKCc8ZGl2IGlkPSJodG1sXzk0ZTVkMWY5YTU2MDQ2MDI5NjBjNGE4Yjc4NTUxM2Y2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HdWlsZHdvb2QsTW9ybmluZ3NpZGUsV2VzdCBIaWxsLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNGRiNzg5Nzk4ZWFkNGY5OWFiYWZmNGUyYTZkMTMxYTUuc2V0Q29udGVudChodG1sXzk0ZTVkMWY5YTU2MDQ2MDI5NjBjNGE4Yjc4NTUxM2Y2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZhMmM0NjY3NTkwNjRkNWI4NDk4YTQ4ZmMwMjk3ODZhLmJpbmRQb3B1cChwb3B1cF80ZGI3ODk3OThlYWQ0Zjk5YWJhZmY0ZTJhNmQxMzFhNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zZTBlZDBlMDU5MzU0OTk4YWQ1OGVkN2RhMDRmNjFiYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MDk5MjEsLTc5LjIxNjkxNzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U2MWZlMzQxM2E4NjRmNDk5OThjYTQzNTA2ZjkwM2FiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI4MWRhYTU4ODI5YTQ5YmNhODAwNjU1Y2FlNGRmNjQwID0gJCgnPGRpdiBpZD0iaHRtbF8yODFkYWE1ODgyOWE0OWJjYTgwMDY1NWNhZTRkZjY0MCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V29idXJuLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTYxZmUzNDEzYTg2NGY0OTk5OGNhNDM1MDZmOTAzYWIuc2V0Q29udGVudChodG1sXzI4MWRhYTU4ODI5YTQ5YmNhODAwNjU1Y2FlNGRmNjQwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNlMGVkMGUwNTkzNTQ5OThhZDU4ZWQ3ZGEwNGY2MWJiLmJpbmRQb3B1cChwb3B1cF9lNjFmZTM0MTNhODY0ZjQ5OTk4Y2E0MzUwNmY5MDNhYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wYjgzNmI4OTEyOWE0M2YwYjVhODdhOGRhN2I1OTY5MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MzEzNiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWQ2NTkwNmE0NTFhNGUzMThiODg4YzVjNDM1NjY1YzggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGFlYjhmMDI5NWQ0NDA3MDlkZTc2ZThmYzFmNzk4OTkgPSAkKCc8ZGl2IGlkPSJodG1sXzhhZWI4ZjAyOTVkNDQwNzA5ZGU3NmU4ZmMxZjc5ODk5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZWRhcmJyYWUsIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xZDY1OTA2YTQ1MWE0ZTMxOGI4ODhjNWM0MzU2NjVjOC5zZXRDb250ZW50KGh0bWxfOGFlYjhmMDI5NWQ0NDA3MDlkZTc2ZThmYzFmNzk4OTkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMGI4MzZiODkxMjlhNDNmMGI1YTg3YThkYTdiNTk2OTEuYmluZFBvcHVwKHBvcHVwXzFkNjU5MDZhNDUxYTRlMzE4Yjg4OGM1YzQzNTY2NWM4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI1ZjcwNDk5YjkzYjRhMDE4MDc4MDY1YzAwZGZkYzBjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ0NzM0MiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTkyMmViZjE1ZDVjNDk4ZWI3ZmIzNzBhYjE0ZTZlNDMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2ZiNzlkMzY1MTFkNDk1MjkyOThlNWEwYmY3MmEzNDMgPSAkKCc8ZGl2IGlkPSJodG1sXzdmYjc5ZDM2NTExZDQ5NTI5Mjk4ZTVhMGJmNzJhMzQzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TY2FyYm9yb3VnaCBWaWxsYWdlLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTkyMmViZjE1ZDVjNDk4ZWI3ZmIzNzBhYjE0ZTZlNDMuc2V0Q29udGVudChodG1sXzdmYjc5ZDM2NTExZDQ5NTI5Mjk4ZTVhMGJmNzJhMzQzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzI1ZjcwNDk5YjkzYjRhMDE4MDc4MDY1YzAwZGZkYzBjLmJpbmRQb3B1cChwb3B1cF9lOTIyZWJmMTVkNWM0OThlYjdmYjM3MGFiMTRlNmU0Myk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lMmZhNmFjNDMxOTk0Y2NmOWE0OWY3NWFhZjM4ZmRkYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNzkyOTIsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzlkODI3ODY0NWUxNzQxZTZiZjRjNTYxNzkyM2I4MzA0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzM0MGFjZDEzYTllYjQ5YTg5Nzc3ODlmMjVjYzIwZDNkID0gJCgnPGRpdiBpZD0iaHRtbF8zNDBhY2QxM2E5ZWI0OWE4OTc3Nzg5ZjI1Y2MyMGQzZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdCBCaXJjaG1vdW50IFBhcmssSW9udmlldyxLZW5uZWR5IFBhcmssIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85ZDgyNzg2NDVlMTc0MWU2YmY0YzU2MTc5MjNiODMwNC5zZXRDb250ZW50KGh0bWxfMzQwYWNkMTNhOWViNDlhODk3Nzc4OWYyNWNjMjBkM2QpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTJmYTZhYzQzMTk5NGNjZjlhNDlmNzVhYWYzOGZkZGIuYmluZFBvcHVwKHBvcHVwXzlkODI3ODY0NWUxNzQxZTZiZjRjNTYxNzkyM2I4MzA0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzgyZjZhMjBmZjUyMzQzNDQ4ZjU1ZWUzNmRlZTEzMDAzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzExMTExNzAwMDAwMDA0LC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RhMDliNzFlMmMxZTQ1MGY5ZjVkMWU3YWM3Y2ViYjRlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2RiOTM0ZDZmZmM0NzRlZDM5Y2Q0YmQyNzVmOThlYzlkID0gJCgnPGRpdiBpZD0iaHRtbF9kYjkzNGQ2ZmZjNDc0ZWQzOWNkNGJkMjc1Zjk4ZWM5ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2xhaXJsZWEsR29sZGVuIE1pbGUsT2FrcmlkZ2UsIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kYTA5YjcxZTJjMWU0NTBmOWY1ZDFlN2FjN2NlYmI0ZS5zZXRDb250ZW50KGh0bWxfZGI5MzRkNmZmYzQ3NGVkMzljZDRiZDI3NWY5OGVjOWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODJmNmEyMGZmNTIzNDM0NDhmNTVlZTM2ZGVlMTMwMDMuYmluZFBvcHVwKHBvcHVwX2RhMDliNzFlMmMxZTQ1MGY5ZjVkMWU3YWM3Y2ViYjRlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJhZDU4Njg3YTc4NjQ1Mzc4NDNjZWMwNjY1YTcyMWMyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE2MzE2LC03OS4yMzk0NzYwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kYjQzMzhkZjFmOWQ0NmM4YTk4YWIyNmZlNTdmNGQyNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNDNhMjNjMmE5ZWE0YmU1OGIyMjg1OTAzMzlhZWI0NCA9ICQoJzxkaXYgaWQ9Imh0bWxfMzQzYTIzYzJhOWVhNGJlNThiMjI4NTkwMzM5YWViNDQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsaWZmY3Jlc3QsQ2xpZmZzaWRlLFNjYXJib3JvdWdoIFZpbGxhZ2UgV2VzdCwgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RiNDMzOGRmMWY5ZDQ2YzhhOThhYjI2ZmU1N2Y0ZDI3LnNldENvbnRlbnQoaHRtbF8zNDNhMjNjMmE5ZWE0YmU1OGIyMjg1OTAzMzlhZWI0NCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yYWQ1ODY4N2E3ODY0NTM3ODQzY2VjMDY2NWE3MjFjMi5iaW5kUG9wdXAocG9wdXBfZGI0MzM4ZGYxZjlkNDZjOGE5OGFiMjZmZTU3ZjRkMjcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfM2I2ZDJhYTY3Nzk2NDk2ODhlNGI5NmZjMzgyYjFmMzYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTI2NTcwMDAwMDAwMDQsLTc5LjI2NDg0ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmFjNDY0ZDgyYjI0NDAzNTlmZTYwODU5MjlhNmI3ZjcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODk1MWJlYmVjNTQ1NDY0ZWJlMzlmMzFiYjkyNGYwNTUgPSAkKCc8ZGl2IGlkPSJodG1sXzg5NTFiZWJlYzU0NTQ2NGViZTM5ZjMxYmI5MjRmMDU1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CaXJjaCBDbGlmZixDbGlmZnNpZGUgV2VzdCwgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZhYzQ2NGQ4MmIyNDQwMzU5ZmU2MDg1OTI5YTZiN2Y3LnNldENvbnRlbnQoaHRtbF84OTUxYmViZWM1NDU0NjRlYmUzOWYzMWJiOTI0ZjA1NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zYjZkMmFhNjc3OTY0OTY4OGU0Yjk2ZmMzODJiMWYzNi5iaW5kUG9wdXAocG9wdXBfZmFjNDY0ZDgyYjI0NDAzNTlmZTYwODU5MjlhNmI3ZjcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzNmYzI4MDZkOTAwNDA1MGI4NmY1OGIyZTY0YzNlZjIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTc0MDk2LC03OS4yNzMzMDQwMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ZmM3YzJhOTI5MjY0NjhmOTM2NGE3OTU0YmI3MTVkNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iZjYzZGZjYjNiZTI0ZDAzOGNiOWM0MTk0YzE2YzNlZiA9ICQoJzxkaXYgaWQ9Imh0bWxfYmY2M2RmY2IzYmUyNGQwMzhjYjljNDE5NGMxNmMzZWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvcnNldCBQYXJrLFNjYXJib3JvdWdoIFRvd24gQ2VudHJlLFdleGZvcmQgSGVpZ2h0cywgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRmYzdjMmE5MjkyNjQ2OGY5MzY0YTc5NTRiYjcxNWQ3LnNldENvbnRlbnQoaHRtbF9iZjYzZGZjYjNiZTI0ZDAzOGNiOWM0MTk0YzE2YzNlZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83M2ZjMjgwNmQ5MDA0MDUwYjg2ZjU4YjJlNjRjM2VmMi5iaW5kUG9wdXAocG9wdXBfNGZjN2MyYTkyOTI2NDY4ZjkzNjRhNzk1NGJiNzE1ZDcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWZiZDJiMmFmMTU3NGNlODlhNjEwOTRlNzlhOWQ4MjIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTAwNzE1MDAwMDAwMDQsLTc5LjI5NTg0OTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTg3MTAyN2Y4Y2QxNDY5ZjkzMWI1YmNmMWU2MTUwMGQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTQ1YjI3NTA4ZDUzNDBhMGFhNzA0MjRlNTQwNzRkYTAgPSAkKCc8ZGl2IGlkPSJodG1sX2E0NWIyNzUwOGQ1MzQwYTBhYTcwNDI0ZTU0MDc0ZGEwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJ5dmFsZSxXZXhmb3JkLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTg3MTAyN2Y4Y2QxNDY5ZjkzMWI1YmNmMWU2MTUwMGQuc2V0Q29udGVudChodG1sX2E0NWIyNzUwOGQ1MzQwYTBhYTcwNDI0ZTU0MDc0ZGEwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFmYmQyYjJhZjE1NzRjZTg5YTYxMDk0ZTc5YTlkODIyLmJpbmRQb3B1cChwb3B1cF85ODcxMDI3ZjhjZDE0NjlmOTMxYjViY2YxZTYxNTAwZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jMmE3NjIyMzQzNmM0YmQzYTFhZmQ0NGVhYTcxZjI0MyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5NDIwMDMsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2FjNTE5OTc2YzllMzQ3MjhiY2UzNTFiNWJjNDc1NzZlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI2MDc2NmYzYjc2MTQ3YjFiMWM4MDYxOGNjZWE0MzMxID0gJCgnPGRpdiBpZD0iaHRtbF8yNjA3NjZmM2I3NjE0N2IxYjFjODA2MThjY2VhNDMzMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0LCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWM1MTk5NzZjOWUzNDcyOGJjZTM1MWI1YmM0NzU3NmUuc2V0Q29udGVudChodG1sXzI2MDc2NmYzYjc2MTQ3YjFiMWM4MDYxOGNjZWE0MzMxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2MyYTc2MjIzNDM2YzRiZDNhMWFmZDQ0ZWFhNzFmMjQzLmJpbmRQb3B1cChwb3B1cF9hYzUxOTk3NmM5ZTM0NzI4YmNlMzUxYjViYzQ3NTc2ZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wNzNkMjA2MDBiNmM0NTA3YmVmOTdhOWQ0YjhlOWUyNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4MTYzNzUsLTc5LjMwNDMwMjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWVkZjcyYjFiNjA1NGVhOWJhMzg1NjcxNjFiMjlhYWUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjljMjYyNDQxMTMxNGJmYWE0NDc1NDU2YWEwZmEzNWEgPSAkKCc8ZGl2IGlkPSJodG1sXzY5YzI2MjQ0MTEzMTRiZmFhNDQ3NTQ1NmFhMGZhMzVhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGFya3MgQ29ybmVycyxTdWxsaXZhbixUYW0gTyYjMzk7U2hhbnRlciwgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVlZGY3MmIxYjYwNTRlYTliYTM4NTY3MTYxYjI5YWFlLnNldENvbnRlbnQoaHRtbF82OWMyNjI0NDExMzE0YmZhYTQ0NzU0NTZhYTBmYTM1YSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wNzNkMjA2MDBiNmM0NTA3YmVmOTdhOWQ0YjhlOWUyNS5iaW5kUG9wdXAocG9wdXBfNWVkZjcyYjFiNjA1NGVhOWJhMzg1NjcxNjFiMjlhYWUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTEzMWQwNTNiN2RmNDI1Y2JmYTA0NzAxZThkYjYyOTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My44MTUyNTIyLC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk3N2JmMjkxYjc0OTQzNDRiYjljOTJhNDVjOTA5ZTEyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzdlOWIwMWY4OTFlNjQzMjFiZTEwNzc1N2Q1NWQxODhjID0gJCgnPGRpdiBpZD0iaHRtbF83ZTliMDFmODkxZTY0MzIxYmUxMDc3NTdkNTVkMTg4YyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0IE5vcnRoLEwmIzM5O0Ftb3JlYXV4IEVhc3QsTWlsbGlrZW4sU3RlZWxlcyBFYXN0LCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTc3YmYyOTFiNzQ5NDM0NGJiOWM5MmE0NWM5MDllMTIuc2V0Q29udGVudChodG1sXzdlOWIwMWY4OTFlNjQzMjFiZTEwNzc1N2Q1NWQxODhjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UxMzFkMDUzYjdkZjQyNWNiZmEwNDcwMWU4ZGI2MjkzLmJpbmRQb3B1cChwb3B1cF85NzdiZjI5MWI3NDk0MzQ0YmI5YzkyYTQ1YzkwOWUxMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82ZWQyNzYwNTE1NDk0MzNhOGNjZjQxYmU4MmRlMDMwZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5OTUyNTIwMDAwMDAwNSwtNzkuMzE4Mzg4N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ZGM5ZmZjYWM3ZDM0MmRlYTcxYWYwMmIzOGMzNGViMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80NjFiMTg1OTM2ZDU0ZWM3YjMyNjA1YjYyYTMyNWJjYiA9ICQoJzxkaXYgaWQ9Imh0bWxfNDYxYjE4NTkzNmQ1NGVjN2IzMjYwNWI2MmEzMjViY2IiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkwmIzM5O0Ftb3JlYXV4IFdlc3QsIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80ZGM5ZmZjYWM3ZDM0MmRlYTcxYWYwMmIzOGMzNGViMC5zZXRDb250ZW50KGh0bWxfNDYxYjE4NTkzNmQ1NGVjN2IzMjYwNWI2MmEzMjViY2IpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmVkMjc2MDUxNTQ5NDMzYThjY2Y0MWJlODJkZTAzMGUuYmluZFBvcHVwKHBvcHVwXzRkYzlmZmNhYzdkMzQyZGVhNzFhZjAyYjM4YzM0ZWIwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q5ZTBiZjdlZmUyMDRhYTNhYjQ1NDcyNzQ3Y2Y5YWU3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuODM2MTI0NzAwMDAwMDA2LC03OS4yMDU2MzYwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84ZDQ0NzhkMDAzMGU0MGY0YmI1ZjEzZTZhYTU4YTMyNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84NDZiZjc5NjhmMmI0OWRlYjZhNDk4OGU0MzE2NjM0NiA9ICQoJzxkaXYgaWQ9Imh0bWxfODQ2YmY3OTY4ZjJiNDlkZWI2YTQ5ODhlNDMxNjYzNDYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlVwcGVyIFJvdWdlLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGQ0NDc4ZDAwMzBlNDBmNGJiNWYxM2U2YWE1OGEzMjUuc2V0Q29udGVudChodG1sXzg0NmJmNzk2OGYyYjQ5ZGViNmE0OTg4ZTQzMTY2MzQ2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q5ZTBiZjdlZmUyMDRhYTNhYjQ1NDcyNzQ3Y2Y5YWU3LmJpbmRQb3B1cChwb3B1cF84ZDQ0NzhkMDAzMGU0MGY0YmI1ZjEzZTZhYTU4YTMyNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yNTgxNzg1NWQ0ZWY0ODgxYjViNzE2YzE1ZjUyNzIxZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjgwMzc2MjIsLTc5LjM2MzQ1MTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjMxMzUyOGFjNWJlNDk2ZWJlYWRkN2YxYzUxYjcwMWUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYzQ5MmJjMzJmMjFlNDdmODlkODE1ZjBjNDhkMTMyYTggPSAkKCc8ZGl2IGlkPSJodG1sX2M0OTJiYzMyZjIxZTQ3Zjg5ZDgxNWYwYzQ4ZDEzMmE4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IaWxsY3Jlc3QgVmlsbGFnZSwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yMzEzNTI4YWM1YmU0OTZlYmVhZGQ3ZjFjNTFiNzAxZS5zZXRDb250ZW50KGh0bWxfYzQ5MmJjMzJmMjFlNDdmODlkODE1ZjBjNDhkMTMyYTgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjU4MTc4NTVkNGVmNDg4MWI1YjcxNmMxNWY1MjcyMWQuYmluZFBvcHVwKHBvcHVwXzIzMTM1MjhhYzViZTQ5NmViZWFkZDdmMWM1MWI3MDFlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzg1YmFlZDM0ZGZjZjQzMGRiNjQyN2ViZDRiZjhlNTJhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzc4NTE3NSwtNzkuMzQ2NTU1N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81ZTA3MWViYjkyYTk0ZDgwOGIyNjZjYmNiNDY5YmMwZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mNTliODE5NzNmMjU0YmVhOWJkMmI5M2JmOTE2MDM5ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfZjU5YjgxOTczZjI1NGJlYTliZDJiOTNiZjkxNjAzOWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZhaXJ2aWV3LEhlbnJ5IEZhcm0sT3Jpb2xlLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVlMDcxZWJiOTJhOTRkODA4YjI2NmNiY2I0NjliYzBlLnNldENvbnRlbnQoaHRtbF9mNTliODE5NzNmMjU0YmVhOWJkMmI5M2JmOTE2MDM5ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84NWJhZWQzNGRmY2Y0MzBkYjY0MjdlYmQ0YmY4ZTUyYS5iaW5kUG9wdXAocG9wdXBfNWUwNzFlYmI5MmE5NGQ4MDhiMjY2Y2JjYjQ2OWJjMGUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjFhOWVhOTdmMDQ1NDIxNTkyMjEwNDVmY2QwNWVjZGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43ODY5NDczLC03OS4zODU5NzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWFkYjk3NWFmMjFlNGM5YzhjYjdmMzc3Mjk3YmI4MWQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2FmODNlNzUzZDk5NGIxOTg3MWZjOWIwNDIxYzM3NDYgPSAkKCc8ZGl2IGlkPSJodG1sX2NhZjgzZTc1M2Q5OTRiMTk4NzFmYzliMDQyMWMzNzQ2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXl2aWV3IFZpbGxhZ2UsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWFkYjk3NWFmMjFlNGM5YzhjYjdmMzc3Mjk3YmI4MWQuc2V0Q29udGVudChodG1sX2NhZjgzZTc1M2Q5OTRiMTk4NzFmYzliMDQyMWMzNzQ2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzIxYTllYTk3ZjA0NTQyMTU5MjIxMDQ1ZmNkMDVlY2RmLmJpbmRQb3B1cChwb3B1cF9hYWRiOTc1YWYyMWU0YzljOGNiN2YzNzcyOTdiYjgxZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ODQ0M2VhZTRkOGE0NGE0YjJiMDBiYzNjYzM1M2MyNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1NzQ5MDIsLTc5LjM3NDcxNDA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk4MzFmMmFkZWNhYjQ1NWViOTMxODEyZmFkNGM5MjM2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzcxMWVlYjZkZDM2ZTRhMGI5YmQ5MzA2ZjM1YjI0OTM5ID0gJCgnPGRpdiBpZD0iaHRtbF83MTFlZWI2ZGQzNmU0YTBiOWJkOTMwNmYzNWIyNDkzOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U2lsdmVyIEhpbGxzLFlvcmsgTWlsbHMsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTgzMWYyYWRlY2FiNDU1ZWI5MzE4MTJmYWQ0YzkyMzYuc2V0Q29udGVudChodG1sXzcxMWVlYjZkZDM2ZTRhMGI5YmQ5MzA2ZjM1YjI0OTM5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc4NDQzZWFlNGQ4YTQ0YTRiMmIwMGJjM2NjMzUzYzI2LmJpbmRQb3B1cChwb3B1cF85ODMxZjJhZGVjYWI0NTVlYjkzMTgxMmZhZDRjOTIzNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81MDc4ZTgwMTg0NDk0N2NjOWZjZWU1OWEzZWNiMmQ0MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4OTA1MywtNzkuNDA4NDkyNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWY2YWE1N2EyZGFkNGRhYWJjZjA3OTM5ZmZlODhmODEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGNhOGRhZGJlMDBhNGM5MzgwN2Y0N2RmZDNkZjEzNzYgPSAkKCc8ZGl2IGlkPSJodG1sXzRjYThkYWRiZTAwYTRjOTM4MDdmNDdkZmQzZGYxMzc2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5OZXd0b25icm9vayxXaWxsb3dkYWxlLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVmNmFhNTdhMmRhZDRkYWFiY2YwNzkzOWZmZTg4ZjgxLnNldENvbnRlbnQoaHRtbF80Y2E4ZGFkYmUwMGE0YzkzODA3ZjQ3ZGZkM2RmMTM3Nik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81MDc4ZTgwMTg0NDk0N2NjOWZjZWU1OWEzZWNiMmQ0MS5iaW5kUG9wdXAocG9wdXBfNWY2YWE1N2EyZGFkNGRhYWJjZjA3OTM5ZmZlODhmODEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTU4MTRhOTM4MmJlNDg1Yjk4NDUxNjlmZjBmODEzNGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NzAxMTk5LC03OS40MDg0OTI3OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80MTI4MzJjY2I5YTE0OWUwODJkZmY1MmQzNmRmZWQzOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mNmNiMDQ3ZmFhM2U0MmNlYTFhOTBlNTZmNGFkYjhhNCA9ICQoJzxkaXYgaWQ9Imh0bWxfZjZjYjA0N2ZhYTNlNDJjZWExYTkwZTU2ZjRhZGI4YTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxvd2RhbGUgU291dGgsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDEyODMyY2NiOWExNDllMDgyZGZmNTJkMzZkZmVkMzkuc2V0Q29udGVudChodG1sX2Y2Y2IwNDdmYWEzZTQyY2VhMWE5MGU1NmY0YWRiOGE0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2E1ODE0YTkzODJiZTQ4NWI5ODQ1MTY5ZmYwZjgxMzRiLmJpbmRQb3B1cChwb3B1cF80MTI4MzJjY2I5YTE0OWUwODJkZmY1MmQzNmRmZWQzOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84YjQ3OWU2MmQ2YmI0OGQ3ODVjZDE3NGI5Mzk1ZjU0YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1Mjc1ODI5OTk5OTk5NiwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMDFmMDAyMDBmNWY0MmU4YjFhM2E1OTViZWMyMGYxNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kNjVlYzVkYzFlZTU0MGViYTY5OWQyOGI3Y2E3OTA3MyA9ICQoJzxkaXYgaWQ9Imh0bWxfZDY1ZWM1ZGMxZWU1NDBlYmE2OTlkMjhiN2NhNzkwNzMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPllvcmsgTWlsbHMgV2VzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mMDFmMDAyMDBmNWY0MmU4YjFhM2E1OTViZWMyMGYxNi5zZXRDb250ZW50KGh0bWxfZDY1ZWM1ZGMxZWU1NDBlYmE2OTlkMjhiN2NhNzkwNzMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGI0NzllNjJkNmJiNDhkNzg1Y2QxNzRiOTM5NWY1NGMuYmluZFBvcHVwKHBvcHVwX2YwMWYwMDIwMGY1ZjQyZThiMWEzYTU5NWJlYzIwZjE2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UxOWFkMGZhN2Y4NTQzY2ZhZTczOWZkNTEzODA5M2ZlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzgyNzM2NCwtNzkuNDQyMjU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zZTM3MzQxMzNiMjU0YWI1ODE1MDMxOGZjNjU0NzE2YiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84NDYzMjBjZTY1NzM0NGJiOTIwZGU3YmRlZTI2YzkyOSA9ICQoJzxkaXYgaWQ9Imh0bWxfODQ2MzIwY2U2NTczNDRiYjkyMGRlN2JkZWUyNmM5MjkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxvd2RhbGUgV2VzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zZTM3MzQxMzNiMjU0YWI1ODE1MDMxOGZjNjU0NzE2Yi5zZXRDb250ZW50KGh0bWxfODQ2MzIwY2U2NTczNDRiYjkyMGRlN2JkZWUyNmM5MjkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTE5YWQwZmE3Zjg1NDNjZmFlNzM5ZmQ1MTM4MDkzZmUuYmluZFBvcHVwKHBvcHVwXzNlMzczNDEzM2IyNTRhYjU4MTUwMzE4ZmM2NTQ3MTZiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzViOWVkNmYxOWM1MDQ1ZTNhMjFiY2M0NWJjNTJiZjg2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzUzMjU4NiwtNzkuMzI5NjU2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iOTZiNGViZjEzYzc0YzMzYTlmZWI0YTA3N2I2ZGJhYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lNThmNDcyNjk4MWY0NDUyOWE3NjNhZTMzMDgzZmI0ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfZTU4ZjQ3MjY5ODFmNDQ1MjlhNzYzYWUzMzA4M2ZiNGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBhcmt3b29kcywgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iOTZiNGViZjEzYzc0YzMzYTlmZWI0YTA3N2I2ZGJhYi5zZXRDb250ZW50KGh0bWxfZTU4ZjQ3MjY5ODFmNDQ1MjlhNzYzYWUzMzA4M2ZiNGYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNWI5ZWQ2ZjE5YzUwNDVlM2EyMWJjYzQ1YmM1MmJmODYuYmluZFBvcHVwKHBvcHVwX2I5NmI0ZWJmMTNjNzRjMzNhOWZlYjRhMDc3YjZkYmFiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk4ZGE5ZTkyYjUxNjRmMjY5NzEzZTc0YmI0YzQ3ZWU3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ1OTA1Nzk5OTk5OTk2LC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjFlYTIyYjM3YTE4NDBlNGEzMGU3N2ViMWQzYTE3NjggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDgwYTkzYzJmMTVjNGM5MGJiN2VmNmEzYTBlYjc3MmMgPSAkKCc8ZGl2IGlkPSJodG1sXzQ4MGE5M2MyZjE1YzRjOTBiYjdlZjZhM2EwZWI3NzJjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb24gTWlsbHMgTm9ydGgsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjFlYTIyYjM3YTE4NDBlNGEzMGU3N2ViMWQzYTE3Njguc2V0Q29udGVudChodG1sXzQ4MGE5M2MyZjE1YzRjOTBiYjdlZjZhM2EwZWI3NzJjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk4ZGE5ZTkyYjUxNjRmMjY5NzEzZTc0YmI0YzQ3ZWU3LmJpbmRQb3B1cChwb3B1cF82MWVhMjJiMzdhMTg0MGU0YTMwZTc3ZWIxZDNhMTc2OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84YTZjNzEzMzdkM2E0ZTQzOTY5NjdhYmU3Mjg1OWQzMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNTg5OTcwMDAwMDAxLC03OS4zNDA5MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTEwMjJiY2ZhYTY3NGQ3NWExNDI1ODVjYTdkNWM5YjMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzNlZDVlYTQ2NDg0NDZmNjgxMWExYzgxYmI5MzhiNGYgPSAkKCc8ZGl2IGlkPSJodG1sXzczZWQ1ZWE0NjQ4NDQ2ZjY4MTFhMWM4MWJiOTM4YjRmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GbGVtaW5nZG9uIFBhcmssRG9uIE1pbGxzIFNvdXRoLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzUxMDIyYmNmYWE2NzRkNzVhMTQyNTg1Y2E3ZDVjOWIzLnNldENvbnRlbnQoaHRtbF83M2VkNWVhNDY0ODQ0NmY2ODExYTFjODFiYjkzOGI0Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84YTZjNzEzMzdkM2E0ZTQzOTY5NjdhYmU3Mjg1OWQzMS5iaW5kUG9wdXAocG9wdXBfNTEwMjJiY2ZhYTY3NGQ3NWExNDI1ODVjYTdkNWM5YjMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmRjNjczMDRlMjFlNDAwYTgzY2MwZDFlNmUzNzZkMTYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTQzMjgzLC03OS40NDIyNTkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzM5ZDcxMDAzZDNmMzQ5OGQ4NzQ4ZjBhMzIzNGNkZDZjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzMzMGI2YmQ5NWQ0MDQ0ZjI5NjEwYWY1OTkzMmNkOTkyID0gJCgnPGRpdiBpZD0iaHRtbF8zMzBiNmJkOTVkNDA0NGYyOTYxMGFmNTk5MzJjZDk5MiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmF0aHVyc3QgTWFub3IsRG93bnN2aWV3IE5vcnRoLFdpbHNvbiBIZWlnaHRzLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzM5ZDcxMDAzZDNmMzQ5OGQ4NzQ4ZjBhMzIzNGNkZDZjLnNldENvbnRlbnQoaHRtbF8zMzBiNmJkOTVkNDA0NGYyOTYxMGFmNTk5MzJjZDk5Mik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iZGM2NzMwNGUyMWU0MDBhODNjYzBkMWU2ZTM3NmQxNi5iaW5kUG9wdXAocG9wdXBfMzlkNzEwMDNkM2YzNDk4ZDg3NDhmMGEzMjM0Y2RkNmMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmFmMDY3YjY2MTFhNGRjMjk3YTg1M2Y3M2RjODUyZTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Njc5ODAzLC03OS40ODcyNjE5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ODFlNWY2YzNiYzA0MGU5YWZhNDk5MDA0ZWYxOTIyMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zYzljNjViMzExNDM0NGU1Yjg2Y2M2NzRlMjZhZjA4NCA9ICQoJzxkaXYgaWQ9Imh0bWxfM2M5YzY1YjMxMTQzNDRlNWI4NmNjNjc0ZTI2YWYwODQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vcnRod29vZCBQYXJrLFlvcmsgVW5pdmVyc2l0eSwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80ODFlNWY2YzNiYzA0MGU5YWZhNDk5MDA0ZWYxOTIyMy5zZXRDb250ZW50KGh0bWxfM2M5YzY1YjMxMTQzNDRlNWI4NmNjNjc0ZTI2YWYwODQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmFmMDY3YjY2MTFhNGRjMjk3YTg1M2Y3M2RjODUyZTEuYmluZFBvcHVwKHBvcHVwXzQ4MWU1ZjZjM2JjMDQwZTlhZmE0OTkwMDRlZjE5MjIzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzcyZmE4MTczMWEzNTRlOTE4YTBhOTkwOWY0NzhkMTFlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzM3NDczMjAwMDAwMDA0LC03OS40NjQ3NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yNWIzODMxMmNkZjI0OWYzODNjM2JkYWQxMTZlNzY3NSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wNjMyMmQyNzFhZGM0NDRiYmZmZGVlZjFjNmUyNTk4NyA9ICQoJzxkaXYgaWQ9Imh0bWxfMDYzMjJkMjcxYWRjNDQ0YmJmZmRlZWYxYzZlMjU5ODciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNGQiBUb3JvbnRvLERvd25zdmlldyBFYXN0LCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI1YjM4MzEyY2RmMjQ5ZjM4M2MzYmRhZDExNmU3Njc1LnNldENvbnRlbnQoaHRtbF8wNjMyMmQyNzFhZGM0NDRiYmZmZGVlZjFjNmUyNTk4Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83MmZhODE3MzFhMzU0ZTkxOGEwYTk5MDlmNDc4ZDExZS5iaW5kUG9wdXAocG9wdXBfMjViMzgzMTJjZGYyNDlmMzgzYzNiZGFkMTE2ZTc2NzUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDFkOTY2MjM2MTIwNDA4YWJkMDMzZmQyNDk4OGVhZDQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MzkwMTQ2LC03OS41MDY5NDM2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA0M2RiODFlMTMwZTQ3MDJiMDExNmJmNDE5OTkyMjRjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI5YjRlOTNmY2FhNTRiNzRiYWQ4ZThhNjZiNmEyMDkzID0gJCgnPGRpdiBpZD0iaHRtbF8yOWI0ZTkzZmNhYTU0Yjc0YmFkOGU4YTY2YjZhMjA5MyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IFdlc3QsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDQzZGI4MWUxMzBlNDcwMmIwMTE2YmY0MTk5OTIyNGMuc2V0Q29udGVudChodG1sXzI5YjRlOTNmY2FhNTRiNzRiYWQ4ZThhNjZiNmEyMDkzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2QxZDk2NjIzNjEyMDQwOGFiZDAzM2ZkMjQ5ODhlYWQ0LmJpbmRQb3B1cChwb3B1cF8wNDNkYjgxZTEzMGU0NzAyYjAxMTZiZjQxOTk5MjI0Yyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wNmY0NzE1MDNkOWU0N2NhODZlOGI3ZmY5NzM2OTVhNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyODQ5NjQsLTc5LjQ5NTY5NzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2E3ODA3YWJmZjQ5NDRmNjQ4NjY0ODE5Y2Q3ODc2Yjc0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzcwOWYyZDBmZDQzMzRkMmE4N2ZlNGE5ZWEwOWY4MTI5ID0gJCgnPGRpdiBpZD0iaHRtbF83MDlmMmQwZmQ0MzM0ZDJhODdmZTRhOWVhMDlmODEyOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IENlbnRyYWwsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTc4MDdhYmZmNDk0NGY2NDg2NjQ4MTljZDc4NzZiNzQuc2V0Q29udGVudChodG1sXzcwOWYyZDBmZDQzMzRkMmE4N2ZlNGE5ZWEwOWY4MTI5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzA2ZjQ3MTUwM2Q5ZTQ3Y2E4NmU4YjdmZjk3MzY5NWE2LmJpbmRQb3B1cChwb3B1cF9hNzgwN2FiZmY0OTQ0ZjY0ODY2NDgxOWNkNzg3NmI3NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hMjMyOTYwMzllMmY0YjFiYmFhODZhYmFlNGNlODRhNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc2MTYzMTMsLTc5LjUyMDk5OTQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U2ODUwYzExZWM2NDQzMTE4NDU1Y2JiOGJkNTNjZTgyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU0YTkxMGFmZWJlNDQ3ODNiNWE4ZTAxMmE5YmM0NTA2ID0gJCgnPGRpdiBpZD0iaHRtbF81NGE5MTBhZmViZTQ0NzgzYjVhOGUwMTJhOWJjNDUwNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IE5vcnRod2VzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lNjg1MGMxMWVjNjQ0MzExODQ1NWNiYjhiZDUzY2U4Mi5zZXRDb250ZW50KGh0bWxfNTRhOTEwYWZlYmU0NDc4M2I1YThlMDEyYTliYzQ1MDYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTIzMjk2MDM5ZTJmNGIxYmJhYTg2YWJhZTRjZTg0YTQuYmluZFBvcHVwKHBvcHVwX2U2ODUwYzExZWM2NDQzMTE4NDU1Y2JiOGJkNTNjZTgyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2QyNDk4ZmY4MWJmODRkMGE5ZDhmNmMxZjgxYjFiYWQ3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI1ODgyMjk5OTk5OTk1LC03OS4zMTU1NzE1OTk5OTk5OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNWFiMzAyOWFhZGY0YjIzOWVmNTYyOTMzMjAxOTJiYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81ZGMwNjRkZGNkNGY0ZDFjYWU3MDc4MWY4NmQ2NmY0ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfNWRjMDY0ZGRjZDRmNGQxY2FlNzA3ODFmODZkNjZmNGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlZpY3RvcmlhIFZpbGxhZ2UsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTVhYjMwMjlhYWRmNGIyMzllZjU2MjkzMzIwMTkyYmEuc2V0Q29udGVudChodG1sXzVkYzA2NGRkY2Q0ZjRkMWNhZTcwNzgxZjg2ZDY2ZjRmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2QyNDk4ZmY4MWJmODRkMGE5ZDhmNmMxZjgxYjFiYWQ3LmJpbmRQb3B1cChwb3B1cF9hNWFiMzAyOWFhZGY0YjIzOWVmNTYyOTMzMjAxOTJiYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNTlkOWI5OGE5YTc0ZDZkODMzNzE0OGM4NDBlZDk4YiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcwNjM5NzIsLTc5LjMwOTkzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84ZDI0NDQyOTk3ZDQ0MDE0YTc2NWJjMGRkYjEyMTkyMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80MWNjOGU1MGRhYjY0NjQxYWVjZWRjMWVhOTdmNGQzYiA9ICQoJzxkaXYgaWQ9Imh0bWxfNDFjYzhlNTBkYWI2NDY0MWFlY2VkYzFlYTk3ZjRkM2IiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldvb2RiaW5lIEdhcmRlbnMsUGFya3ZpZXcgSGlsbCwgRWFzdFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhkMjQ0NDI5OTdkNDQwMTRhNzY1YmMwZGRiMTIxOTIxLnNldENvbnRlbnQoaHRtbF80MWNjOGU1MGRhYjY0NjQxYWVjZWRjMWVhOTdmNGQzYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xNTlkOWI5OGE5YTc0ZDZkODMzNzE0OGM4NDBlZDk4Yi5iaW5kUG9wdXAocG9wdXBfOGQyNDQ0Mjk5N2Q0NDAxNGE3NjViYzBkZGIxMjE5MjEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDA1MjM0OWE1ZWI4NDgyMWJlYjNkZjJhMzQ3ODZhODUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTUzNDM5MDAwMDAwMDUsLTc5LjMxODM4ODddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDE2NTI0NThlODVmNGRlNGI1YjQwZjMxZjY3OWRlODggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOWNjZmI0NTc5Mjc1NDI2MmI2NjQ4NjM3ZjI2ZjRjMmUgPSAkKCc8ZGl2IGlkPSJodG1sXzljY2ZiNDU3OTI3NTQyNjJiNjY0ODYzN2YyNmY0YzJlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Xb29kYmluZSBIZWlnaHRzLCBFYXN0WW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDE2NTI0NThlODVmNGRlNGI1YjQwZjMxZjY3OWRlODguc2V0Q29udGVudChodG1sXzljY2ZiNDU3OTI3NTQyNjJiNjY0ODYzN2YyNmY0YzJlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQwNTIzNDlhNWViODQ4MjFiZWIzZGYyYTM0Nzg2YTg1LmJpbmRQb3B1cChwb3B1cF8wMTY1MjQ1OGU4NWY0ZGU0YjViNDBmMzFmNjc5ZGU4OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zZWU3NTQ2NDdmNmI0MjkxYWQ5ODAwYTQzMmZmZGI4ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY3NjM1NzM5OTk5OTk5LC03OS4yOTMwMzEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y1ZjUyZTI0OTU4OTQwMzk5MGJiZTBmYTg4MjQ3OTg3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2IwODVmOTAzMjAyMjRjMmU5YWFjZTg0OTI3Y2VhNDY0ID0gJCgnPGRpdiBpZD0iaHRtbF9iMDg1ZjkwMzIwMjI0YzJlOWFhY2U4NDkyN2NlYTQ2NCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhlIEJlYWNoZXMsIEVhc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNWY1MmUyNDk1ODk0MDM5OTBiYmUwZmE4ODI0Nzk4Ny5zZXRDb250ZW50KGh0bWxfYjA4NWY5MDMyMDIyNGMyZTlhYWNlODQ5MjdjZWE0NjQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2VlNzU0NjQ3ZjZiNDI5MWFkOTgwMGE0MzJmZmRiOGQuYmluZFBvcHVwKHBvcHVwX2Y1ZjUyZTI0OTU4OTQwMzk5MGJiZTBmYTg4MjQ3OTg3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzgxNGYxNDk0MjEwZjRhOGQ4NWY5MWM2ZmNjNDY5OGRkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA5MDYwNCwtNzkuMzYzNDUxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80NTRhYzU2NTI2NWM0ZDNlODQyOWI0ZDVhZmUzMTg1YyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kZmEwMTIzMDE5ZDE0Mjg5YTFlNmZkNzk5ZGJkYmViMiA9ICQoJzxkaXYgaWQ9Imh0bWxfZGZhMDEyMzAxOWQxNDI4OWExZTZmZDc5OWRiZGJlYjIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxlYXNpZGUsIEVhc3RZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80NTRhYzU2NTI2NWM0ZDNlODQyOWI0ZDVhZmUzMTg1Yy5zZXRDb250ZW50KGh0bWxfZGZhMDEyMzAxOWQxNDI4OWExZTZmZDc5OWRiZGJlYjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODE0ZjE0OTQyMTBmNGE4ZDg1ZjkxYzZmY2M0Njk4ZGQuYmluZFBvcHVwKHBvcHVwXzQ1NGFjNTY1MjY1YzRkM2U4NDI5YjRkNWFmZTMxODVjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZkMTFkMjVhNDVkNDQ0MGJiNDk5YTkwY2U3MzU5NzA2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA1MzY4OSwtNzkuMzQ5MzcxOTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjIyMjIzMDE2ODg1NGUyZWI0NjlhOWM5MTg5YzNkZTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZThjNGRjYzhmNjkzNDM1NGEyMzMwZGVlNmNlMzg0Y2UgPSAkKCc8ZGl2IGlkPSJodG1sX2U4YzRkY2M4ZjY5MzQzNTRhMjMzMGRlZTZjZTM4NGNlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaG9ybmNsaWZmZSBQYXJrLCBFYXN0WW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjIyMjIzMDE2ODg1NGUyZWI0NjlhOWM5MTg5YzNkZTkuc2V0Q29udGVudChodG1sX2U4YzRkY2M4ZjY5MzQzNTRhMjMzMGRlZTZjZTM4NGNlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZkMTFkMjVhNDVkNDQ0MGJiNDk5YTkwY2U3MzU5NzA2LmJpbmRQb3B1cChwb3B1cF9iMjIyMjMwMTY4ODU0ZTJlYjQ2OWE5YzkxODljM2RlOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yOWNjMjgxMGZhMTc0NGM5OTk1YWM5OGU3YzBjNzNkNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY4NTM0NywtNzkuMzM4MTA2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82NjQ2MGU5OGU3NWM0MmQ1OGNjMmFhOTc1ZDMzNWMxNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83M2NkN2QxZWVlY2Q0ODMwOTdiMTNmZGJkN2ExODI5OCA9ICQoJzxkaXYgaWQ9Imh0bWxfNzNjZDdkMWVlZWNkNDgzMDk3YjEzZmRiZDdhMTgyOTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgVG9yb250bywgRWFzdFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzY2NDYwZTk4ZTc1YzQyZDU4Y2MyYWE5NzVkMzM1YzE3LnNldENvbnRlbnQoaHRtbF83M2NkN2QxZWVlY2Q0ODMwOTdiMTNmZGJkN2ExODI5OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yOWNjMjgxMGZhMTc0NGM5OTk1YWM5OGU3YzBjNzNkNC5iaW5kUG9wdXAocG9wdXBfNjY0NjBlOThlNzVjNDJkNThjYzJhYTk3NWQzMzVjMTcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjliMWMzOTA5OGY5NDdlNzlkN2UwMTdjOTY1MjMxYTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Nzk1NTcxLC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWFiNzM2YzJhMjBiNDFkNDliNTMyY2IyNjY4NWQxOTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGRiOTM4MDBiOWU3NGZkZjkxMjE3YmQwMzc5ZmY5OTkgPSAkKCc8ZGl2IGlkPSJodG1sXzhkYjkzODAwYjllNzRmZGY5MTIxN2JkMDM3OWZmOTk5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgRGFuZm9ydGggV2VzdCxSaXZlcmRhbGUsIEVhc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hYWI3MzZjMmEyMGI0MWQ0OWI1MzJjYjI2Njg1ZDE5OS5zZXRDb250ZW50KGh0bWxfOGRiOTM4MDBiOWU3NGZkZjkxMjE3YmQwMzc5ZmY5OTkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjliMWMzOTA5OGY5NDdlNzlkN2UwMTdjOTY1MjMxYTAuYmluZFBvcHVwKHBvcHVwX2FhYjczNmMyYTIwYjQxZDQ5YjUzMmNiMjY2ODVkMTk5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRmMGJjZDllM2ZmNjQwNjBiZTE0MzE2M2YzNGEyNWFiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY4OTk4NSwtNzkuMzE1NTcxNTk5OTk5OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWZlNjI3MjgwOGRiNGMwYjkzZWEwNDQyZDYyNTQyYTUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMmE5YTA4NGM2MjYzNDlkMjhhM2Q4ZGNjNGE5NTg1ZjUgPSAkKCc8ZGl2IGlkPSJodG1sXzJhOWEwODRjNjI2MzQ5ZDI4YTNkOGRjYzRhOTU4NWY1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgQmVhY2hlcyBXZXN0LEluZGlhIEJhemFhciwgRWFzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzlmZTYyNzI4MDhkYjRjMGI5M2VhMDQ0MmQ2MjU0MmE1LnNldENvbnRlbnQoaHRtbF8yYTlhMDg0YzYyNjM0OWQyOGEzZDhkY2M0YTk1ODVmNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80ZjBiY2Q5ZTNmZjY0MDYwYmUxNDMxNjNmMzRhMjVhYi5iaW5kUG9wdXAocG9wdXBfOWZlNjI3MjgwOGRiNGMwYjkzZWEwNDQyZDYyNTQyYTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGY0NzQzOGM4MzI5NGQzYWFkYmIxMTNhZmU0NTUyODUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTk1MjU1LC03OS4zNDA5MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZWI5ZDE5MTlkOGQ3NGRiYWI0NGUxMTg0MTc4NTNkM2IgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWQzMzBhYzM1Yzg1NDkyN2FkNzZhYjA2ZTQ5MjY5NWQgPSAkKCc8ZGl2IGlkPSJodG1sXzVkMzMwYWMzNWM4NTQ5MjdhZDc2YWIwNmU0OTI2OTVkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdHVkaW8gRGlzdHJpY3QsIEVhc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lYjlkMTkxOWQ4ZDc0ZGJhYjQ0ZTExODQxNzg1M2QzYi5zZXRDb250ZW50KGh0bWxfNWQzMzBhYzM1Yzg1NDkyN2FkNzZhYjA2ZTQ5MjY5NWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGY0NzQzOGM4MzI5NGQzYWFkYmIxMTNhZmU0NTUyODUuYmluZFBvcHVwKHBvcHVwX2ViOWQxOTE5ZDhkNzRkYmFiNDRlMTE4NDE3ODUzZDNiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RjYWIwODg5YjZlNTQ1OGRhM2U1YjFjYTM3ZjE3ZDE4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI4MDIwNSwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zYzk1NjUxNzEwYjY0YTlhOGU1ZDM1OTljMzdmMWZjZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85NjEzZGQ3YmRlYjY0ZDg3OGEwYTRlMjY3YjhlMDYyNiA9ICQoJzxkaXYgaWQ9Imh0bWxfOTYxM2RkN2JkZWI2NGQ4NzhhMGE0ZTI2N2I4ZTA2MjYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIFBhcmssIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zYzk1NjUxNzEwYjY0YTlhOGU1ZDM1OTljMzdmMWZjZC5zZXRDb250ZW50KGh0bWxfOTYxM2RkN2JkZWI2NGQ4NzhhMGE0ZTI2N2I4ZTA2MjYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGNhYjA4ODliNmU1NDU4ZGEzZTViMWNhMzdmMTdkMTguYmluZFBvcHVwKHBvcHVwXzNjOTU2NTE3MTBiNjRhOWE4ZTVkMzU5OWMzN2YxZmNkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZhYzM4NWM4M2UzNTRlZjNiMjBiODg2MGJjN2FiY2QwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzEyNzUxMSwtNzkuMzkwMTk3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yZTNmNzRiN2U4NWM0Y2M5ODEwNzczY2M2ZDU5YjFkYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zZjZhNTM3MDMzMTI0ODEwOGE3MTFjYTk2Yjc3NzU3ZCA9ICQoJzxkaXYgaWQ9Imh0bWxfM2Y2YTUzNzAzMzEyNDgxMDhhNzExY2E5NmI3Nzc1N2QiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUgTm9ydGgsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yZTNmNzRiN2U4NWM0Y2M5ODEwNzczY2M2ZDU5YjFkYi5zZXRDb250ZW50KGh0bWxfM2Y2YTUzNzAzMzEyNDgxMDhhNzExY2E5NmI3Nzc1N2QpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmFjMzg1YzgzZTM1NGVmM2IyMGI4ODYwYmM3YWJjZDAuYmluZFBvcHVwKHBvcHVwXzJlM2Y3NGI3ZTg1YzRjYzk4MTA3NzNjYzZkNTliMWRiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJhNWJiYzJhYzA5ODQ3NzBhNjA1ZGZiM2EzOTQ3NDQ5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE1MzgzNCwtNzkuNDA1Njc4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmQ5MWJmOWFmNWI3NGNkMDk1NjY1NGJhOGQ3OWJiYzYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjkwZGRmY2JlZDJiNGQ0ZjlhNGJmODYwYjJjOGFiYzEgPSAkKCc8ZGl2IGlkPSJodG1sX2Y5MGRkZmNiZWQyYjRkNGY5YTRiZjg2MGIyYzhhYmMxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aCBUb3JvbnRvIFdlc3QsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yZDkxYmY5YWY1Yjc0Y2QwOTU2NjU0YmE4ZDc5YmJjNi5zZXRDb250ZW50KGh0bWxfZjkwZGRmY2JlZDJiNGQ0ZjlhNGJmODYwYjJjOGFiYzEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmE1YmJjMmFjMDk4NDc3MGE2MDVkZmIzYTM5NDc0NDkuYmluZFBvcHVwKHBvcHVwXzJkOTFiZjlhZjViNzRjZDA5NTY2NTRiYThkNzliYmM2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI3ZDQxZmExOTBhMzRmNjg4YjM5YmEzYzRlODVmNmMzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA0MzI0NCwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lNzg4MDA4NzU0MjE0NTk0YmVlM2QwNzcyZDhlNGQ4NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wMjcwODU5ZDE2NmI0ZjkxYjRhY2VjNWQ1NDg5ZTQ5ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfMDI3MDg1OWQxNjZiNGY5MWI0YWNlYzVkNTQ4OWU0OWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lNzg4MDA4NzU0MjE0NTk0YmVlM2QwNzcyZDhlNGQ4NC5zZXRDb250ZW50KGh0bWxfMDI3MDg1OWQxNjZiNGY5MWI0YWNlYzVkNTQ4OWU0OWYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjdkNDFmYTE5MGEzNGY2ODhiMzliYTNjNGU4NWY2YzMuYmluZFBvcHVwKHBvcHVwX2U3ODgwMDg3NTQyMTQ1OTRiZWUzZDA3NzJkOGU0ZDg0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk0MjI1MjZmYzI3NzQ2ODlhOTVjNzU5OWMyY2M0NWZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg5NTc0MywtNzkuMzgzMTU5OTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWE3YmMxMzNlNTI3NDBlMzhmYmVjZDRjOTI0M2JjMTQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOWI2Y2IzZjU0ODg0NDc1Mzk3NjA4YmVkNjQ4OTcxZDkgPSAkKCc8ZGl2IGlkPSJodG1sXzliNmNiM2Y1NDg4NDQ3NTM5NzYwOGJlZDY0ODk3MWQ5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb29yZSBQYXJrLFN1bW1lcmhpbGwgRWFzdCwgQ2VudHJhbFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FhN2JjMTMzZTUyNzQwZTM4ZmJlY2Q0YzkyNDNiYzE0LnNldENvbnRlbnQoaHRtbF85YjZjYjNmNTQ4ODQ0NzUzOTc2MDhiZWQ2NDg5NzFkOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85NDIyNTI2ZmMyNzc0Njg5YTk1Yzc1OTljMmNjNDVmYS5iaW5kUG9wdXAocG9wdXBfYWE3YmMxMzNlNTI3NDBlMzhmYmVjZDRjOTI0M2JjMTQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTNjNzVhN2Q5NDU3NGViNzlmMTI5N2NiMzRiODQ3NWEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42ODY0MTIyOTk5OTk5OSwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xMWVkZDIxM2Y4OTM0OWMwYTk4ZWNmNWYyNTc0MTI1YyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kNjdlMmFlOTMxODM0NTJmOWYxYjEyODZkNWNlZTRmNCA9ICQoJzxkaXYgaWQ9Imh0bWxfZDY3ZTJhZTkzMTgzNDUyZjlmMWIxMjg2ZDVjZWU0ZjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRlZXIgUGFyayxGb3Jlc3QgSGlsbCBTRSxSYXRobmVsbHksU291dGggSGlsbCxTdW1tZXJoaWxsIFdlc3QsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xMWVkZDIxM2Y4OTM0OWMwYTk4ZWNmNWYyNTc0MTI1Yy5zZXRDb250ZW50KGh0bWxfZDY3ZTJhZTkzMTgzNDUyZjlmMWIxMjg2ZDVjZWU0ZjQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTNjNzVhN2Q5NDU3NGViNzlmMTI5N2NiMzRiODQ3NWEuYmluZFBvcHVwKHBvcHVwXzExZWRkMjEzZjg5MzQ5YzBhOThlY2Y1ZjI1NzQxMjVjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y1OTY4YTc5MDBjYTQwNDY4NmJhNWNkYWM4MmFhODhjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjc5NTYyNiwtNzkuMzc3NTI5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTE2OTNjMTlkNzY2NDRlYzg0MzE0NjI1YmFhMmY1YTUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYWYwMjk2NTVlOTg0NDg2YThhYTcyNGUwMjExY2M4MmMgPSAkKCc8ZGl2IGlkPSJodG1sX2FmMDI5NjU1ZTk4NDQ4NmE4YWE3MjRlMDIxMWNjODJjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlZGFsZSwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lMTY5M2MxOWQ3NjY0NGVjODQzMTQ2MjViYWEyZjVhNS5zZXRDb250ZW50KGh0bWxfYWYwMjk2NTVlOTg0NDg2YThhYTcyNGUwMjExY2M4MmMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjU5NjhhNzkwMGNhNDA0Njg2YmE1Y2RhYzgyYWE4OGMuYmluZFBvcHVwKHBvcHVwX2UxNjkzYzE5ZDc2NjQ0ZWM4NDMxNDYyNWJhYTJmNWE1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M2OGEyZWE5YzU1MTQ0Y2I4ZjUzYTQ5ZTJhNmZkM2YzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY3OTY3LC03OS4zNjc2NzUzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzY0MzA4OTU5M2M5NzQ5ZTc5YjkyMjU4MmUxNmFjNDQ0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FkMWZlMGFlMjg5MDQxYzc4NDdiOTk2NjUwODY5N2UyID0gJCgnPGRpdiBpZD0iaHRtbF9hZDFmZTBhZTI4OTA0MWM3ODQ3Yjk5NjY1MDg2OTdlMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FiYmFnZXRvd24sU3QuIEphbWVzIFRvd24sIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjQzMDg5NTkzYzk3NDllNzliOTIyNTgyZTE2YWM0NDQuc2V0Q29udGVudChodG1sX2FkMWZlMGFlMjg5MDQxYzc4NDdiOTk2NjUwODY5N2UyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M2OGEyZWE5YzU1MTQ0Y2I4ZjUzYTQ5ZTJhNmZkM2YzLmJpbmRQb3B1cChwb3B1cF82NDMwODk1OTNjOTc0OWU3OWI5MjI1ODJlMTZhYzQ0NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80M2Q3ZjdlYTE2N2Y0NmY1OGU5YjliYTRlNjBjYjk5MyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2NTg1OTksLTc5LjM4MzE1OTkwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg0MGVmZWJlY2ZjNjQ4MDhhM2IxZDYxNTRjZjBjZTFjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzg5YjMzNjFlNGE0MDRiZGE4NjA5NTZiOGMwNjE0M2JjID0gJCgnPGRpdiBpZD0iaHRtbF84OWIzMzYxZTRhNDA0YmRhODYwOTU2YjhjMDYxNDNiYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2h1cmNoIGFuZCBXZWxsZXNsZXksIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODQwZWZlYmVjZmM2NDgwOGEzYjFkNjE1NGNmMGNlMWMuc2V0Q29udGVudChodG1sXzg5YjMzNjFlNGE0MDRiZGE4NjA5NTZiOGMwNjE0M2JjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQzZDdmN2VhMTY3ZjQ2ZjU4ZTliOWJhNGU2MGNiOTkzLmJpbmRQb3B1cChwb3B1cF84NDBlZmViZWNmYzY0ODA4YTNiMWQ2MTU0Y2YwY2UxYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MzI0ZTliYzlkNDk0YjhlYjk0ZWY4MjhmZTI0MGM0ZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1NDI1OTksLTc5LjM2MDYzNTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfY2VmZTIxNjEyMWY1NDdmMDgwMTBhODA5ZDFlOTAyY2MgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNmNlYTVjOTI1ZTc4NDYwYTljNDRhZTJmMGIwOTU3Y2IgPSAkKCc8ZGl2IGlkPSJodG1sXzZjZWE1YzkyNWU3ODQ2MGE5YzQ0YWUyZjBiMDk1N2NiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQsUmVnZW50IFBhcmssIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfY2VmZTIxNjEyMWY1NDdmMDgwMTBhODA5ZDFlOTAyY2Muc2V0Q29udGVudChodG1sXzZjZWE1YzkyNWU3ODQ2MGE5YzQ0YWUyZjBiMDk1N2NiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkzMjRlOWJjOWQ0OTRiOGViOTRlZjgyOGZlMjQwYzRmLmJpbmRQb3B1cChwb3B1cF9jZWZlMjE2MTIxZjU0N2YwODAxMGE4MDlkMWU5MDJjYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hYmY5OGJmOTdiODc0NjkwYjhiNWNjMDY3MDgwOTQyYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1NzE2MTgsLTc5LjM3ODkzNzA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA3Mzc3MThhYjNjZTQ0MmRiOGNmOWI3YjNjZjJkNzhlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FjNGU4ZTRmOGViMjQwNGJhZTcyNTg1MTQzMzgwZjYyID0gJCgnPGRpdiBpZD0iaHRtbF9hYzRlOGU0ZjhlYjI0MDRiYWU3MjU4NTE0MzM4MGY2MiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UnllcnNvbixHYXJkZW4gRGlzdHJpY3QsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDczNzcxOGFiM2NlNDQyZGI4Y2Y5YjdiM2NmMmQ3OGUuc2V0Q29udGVudChodG1sX2FjNGU4ZTRmOGViMjQwNGJhZTcyNTg1MTQzMzgwZjYyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2FiZjk4YmY5N2I4NzQ2OTBiOGI1Y2MwNjcwODA5NDJjLmJpbmRQb3B1cChwb3B1cF8wNzM3NzE4YWIzY2U0NDJkYjhjZjliN2IzY2YyZDc4ZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82MjAzNGE4ZGZhY2E0Mjk1OTdmNjI0YzA2NDc4Mjc5MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1MTQ5MzksLTc5LjM3NTQxNzldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjEzNjA5Y2UwYjRlNDI0ZDk5YzMwMTJjZmVjMGVkMGMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDhiOGRiNzRiYjkwNDczYzkxZDUxOTJmYjc2YWU2ZTEgPSAkKCc8ZGl2IGlkPSJodG1sX2Q4YjhkYjc0YmI5MDQ3M2M5MWQ1MTkyZmI3NmFlNmUxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdC4gSmFtZXMgVG93biwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mMTM2MDljZTBiNGU0MjRkOTljMzAxMmNmZWMwZWQwYy5zZXRDb250ZW50KGh0bWxfZDhiOGRiNzRiYjkwNDczYzkxZDUxOTJmYjc2YWU2ZTEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjIwMzRhOGRmYWNhNDI5NTk3ZjYyNGMwNjQ3ODI3OTAuYmluZFBvcHVwKHBvcHVwX2YxMzYwOWNlMGI0ZTQyNGQ5OWMzMDEyY2ZlYzBlZDBjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc3YmM0OTFhZTZkOTQ2MGJiN2ZiNGVlYzhjMzUwMGNjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ0NzcwNzk5OTk5OTk2LC03OS4zNzMzMDY0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzZlODQzZTI3NzVhOTQ5ZjQ5YmUyMjFkNDAyNDgwNWI2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNkY2I2MDQxMmE0YjRjNGQ4YzUxZWM0M2E1OTlmNWRhID0gJCgnPGRpdiBpZD0iaHRtbF8zZGNiNjA0MTJhNGI0YzRkOGM1MWVjNDNhNTk5ZjVkYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVyY3p5IFBhcmssIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmU4NDNlMjc3NWE5NDlmNDliZTIyMWQ0MDI0ODA1YjYuc2V0Q29udGVudChodG1sXzNkY2I2MDQxMmE0YjRjNGQ4YzUxZWM0M2E1OTlmNWRhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc3YmM0OTFhZTZkOTQ2MGJiN2ZiNGVlYzhjMzUwMGNjLmJpbmRQb3B1cChwb3B1cF82ZTg0M2UyNzc1YTk0OWY0OWJlMjIxZDQwMjQ4MDViNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kYzY2YjI2ODNiNmQ0MjIyODAwZGI4ZjJhMTFmMzUxNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1Nzk1MjQsLTc5LjM4NzM4MjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjlkNDhiM2I0OWI5NGM2M2IwZjc5Y2M5ZTM1MmNhMzAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjUzOWY1OWMyYjg3NGZmY2ExMjE2OTUwMWEyZTcxOWYgPSAkKCc8ZGl2IGlkPSJodG1sXzY1MzlmNTljMmI4NzRmZmNhMTIxNjk1MDFhMmU3MTlmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZW50cmFsIEJheSBTdHJlZXQsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjlkNDhiM2I0OWI5NGM2M2IwZjc5Y2M5ZTM1MmNhMzAuc2V0Q29udGVudChodG1sXzY1MzlmNTljMmI4NzRmZmNhMTIxNjk1MDFhMmU3MTlmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2RjNjZiMjY4M2I2ZDQyMjI4MDBkYjhmMmExMWYzNTE1LmJpbmRQb3B1cChwb3B1cF82OWQ0OGIzYjQ5Yjk0YzYzYjBmNzljYzllMzUyY2EzMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yY2JjMDIyMmM2MGE0NTAwOWI3MjE1ZjdhYmE4ZDc1NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1MDU3MTIwMDAwMDAxLC03OS4zODQ1Njc1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2I0NThhNjgwOTJiYjRiNGZiNTY4ZDQxMWU1Y2UwOWQ4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2NhNjAxOGQwZTIyYzRmN2JhMGRjNzljYTIyNDI4NzFkID0gJCgnPGRpdiBpZD0iaHRtbF9jYTYwMThkMGUyMmM0ZjdiYTBkYzc5Y2EyMjQyODcxZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWRlbGFpZGUsS2luZyxSaWNobW9uZCwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iNDU4YTY4MDkyYmI0YjRmYjU2OGQ0MTFlNWNlMDlkOC5zZXRDb250ZW50KGh0bWxfY2E2MDE4ZDBlMjJjNGY3YmEwZGM3OWNhMjI0Mjg3MWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmNiYzAyMjJjNjBhNDUwMDliNzIxNWY3YWJhOGQ3NTcuYmluZFBvcHVwKHBvcHVwX2I0NThhNjgwOTJiYjRiNGZiNTY4ZDQxMWU1Y2UwOWQ4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y2MjU5Y2JiZmRlNjQxYzk4NGRkNTUyZjIxNTI0MTM1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQwODE1NywtNzkuMzgxNzUyMjk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmNmZGY5MTVlOWUxNDI4NGI1Yzg2ODk5ZGEyZDhhZjEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzY4ZjhiOGQ1N2EzNDA0NWIxNzg1YzJkMGZlNTc5OTMgPSAkKCc8ZGl2IGlkPSJodG1sXzc2OGY4YjhkNTdhMzQwNDViMTc4NWMyZDBmZTU3OTkzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQgRWFzdCxUb3JvbnRvIElzbGFuZHMsVW5pb24gU3RhdGlvbiwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yY2ZkZjkxNWU5ZTE0Mjg0YjVjODY4OTlkYTJkOGFmMS5zZXRDb250ZW50KGh0bWxfNzY4ZjhiOGQ1N2EzNDA0NWIxNzg1YzJkMGZlNTc5OTMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjYyNTljYmJmZGU2NDFjOTg0ZGQ1NTJmMjE1MjQxMzUuYmluZFBvcHVwKHBvcHVwXzJjZmRmOTE1ZTllMTQyODRiNWM4Njg5OWRhMmQ4YWYxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzcxNzNlYmJhYmJlOTRlNmE4ZTdkODk1MzlhMWUxNTU5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ3MTc2OCwtNzkuMzgxNTc2NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDM3ZWRkNjBlNGMwNGJjOWJkZGIzNTNmODZkMjE5ZjcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYmQzYmNjNGJjMjc4NDQyZjhlM2QyMzQ4NmJjYjQ2ZTMgPSAkKCc8ZGl2IGlkPSJodG1sX2JkM2JjYzRiYzI3ODQ0MmY4ZTNkMjM0ODZiY2I0NmUzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5EZXNpZ24gRXhjaGFuZ2UsVG9yb250byBEb21pbmlvbiBDZW50cmUsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDM3ZWRkNjBlNGMwNGJjOWJkZGIzNTNmODZkMjE5Zjcuc2V0Q29udGVudChodG1sX2JkM2JjYzRiYzI3ODQ0MmY4ZTNkMjM0ODZiY2I0NmUzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzcxNzNlYmJhYmJlOTRlNmE4ZTdkODk1MzlhMWUxNTU5LmJpbmRQb3B1cChwb3B1cF80MzdlZGQ2MGU0YzA0YmM5YmRkYjM1M2Y4NmQyMTlmNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85OGRkMDc2YTQ4MDY0NjRlODU0MzcyZDUyNTdmYjM2OSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY0ODE5ODUsLTc5LjM3OTgxNjkwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzU4MzZjMWY4ZGY5NTQ0NGY5Zjk0ODU5YmU3NjQ4MTkxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzc4ZjdjZDI4OTM4MTRhMDJhOWIwOWVlZmQzMzgxZmJhID0gJCgnPGRpdiBpZD0iaHRtbF83OGY3Y2QyODkzODE0YTAyYTliMDllZWZkMzM4MWZiYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q29tbWVyY2UgQ291cnQsVmljdG9yaWEgSG90ZWwsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNTgzNmMxZjhkZjk1NDQ0ZjlmOTQ4NTliZTc2NDgxOTEuc2V0Q29udGVudChodG1sXzc4ZjdjZDI4OTM4MTRhMDJhOWIwOWVlZmQzMzgxZmJhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk4ZGQwNzZhNDgwNjQ2NGU4NTQzNzJkNTI1N2ZiMzY5LmJpbmRQb3B1cChwb3B1cF81ODM2YzFmOGRmOTU0NDRmOWY5NDg1OWJlNzY0ODE5MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80OGNiNDExZGMwODA0YjVlYWMwNDgwYWE5YzdhNTA1YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjczMzI4MjUsLTc5LjQxOTc0OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODJlODM1MmE4ZDFkNDVlZjljMDI4MGZiZDQ0ODU0ZDEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmI2NzAxODEzOTI5NDk0NTg1NWIzMWI5Y2I0NTA4YWYgPSAkKCc8ZGl2IGlkPSJodG1sX2ZiNjcwMTgxMzkyOTQ5NDU4NTViMzFiOWNiNDUwOGFmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWRmb3JkIFBhcmssTGF3cmVuY2UgTWFub3IgRWFzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MmU4MzUyYThkMWQ0NWVmOWMwMjgwZmJkNDQ4NTRkMS5zZXRDb250ZW50KGh0bWxfZmI2NzAxODEzOTI5NDk0NTg1NWIzMWI5Y2I0NTA4YWYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDhjYjQxMWRjMDgwNGI1ZWFjMDQ4MGFhOWM3YTUwNWEuYmluZFBvcHVwKHBvcHVwXzgyZTgzNTJhOGQxZDQ1ZWY5YzAyODBmYmQ0NDg1NGQxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M1ZGY2YWYwOTM1ZDRiNGE5YmUyYjhlN2IzZmFkODNkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzExNjk0OCwtNzkuNDE2OTM1NTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmZjOWUyMjM2MTliNDIyYWE4ZWFjYmJjNTQyMjUxYmMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzMwYjZkZjI3Y2FkNGI0YWI4MWU1NzA4YWNkNTRhMmQgPSAkKCc8ZGl2IGlkPSJodG1sXzMzMGI2ZGYyN2NhZDRiNGFiODFlNTcwOGFjZDU0YTJkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlbGF3biwgQ2VudHJhbFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzJmYzllMjIzNjE5YjQyMmFhOGVhY2JiYzU0MjI1MWJjLnNldENvbnRlbnQoaHRtbF8zMzBiNmRmMjdjYWQ0YjRhYjgxZTU3MDhhY2Q1NGEyZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jNWRmNmFmMDkzNWQ0YjRhOWJlMmI4ZTdiM2ZhZDgzZC5iaW5kUG9wdXAocG9wdXBfMmZjOWUyMjM2MTliNDIyYWE4ZWFjYmJjNTQyMjUxYmMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGI0YjdiNjM1ZTY5NDIyNmJkOTNhZGM0Mjc3ZmQzYjAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTY5NDc2LC03OS40MTEzMDcyMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84MTA3NTk1YWIwNzA0NjIxODFkMThjNzI4YjVmZDZlNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wZDg5NjA0MTk3MmQ0YmNhODY3MjIyMTI5NGQ3MDQyOCA9ICQoJzxkaXYgaWQ9Imh0bWxfMGQ4OTYwNDE5NzJkNGJjYTg2NzIyMjEyOTRkNzA0MjgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZvcmVzdCBIaWxsIE5vcnRoLEZvcmVzdCBIaWxsIFdlc3QsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MTA3NTk1YWIwNzA0NjIxODFkMThjNzI4YjVmZDZlNi5zZXRDb250ZW50KGh0bWxfMGQ4OTYwNDE5NzJkNGJjYTg2NzIyMjEyOTRkNzA0MjgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGI0YjdiNjM1ZTY5NDIyNmJkOTNhZGM0Mjc3ZmQzYjAuYmluZFBvcHVwKHBvcHVwXzgxMDc1OTVhYjA3MDQ2MjE4MWQxOGM3MjhiNWZkNmU2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhlZjQ4MDQ0ZjJkMzRlMmNiNmNlZTIxNDMxNjRiNWM5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjcyNzA5NywtNzkuNDA1Njc4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTNhMTc0N2FiZjU1NGI4NTg3OTcwYjA5MThjNDEyODQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDhjMWJiZjlkZjVlNDVkOGFmZjkxN2E2NmFlZjAxYzAgPSAkKCc8ZGl2IGlkPSJodG1sXzA4YzFiYmY5ZGY1ZTQ1ZDhhZmY5MTdhNjZhZWYwMWMwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgQW5uZXgsTm9ydGggTWlkdG93bixZb3JrdmlsbGUsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hM2ExNzQ3YWJmNTU0Yjg1ODc5NzBiMDkxOGM0MTI4NC5zZXRDb250ZW50KGh0bWxfMDhjMWJiZjlkZjVlNDVkOGFmZjkxN2E2NmFlZjAxYzApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGVmNDgwNDRmMmQzNGUyY2I2Y2VlMjE0MzE2NGI1YzkuYmluZFBvcHVwKHBvcHVwX2EzYTE3NDdhYmY1NTRiODU4Nzk3MGIwOTE4YzQxMjg0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2JjYjlkYzY1Yzg1NDQxYzlhNTdjM2JhZmFhOGIxZDk1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjYyNjk1NiwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kMmM5NTI1NWU3MTA0NTMyOGU2ZjIyNjM5YzIyM2RkYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xOTU5NmE1Mjk2ZTI0NGEyOTI3YTZiNWU5YzZhYzM5NCA9ICQoJzxkaXYgaWQ9Imh0bWxfMTk1OTZhNTI5NmUyNDRhMjkyN2E2YjVlOWM2YWMzOTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhhcmJvcmQsVW5pdmVyc2l0eSBvZiBUb3JvbnRvLCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2QyYzk1MjU1ZTcxMDQ1MzI4ZTZmMjI2MzljMjIzZGRhLnNldENvbnRlbnQoaHRtbF8xOTU5NmE1Mjk2ZTI0NGEyOTI3YTZiNWU5YzZhYzM5NCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iY2I5ZGM2NWM4NTQ0MWM5YTU3YzNiYWZhYThiMWQ5NS5iaW5kUG9wdXAocG9wdXBfZDJjOTUyNTVlNzEwNDUzMjhlNmYyMjYzOWMyMjNkZGEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjNjYWFiYjVhYjY0NDdlOWE4YjE3OWI0ZWUxZjRkODkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTMyMDU3LC03OS40MDAwNDkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2MzZTNlYTE1OWI4NjRmOWJhMjA1OWYzNTM4MWI3NWQ1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzEwZGI4ZGJkMGNhYzQwZTViZGEwM2FiODY1NWUzOGIyID0gJCgnPGRpdiBpZD0iaHRtbF8xMGRiOGRiZDBjYWM0MGU1YmRhMDNhYjg2NTVlMzhiMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2hpbmF0b3duLEdyYW5nZSBQYXJrLEtlbnNpbmd0b24gTWFya2V0LCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2MzZTNlYTE1OWI4NjRmOWJhMjA1OWYzNTM4MWI3NWQ1LnNldENvbnRlbnQoaHRtbF8xMGRiOGRiZDBjYWM0MGU1YmRhMDNhYjg2NTVlMzhiMik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mM2NhYWJiNWFiNjQ0N2U5YThiMTc5YjRlZTFmNGQ4OS5iaW5kUG9wdXAocG9wdXBfYzNlM2VhMTU5Yjg2NGY5YmEyMDU5ZjM1MzgxYjc1ZDUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzFiMTQ4OWI2YWRkNDk5YThkOTk5YWZmMGRlZTcyMDMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Mjg5NDY3LC03OS4zOTQ0MTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE4NThhYjBiMGNkNDRlM2E4NzBlN2ZlY2RkMjNiNWVmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzk1YmJkMWQxMjI1NDRiMGNhNzNmMGMwNTVjNDA0YmQ3ID0gJCgnPGRpdiBpZD0iaHRtbF85NWJiZDFkMTIyNTQ0YjBjYTczZjBjMDU1YzQwNGJkNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q04gVG93ZXIsQmF0aHVyc3QgUXVheSxJc2xhbmQgYWlycG9ydCxIYXJib3VyZnJvbnQgV2VzdCxLaW5nIGFuZCBTcGFkaW5hLFJhaWx3YXkgTGFuZHMsU291dGggTmlhZ2FyYSwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xODU4YWIwYjBjZDQ0ZTNhODcwZTdmZWNkZDIzYjVlZi5zZXRDb250ZW50KGh0bWxfOTViYmQxZDEyMjU0NGIwY2E3M2YwYzA1NWM0MDRiZDcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzFiMTQ4OWI2YWRkNDk5YThkOTk5YWZmMGRlZTcyMDMuYmluZFBvcHVwKHBvcHVwXzE4NThhYjBiMGNkNDRlM2E4NzBlN2ZlY2RkMjNiNWVmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBhM2Y1M2RmMGZhYjQ3MDE4MTBjYmNkYzI4NmQwMGZmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ2NDM1MiwtNzkuMzc0ODQ1OTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjdiYzFiZGExNTYxNDk5NDkxMjlmOTA0ZmRiNzM1N2QgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYzgxODQxY2FjMmE1NGYzY2FkMDFkNjQ5NTBjM2NiZjEgPSAkKCc8ZGl2IGlkPSJodG1sX2M4MTg0MWNhYzJhNTRmM2NhZDAxZDY0OTUwYzNjYmYxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdG4gQSBQTyBCb3hlcyAyNSBUaGUgRXNwbGFuYWRlLCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzY3YmMxYmRhMTU2MTQ5OTQ5MTI5ZjkwNGZkYjczNTdkLnNldENvbnRlbnQoaHRtbF9jODE4NDFjYWMyYTU0ZjNjYWQwMWQ2NDk1MGMzY2JmMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wYTNmNTNkZjBmYWI0NzAxODEwY2JjZGMyODZkMDBmZi5iaW5kUG9wdXAocG9wdXBfNjdiYzFiZGExNTYxNDk5NDkxMjlmOTA0ZmRiNzM1N2QpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfM2ZhN2UwNzE3M2MzNDg3MTgwMmVlM2YyMWYxNjdhOGMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDg0MjkyLC03OS4zODIyODAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzExNjA5ZjgyMzE3YTQyOTY5NDc0NjhmOTc4MjA1NTg0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2M2MzIzZjVmOTgxNTQ5Mjk5YmM3N2EzMjhmMGIwNDlkID0gJCgnPGRpdiBpZD0iaHRtbF9jNjMyM2Y1Zjk4MTU0OTI5OWJjNzdhMzI4ZjBiMDQ5ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rmlyc3QgQ2FuYWRpYW4gUGxhY2UsVW5kZXJncm91bmQgY2l0eSwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xMTYwOWY4MjMxN2E0Mjk2OTQ3NDY4Zjk3ODIwNTU4NC5zZXRDb250ZW50KGh0bWxfYzYzMjNmNWY5ODE1NDkyOTliYzc3YTMyOGYwYjA0OWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2ZhN2UwNzE3M2MzNDg3MTgwMmVlM2YyMWYxNjdhOGMuYmluZFBvcHVwKHBvcHVwXzExNjA5ZjgyMzE3YTQyOTY5NDc0NjhmOTc4MjA1NTg0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ExNmMyZTk3YTJiNTRiNWM5NjM3ZjYyOGU3MTIzYWQ2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE4NTE3OTk5OTk5OTk2LC03OS40NjQ3NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lMTgwODQ3NDc4ZTY0YTYzODk0NWFhNTUzMTUzYmU5ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jNDUwNDUwMDQ2ODE0OTI0ODI5NjY1OTQwYTQ3Mjk2MCA9ICQoJzxkaXYgaWQ9Imh0bWxfYzQ1MDQ1MDA0NjgxNDkyNDgyOTY2NTk0MGE0NzI5NjAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIEhlaWdodHMsTGF3cmVuY2UgTWFub3IsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTE4MDg0NzQ3OGU2NGE2Mzg5NDVhYTU1MzE1M2JlOWYuc2V0Q29udGVudChodG1sX2M0NTA0NTAwNDY4MTQ5MjQ4Mjk2NjU5NDBhNDcyOTYwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ExNmMyZTk3YTJiNTRiNWM5NjM3ZjYyOGU3MTIzYWQ2LmJpbmRQb3B1cChwb3B1cF9lMTgwODQ3NDc4ZTY0YTYzODk0NWFhNTUzMTUzYmU5Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84ZWYzNjUzMTNjMTE0MmIxYTM2OGIxYWEwMzM4Y2VmYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcwOTU3NywtNzkuNDQ1MDcyNTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTY3ODI1NjI0NjE4NGJhNWE2ZmM3OGVjOTM4OWM5YzEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTc2NzgzNmJjMTBiNDdjYWI0ZTJiZjJhYjkwOTMzODUgPSAkKCc8ZGl2IGlkPSJodG1sXzU3Njc4MzZiYzEwYjQ3Y2FiNGUyYmYyYWI5MDkzMzg1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HbGVuY2Fpcm4sIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNTY3ODI1NjI0NjE4NGJhNWE2ZmM3OGVjOTM4OWM5YzEuc2V0Q29udGVudChodG1sXzU3Njc4MzZiYzEwYjQ3Y2FiNGUyYmYyYWI5MDkzMzg1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhlZjM2NTMxM2MxMTQyYjFhMzY4YjFhYTAzMzhjZWZiLmJpbmRQb3B1cChwb3B1cF81Njc4MjU2MjQ2MTg0YmE1YTZmYzc4ZWM5Mzg5YzljMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yZmRjZDEzMDU2MTI0MGYyYmI1MGUzMzZmOWRkNDgwMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5Mzc4MTMsLTc5LjQyODE5MTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U2ZGFmMGNkMzBhZjRiNzliYWVjYWVkZTBlNjg1MzkzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FlMDFlZjlhMWM2NzQ3OGY4OGJmNGI2M2IzYjAxYTdmID0gJCgnPGRpdiBpZD0iaHRtbF9hZTAxZWY5YTFjNjc0NzhmODhiZjRiNjNiM2IwMWE3ZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtZXdvb2QtQ2VkYXJ2YWxlLCBZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lNmRhZjBjZDMwYWY0Yjc5YmFlY2FlZGUwZTY4NTM5My5zZXRDb250ZW50KGh0bWxfYWUwMWVmOWExYzY3NDc4Zjg4YmY0YjYzYjNiMDFhN2YpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmZkY2QxMzA1NjEyNDBmMmJiNTBlMzM2ZjlkZDQ4MDAuYmluZFBvcHVwKHBvcHVwX2U2ZGFmMGNkMzBhZjRiNzliYWVjYWVkZTBlNjg1MzkzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2YyZTkxNWEyNzJhMjQyM2FhOTQxZGIwNjlhOTJiOWI0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg5MDI1NiwtNzkuNDUzNTEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2VlOTdmNzM4MWRkNDRlYjY5MGMzNTE5YmI0ZTI3NzRmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU0NzM0ZjE0MGQ5YjRmNDhhOTUxMjJjZDE4ZGU3NmEyID0gJCgnPGRpdiBpZD0iaHRtbF81NDczNGYxNDBkOWI0ZjQ4YTk1MTIyY2QxOGRlNzZhMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FsZWRvbmlhLUZhaXJiYW5rcywgWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZWU5N2Y3MzgxZGQ0NGViNjkwYzM1MTliYjRlMjc3NGYuc2V0Q29udGVudChodG1sXzU0NzM0ZjE0MGQ5YjRmNDhhOTUxMjJjZDE4ZGU3NmEyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2YyZTkxNWEyNzJhMjQyM2FhOTQxZGIwNjlhOTJiOWI0LmJpbmRQb3B1cChwb3B1cF9lZTk3ZjczODFkZDQ0ZWI2OTBjMzUxOWJiNGUyNzc0Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81YjE4MjE5ZmYzZjQ0N2NkOTc0NTYzZmZiYjVhZjZmNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2OTU0MiwtNzkuNDIyNTYzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jOGVkNjU0YWIwYjU0MTY4OTYxYWRhODZhODUzYWRjOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83YzY5MGYyOGRhNjM0MzFhODIzMzRmNTA4YmU5ZjY2MCA9ICQoJzxkaXYgaWQ9Imh0bWxfN2M2OTBmMjhkYTYzNDMxYTgyMzM0ZjUwOGJlOWY2NjAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNocmlzdGllLCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M4ZWQ2NTRhYjBiNTQxNjg5NjFhZGE4NmE4NTNhZGM4LnNldENvbnRlbnQoaHRtbF83YzY5MGYyOGRhNjM0MzFhODIzMzRmNTA4YmU5ZjY2MCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81YjE4MjE5ZmYzZjQ0N2NkOTc0NTYzZmZiYjVhZjZmNC5iaW5kUG9wdXAocG9wdXBfYzhlZDY1NGFiMGI1NDE2ODk2MWFkYTg2YTg1M2FkYzgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTM2ZDc5ODVlNjEyNGM2OWI3ODUzMDQ1ZTU3MzFiZDUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjkwMDUxMDAwMDAwMSwtNzkuNDQyMjU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81MWU1ZjM1M2Y0YjM0ZGRiYjU2ZTg3YzdmNzExNTg0ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83ZTM1Y2I5YmUwZjU0YTVjYWJiNWIyZDJiMTYyYjVlZCA9ICQoJzxkaXYgaWQ9Imh0bWxfN2UzNWNiOWJlMGY1NGE1Y2FiYjViMmQyYjE2MmI1ZWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvdmVyY291cnQgVmlsbGFnZSxEdWZmZXJpbiwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzUxZTVmMzUzZjRiMzRkZGJiNTZlODdjN2Y3MTE1ODRkLnNldENvbnRlbnQoaHRtbF83ZTM1Y2I5YmUwZjU0YTVjYWJiNWIyZDJiMTYyYjVlZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81MzZkNzk4NWU2MTI0YzY5Yjc4NTMwNDVlNTczMWJkNS5iaW5kUG9wdXAocG9wdXBfNTFlNWYzNTNmNGIzNGRkYmI1NmU4N2M3ZjcxMTU4NGQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjk4ZGM1MmFhMGIwNDY0ZWI3ZjUxNmYxNmFlMjA4MzIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDc5MjY3MDAwMDAwMDYsLTc5LjQxOTc0OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjU2ODBhYjk3OTRjNDYwOTg4M2MzM2ZiZTVkY2ExMzggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjBkNWFmMmQwODUxNDg3N2EyN2M1MGZjNzgyZGE5NjcgPSAkKCc8ZGl2IGlkPSJodG1sXzYwZDVhZjJkMDg1MTQ4NzdhMjdjNTBmYzc4MmRhOTY3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5MaXR0bGUgUG9ydHVnYWwsVHJpbml0eSwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y1NjgwYWI5Nzk0YzQ2MDk4ODNjMzNmYmU1ZGNhMTM4LnNldENvbnRlbnQoaHRtbF82MGQ1YWYyZDA4NTE0ODc3YTI3YzUwZmM3ODJkYTk2Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mOThkYzUyYWEwYjA0NjRlYjdmNTE2ZjE2YWUyMDgzMi5iaW5kUG9wdXAocG9wdXBfZjU2ODBhYjk3OTRjNDYwOTg4M2MzM2ZiZTVkY2ExMzgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzlmYTc1NGQwMDk4NGY3Yjk4NDI0ZmZjOGEwMGMxYmEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MzY4NDcyLC03OS40MjgxOTE0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80MGY1NzM1ZTNkNTQ0YzU1OGU3NDA2NTE5ZTMzZmVlNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wYjA5MjJjYmE3MzI0MWFiYTM5Y2M3N2FmMjg2OTFiMiA9ICQoJzxkaXYgaWQ9Imh0bWxfMGIwOTIyY2JhNzMyNDFhYmEzOWNjNzdhZjI4NjkxYjIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJyb2NrdG9uLEV4aGliaXRpb24gUGxhY2UsUGFya2RhbGUgVmlsbGFnZSwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQwZjU3MzVlM2Q1NDRjNTU4ZTc0MDY1MTllMzNmZWU1LnNldENvbnRlbnQoaHRtbF8wYjA5MjJjYmE3MzI0MWFiYTM5Y2M3N2FmMjg2OTFiMik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zOWZhNzU0ZDAwOTg0ZjdiOTg0MjRmZmM4YTAwYzFiYS5iaW5kUG9wdXAocG9wdXBfNDBmNTczNWUzZDU0NGM1NThlNzQwNjUxOWUzM2ZlZTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjU2NmM1N2JmOTNjNDJlMjk0ZmVmZjdiN2U1ZTQ1MGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MTM3NTYyMDAwMDAwMDYsLTc5LjQ5MDA3MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjUwYTgzYTI4MmNiNGIwMDg3ODkyMmM5YTExNGFiYWQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzcxMDVhOGY4YmM2NDhiNGE1NzFlYjAyMjQ4MzNjNTMgPSAkKCc8ZGl2IGlkPSJodG1sXzM3MTA1YThmOGJjNjQ4YjRhNTcxZWIwMjI0ODMzYzUzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb3duc3ZpZXcsTm9ydGggUGFyayxVcHdvb2QgUGFyaywgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNTBhODNhMjgyY2I0YjAwODc4OTIyYzlhMTE0YWJhZC5zZXRDb250ZW50KGh0bWxfMzcxMDVhOGY4YmM2NDhiNGE1NzFlYjAyMjQ4MzNjNTMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjU2NmM1N2JmOTNjNDJlMjk0ZmVmZjdiN2U1ZTQ1MGIuYmluZFBvcHVwKHBvcHVwX2Y1MGE4M2EyODJjYjRiMDA4Nzg5MjJjOWExMTRhYmFkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzU2YWU3ZmMwZDdkNjQ0NmI5OTRkMmQ5M2RiNmE1YTU5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjkxMTE1OCwtNzkuNDc2MDEzMjk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTJkOTA2MWY4MDk3NGZkMjk3YTI5N2Q3Yzc4ZGY3OWUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjc5NWMzMDAyZTE2NGVjZWE1OGZhZWU2ZDEwOThmZDkgPSAkKCc8ZGl2IGlkPSJodG1sX2Y3OTVjMzAwMmUxNjRlY2VhNThmYWVlNmQxMDk4ZmQ5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5EZWwgUmF5LEtlZWxlc2RhbGUsTW91bnQgRGVubmlzLFNpbHZlcnRob3JuLCBZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lMmQ5MDYxZjgwOTc0ZmQyOTdhMjk3ZDdjNzhkZjc5ZS5zZXRDb250ZW50KGh0bWxfZjc5NWMzMDAyZTE2NGVjZWE1OGZhZWU2ZDEwOThmZDkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTZhZTdmYzBkN2Q2NDQ2Yjk5NGQyZDkzZGI2YTVhNTkuYmluZFBvcHVwKHBvcHVwX2UyZDkwNjFmODA5NzRmZDI5N2EyOTdkN2M3OGRmNzllKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I0ZjA0ZDU4N2VlMjRiMjI4MmIxNmI1ZmU2OTE5ZTJmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjczMTg1Mjk5OTk5OTksLTc5LjQ4NzI2MTkwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U1YTMzZTJmNDBmYjRjM2RiMDMzMDFlNGU5OGJjODFiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzBjMThhNTRlZDRjMTQ4ZDI5N2YyY2JjZDJjNGYyYWE4ID0gJCgnPGRpdiBpZD0iaHRtbF8wYzE4YTU0ZWQ0YzE0OGQyOTdmMmNiY2QyYzRmMmFhOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhlIEp1bmN0aW9uIE5vcnRoLFJ1bm55bWVkZSwgWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTVhMzNlMmY0MGZiNGMzZGIwMzMwMWU0ZTk4YmM4MWIuc2V0Q29udGVudChodG1sXzBjMThhNTRlZDRjMTQ4ZDI5N2YyY2JjZDJjNGYyYWE4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2I0ZjA0ZDU4N2VlMjRiMjI4MmIxNmI1ZmU2OTE5ZTJmLmJpbmRQb3B1cChwb3B1cF9lNWEzM2UyZjQwZmI0YzNkYjAzMzAxZTRlOThiYzgxYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84YjFhNjBjMjg1ZWQ0N2Y1ODU2NjhkODY3MDBkOTA1ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MTYwODMsLTc5LjQ2NDc2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzIyNGIxODI2MzhiZjQ2MzZiOWMwMmJmZWQ1NDVjOTVmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2MxMTQ4OTY1NWEwZTRiZjM4MDg2M2NkY2JmZjhkYzI5ID0gJCgnPGRpdiBpZD0iaHRtbF9jMTE0ODk2NTVhMGU0YmYzODA4NjNjZGNiZmY4ZGMyOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaCBQYXJrLFRoZSBKdW5jdGlvbiBTb3V0aCwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzIyNGIxODI2MzhiZjQ2MzZiOWMwMmJmZWQ1NDVjOTVmLnNldENvbnRlbnQoaHRtbF9jMTE0ODk2NTVhMGU0YmYzODA4NjNjZGNiZmY4ZGMyOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84YjFhNjBjMjg1ZWQ0N2Y1ODU2NjhkODY3MDBkOTA1ZS5iaW5kUG9wdXAocG9wdXBfMjI0YjE4MjYzOGJmNDYzNmI5YzAyYmZlZDU0NWM5NWYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTg0OTg5ODFlNzMwNDM3NWJlN2ExNTAxY2NkNDI1ZjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDg5NTk3LC03OS40NTYzMjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfY2U2NmU4NGE4ZmUwNDdkNTk2OTYzZjhkNmE2YWI0ZjMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzViZWUzMjRiN2I1NDE3YWJiZDI3NzYwZWU5N2E1NmEgPSAkKCc8ZGl2IGlkPSJodG1sXzc1YmVlMzI0YjdiNTQxN2FiYmQyNzc2MGVlOTdhNTZhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrZGFsZSxSb25jZXN2YWxsZXMsIFdlc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jZTY2ZTg0YThmZTA0N2Q1OTY5NjNmOGQ2YTZhYjRmMy5zZXRDb250ZW50KGh0bWxfNzViZWUzMjRiN2I1NDE3YWJiZDI3NzYwZWU5N2E1NmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTg0OTg5ODFlNzMwNDM3NWJlN2ExNTAxY2NkNDI1ZjguYmluZFBvcHVwKHBvcHVwX2NlNjZlODRhOGZlMDQ3ZDU5Njk2M2Y4ZDZhNmFiNGYzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzcxOTBkYTg1N2VhZTRlNzM4MzVhZDA3Y2E4MmQ5NTdjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUxNTcwNiwtNzkuNDg0NDQ5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83Y2NhMzdiMzA0ZmQ0MjA2YTIzOGVmNTAzODQ0NmFkNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mMGEzOTRiN2YwZmM0OWFhYTQzY2I0OTBhN2ZkOTA2NSA9ICQoJzxkaXYgaWQ9Imh0bWxfZjBhMzk0YjdmMGZjNDlhYWE0M2NiNDkwYTdmZDkwNjUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJ1bm55bWVkZSxTd2Fuc2VhLCBXZXN0VG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfN2NjYTM3YjMwNGZkNDIwNmEyMzhlZjUwMzg0NDZhZDUuc2V0Q29udGVudChodG1sX2YwYTM5NGI3ZjBmYzQ5YWFhNDNjYjQ5MGE3ZmQ5MDY1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzcxOTBkYTg1N2VhZTRlNzM4MzVhZDA3Y2E4MmQ5NTdjLmJpbmRQb3B1cChwb3B1cF83Y2NhMzdiMzA0ZmQ0MjA2YTIzOGVmNTAzODQ0NmFkNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84YTBhM2E5ZDIzMTQ0NTY4YTdmNDU1ZTBkNjI4YTc1YiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MjMwMTUsLTc5LjM4OTQ5MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWM3ZWE3OTg3NTcwNDM3YWE5NGUwODFjY2YxYjRmNjIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYWI1ODgzNmRhYjZkNDFhMjg5MzdlMDYwZjRmZWZlYTkgPSAkKCc8ZGl2IGlkPSJodG1sX2FiNTg4MzZkYWI2ZDQxYTI4OTM3ZTA2MGY0ZmVmZWE5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5RdWVlbiYjMzk7cyBQYXJrLCBRdWVlbiYjMzk7c1Bhcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FjN2VhNzk4NzU3MDQzN2FhOTRlMDgxY2NmMWI0ZjYyLnNldENvbnRlbnQoaHRtbF9hYjU4ODM2ZGFiNmQ0MWEyODkzN2UwNjBmNGZlZmVhOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84YTBhM2E5ZDIzMTQ0NTY4YTdmNDU1ZTBkNjI4YTc1Yi5iaW5kUG9wdXAocG9wdXBfYWM3ZWE3OTg3NTcwNDM3YWE5NGUwODFjY2YxYjRmNjIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTI4MTNiMzA4NWVkNDVmOThmZGFhZDdlZjExYjZjZTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MzY5NjU2LC03OS42MTU4MTg5OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lNjczMmU2ZTdjMDk0NDEwOWRhZTM2ZTIzNzc2YWFiNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iODA4MTQwNTEwNWQ0NzU2YTNiZDc0YjU1ZDEyNDU1MyA9ICQoJzxkaXYgaWQ9Imh0bWxfYjgwODE0MDUxMDVkNDc1NmEzYmQ3NGI1NWQxMjQ1NTMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNhbmFkYSBQb3N0IEdhdGV3YXkgUHJvY2Vzc2luZyBDZW50cmUsIE1pc3Npc3NhdWdhPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lNjczMmU2ZTdjMDk0NDEwOWRhZTM2ZTIzNzc2YWFiNi5zZXRDb250ZW50KGh0bWxfYjgwODE0MDUxMDVkNDc1NmEzYmQ3NGI1NWQxMjQ1NTMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTI4MTNiMzA4NWVkNDVmOThmZGFhZDdlZjExYjZjZTcuYmluZFBvcHVwKHBvcHVwX2U2NzMyZTZlN2MwOTQ0MTA5ZGFlMzZlMjM3NzZhYWI2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzAxZTQ4MTViNGQ0MjQ3ODQ4ZTlhODVhY2UzZjc5YzRhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjYyNzQzOSwtNzkuMzIxNTU4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzYwYmVjZTg3MzUzNzQ1OTk5MzRlYWYyY2JmZDZiOTNiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzhmM2EyMTk2ODVkZTQ3YzQ4YmQ4MjEwOTU4M2VlZDViID0gJCgnPGRpdiBpZD0iaHRtbF84ZjNhMjE5Njg1ZGU0N2M0OGJkODIxMDk1ODNlZWQ1YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnVzaW5lc3MgUmVwbHkgTWFpbCBQcm9jZXNzaW5nIENlbnRyZSA5NjkgRWFzdGVybiwgRWFzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzYwYmVjZTg3MzUzNzQ1OTk5MzRlYWYyY2JmZDZiOTNiLnNldENvbnRlbnQoaHRtbF84ZjNhMjE5Njg1ZGU0N2M0OGJkODIxMDk1ODNlZWQ1Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wMWU0ODE1YjRkNDI0Nzg0OGU5YTg1YWNlM2Y3OWM0YS5iaW5kUG9wdXAocG9wdXBfNjBiZWNlODczNTM3NDU5OTkzNGVhZjJjYmZkNmI5M2IpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWI1YjQwODJhZjlhNDc2ZTg1NDAwMjYyYjNkZjYxYWYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MDU2NDY2LC03OS41MDEzMjA3MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mODc0MTQwZGQ4Y2U0ZTY0YTJkZjhlZjlmYWFiOTY4MCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85NzIzMmQ1YWVmYjI0MWFjYWVmNGE2M2MwZmJiOWY3OCA9ICQoJzxkaXYgaWQ9Imh0bWxfOTcyMzJkNWFlZmIyNDFhY2FlZjRhNjNjMGZiYjlmNzgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWJlciBCYXkgU2hvcmVzLE1pbWljbyBTb3V0aCxOZXcgVG9yb250bywgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mODc0MTQwZGQ4Y2U0ZTY0YTJkZjhlZjlmYWFiOTY4MC5zZXRDb250ZW50KGh0bWxfOTcyMzJkNWFlZmIyNDFhY2FlZjRhNjNjMGZiYjlmNzgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWI1YjQwODJhZjlhNDc2ZTg1NDAwMjYyYjNkZjYxYWYuYmluZFBvcHVwKHBvcHVwX2Y4NzQxNDBkZDhjZTRlNjRhMmRmOGVmOWZhYWI5NjgwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMwMzg4MjQ5NjIwNzRlZDViZjZjYjJiZmJmZmZjMGYyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjAyNDEzNzAwMDAwMDEsLTc5LjU0MzQ4NDA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzllMTRiZmI4NWIzNjRjZDc4NTRhYTRkZDEwZjJiYzY5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzBiMGIwMmJmZjIzMzQzMDQ4Y2FjOTM0NWE3YTBmOTJhID0gJCgnPGRpdiBpZD0iaHRtbF8wYjBiMDJiZmYyMzM0MzA0OGNhYzkzNDVhN2EwZjkyYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWxkZXJ3b29kLExvbmcgQnJhbmNoLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzllMTRiZmI4NWIzNjRjZDc4NTRhYTRkZDEwZjJiYzY5LnNldENvbnRlbnQoaHRtbF8wYjBiMDJiZmYyMzM0MzA0OGNhYzkzNDVhN2EwZjkyYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMDM4ODI0OTYyMDc0ZWQ1YmY2Y2IyYmZiZmZmYzBmMi5iaW5kUG9wdXAocG9wdXBfOWUxNGJmYjg1YjM2NGNkNzg1NGFhNGRkMTBmMmJjNjkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWQwMGI1YTQyMzc0NGUyNWE0ZTI0NjNkNDMxNjk5MGQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTM2NTM2MDAwMDAwMDUsLTc5LjUwNjk0MzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNmEwMmVkNjI2NTU2NGQyN2I5M2IzYjM2Y2RiOGM4YmMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjAzYmM1Yzg1NmI2NGFjZWFkNTQxODNmM2YzYTg1NzUgPSAkKCc8ZGl2IGlkPSJodG1sX2IwM2JjNWM4NTZiNjRhY2VhZDU0MTgzZjNmM2E4NTc1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgS2luZ3N3YXksTW9udGdvbWVyeSBSb2FkLE9sZCBNaWxsIE5vcnRoLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZhMDJlZDYyNjU1NjRkMjdiOTNiM2IzNmNkYjhjOGJjLnNldENvbnRlbnQoaHRtbF9iMDNiYzVjODU2YjY0YWNlYWQ1NDE4M2YzZjNhODU3NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85ZDAwYjVhNDIzNzQ0ZTI1YTRlMjQ2M2Q0MzE2OTkwZC5iaW5kUG9wdXAocG9wdXBfNmEwMmVkNjI2NTU2NGQyN2I5M2IzYjM2Y2RiOGM4YmMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMGEzYjdiMDU2MjJhNDZjYjkwN2VlZTcwMTY2YzRhMTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MzYyNTc5LC03OS40OTg1MDkwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85MDU4MjNlNTgxNzk0NDMwOWQ2ZjMyMTk3Y2Y3YmNlZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wNmJjNzdmNGZjNGY0MjVlODllYTY0YzdhNjlmN2MxZSA9ICQoJzxkaXYgaWQ9Imh0bWxfMDZiYzc3ZjRmYzRmNDI1ZTg5ZWE2NGM3YTY5ZjdjMWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWJlciBCYXksS2luZyYjMzk7cyBNaWxsIFBhcmssS2luZ3N3YXkgUGFyayBTb3V0aCBFYXN0LE1pbWljbyBORSxPbGQgTWlsbCBTb3V0aCxUaGUgUXVlZW5zd2F5IEVhc3QsUm95YWwgWW9yayBTb3V0aCBFYXN0LFN1bm55bGVhLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzkwNTgyM2U1ODE3OTQ0MzA5ZDZmMzIxOTdjZjdiY2VmLnNldENvbnRlbnQoaHRtbF8wNmJjNzdmNGZjNGY0MjVlODllYTY0YzdhNjlmN2MxZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wYTNiN2IwNTYyMmE0NmNiOTA3ZWVlNzAxNjZjNGExNy5iaW5kUG9wdXAocG9wdXBfOTA1ODIzZTU4MTc5NDQzMDlkNmYzMjE5N2NmN2JjZWYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzk0MjcwZjYzMmU2NDNjNjk3OWM2YjQ5NjVkNjZjMTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Mjg4NDA4LC03OS41MjA5OTk0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wODdmN2YyMWE5YmM0ZTJmYTU1ZDQ0OWEyYzkwMTljOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yNDRlOWNjMDFjZTg0ZGI0YWRmNGRhZjc1OWE0OWFhYiA9ICQoJzxkaXYgaWQ9Imh0bWxfMjQ0ZTljYzAxY2U4NGRiNGFkZjRkYWY3NTlhNDlhYWIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPktpbmdzd2F5IFBhcmsgU291dGggV2VzdCxNaW1pY28gTlcsVGhlIFF1ZWVuc3dheSBXZXN0LFJveWFsIFlvcmsgU291dGggV2VzdCxTb3V0aCBvZiBCbG9vciwgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wODdmN2YyMWE5YmM0ZTJmYTU1ZDQ0OWEyYzkwMTljOS5zZXRDb250ZW50KGh0bWxfMjQ0ZTljYzAxY2U4NGRiNGFkZjRkYWY3NTlhNDlhYWIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzk0MjcwZjYzMmU2NDNjNjk3OWM2YjQ5NjVkNjZjMTMuYmluZFBvcHVwKHBvcHVwXzA4N2Y3ZjIxYTliYzRlMmZhNTVkNDQ5YTJjOTAxOWM5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzU3MjdjZTMyMDQ3MTQwZGU5ZDI3ZDA4YzM4NzM1ZmRiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY3ODU1NiwtNzkuNTMyMjQyNDAwMDAwMDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTczMDgzYTFmZDQyNDM5MTljZDhhMzhlOTBiYTdlNjkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjNmMjVjN2ZjNDUwNGEwODk3ZmE3ZmQyNDk3ZjBjNjQgPSAkKCc8ZGl2IGlkPSJodG1sX2YzZjI1YzdmYzQ1MDRhMDg5N2ZhN2ZkMjQ5N2YwYzY0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Jc2xpbmd0b24gQXZlbnVlLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU3MzA4M2ExZmQ0MjQzOTE5Y2Q4YTM4ZTkwYmE3ZTY5LnNldENvbnRlbnQoaHRtbF9mM2YyNWM3ZmM0NTA0YTA4OTdmYTdmZDI0OTdmMGM2NCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81NzI3Y2UzMjA0NzE0MGRlOWQyN2QwOGMzODczNWZkYi5iaW5kUG9wdXAocG9wdXBfNTczMDgzYTFmZDQyNDM5MTljZDhhMzhlOTBiYTdlNjkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjkyNzk4NzRhNGM2NDVhMDkxMjExOTZmODBiMzMyMDMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTA5NDMyLC03OS41NTQ3MjQ0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wZmNhYTkwNzlhMWI0ZDQ2YTgwNmI2N2RjZGI5NzE2NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lZmYzM2M1MTI2ZWQ0Yjg5OGE0OWYzNzY1YTBlNmQ5MyA9ICQoJzxkaXYgaWQ9Imh0bWxfZWZmMzNjNTEyNmVkNGI4OThhNDlmMzc2NWEwZTZkOTMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsb3ZlcmRhbGUsSXNsaW5ndG9uLE1hcnRpbiBHcm92ZSxQcmluY2VzcyBHYXJkZW5zLFdlc3QgRGVhbmUgUGFyaywgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wZmNhYTkwNzlhMWI0ZDQ2YTgwNmI2N2RjZGI5NzE2NC5zZXRDb250ZW50KGh0bWxfZWZmMzNjNTEyNmVkNGI4OThhNDlmMzc2NWEwZTZkOTMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjkyNzk4NzRhNGM2NDVhMDkxMjExOTZmODBiMzMyMDMuYmluZFBvcHVwKHBvcHVwXzBmY2FhOTA3OWExYjRkNDZhODA2YjY3ZGNkYjk3MTY0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IxZWJkODE5Y2MwNTRkNDJiNTU2ZjRjMTkwMTQ3M2E0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQzNTE1MiwtNzkuNTc3MjAwNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDk0ZjhiZjZlYjZjNGI0Zjk5YzNhYTAwZjI0NzBmMWQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTE4ZWJjYzE2MGE0NGNiOGE2MWE2NTY2ZGU0MzViNjYgPSAkKCc8ZGl2IGlkPSJodG1sX2ExOGViY2MxNjBhNDRjYjhhNjFhNjU2NmRlNDM1YjY2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CbG9vcmRhbGUgR2FyZGVucyxFcmluZ2F0ZSxNYXJrbGFuZCBXb29kLE9sZCBCdXJuaGFtdGhvcnBlLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzA5NGY4YmY2ZWI2YzRiNGY5OWMzYWEwMGYyNDcwZjFkLnNldENvbnRlbnQoaHRtbF9hMThlYmNjMTYwYTQ0Y2I4YTYxYTY1NjZkZTQzNWI2Nik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iMWViZDgxOWNjMDU0ZDQyYjU1NmY0YzE5MDE0NzNhNC5iaW5kUG9wdXAocG9wdXBfMDk0ZjhiZjZlYjZjNGI0Zjk5YzNhYTAwZjI0NzBmMWQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZGIxODlhMjVkZjg5NGViYmJmMDdhNjhmMGJkZjgwMzYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTYzMDMzLC03OS41NjU5NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83MzEwMmQ3MTZiMzU0YzE1OTE4NDg2NTBmMjk4ZTQ3OCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84MThiZDI2YTZmNTE0OTZkOTFhZjMwN2Q4NmMwODIxNCA9ICQoJzxkaXYgaWQ9Imh0bWxfODE4YmQyNmE2ZjUxNDk2ZDkxYWYzMDdkODZjMDgyMTQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWJlciBTdW1taXQsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzMxMDJkNzE2YjM1NGMxNTkxODQ4NjUwZjI5OGU0Nzguc2V0Q29udGVudChodG1sXzgxOGJkMjZhNmY1MTQ5NmQ5MWFmMzA3ZDg2YzA4MjE0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2RiMTg5YTI1ZGY4OTRlYmJiZjA3YTY4ZjBiZGY4MDM2LmJpbmRQb3B1cChwb3B1cF83MzEwMmQ3MTZiMzU0YzE1OTE4NDg2NTBmMjk4ZTQ3OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mZjM4OWZiMjBjNWM0MWYxOTE4NGMyYzI2ZDM2NGFjMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNDc2NTksLTc5LjUzMjI0MjQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzkyMzYyMDA4MjYyNjQ5ODI4ZDUzODNiOTAxNmE3NDRhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzhkZGExMTY3MDYwNTRmNzY4Mzg5MDMzNzcyMTM2YWUzID0gJCgnPGRpdiBpZD0iaHRtbF84ZGRhMTE2NzA2MDU0Zjc2ODM4OTAzMzc3MjEzNmFlMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RW1lcnksSHVtYmVybGVhLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzkyMzYyMDA4MjYyNjQ5ODI4ZDUzODNiOTAxNmE3NDRhLnNldENvbnRlbnQoaHRtbF84ZGRhMTE2NzA2MDU0Zjc2ODM4OTAzMzc3MjEzNmFlMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mZjM4OWZiMjBjNWM0MWYxOTE4NGMyYzI2ZDM2NGFjMC5iaW5kUG9wdXAocG9wdXBfOTIzNjIwMDgyNjI2NDk4MjhkNTM4M2I5MDE2YTc0NGEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjk2ZmQ3MjRkNDkzNGIwN2JhZGU3NmRiZTk1MDIxYTUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MDY4NzYsLTc5LjUxODE4ODQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE3ZGViYWZlMWMzODQyN2E5MzRmNmFhYmYwMDRjMzJmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2EyNjc4ZjYyZDI5OTRjMGQ4NmY0OWNmOWUxNTgxOGVlID0gJCgnPGRpdiBpZD0iaHRtbF9hMjY3OGY2MmQyOTk0YzBkODZmNDljZjllMTU4MThlZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2VzdG9uLCBZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xN2RlYmFmZTFjMzg0MjdhOTM0ZjZhYWJmMDA0YzMyZi5zZXRDb250ZW50KGh0bWxfYTI2NzhmNjJkMjk5NGMwZDg2ZjQ5Y2Y5ZTE1ODE4ZWUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjk2ZmQ3MjRkNDkzNGIwN2JhZGU3NmRiZTk1MDIxYTUuYmluZFBvcHVwKHBvcHVwXzE3ZGViYWZlMWMzODQyN2E5MzRmNmFhYmYwMDRjMzJmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdiNmFhZTdlOGViNDQyNjViZjRjNmRjYjIwMTU1NGMyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjk2MzE5LC03OS41MzIyNDI0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81ODIxOTI0YTk2MDg0ZTVjYjNjZDcxNjNiYTRkMWIwMik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82MGFhYjdhY2Y3OWQ0ZGJhYjg5Mzg1MDA3MTNjNTM1ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mZTRjMzIxMWJjODg0ZTEzOWRiOWI5OWI1NWQzMjg0YiA9ICQoJzxkaXYgaWQ9Imh0bWxfZmU0YzMyMTFiYzg4NGUxMzlkYjliOTliNTVkMzI4NGIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldlc3Rtb3VudCwgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82MGFhYjdhY2Y3OWQ0ZGJhYjg5Mzg1MDA3MTNjNTM1Zi5zZXRDb250ZW50KGh0bWxfZmU0YzMyMTFiYzg4NGUxMzlkYjliOTliNTVkMzI4NGIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2I2YWFlN2U4ZWI0NDI2NWJmNGM2ZGNiMjAxNTU0YzIuYmluZFBvcHVwKHBvcHVwXzYwYWFiN2FjZjc5ZDRkYmFiODkzODUwMDcxM2M1MzVmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzU4ODFiYjc4NjMxODQxZmFhNTFhNjVmMGY0NTBhYjcwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg4OTA1NCwtNzkuNTU0NzI0NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTgyMThkZjhlNDFlNGYyNmEwM2U2YmUzYzU1Y2Q1YWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDkyYmFmMDRmMGRjNDE0ZGIzODlkZjM0NTE5OWZmMTQgPSAkKCc8ZGl2IGlkPSJodG1sXzA5MmJhZjA0ZjBkYzQxNGRiMzg5ZGYzNDUxOTlmZjE0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc3ZpZXcgVmlsbGFnZSxNYXJ0aW4gR3JvdmUgR2FyZGVucyxSaWNodmlldyBHYXJkZW5zLFN0LiBQaGlsbGlwcywgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hODIxOGRmOGU0MWU0ZjI2YTAzZTZiZTNjNTVjZDVhYS5zZXRDb250ZW50KGh0bWxfMDkyYmFmMDRmMGRjNDE0ZGIzODlkZjM0NTE5OWZmMTQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTg4MWJiNzg2MzE4NDFmYWE1MWE2NWYwZjQ1MGFiNzAuYmluZFBvcHVwKHBvcHVwX2E4MjE4ZGY4ZTQxZTRmMjZhMDNlNmJlM2M1NWNkNWFhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhkM2I0ZDJiMjdiZTRlYTZhYTNhNjg0MmI5MzFlMGU4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzM5NDE2Mzk5OTk5OTk2LC03OS41ODg0MzY5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU4MjE5MjRhOTYwODRlNWNiM2NkNzE2M2JhNGQxYjAyKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzViMzYwZWY1OTViODQzMDJiZWNkZjcxMjVjNzNkMTIzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzkzMTBhNjM4NmQ3ODQ3NWVhN2Y0YjcyNzEyZGZmNWY5ID0gJCgnPGRpdiBpZD0iaHRtbF85MzEwYTYzODZkNzg0NzVlYTdmNGI3MjcxMmRmZjVmOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWxiaW9uIEdhcmRlbnMsQmVhdW1vbmQgSGVpZ2h0cyxIdW1iZXJnYXRlLEphbWVzdG93bixNb3VudCBPbGl2ZSxTaWx2ZXJzdG9uZSxTb3V0aCBTdGVlbGVzLFRoaXN0bGV0b3duLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzViMzYwZWY1OTViODQzMDJiZWNkZjcxMjVjNzNkMTIzLnNldENvbnRlbnQoaHRtbF85MzEwYTYzODZkNzg0NzVlYTdmNGI3MjcxMmRmZjVmOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84ZDNiNGQyYjI3YmU0ZWE2YWEzYTY4NDJiOTMxZTBlOC5iaW5kUG9wdXAocG9wdXBfNWIzNjBlZjU5NWI4NDMwMmJlY2RmNzEyNWM3M2QxMjMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjgyMTY1ZDA1NmY3NDFiYWJiZmUzZGNhYzlmNGFkODQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MDY3NDgyOTk5OTk5OTQsLTc5LjU5NDA1NDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTgyMTkyNGE5NjA4NGU1Y2IzY2Q3MTYzYmE0ZDFiMDIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjk0MGY0NWZlMzNjNDNhYjhmZGE4Y2IyYzZiODNkOGEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2Y2Yzg3ZTczYWNhNDVmYjliNDhjYjdmZGI2YzhjOTUgPSAkKCc8ZGl2IGlkPSJodG1sX2NmNmM4N2U3M2FjYTQ1ZmI5YjQ4Y2I3ZmRiNmM4Yzk1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aHdlc3QsIEV0b2JpY29rZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjk0MGY0NWZlMzNjNDNhYjhmZGE4Y2IyYzZiODNkOGEuc2V0Q29udGVudChodG1sX2NmNmM4N2U3M2FjYTQ1ZmI5YjQ4Y2I3ZmRiNmM4Yzk1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzY4MjE2NWQwNTZmNzQxYmFiYmZlM2RjYWM5ZjRhZDg0LmJpbmRQb3B1cChwb3B1cF9iOTQwZjQ1ZmUzM2M0M2FiOGZkYThjYjJjNmI4M2Q4YSk7CgogICAgICAgICAgICAKICAgICAgICAKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



# Using Foursquare API to explore the neighborhoods


```python
#@hidden_cell
CLIENT_ID = 'XMCICN4YC1PQCMXSJEA2YVR5PRAC4N22MLOUV115WCWNA1HW' 
CLIENT_SECRET = '2VYYN4JX2SG1NTZUOGDOCKY1MRM12V40FV5KYFBMQUBLWRFY'
VERSION = '20180605'
radius=500
url = 'https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&ll={},{}&v={}&radius={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, radius)
results = requests.get(url).json()
```

Define a function to get the category


```python
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']
```

Using the get_category_type function, we clean up the json and turn it into a pandas DF. Before we start we need to import certain libraries.


```python
import json
from pandas.io.json import json_normalize 
```


```python
venues = results['response']['groups'][0]['items']
   
nearby_venues = json_normalize(venues) # flatten JSON

filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
nearby_venues =nearby_venues.loc[:, filtered_columns]

nearby_venues['venue.categories'] = nearby_venues.apply(get_category_type, axis=1)

nearby_venues.columns = [col.split(".")[-1] for col in nearby_venues.columns]

nearby_venues.head()
```




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


```python
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
```


```python
toronto_venues = getNearbyVenues(names=df_5['Neighbourhood'],
                                   latitudes=df_5['Latitude'],
                                   longitudes=df_5['Longitude']
                                  )
```

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



```python
print(toronto_venues.shape)
toronto_venues.head()
```

    (1333, 7)





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


```python
toronto_venues.groupby('Neighborhood').count()
```




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



We then check to see how many unique categories of venues there are in the Toronto


```python
print('There are {} uniques categories.'.format(len(toronto_venues['Venue Category'].unique())))
```

    There are 237 uniques categories.


We check to see which places are most visited by neighborhood


```python
toronto_onehot = pd.get_dummies(toronto_venues[['Venue Category']], prefix="", prefix_sep="")

toronto_onehot['Neighborhood'] = toronto_venues['Neighborhood'] 

fixed_columns = [toronto_onehot.columns[-1]] + list(toronto_onehot.columns[:-1])
toronto_onehot = toronto_onehot[fixed_columns]
```


```python
toronto_grouped = toronto_onehot.groupby('Neighborhood').mean().reset_index()
toronto_grouped
```




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


```python
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
```

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
    
    


Even better, we can see in a Pandas data frame the top ten common venues in each neighborhood


```python
def _most_common_venues(row, num_top_venues):
    row_categories = row.iloc[1:]
    row_categories_sorted = row_categories.sort_values(ascending=False)
    
    return row_categories_sorted.index.values[0:num_top_venues]
```


```python
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
```




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



# Clustering


```python
kclusters = 5

toronto_grouped_clustering = toronto_grouped.drop('Neighborhood', 1)

kmeans = KMeans(n_clusters=kclusters, random_state=0).fit(toronto_grouped_clustering)

kmeans.labels_[0:98]
```




    array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0,
           0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 3, 0, 4, 4, 0, 4, 3, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 4, 0, 0, 0, 4, 0, 0, 0,
           1, 2, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 4, 0, 0, 4,
           4, 0, 0, 0, 4, 0, 0, 0, 0, 0], dtype=int32)




```python
#sorted_neighborhoods_venues.drop(['Cluster Labels'],axis=1,inplace=True)
sorted_neighborhoods_venues.insert(0, 'Cluster Labels', kmeans.labels_)
toronto_merged = df_5
# merge toronto_grouped with toronto_data to add latitude/longitude for each neighborhood
toronto_merged = toronto_merged.join(sorted_neighborhoods_venues.set_index('Neighborhood'), on='Neighbourhood')
toronto_merged.dropna(subset=["Cluster Labels"], axis=0, inplace=True)
toronto_merged.reset_index(drop=True, inplace=True)
toronto_merged['Cluster Labels'].astype(int)
toronto_merged.head()
```




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


```python
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
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYiA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYicsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDMuNjUzOTYzLC03OS4zODcyMDddLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTEsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyX2RkOWVlNmI5ZmMyNzQ1ZmQ5ZmQ4MTQwZjNkMThhNzcyID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICJtYXhab29tIjogMTgsCiAgIm1pblpvb20iOiAxLAogICJub1dyYXAiOiBmYWxzZSwKICAic3ViZG9tYWlucyI6ICJhYmMiCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85OTAwNzM1NWJmMWM0OTQzOTM3ZDI1NTA0OWZiOTYxMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjgwNjY4NjI5OTk5OTk5NiwtNzkuMTk0MzUzNDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzY2NzRjZDlhYzAyNDA0NjgxNmMxOTlmMGM4MjBkYmEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODVjODI1Y2JjMDc5NGMwNThlZjRiYmIzMmI4YTdhYWQgPSAkKCc8ZGl2IGlkPSJodG1sXzg1YzgyNWNiYzA3OTRjMDU4ZWY0YmJiMzJiOGE3YWFkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3VnZSxNYWx2ZXJuIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzY2NzRjZDlhYzAyNDA0NjgxNmMxOTlmMGM4MjBkYmEuc2V0Q29udGVudChodG1sXzg1YzgyNWNiYzA3OTRjMDU4ZWY0YmJiMzJiOGE3YWFkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk5MDA3MzU1YmYxYzQ5NDM5MzdkMjU1MDQ5ZmI5NjEwLmJpbmRQb3B1cChwb3B1cF83NjY3NGNkOWFjMDI0MDQ2ODE2YzE5OWYwYzgyMGRiYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNTRhNjk1YmIxNTM0NTM1OTdlYTU4ZGUxOTgzOGJjYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4NDUzNTEsLTc5LjE2MDQ5NzA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzMwYWVmZWY5NGI0MTRjYTM5NjAxMTczMGZmZmZmMTRkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Q3ZThlYjk5NGNjNzQwNjFhMGQwODc5MTgzNzgzMTcyID0gJCgnPGRpdiBpZD0iaHRtbF9kN2U4ZWI5OTRjYzc0MDYxYTBkMDg3OTE4Mzc4MzE3MiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaGxhbmQgQ3JlZWssUm91Z2UgSGlsbCxQb3J0IFVuaW9uIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzBhZWZlZjk0YjQxNGNhMzk2MDExNzMwZmZmZmYxNGQuc2V0Q29udGVudChodG1sX2Q3ZThlYjk5NGNjNzQwNjFhMGQwODc5MTgzNzgzMTcyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q1NGE2OTViYjE1MzQ1MzU5N2VhNThkZTE5ODM4YmNjLmJpbmRQb3B1cChwb3B1cF8zMGFlZmVmOTRiNDE0Y2EzOTYwMTE3MzBmZmZmZjE0ZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zY2FjOTA4MWYxNzQ0MWY5YjFjODBjYzYxZGIyZTRhOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc2MzU3MjYsLTc5LjE4ODcxMTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjdlZWM4NjkwODY0NGI1N2FlYjE5NGY5MDYwNTY5YjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjNiMTEyNDMyZjY0NGQ0Njg4Y2EzZmFjNWRjOTc4NDggPSAkKCc8ZGl2IGlkPSJodG1sXzIzYjExMjQzMmY2NDRkNDY4OGNhM2ZhYzVkYzk3ODQ4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HdWlsZHdvb2QsTW9ybmluZ3NpZGUsV2VzdCBIaWxsIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjdlZWM4NjkwODY0NGI1N2FlYjE5NGY5MDYwNTY5YjUuc2V0Q29udGVudChodG1sXzIzYjExMjQzMmY2NDRkNDY4OGNhM2ZhYzVkYzk3ODQ4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNjYWM5MDgxZjE3NDQxZjliMWM4MGNjNjFkYjJlNGE4LmJpbmRQb3B1cChwb3B1cF8yN2VlYzg2OTA4NjQ0YjU3YWViMTk0ZjkwNjA1NjliNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kZWM4OGZlNDAyMTA0ODk5OTZlYTFiOTkyNDIxMDhmMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MDk5MjEsLTc5LjIxNjkxNzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y0NTQwZmQ5ODVkMjQwMjM4OTFlMTIzOTgwMzM5OTljID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzUwMjBiOWEwNjE0NjQ1Njk4MDViZDVhNjY0Njk4NWEyID0gJCgnPGRpdiBpZD0iaHRtbF81MDIwYjlhMDYxNDY0NTY5ODA1YmQ1YTY2NDY5ODVhMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V29idXJuIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjQ1NDBmZDk4NWQyNDAyMzg5MWUxMjM5ODAzMzk5OWMuc2V0Q29udGVudChodG1sXzUwMjBiOWEwNjE0NjQ1Njk4MDViZDVhNjY0Njk4NWEyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2RlYzg4ZmU0MDIxMDQ4OTk5NmVhMWI5OTI0MjEwOGYwLmJpbmRQb3B1cChwb3B1cF9mNDU0MGZkOTg1ZDI0MDIzODkxZTEyMzk4MDMzOTk5Yyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lZDBiOGU4MWZkNDY0ZWJhODY3MGI3MGQ4OWZkNDEyOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MzEzNiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMGRmZDEyM2E0MjA3NDE0YjhlNDJhNzE4YTM4YmMxZTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYzE3ODQxYWIzNzJmNGE0MWJkZGEzNDA1MjM2ZmMxYTAgPSAkKCc8ZGl2IGlkPSJodG1sX2MxNzg0MWFiMzcyZjRhNDFiZGRhMzQwNTIzNmZjMWEwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZWRhcmJyYWUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wZGZkMTIzYTQyMDc0MTRiOGU0MmE3MThhMzhiYzFlNy5zZXRDb250ZW50KGh0bWxfYzE3ODQxYWIzNzJmNGE0MWJkZGEzNDA1MjM2ZmMxYTApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZWQwYjhlODFmZDQ2NGViYTg2NzBiNzBkODlmZDQxMjguYmluZFBvcHVwKHBvcHVwXzBkZmQxMjNhNDIwNzQxNGI4ZTQyYTcxOGEzOGJjMWU3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzVkMTJhZDJlNTk1MjRkMDRhN2NjZTgzZmU3YmQ4NjQ5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ0NzM0MiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTJlMzc5MjNhMGQ0NGU5MDllYzllNGI5ODMyMWEyN2EgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDkzM2MxZDNjYWNiNGUyNWI4YTI5ZWE5YjRiYTdhMTYgPSAkKCc8ZGl2IGlkPSJodG1sXzQ5MzNjMWQzY2FjYjRlMjViOGEyOWVhOWI0YmE3YTE2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TY2FyYm9yb3VnaCBWaWxsYWdlIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTJlMzc5MjNhMGQ0NGU5MDllYzllNGI5ODMyMWEyN2Euc2V0Q29udGVudChodG1sXzQ5MzNjMWQzY2FjYjRlMjViOGEyOWVhOWI0YmE3YTE2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzVkMTJhZDJlNTk1MjRkMDRhN2NjZTgzZmU3YmQ4NjQ5LmJpbmRQb3B1cChwb3B1cF9hMmUzNzkyM2EwZDQ0ZTkwOWVjOWU0Yjk4MzIxYTI3YSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81NTZmYzFkMGFjYmQ0NDViYWI5OTdkNjIzMjlhZGFhZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNzkyOTIsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzlmZmQ3YmJhN2ZiYTQ3ZDA5YTQ1MmQxYjA1Zjk2OTlmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzhjODI4MzkzMGY1NTQyMmViMmMwZjU1OWNjMjQ2MTRhID0gJCgnPGRpdiBpZD0iaHRtbF84YzgyODM5MzBmNTU0MjJlYjJjMGY1NTljYzI0NjE0YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdCBCaXJjaG1vdW50IFBhcmssSW9udmlldyxLZW5uZWR5IFBhcmsgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85ZmZkN2JiYTdmYmE0N2QwOWE0NTJkMWIwNWY5Njk5Zi5zZXRDb250ZW50KGh0bWxfOGM4MjgzOTMwZjU1NDIyZWIyYzBmNTU5Y2MyNDYxNGEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTU2ZmMxZDBhY2JkNDQ1YmFiOTk3ZDYyMzI5YWRhYWYuYmluZFBvcHVwKHBvcHVwXzlmZmQ3YmJhN2ZiYTQ3ZDA5YTQ1MmQxYjA1Zjk2OTlmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQwNTk1ZGEzOGVlZjQ2MzZiMjgwY2E5NzRmYmRiYTYzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzExMTExNzAwMDAwMDA0LC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Q1NzAwMzc1ODdiODQ5Y2U5NGJjNGMyMmVhM2YyY2FmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFlNmU5MjEyYTA1MzQ4ZGNiMDljNGY1ODc5OTY0MzBlID0gJCgnPGRpdiBpZD0iaHRtbF8xZTZlOTIxMmEwNTM0OGRjYjA5YzRmNTg3OTk2NDMwZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2xhaXJsZWEsR29sZGVuIE1pbGUsT2FrcmlkZ2UgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kNTcwMDM3NTg3Yjg0OWNlOTRiYzRjMjJlYTNmMmNhZi5zZXRDb250ZW50KGh0bWxfMWU2ZTkyMTJhMDUzNDhkY2IwOWM0ZjU4Nzk5NjQzMGUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDA1OTVkYTM4ZWVmNDYzNmIyODBjYTk3NGZiZGJhNjMuYmluZFBvcHVwKHBvcHVwX2Q1NzAwMzc1ODdiODQ5Y2U5NGJjNGMyMmVhM2YyY2FmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRjOGU5YzM0NDU2NDQ5NjE5OTRkYTc5MTQ5NjQ1ODRhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE2MzE2LC03OS4yMzk0NzYwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xZTQ5OGNjZTZmZmQ0MjZlYWZjZDI1NmZhZDhkZWNkNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNDRhY2M3ZThjMjQ0NTE4Yjg2MDlhNDExMjJkOWYzYyA9ICQoJzxkaXYgaWQ9Imh0bWxfMTQ0YWNjN2U4YzI0NDUxOGI4NjA5YTQxMTIyZDlmM2MiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsaWZmY3Jlc3QsQ2xpZmZzaWRlLFNjYXJib3JvdWdoIFZpbGxhZ2UgV2VzdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFlNDk4Y2NlNmZmZDQyNmVhZmNkMjU2ZmFkOGRlY2Q2LnNldENvbnRlbnQoaHRtbF8xNDRhY2M3ZThjMjQ0NTE4Yjg2MDlhNDExMjJkOWYzYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80YzhlOWMzNDQ1NjQ0OTYxOTk0ZGE3OTE0OTY0NTg0YS5iaW5kUG9wdXAocG9wdXBfMWU0OThjY2U2ZmZkNDI2ZWFmY2QyNTZmYWQ4ZGVjZDYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmI3YjZmODY5MGZkNDljOWJmYmRmZjViMWY4N2JjOGMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTI2NTcwMDAwMDAwMDQsLTc5LjI2NDg0ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzU3OGU5MjliYzZiNDAxNDkxMjY5M2YyMzgwZTZmYWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGE2MDM3ZDMzZjZmNDNkY2JmMDg2MmZjMjhmMmEyMDEgPSAkKCc8ZGl2IGlkPSJodG1sXzhhNjAzN2QzM2Y2ZjQzZGNiZjA4NjJmYzI4ZjJhMjAxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CaXJjaCBDbGlmZixDbGlmZnNpZGUgV2VzdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M1NzhlOTI5YmM2YjQwMTQ5MTI2OTNmMjM4MGU2ZmFjLnNldENvbnRlbnQoaHRtbF84YTYwMzdkMzNmNmY0M2RjYmYwODYyZmMyOGYyYTIwMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yYjdiNmY4NjkwZmQ0OWM5YmZiZGZmNWIxZjg3YmM4Yy5iaW5kUG9wdXAocG9wdXBfYzU3OGU5MjliYzZiNDAxNDkxMjY5M2YyMzgwZTZmYWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTdmZWJhNTNiYjJmNDdiY2JmYWYxNDNmZDJkZTI5YTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTc0MDk2LC03OS4yNzMzMDQwMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yMjVmM2I2M2Y2MzE0MDFmYTdlMTAzMzc4MDk5MjVkOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xYTZjMDY5YTU4Zjc0ZDI3YTE0MjQxNGVlZTI0ODNiNSA9ICQoJzxkaXYgaWQ9Imh0bWxfMWE2YzA2OWE1OGY3NGQyN2ExNDI0MTRlZWUyNDgzYjUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvcnNldCBQYXJrLFNjYXJib3JvdWdoIFRvd24gQ2VudHJlLFdleGZvcmQgSGVpZ2h0cyBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzIyNWYzYjYzZjYzMTQwMWZhN2UxMDMzNzgwOTkyNWQ5LnNldENvbnRlbnQoaHRtbF8xYTZjMDY5YTU4Zjc0ZDI3YTE0MjQxNGVlZTI0ODNiNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lN2ZlYmE1M2JiMmY0N2JjYmZhZjE0M2ZkMmRlMjlhNy5iaW5kUG9wdXAocG9wdXBfMjI1ZjNiNjNmNjMxNDAxZmE3ZTEwMzM3ODA5OTI1ZDkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmNjYzg5ZTc1YzRlNDU4MWI1MmQyNzRkZmQzNGVjYzAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTAwNzE1MDAwMDAwMDQsLTc5LjI5NTg0OTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGFkNDgxNDYzYmI5NDY2ODkxZDdiNmM3NzlhMGVjOTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDY3OGZmMzUzZWVlNDMxZmE2YThiYjcwMzZkODg4MjMgPSAkKCc8ZGl2IGlkPSJodG1sX2Q2NzhmZjM1M2VlZTQzMWZhNmE4YmI3MDM2ZDg4ODIzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJ5dmFsZSxXZXhmb3JkIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGFkNDgxNDYzYmI5NDY2ODkxZDdiNmM3NzlhMGVjOTcuc2V0Q29udGVudChodG1sX2Q2NzhmZjM1M2VlZTQzMWZhNmE4YmI3MDM2ZDg4ODIzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZjY2M4OWU3NWM0ZTQ1ODFiNTJkMjc0ZGZkMzRlY2MwLmJpbmRQb3B1cChwb3B1cF9kYWQ0ODE0NjNiYjk0NjY4OTFkN2I2Yzc3OWEwZWM5Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81YjJmNWQ1YTU1YjQ0MGJiYTIxNDY0ZTg4ZDc4MTc5MyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5NDIwMDMsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RiOTNjOGY1MWM1MjRmM2NiNGZmYTdlODNiZDVkMjdjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2NkOThmY2NmMDJkMDQ3M2M4ZDdmNTdkNzZmOWU2YWMzID0gJCgnPGRpdiBpZD0iaHRtbF9jZDk4ZmNjZjAyZDA0NzNjOGQ3ZjU3ZDc2ZjllNmFjMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGI5M2M4ZjUxYzUyNGYzY2I0ZmZhN2U4M2JkNWQyN2Muc2V0Q29udGVudChodG1sX2NkOThmY2NmMDJkMDQ3M2M4ZDdmNTdkNzZmOWU2YWMzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzViMmY1ZDVhNTViNDQwYmJhMjE0NjRlODhkNzgxNzkzLmJpbmRQb3B1cChwb3B1cF9kYjkzYzhmNTFjNTI0ZjNjYjRmZmE3ZTgzYmQ1ZDI3Yyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81NzAyNjAxYThiN2I0ZGNkOWJiMTc2MDQ5MTZhZmI3NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4MTYzNzUsLTc5LjMwNDMwMjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTEwMzRkNjE5MmRjNDhhMmI3NTM4NTUxZjcyZTc0ODAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDkxMTU1ZDk3YjYzNDUxZGFlMThmNDIxMjk2MzZkY2IgPSAkKCc8ZGl2IGlkPSJodG1sXzQ5MTE1NWQ5N2I2MzQ1MWRhZTE4ZjQyMTI5NjM2ZGNiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGFya3MgQ29ybmVycyxTdWxsaXZhbixUYW0gTyYjMzk7U2hhbnRlciBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzExMDM0ZDYxOTJkYzQ4YTJiNzUzODU1MWY3MmU3NDgwLnNldENvbnRlbnQoaHRtbF80OTExNTVkOTdiNjM0NTFkYWUxOGY0MjEyOTYzNmRjYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81NzAyNjAxYThiN2I0ZGNkOWJiMTc2MDQ5MTZhZmI3Ny5iaW5kUG9wdXAocG9wdXBfMTEwMzRkNjE5MmRjNDhhMmI3NTM4NTUxZjcyZTc0ODApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDQ4YmIxMDU1ZmU5NGQ5OTg1YmZlZDUxMTcwOWZjZjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My44MTUyNTIyLC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzgzZTc0Nzk3ZDU1NDQwYjg5MTBjZTg1MjIwNmNlMmMwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzg3NjkzYmFlMzhlNjQ0OWRiODNiZDA1M2EzMGRiMTIzID0gJCgnPGRpdiBpZD0iaHRtbF84NzY5M2JhZTM4ZTY0NDlkYjgzYmQwNTNhMzBkYjEyMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0IE5vcnRoLEwmIzM5O0Ftb3JlYXV4IEVhc3QsTWlsbGlrZW4sU3RlZWxlcyBFYXN0IENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODNlNzQ3OTdkNTU0NDBiODkxMGNlODUyMjA2Y2UyYzAuc2V0Q29udGVudChodG1sXzg3NjkzYmFlMzhlNjQ0OWRiODNiZDA1M2EzMGRiMTIzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q0OGJiMTA1NWZlOTRkOTk4NWJmZWQ1MTE3MDlmY2Y4LmJpbmRQb3B1cChwb3B1cF84M2U3NDc5N2Q1NTQ0MGI4OTEwY2U4NTIyMDZjZTJjMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZDdjYTUzZjI5Nzc0MWE3YTViYjNkMDBkM2VmZDVkYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5OTUyNTIwMDAwMDAwNSwtNzkuMzE4Mzg4N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84OWVhYjgwZGEyMGU0ODk0OWM5NDMyMTNiMTFhMWI3ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hYmU1MWQ5ZTRkMDQ0NjUxOTU2YTg0ZjIwYjdmM2IwMSA9ICQoJzxkaXYgaWQ9Imh0bWxfYWJlNTFkOWU0ZDA0NDY1MTk1NmE4NGYyMGI3ZjNiMDEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkwmIzM5O0Ftb3JlYXV4IFdlc3QgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84OWVhYjgwZGEyMGU0ODk0OWM5NDMyMTNiMTFhMWI3Zi5zZXRDb250ZW50KGh0bWxfYWJlNTFkOWU0ZDA0NDY1MTk1NmE4NGYyMGI3ZjNiMDEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2Q3Y2E1M2YyOTc3NDFhN2E1YmIzZDAwZDNlZmQ1ZGIuYmluZFBvcHVwKHBvcHVwXzg5ZWFiODBkYTIwZTQ4OTQ5Yzk0MzIxM2IxMWExYjdmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzYzYzA1ZGUxODIzMzQ3ZTViMWMxNWVjOTMzYjdkMTZmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuODAzNzYyMiwtNzkuMzYzNDUxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lZjIxYmViOWYxYmI0YmQyYWZjZTRkNDlkODJlZjY3ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jN2UzMjRmZGJhMjI0NGI2ODA1YWQ1ODFlM2UzODM3MCA9ICQoJzxkaXYgaWQ9Imh0bWxfYzdlMzI0ZmRiYTIyNDRiNjgwNWFkNTgxZTNlMzgzNzAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhpbGxjcmVzdCBWaWxsYWdlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZWYyMWJlYjlmMWJiNGJkMmFmY2U0ZDQ5ZDgyZWY2N2Yuc2V0Q29udGVudChodG1sX2M3ZTMyNGZkYmEyMjQ0YjY4MDVhZDU4MWUzZTM4MzcwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzYzYzA1ZGUxODIzMzQ3ZTViMWMxNWVjOTMzYjdkMTZmLmJpbmRQb3B1cChwb3B1cF9lZjIxYmViOWYxYmI0YmQyYWZjZTRkNDlkODJlZjY3Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80YWVjOTY0Yjc1ZTg0N2RiYjRlOWZiYThmZTg1YWJjZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3ODUxNzUsLTc5LjM0NjU1NTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNmY2YmFkYzY0N2IzNDFiMDgzOTRkZDI2MTU4NDAwZWQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTJhNzE5ODU0N2Q0NGMzNzgzY2VjYWYyYTkyOWJmYTkgPSAkKCc8ZGl2IGlkPSJodG1sXzUyYTcxOTg1NDdkNDRjMzc4M2NlY2FmMmE5MjliZmE5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GYWlydmlldyxIZW5yeSBGYXJtLE9yaW9sZSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZmNmJhZGM2NDdiMzQxYjA4Mzk0ZGQyNjE1ODQwMGVkLnNldENvbnRlbnQoaHRtbF81MmE3MTk4NTQ3ZDQ0YzM3ODNjZWNhZjJhOTI5YmZhOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80YWVjOTY0Yjc1ZTg0N2RiYjRlOWZiYThmZTg1YWJjZC5iaW5kUG9wdXAocG9wdXBfNmY2YmFkYzY0N2IzNDFiMDgzOTRkZDI2MTU4NDAwZWQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmMyNWZlNDU3MjBlNDE1NmFlMTg0Yjc1YjMxMGQ1ZGEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43ODY5NDczLC03OS4zODU5NzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmJjNTA0NjIyNzhhNDQ2NGJkNzYyZjk0YTg5YzBhODcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMGMyZTY4YmZkMzhlNGQ1YmIxMjZhMDBmZThkNTExYzAgPSAkKCc8ZGl2IGlkPSJodG1sXzBjMmU2OGJmZDM4ZTRkNWJiMTI2YTAwZmU4ZDUxMWMwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXl2aWV3IFZpbGxhZ2UgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iYmM1MDQ2MjI3OGE0NDY0YmQ3NjJmOTRhODljMGE4Ny5zZXRDb250ZW50KGh0bWxfMGMyZTY4YmZkMzhlNGQ1YmIxMjZhMDBmZThkNTExYzApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZmMyNWZlNDU3MjBlNDE1NmFlMTg0Yjc1YjMxMGQ1ZGEuYmluZFBvcHVwKHBvcHVwX2JiYzUwNDYyMjc4YTQ0NjRiZDc2MmY5NGE4OWMwYTg3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VmMWRiNmJjOGIxMTQ4YmZhYzgxZjYwZDExMjU1ZDIxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzg5MDUzLC03OS40MDg0OTI3OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85ZDBhODM1Y2QxYTM0NzM3YWE3ZDcwMmY0NGUyYjAyNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85YWY2ZGQ4NzljMDY0ZDIyOWZkMmZjYThjYzMyYzQ0MCA9ICQoJzxkaXYgaWQ9Imh0bWxfOWFmNmRkODc5YzA2NGQyMjlmZDJmY2E4Y2MzMmM0NDAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5ld3RvbmJyb29rLFdpbGxvd2RhbGUgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85ZDBhODM1Y2QxYTM0NzM3YWE3ZDcwMmY0NGUyYjAyNS5zZXRDb250ZW50KGh0bWxfOWFmNmRkODc5YzA2NGQyMjlmZDJmY2E4Y2MzMmM0NDApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZWYxZGI2YmM4YjExNDhiZmFjODFmNjBkMTEyNTVkMjEuYmluZFBvcHVwKHBvcHVwXzlkMGE4MzVjZDFhMzQ3MzdhYTdkNzAyZjQ0ZTJiMDI1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY4MzU1ZGM0Yjg2ZTQ4NWM5NGY5NTczNTZmN2JmNTNkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzcwMTE5OSwtNzkuNDA4NDkyNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjIyYTdmMmU2MGUyNDFiZmFlMTY2NDI5YzljNzFhMTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOWVmOTk2NzE3MThiNDNiZWJiNWFjNTM4MWYyZTgwZDIgPSAkKCc8ZGl2IGlkPSJodG1sXzllZjk5NjcxNzE4YjQzYmViYjVhYzUzODFmMmU4MGQyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XaWxsb3dkYWxlIFNvdXRoIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjIyYTdmMmU2MGUyNDFiZmFlMTY2NDI5YzljNzFhMTkuc2V0Q29udGVudChodG1sXzllZjk5NjcxNzE4YjQzYmViYjVhYzUzODFmMmU4MGQyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzY4MzU1ZGM0Yjg2ZTQ4NWM5NGY5NTczNTZmN2JmNTNkLmJpbmRQb3B1cChwb3B1cF9mMjJhN2YyZTYwZTI0MWJmYWUxNjY0MjljOWM3MWExOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84NzZjYjhjZTA5NjE0NzAxYWE1OGZjOTdjZGI5MTRiZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1Mjc1ODI5OTk5OTk5NiwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hZmFhYzVlYWEwYWQ0MGQxOGExYTFlMmI3NDZhYzJjMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83YmVmZGI1ODM4MGM0ZjA5OTE2YmE4MjI3N2ZmM2Q5ZCA9ICQoJzxkaXYgaWQ9Imh0bWxfN2JlZmRiNTgzODBjNGYwOTkxNmJhODIyNzdmZjNkOWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPllvcmsgTWlsbHMgV2VzdCBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FmYWFjNWVhYTBhZDQwZDE4YTFhMWUyYjc0NmFjMmMyLnNldENvbnRlbnQoaHRtbF83YmVmZGI1ODM4MGM0ZjA5OTE2YmE4MjI3N2ZmM2Q5ZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84NzZjYjhjZTA5NjE0NzAxYWE1OGZjOTdjZGI5MTRiZi5iaW5kUG9wdXAocG9wdXBfYWZhYWM1ZWFhMGFkNDBkMThhMWExZTJiNzQ2YWMyYzIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjIyNGJjZGFlNmEzNDk5YjkzMDg3NDg3YzRlMGZhMzQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43ODI3MzY0LC03OS40NDIyNTkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk5YmZkYzgyMzI5NzRmMjI5MGM3N2ViYzI5NmZkYzgwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzA4ZjU5NzZiYTZkODQxMTFiOTY3OTFiYzdiYmYxZmQ4ID0gJCgnPGRpdiBpZD0iaHRtbF8wOGY1OTc2YmE2ZDg0MTExYjk2NzkxYmM3YmJmMWZkOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2lsbG93ZGFsZSBXZXN0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTliZmRjODIzMjk3NGYyMjkwYzc3ZWJjMjk2ZmRjODAuc2V0Q29udGVudChodG1sXzA4ZjU5NzZiYTZkODQxMTFiOTY3OTFiYzdiYmYxZmQ4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzIyMjRiY2RhZTZhMzQ5OWI5MzA4NzQ4N2M0ZTBmYTM0LmJpbmRQb3B1cChwb3B1cF85OWJmZGM4MjMyOTc0ZjIyOTBjNzdlYmMyOTZmZGM4MCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83NTgzYTk5NDRlZjY0ZjBjOTg4NDg3ZDQwNmIxMmU5MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1MzI1ODYsLTc5LjMyOTY1NjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODE3ZmNiZmY5ZWUwNGE5YzhlOWEzNjhiMDFhODRhNmEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYWQzYjIxMzZlMDlkNDE3Njg0YTQzNjY2MzNjZWNjMDUgPSAkKCc8ZGl2IGlkPSJodG1sX2FkM2IyMTM2ZTA5ZDQxNzY4NGE0MzY2NjMzY2VjYzA1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrd29vZHMgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MTdmY2JmZjllZTA0YTljOGU5YTM2OGIwMWE4NGE2YS5zZXRDb250ZW50KGh0bWxfYWQzYjIxMzZlMDlkNDE3Njg0YTQzNjY2MzNjZWNjMDUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzU4M2E5OTQ0ZWY2NGYwYzk4ODQ4N2Q0MDZiMTJlOTAuYmluZFBvcHVwKHBvcHVwXzgxN2ZjYmZmOWVlMDRhOWM4ZTlhMzY4YjAxYTg0YTZhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2QwNmEzYTVjOTliMzRlNDI4ZDJiODI1YjYzYzY5NWZjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ1OTA1Nzk5OTk5OTk2LC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjM5Yjk4NzM1NmU3NDNmNzk2MzFlYWFjOGQ1ODM3ZmMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzEwMDQ5ZTNlZWY1NDA5MWE2YWI4MmI5NTYxODllZmYgPSAkKCc8ZGl2IGlkPSJodG1sXzcxMDA0OWUzZWVmNTQwOTFhNmFiODJiOTU2MTg5ZWZmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb24gTWlsbHMgTm9ydGggQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yMzliOTg3MzU2ZTc0M2Y3OTYzMWVhYWM4ZDU4MzdmYy5zZXRDb250ZW50KGh0bWxfNzEwMDQ5ZTNlZWY1NDA5MWE2YWI4MmI5NTYxODllZmYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDA2YTNhNWM5OWIzNGU0MjhkMmI4MjViNjNjNjk1ZmMuYmluZFBvcHVwKHBvcHVwXzIzOWI5ODczNTZlNzQzZjc5NjMxZWFhYzhkNTgzN2ZjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzkyNWI2N2U2YjA2ZDQxOGRiMDY2NDE1NDQyMjBmOGNjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI1ODk5NzAwMDAwMDEsLTc5LjM0MDkyM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jYTU4Y2JmMWExODQ0NjEwYjdjZjNmZDU1NmM3ODI1MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80ZjliZDY3YjI4MTk0ZWNjYjU1OGJlNDQ5ZmU4MmY2ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfNGY5YmQ2N2IyODE5NGVjY2I1NThiZTQ0OWZlODJmNmUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZsZW1pbmdkb24gUGFyayxEb24gTWlsbHMgU291dGggQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jYTU4Y2JmMWExODQ0NjEwYjdjZjNmZDU1NmM3ODI1Mi5zZXRDb250ZW50KGh0bWxfNGY5YmQ2N2IyODE5NGVjY2I1NThiZTQ0OWZlODJmNmUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTI1YjY3ZTZiMDZkNDE4ZGIwNjY0MTU0NDIyMGY4Y2MuYmluZFBvcHVwKHBvcHVwX2NhNThjYmYxYTE4NDQ2MTBiN2NmM2ZkNTU2Yzc4MjUyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M1M2MwNjc4MDhmYjQ5OTY5NTBkYmViZWY1MGNlZmRmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzU0MzI4MywtNzkuNDQyMjU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84YWIxNTgxN2IwYjg0ZjIyYmM2Y2JkMzc3OGJmNzE3YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jZTU4MGIxNTZmMDg0N2IzYTI4MzhhYjM2OGI3M2NmYyA9ICQoJzxkaXYgaWQ9Imh0bWxfY2U1ODBiMTU2ZjA4NDdiM2EyODM4YWIzNjhiNzNjZmMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJhdGh1cnN0IE1hbm9yLERvd25zdmlldyBOb3J0aCxXaWxzb24gSGVpZ2h0cyBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhhYjE1ODE3YjBiODRmMjJiYzZjYmQzNzc4YmY3MTdhLnNldENvbnRlbnQoaHRtbF9jZTU4MGIxNTZmMDg0N2IzYTI4MzhhYjM2OGI3M2NmYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jNTNjMDY3ODA4ZmI0OTk2OTUwZGJlYmVmNTBjZWZkZi5iaW5kUG9wdXAocG9wdXBfOGFiMTU4MTdiMGI4NGYyMmJjNmNiZDM3NzhiZjcxN2EpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmE3ODBjMjBjZTM1NDJmMDhhYzg4YzRlOThkYzk2YjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Njc5ODAzLC03OS40ODcyNjE5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lMGNlNDAxOGI1MjE0NWMwODQ4NWExMTE3ZDA0NTEyMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hYTRmMjhmNmQwY2I0NzIwYWM3MWNhNTYzYjk2YWI1OSA9ICQoJzxkaXYgaWQ9Imh0bWxfYWE0ZjI4ZjZkMGNiNDcyMGFjNzFjYTU2M2I5NmFiNTkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vcnRod29vZCBQYXJrLFlvcmsgVW5pdmVyc2l0eSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2UwY2U0MDE4YjUyMTQ1YzA4NDg1YTExMTdkMDQ1MTIwLnNldENvbnRlbnQoaHRtbF9hYTRmMjhmNmQwY2I0NzIwYWM3MWNhNTYzYjk2YWI1OSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mYTc4MGMyMGNlMzU0MmYwOGFjODhjNGU5OGRjOTZiOC5iaW5kUG9wdXAocG9wdXBfZTBjZTQwMThiNTIxNDVjMDg0ODVhMTExN2QwNDUxMjApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDg1OWQ3MTQyOTM0NDk0MmEwZmQ2OTRkMjU0ZWQwYzYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Mzc0NzMyMDAwMDAwMDQsLTc5LjQ2NDc2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2ExODY5MWI4ZjI1NjQzMGFhNGYwMTAxOTQxZjlkNzMwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzViMmE3OTlmN2IxZTRlYTZiMGU5N2I4ZmE1OTk1M2M0ID0gJCgnPGRpdiBpZD0iaHRtbF81YjJhNzk5ZjdiMWU0ZWE2YjBlOTdiOGZhNTk5NTNjNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q0ZCIFRvcm9udG8sRG93bnN2aWV3IEVhc3QgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hMTg2OTFiOGYyNTY0MzBhYTRmMDEwMTk0MWY5ZDczMC5zZXRDb250ZW50KGh0bWxfNWIyYTc5OWY3YjFlNGVhNmIwZTk3YjhmYTU5OTUzYzQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDg1OWQ3MTQyOTM0NDk0MmEwZmQ2OTRkMjU0ZWQwYzYuYmluZFBvcHVwKHBvcHVwX2ExODY5MWI4ZjI1NjQzMGFhNGYwMTAxOTQxZjlkNzMwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzcwNzc0NjY3YjVjYjQ0MzU4NWE0MTZlYmY5YTRiNGUzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzM5MDE0NiwtNzkuNTA2OTQzNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zNTg1ZmI5MGMzMDY0MDcxOGMyM2EwOTlmMTEwODQ3YiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hMDNiNjUxYmNkODI0NWVmYWVhODhjMzg4NGM2MjkxZiA9ICQoJzxkaXYgaWQ9Imh0bWxfYTAzYjY1MWJjZDgyNDVlZmFlYTg4YzM4ODRjNjI5MWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvd25zdmlldyBXZXN0IENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzU4NWZiOTBjMzA2NDA3MThjMjNhMDk5ZjExMDg0N2Iuc2V0Q29udGVudChodG1sX2EwM2I2NTFiY2Q4MjQ1ZWZhZWE4OGMzODg0YzYyOTFmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzcwNzc0NjY3YjVjYjQ0MzU4NWE0MTZlYmY5YTRiNGUzLmJpbmRQb3B1cChwb3B1cF8zNTg1ZmI5MGMzMDY0MDcxOGMyM2EwOTlmMTEwODQ3Yik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hNzViNmI2MzliYTM0Njk4OWQzMTgxMmRlMWUyNTg1NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyODQ5NjQsLTc5LjQ5NTY5NzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MGZmYjQiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODBmZmI0IiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA5YWU2M2E0ZTc5OTQyNjA4YTViZDQ2NWU0OTVkNWJhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2MxNzlhNTIzODAxMzRkMWM4NjM3ZmFmODJiYWY5MjMzID0gJCgnPGRpdiBpZD0iaHRtbF9jMTc5YTUyMzgwMTM0ZDFjODYzN2ZhZjgyYmFmOTIzMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IENlbnRyYWwgQ2x1c3RlciAzPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wOWFlNjNhNGU3OTk0MjYwOGE1YmQ0NjVlNDk1ZDViYS5zZXRDb250ZW50KGh0bWxfYzE3OWE1MjM4MDEzNGQxYzg2MzdmYWY4MmJhZjkyMzMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTc1YjZiNjM5YmEzNDY5ODlkMzE4MTJkZTFlMjU4NTQuYmluZFBvcHVwKHBvcHVwXzA5YWU2M2E0ZTc5OTQyNjA4YTViZDQ2NWU0OTVkNWJhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBlOTNjZmU2ZjRiNDQ2MTVhNWU2YzBkOTQzZTczNmYxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzYxNjMxMywtNzkuNTIwOTk5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzk0MzQ0YmVjMmIwNDVmYzkyZGUwYTNiOTk4MWJkNmEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOWQ4MThiZDcwMGUzNGM0YmE4ODk2ODM5OWEyNTIzNmMgPSAkKCc8ZGl2IGlkPSJodG1sXzlkODE4YmQ3MDBlMzRjNGJhODg5NjgzOTlhMjUyMzZjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb3duc3ZpZXcgTm9ydGh3ZXN0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzk0MzQ0YmVjMmIwNDVmYzkyZGUwYTNiOTk4MWJkNmEuc2V0Q29udGVudChodG1sXzlkODE4YmQ3MDBlMzRjNGJhODg5NjgzOTlhMjUyMzZjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBlOTNjZmU2ZjRiNDQ2MTVhNWU2YzBkOTQzZTczNmYxLmJpbmRQb3B1cChwb3B1cF9jOTQzNDRiZWMyYjA0NWZjOTJkZTBhM2I5OTgxYmQ2YSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hYjM1ZjZkN2U4N2E0NWQzYTVmNTVmOTg1ZWMxNWYyOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNTg4MjI5OTk5OTk5NSwtNzkuMzE1NTcxNTk5OTk5OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGY0ZTNlNjllNTViNDA4YWFlNWY3YzJiZDNiYzhhYTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDc0YzdjODg0NmE0NDE2ZmI1ZWY0MmNmMjQxNzAyM2QgPSAkKCc8ZGl2IGlkPSJodG1sXzA3NGM3Yzg4NDZhNDQxNmZiNWVmNDJjZjI0MTcwMjNkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5WaWN0b3JpYSBWaWxsYWdlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGY0ZTNlNjllNTViNDA4YWFlNWY3YzJiZDNiYzhhYTYuc2V0Q29udGVudChodG1sXzA3NGM3Yzg4NDZhNDQxNmZiNWVmNDJjZjI0MTcwMjNkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2FiMzVmNmQ3ZTg3YTQ1ZDNhNWY1NWY5ODVlYzE1ZjI5LmJpbmRQb3B1cChwb3B1cF9kZjRlM2U2OWU1NWI0MDhhYWU1ZjdjMmJkM2JjOGFhNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lYzJhMWVkYTMxMzk0MjI4YWQwOThhZDcwNDAyZjVjOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcwNjM5NzIsLTc5LjMwOTkzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84YzlhMTU4NTk4OTA0ZTUxYTJkOTM2YjM5ZmUxZTljMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iODI2NTc1M2MzYjM0MWQyYjhmNTU5ZmFjYjJhNWM0YSA9ICQoJzxkaXYgaWQ9Imh0bWxfYjgyNjU3NTNjM2IzNDFkMmI4ZjU1OWZhY2IyYTVjNGEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldvb2RiaW5lIEdhcmRlbnMsUGFya3ZpZXcgSGlsbCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhjOWExNTg1OTg5MDRlNTFhMmQ5MzZiMzlmZTFlOWMxLnNldENvbnRlbnQoaHRtbF9iODI2NTc1M2MzYjM0MWQyYjhmNTU5ZmFjYjJhNWM0YSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lYzJhMWVkYTMxMzk0MjI4YWQwOThhZDcwNDAyZjVjOC5iaW5kUG9wdXAocG9wdXBfOGM5YTE1ODU5ODkwNGU1MWEyZDkzNmIzOWZlMWU5YzEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODMxOTBlMDI5OTdmNGVkNDhhMGMyNDMxN2ExMmI1ZDAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTUzNDM5MDAwMDAwMDUsLTc5LjMxODM4ODddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGE2NzQ3ODgxZGNmNDU1Yzk5YjM5MzIwMWQ4MzVhODEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzMzN2JmZWM5ZmExNDBmYzhlOWMwOTQ3YzdjODljZDEgPSAkKCc8ZGl2IGlkPSJodG1sXzczMzdiZmVjOWZhMTQwZmM4ZTljMDk0N2M3Yzg5Y2QxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Xb29kYmluZSBIZWlnaHRzIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGE2NzQ3ODgxZGNmNDU1Yzk5YjM5MzIwMWQ4MzVhODEuc2V0Q29udGVudChodG1sXzczMzdiZmVjOWZhMTQwZmM4ZTljMDk0N2M3Yzg5Y2QxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzgzMTkwZTAyOTk3ZjRlZDQ4YTBjMjQzMTdhMTJiNWQwLmJpbmRQb3B1cChwb3B1cF9kYTY3NDc4ODFkY2Y0NTVjOTliMzkzMjAxZDgzNWE4MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hYzMyY2E2M2Y2MDU0ZjBkYmFkODAyNjBlMGI5N2U1NSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY3NjM1NzM5OTk5OTk5LC03OS4yOTMwMzEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI1NjEyYjhkMzNiNTQ1NGRiNTk1NmIxNzAxYTgxZmFkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzAzZDJkNGEwYTk5ZDQ2M2E5ZGMxMTg5ZjViOWMyOWZmID0gJCgnPGRpdiBpZD0iaHRtbF8wM2QyZDRhMGE5OWQ0NjNhOWRjMTE4OWY1YjljMjlmZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhlIEJlYWNoZXMgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yNTYxMmI4ZDMzYjU0NTRkYjU5NTZiMTcwMWE4MWZhZC5zZXRDb250ZW50KGh0bWxfMDNkMmQ0YTBhOTlkNDYzYTlkYzExODlmNWI5YzI5ZmYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWMzMmNhNjNmNjA1NGYwZGJhZDgwMjYwZTBiOTdlNTUuYmluZFBvcHVwKHBvcHVwXzI1NjEyYjhkMzNiNTQ1NGRiNTk1NmIxNzAxYTgxZmFkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBjZjViMmRlNTgwZDQ2NzViN2ZlODJmNGZiOGZjNGMzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA5MDYwNCwtNzkuMzYzNDUxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mYTkyNTMyNGVmZWI0YWU1OGFmNTE4OWY5N2Q0YjY1ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNGEzNmQ1YTFkYjU0OTdkOTViYjk4OTFiZDU3ZDVhYyA9ICQoJzxkaXYgaWQ9Imh0bWxfMzRhMzZkNWExZGI1NDk3ZDk1YmI5ODkxYmQ1N2Q1YWMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxlYXNpZGUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mYTkyNTMyNGVmZWI0YWU1OGFmNTE4OWY5N2Q0YjY1Zi5zZXRDb250ZW50KGh0bWxfMzRhMzZkNWExZGI1NDk3ZDk1YmI5ODkxYmQ1N2Q1YWMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMGNmNWIyZGU1ODBkNDY3NWI3ZmU4MmY0ZmI4ZmM0YzMuYmluZFBvcHVwKHBvcHVwX2ZhOTI1MzI0ZWZlYjRhZTU4YWY1MTg5Zjk3ZDRiNjVmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzViZTNiYmEwMzhkNDQ5ZTQ4MjI5MGQwMmE2NzY0YTMxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA1MzY4OSwtNzkuMzQ5MzcxOTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWI5N2U4Y2Q5NTg2NDgzODk4ODIxMjY4YWYzNzA1ZjAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMGM0YWYzMWE5NWY5NDJhODliMmU4ODAwZmFlNTE0MDggPSAkKCc8ZGl2IGlkPSJodG1sXzBjNGFmMzFhOTVmOTQyYTg5YjJlODgwMGZhZTUxNDA4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaG9ybmNsaWZmZSBQYXJrIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWI5N2U4Y2Q5NTg2NDgzODk4ODIxMjY4YWYzNzA1ZjAuc2V0Q29udGVudChodG1sXzBjNGFmMzFhOTVmOTQyYTg5YjJlODgwMGZhZTUxNDA4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzViZTNiYmEwMzhkNDQ5ZTQ4MjI5MGQwMmE2NzY0YTMxLmJpbmRQb3B1cChwb3B1cF9hYjk3ZThjZDk1ODY0ODM4OTg4MjEyNjhhZjM3MDVmMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83MzUxZTRjMWIwNTc0Nzc4YjZhZDE3NWFlNmY2OTdkZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY4NTM0NywtNzkuMzM4MTA2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kNzFhY2FkNzNkMzI0NzljYTZhN2U4NmY5ZGZkY2QwOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hODQxZGMyNDNkYzk0YTljYTk0ZTcwZWYxNWUxNzgzYyA9ICQoJzxkaXYgaWQ9Imh0bWxfYTg0MWRjMjQzZGM5NGE5Y2E5NGU3MGVmMTVlMTc4M2MiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgVG9yb250byBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q3MWFjYWQ3M2QzMjQ3OWNhNmE3ZTg2ZjlkZmRjZDA4LnNldENvbnRlbnQoaHRtbF9hODQxZGMyNDNkYzk0YTljYTk0ZTcwZWYxNWUxNzgzYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83MzUxZTRjMWIwNTc0Nzc4YjZhZDE3NWFlNmY2OTdkZi5iaW5kUG9wdXAocG9wdXBfZDcxYWNhZDczZDMyNDc5Y2E2YTdlODZmOWRmZGNkMDgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTAyYWNjN2M0OTRjNDRhYjhhZThhZjgyZmRjYzBlYjIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Nzk1NTcxLC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTY2NTVlYjVhNDYxNDZlYjk4NzMwNWExMDI4ZTJlOWQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGExYzExYjU5NTc3NDRhM2JiNTRhYzc4YWFlODc5YzcgPSAkKCc8ZGl2IGlkPSJodG1sX2RhMWMxMWI1OTU3NzQ0YTNiYjU0YWM3OGFhZTg3OWM3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgRGFuZm9ydGggV2VzdCxSaXZlcmRhbGUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNjY1NWViNWE0NjE0NmViOTg3MzA1YTEwMjhlMmU5ZC5zZXRDb250ZW50KGh0bWxfZGExYzExYjU5NTc3NDRhM2JiNTRhYzc4YWFlODc5YzcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTAyYWNjN2M0OTRjNDRhYjhhZThhZjgyZmRjYzBlYjIuYmluZFBvcHVwKHBvcHVwXzE2NjU1ZWI1YTQ2MTQ2ZWI5ODczMDVhMTAyOGUyZTlkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M0ZWQyMGVjNjJmMTQwYWFhMGJjOTZkMTRlNjExYzIyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY4OTk4NSwtNzkuMzE1NTcxNTk5OTk5OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWIzMWY3N2MzMTdlNDllY2IyYzRmMzFmMThhMzk1ZjcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTAxYjM0MTI4ZmEwNDRlMDg0YTZkYTUxZWY0MjU2YTEgPSAkKCc8ZGl2IGlkPSJodG1sXzkwMWIzNDEyOGZhMDQ0ZTA4NGE2ZGE1MWVmNDI1NmExIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgQmVhY2hlcyBXZXN0LEluZGlhIEJhemFhciBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzliMzFmNzdjMzE3ZTQ5ZWNiMmM0ZjMxZjE4YTM5NWY3LnNldENvbnRlbnQoaHRtbF85MDFiMzQxMjhmYTA0NGUwODRhNmRhNTFlZjQyNTZhMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jNGVkMjBlYzYyZjE0MGFhYTBiYzk2ZDE0ZTYxMWMyMi5iaW5kUG9wdXAocG9wdXBfOWIzMWY3N2MzMTdlNDllY2IyYzRmMzFmMThhMzk1ZjcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfM2RmNzU3ODA2MWIwNDZhMWEwMzc5ZjNmMDdlZTdiYzYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTk1MjU1LC03OS4zNDA5MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTgxZmFhMDllYzBlNDNmZGJmNGQ1YzRmYzVhNmU4MDIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDc2ZDlhY2I4ZWVlNGFmNTg3ZDNiOWMyNjg4NDM3ZGMgPSAkKCc8ZGl2IGlkPSJodG1sX2Q3NmQ5YWNiOGVlZTRhZjU4N2QzYjljMjY4ODQzN2RjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdHVkaW8gRGlzdHJpY3QgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85ODFmYWEwOWVjMGU0M2ZkYmY0ZDVjNGZjNWE2ZTgwMi5zZXRDb250ZW50KGh0bWxfZDc2ZDlhY2I4ZWVlNGFmNTg3ZDNiOWMyNjg4NDM3ZGMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2RmNzU3ODA2MWIwNDZhMWEwMzc5ZjNmMDdlZTdiYzYuYmluZFBvcHVwKHBvcHVwXzk4MWZhYTA5ZWMwZTQzZmRiZjRkNWM0ZmM1YTZlODAyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI1NDU1NzkwYTE2NDQwY2I5ZWJhN2YxNTYwZWI4MzMyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI4MDIwNSwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84NjYyODlkMmU1MmI0ODUyYjY2MTBlOWE5M2E4MWQ3OSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80MmFlYmNmZjcxYmY0MTQ4YjUwODFhODQzMGJlZjZiOCA9ICQoJzxkaXYgaWQ9Imh0bWxfNDJhZWJjZmY3MWJmNDE0OGI1MDgxYTg0MzBiZWY2YjgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIFBhcmsgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84NjYyODlkMmU1MmI0ODUyYjY2MTBlOWE5M2E4MWQ3OS5zZXRDb250ZW50KGh0bWxfNDJhZWJjZmY3MWJmNDE0OGI1MDgxYTg0MzBiZWY2YjgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjU0NTU3OTBhMTY0NDBjYjllYmE3ZjE1NjBlYjgzMzIuYmluZFBvcHVwKHBvcHVwXzg2NjI4OWQyZTUyYjQ4NTJiNjYxMGU5YTkzYTgxZDc5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzgyMDVlNjVlYjZlOTQxMWI5NGE0YmI0ZTgyNGRmYWNhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzEyNzUxMSwtNzkuMzkwMTk3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNTY1MGQzNzliN2E0YWRkODYzZWJlM2RhNGM3NzQwMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iN2FiZDY0ZDNlOTI0MmRkOTA0ODJiZDBlYTUwYmVmMyA9ICQoJzxkaXYgaWQ9Imh0bWxfYjdhYmQ2NGQzZTkyNDJkZDkwNDgyYmQwZWE1MGJlZjMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUgTm9ydGggQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hNTY1MGQzNzliN2E0YWRkODYzZWJlM2RhNGM3NzQwMS5zZXRDb250ZW50KGh0bWxfYjdhYmQ2NGQzZTkyNDJkZDkwNDgyYmQwZWE1MGJlZjMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODIwNWU2NWViNmU5NDExYjk0YTRiYjRlODI0ZGZhY2EuYmluZFBvcHVwKHBvcHVwX2E1NjUwZDM3OWI3YTRhZGQ4NjNlYmUzZGE0Yzc3NDAxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzA3M2YzZTJiYzQ2ZjRhZTFiZTcwMzRkZGZkYTQ3YWRjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE1MzgzNCwtNzkuNDA1Njc4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjIwZTdkODE2M2NjNDEwN2FlOGUzMjUxZWE0OTYzYzIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGNiM2ViMDgzMGEwNDVjMDgxYjM2MWJjNWViOGRlMDQgPSAkKCc8ZGl2IGlkPSJodG1sXzRjYjNlYjA4MzBhMDQ1YzA4MWIzNjFiYzVlYjhkZTA0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aCBUb3JvbnRvIFdlc3QgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iMjBlN2Q4MTYzY2M0MTA3YWU4ZTMyNTFlYTQ5NjNjMi5zZXRDb250ZW50KGh0bWxfNGNiM2ViMDgzMGEwNDVjMDgxYjM2MWJjNWViOGRlMDQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDczZjNlMmJjNDZmNGFlMWJlNzAzNGRkZmRhNDdhZGMuYmluZFBvcHVwKHBvcHVwX2IyMGU3ZDgxNjNjYzQxMDdhZThlMzI1MWVhNDk2M2MyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M4ZDEzMmEyYjY4YzRhOTg4MzEwZjM2MDQ3OTAyNzlkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA0MzI0NCwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yMmFmZDVlZmZmYTQ0MGY5OTI5MjljZDBjMDZlMGQzYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jNDQ4NGRlMzYyM2Q0NGM0YmVlN2JiOGQyOGExMDZlOSA9ICQoJzxkaXYgaWQ9Imh0bWxfYzQ0ODRkZTM2MjNkNDRjNGJlZTdiYjhkMjhhMTA2ZTkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yMmFmZDVlZmZmYTQ0MGY5OTI5MjljZDBjMDZlMGQzYS5zZXRDb250ZW50KGh0bWxfYzQ0ODRkZTM2MjNkNDRjNGJlZTdiYjhkMjhhMTA2ZTkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzhkMTMyYTJiNjhjNGE5ODgzMTBmMzYwNDc5MDI3OWQuYmluZFBvcHVwKHBvcHVwXzIyYWZkNWVmZmZhNDQwZjk5MjkyOWNkMGMwNmUwZDNhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI3MDBkOGY4MDZkNzQyMzdiODJiYjQ1ZDI0NDgxODBiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg5NTc0MywtNzkuMzgzMTU5OTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNGY0OWM4YzE2ODAwNDlkYzgxZjIzYTYxMmNmZWQ4YjggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODM0MmNjZTNhODJmNGYwNzhlNmYzMjljYjYzZTk3OGYgPSAkKCc8ZGl2IGlkPSJodG1sXzgzNDJjY2UzYTgyZjRmMDc4ZTZmMzI5Y2I2M2U5NzhmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb29yZSBQYXJrLFN1bW1lcmhpbGwgRWFzdCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRmNDljOGMxNjgwMDQ5ZGM4MWYyM2E2MTJjZmVkOGI4LnNldENvbnRlbnQoaHRtbF84MzQyY2NlM2E4MmY0ZjA3OGU2ZjMyOWNiNjNlOTc4Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yNzAwZDhmODA2ZDc0MjM3YjgyYmI0NWQyNDQ4MTgwYi5iaW5kUG9wdXAocG9wdXBfNGY0OWM4YzE2ODAwNDlkYzgxZjIzYTYxMmNmZWQ4YjgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDBlNTcyZmM5NmMzNDdlNGJhMWFlYmY3NWFjYWYyZTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42ODY0MTIyOTk5OTk5OSwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMjYxNjUxOGYyOGQ0ZDRkOTY1MWU5NmExNmY5YmY0MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xMjUxZDYxYTg2NTQ0Y2I2YTQ5NDQ0ZDJkOWJjZDQ3YyA9ICQoJzxkaXYgaWQ9Imh0bWxfMTI1MWQ2MWE4NjU0NGNiNmE0OTQ0NGQyZDliY2Q0N2MiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRlZXIgUGFyayxGb3Jlc3QgSGlsbCBTRSxSYXRobmVsbHksU291dGggSGlsbCxTdW1tZXJoaWxsIFdlc3QgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMjYxNjUxOGYyOGQ0ZDRkOTY1MWU5NmExNmY5YmY0Mi5zZXRDb250ZW50KGh0bWxfMTI1MWQ2MWE4NjU0NGNiNmE0OTQ0NGQyZDliY2Q0N2MpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDBlNTcyZmM5NmMzNDdlNGJhMWFlYmY3NWFjYWYyZTcuYmluZFBvcHVwKHBvcHVwX2MyNjE2NTE4ZjI4ZDRkNGQ5NjUxZTk2YTE2ZjliZjQyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIyNzQ5OGU4YjQ4ZjRhMDU4ODg4M2QyNTNmNmM2ZTJjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjc5NTYyNiwtNzkuMzc3NTI5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjAxNmYwNWQyNjhiNDk1MmE5MWIzMjUzZDY2N2I3NzkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWRlZDEzNDYxYzY5NGY4Yzg0ODg4ZGVlOWYxNTVhMWIgPSAkKCc8ZGl2IGlkPSJodG1sXzVkZWQxMzQ2MWM2OTRmOGM4NDg4OGRlZTlmMTU1YTFiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlZGFsZSBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2YwMTZmMDVkMjY4YjQ5NTJhOTFiMzI1M2Q2NjdiNzc5LnNldENvbnRlbnQoaHRtbF81ZGVkMTM0NjFjNjk0ZjhjODQ4ODhkZWU5ZjE1NWExYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yMjc0OThlOGI0OGY0YTA1ODg4ODNkMjUzZjZjNmUyYy5iaW5kUG9wdXAocG9wdXBfZjAxNmYwNWQyNjhiNDk1MmE5MWIzMjUzZDY2N2I3NzkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjdlZTlhOGYyODI5NGRlNGI5OTBkMGMwMDMwYTVjMGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Njc5NjcsLTc5LjM2NzY3NTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWFiZWVjNWFiYTdlNGNkMDkzZTgwMTNkNWRkOTBkNDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDc0ZWIwYzIzYWY1NGM5NDk0YmM5NTk1MGYyYzUxZjQgPSAkKCc8ZGl2IGlkPSJodG1sXzA3NGViMGMyM2FmNTRjOTQ5NGJjOTU5NTBmMmM1MWY0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYWJiYWdldG93bixTdC4gSmFtZXMgVG93biBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVhYmVlYzVhYmE3ZTRjZDA5M2U4MDEzZDVkZDkwZDQ5LnNldENvbnRlbnQoaHRtbF8wNzRlYjBjMjNhZjU0Yzk0OTRiYzk1OTUwZjJjNTFmNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iN2VlOWE4ZjI4Mjk0ZGU0Yjk5MGQwYzAwMzBhNWMwYi5iaW5kUG9wdXAocG9wdXBfNWFiZWVjNWFiYTdlNGNkMDkzZTgwMTNkNWRkOTBkNDkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmJiZGQ3MjQ5NjhiNGQyNGFhZTYwYWE5ZWVjMGNiMmYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjU4NTk5LC03OS4zODMxNTk5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85YjQ1OTk3YjQ5MWM0YWFmYmVhMDQzYzljNjA0OTdiZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iZDhhMjIxNzNkNzc0MWU3ODA5ZjM3NjdiYWQwNTg3YSA9ICQoJzxkaXYgaWQ9Imh0bWxfYmQ4YTIyMTczZDc3NDFlNzgwOWYzNzY3YmFkMDU4N2EiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNodXJjaCBhbmQgV2VsbGVzbGV5IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWI0NTk5N2I0OTFjNGFhZmJlYTA0M2M5YzYwNDk3YmQuc2V0Q29udGVudChodG1sX2JkOGEyMjE3M2Q3NzQxZTc4MDlmMzc2N2JhZDA1ODdhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJiYmRkNzI0OTY4YjRkMjRhYWU2MGFhOWVlYzBjYjJmLmJpbmRQb3B1cChwb3B1cF85YjQ1OTk3YjQ5MWM0YWFmYmVhMDQzYzljNjA0OTdiZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80NDM4MWIzNDMyY2M0YjVmYTMyZmJjZjJjMWZjMzJlMyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1NDI1OTksLTc5LjM2MDYzNTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzE3ZjMwNDk0YmVmNGE0NmFlMWU0NjUxODBmMDIwM2YgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2M4ZTliMTcxNTZlNGMxNDlhN2Y2MThkNzI3Mjc0NTUgPSAkKCc8ZGl2IGlkPSJodG1sX2NjOGU5YjE3MTU2ZTRjMTQ5YTdmNjE4ZDcyNzI3NDU1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQsUmVnZW50IFBhcmsgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMTdmMzA0OTRiZWY0YTQ2YWUxZTQ2NTE4MGYwMjAzZi5zZXRDb250ZW50KGh0bWxfY2M4ZTliMTcxNTZlNGMxNDlhN2Y2MThkNzI3Mjc0NTUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDQzODFiMzQzMmNjNGI1ZmEzMmZiY2YyYzFmYzMyZTMuYmluZFBvcHVwKHBvcHVwX2MxN2YzMDQ5NGJlZjRhNDZhZTFlNDY1MTgwZjAyMDNmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFiYWEyMTg1NzA0MDQyZTU4OGE1ZmIyODg1OWI3YTY3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjU3MTYxOCwtNzkuMzc4OTM3MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTBkMTAyZmI4MDUyNDBiYzlmMWI3MmU4M2UxZmQyMjIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjBiMDc1YTdlYjk3NDNjN2I4M2M3YWRlMjFjYjU1ODAgPSAkKCc8ZGl2IGlkPSJodG1sX2YwYjA3NWE3ZWI5NzQzYzdiODNjN2FkZTIxY2I1NTgwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SeWVyc29uLEdhcmRlbiBEaXN0cmljdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2EwZDEwMmZiODA1MjQwYmM5ZjFiNzJlODNlMWZkMjIyLnNldENvbnRlbnQoaHRtbF9mMGIwNzVhN2ViOTc0M2M3YjgzYzdhZGUyMWNiNTU4MCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xYmFhMjE4NTcwNDA0MmU1ODhhNWZiMjg4NTliN2E2Ny5iaW5kUG9wdXAocG9wdXBfYTBkMTAyZmI4MDUyNDBiYzlmMWI3MmU4M2UxZmQyMjIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjcxMGI3MzZmZjdjNDNhODk2YjhkYThiMmZkMTBkMTcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTE0OTM5LC03OS4zNzU0MTc5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzJiMDhlZmI2NzQyYjRmMDhiMGViN2JmMmFmMWY2YmYxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2NjNDgyN2FmMWYzZjQ1YmM4ZTJhZjdkNzI0NDA5N2QzID0gJCgnPGRpdiBpZD0iaHRtbF9jYzQ4MjdhZjFmM2Y0NWJjOGUyYWY3ZDcyNDQwOTdkMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3QuIEphbWVzIFRvd24gQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yYjA4ZWZiNjc0MmI0ZjA4YjBlYjdiZjJhZjFmNmJmMS5zZXRDb250ZW50KGh0bWxfY2M0ODI3YWYxZjNmNDViYzhlMmFmN2Q3MjQ0MDk3ZDMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjcxMGI3MzZmZjdjNDNhODk2YjhkYThiMmZkMTBkMTcuYmluZFBvcHVwKHBvcHVwXzJiMDhlZmI2NzQyYjRmMDhiMGViN2JmMmFmMWY2YmYxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk2YzcyZWU4MWE0MzRjZWI5NGFiYzIxMWMzMTEwN2NjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ0NzcwNzk5OTk5OTk2LC03OS4zNzMzMDY0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzY3ZmI5ZTc4NmFhMjQzNTNhMGQ3NTNmZWI2ODMyNWYwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Q3ZGMyOTU4ZWYwODRjYjJhYzc3ZjI2NjU3MzYxODZkID0gJCgnPGRpdiBpZD0iaHRtbF9kN2RjMjk1OGVmMDg0Y2IyYWM3N2YyNjY1NzM2MTg2ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVyY3p5IFBhcmsgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82N2ZiOWU3ODZhYTI0MzUzYTBkNzUzZmViNjgzMjVmMC5zZXRDb250ZW50KGh0bWxfZDdkYzI5NThlZjA4NGNiMmFjNzdmMjY2NTczNjE4NmQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTZjNzJlZTgxYTQzNGNlYjk0YWJjMjExYzMxMTA3Y2MuYmluZFBvcHVwKHBvcHVwXzY3ZmI5ZTc4NmFhMjQzNTNhMGQ3NTNmZWI2ODMyNWYwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IwMTFmM2RkMmM2YzRjNzRhODFiZTI0NGIyMjQ0NDRlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjU3OTUyNCwtNzkuMzg3MzgyNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80OGUwNjlhNGE3OWI0MTMxOTUyYzI4YjU4OGZlNzFiMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xMGY1ZGEyMDc1MjI0Mjg0OWM2ODVlOTlhN2NlNzhjZiA9ICQoJzxkaXYgaWQ9Imh0bWxfMTBmNWRhMjA3NTIyNDI4NDljNjg1ZTk5YTdjZTc4Y2YiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNlbnRyYWwgQmF5IFN0cmVldCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQ4ZTA2OWE0YTc5YjQxMzE5NTJjMjhiNTg4ZmU3MWIzLnNldENvbnRlbnQoaHRtbF8xMGY1ZGEyMDc1MjI0Mjg0OWM2ODVlOTlhN2NlNzhjZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iMDExZjNkZDJjNmM0Yzc0YTgxYmUyNDRiMjI0NDQ0ZS5iaW5kUG9wdXAocG9wdXBfNDhlMDY5YTRhNzliNDEzMTk1MmMyOGI1ODhmZTcxYjMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWViM2Y1MTViMDcyNDA3YWE4NDcyNWI3NzJkZmY1YTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTA1NzEyMDAwMDAwMSwtNzkuMzg0NTY3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jZjZlYmJhZjcyNGI0ZjAyOTE4ODExNWJkNmY5MDU2YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85ZTc4ODU4MDdiOWU0ZWI5YWM4MWUxMmYzNzE1ZWU3YyA9ICQoJzxkaXYgaWQ9Imh0bWxfOWU3ODg1ODA3YjllNGViOWFjODFlMTJmMzcxNWVlN2MiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZWxhaWRlLEtpbmcsUmljaG1vbmQgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jZjZlYmJhZjcyNGI0ZjAyOTE4ODExNWJkNmY5MDU2YS5zZXRDb250ZW50KGh0bWxfOWU3ODg1ODA3YjllNGViOWFjODFlMTJmMzcxNWVlN2MpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWViM2Y1MTViMDcyNDA3YWE4NDcyNWI3NzJkZmY1YTAuYmluZFBvcHVwKHBvcHVwX2NmNmViYmFmNzI0YjRmMDI5MTg4MTE1YmQ2ZjkwNTZhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQxMWZiMWU1ZTlkYzRkYjc5YjVkZmRmNmE0YzljNGU1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQwODE1NywtNzkuMzgxNzUyMjk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDFiNjA5OGM3OTgzNDY5MDlmY2ZlNGU1MzkzNjkxNmYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmZmYTY1MTcxYmZiNDk0N2FkYTZjY2Q5MDRkOTQzNGQgPSAkKCc8ZGl2IGlkPSJodG1sX2ZmZmE2NTE3MWJmYjQ5NDdhZGE2Y2NkOTA0ZDk0MzRkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQgRWFzdCxUb3JvbnRvIElzbGFuZHMsVW5pb24gU3RhdGlvbiBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQxYjYwOThjNzk4MzQ2OTA5ZmNmZTRlNTM5MzY5MTZmLnNldENvbnRlbnQoaHRtbF9mZmZhNjUxNzFiZmI0OTQ3YWRhNmNjZDkwNGQ5NDM0ZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MTFmYjFlNWU5ZGM0ZGI3OWI1ZGZkZjZhNGM5YzRlNS5iaW5kUG9wdXAocG9wdXBfNDFiNjA5OGM3OTgzNDY5MDlmY2ZlNGU1MzkzNjkxNmYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjlkZDc0NzFmMjgxNDQ2YTg4ZjY3MzlhZGMzMmJkMjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDcxNzY4LC03OS4zODE1NzY0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zYWUyNzI1YTU5NTE0NTUyYjM2YTk4YWE0MzY3MDFlMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mOTM5ZjY1MmVlYzQ0MGI0Yjc2MWJhYzVhYmRhOWFjOCA9ICQoJzxkaXYgaWQ9Imh0bWxfZjkzOWY2NTJlZWM0NDBiNGI3NjFiYWM1YWJkYTlhYzgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRlc2lnbiBFeGNoYW5nZSxUb3JvbnRvIERvbWluaW9uIENlbnRyZSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNhZTI3MjVhNTk1MTQ1NTJiMzZhOThhYTQzNjcwMWUwLnNldENvbnRlbnQoaHRtbF9mOTM5ZjY1MmVlYzQ0MGI0Yjc2MWJhYzVhYmRhOWFjOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iOWRkNzQ3MWYyODE0NDZhODhmNjczOWFkYzMyYmQyNy5iaW5kUG9wdXAocG9wdXBfM2FlMjcyNWE1OTUxNDU1MmIzNmE5OGFhNDM2NzAxZTApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODZlNTBlYjAzZGRlNDczMjlhMTBlMWUyODJiZmQ4YjEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDgxOTg1LC03OS4zNzk4MTY5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83MDgwMzZmOTdjNzE0YjA0ODY4MGMxNjJiY2YzZGU4MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81NmY0MTQ2NjQzMWY0ZDEwOGU3MTA5OTljZTBkZTk2NiA9ICQoJzxkaXYgaWQ9Imh0bWxfNTZmNDE0NjY0MzFmNGQxMDhlNzEwOTk5Y2UwZGU5NjYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvbW1lcmNlIENvdXJ0LFZpY3RvcmlhIEhvdGVsIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzA4MDM2Zjk3YzcxNGIwNDg2ODBjMTYyYmNmM2RlODIuc2V0Q29udGVudChodG1sXzU2ZjQxNDY2NDMxZjRkMTA4ZTcxMDk5OWNlMGRlOTY2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzg2ZTUwZWIwM2RkZTQ3MzI5YTEwZTFlMjgyYmZkOGIxLmJpbmRQb3B1cChwb3B1cF83MDgwMzZmOTdjNzE0YjA0ODY4MGMxNjJiY2YzZGU4Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xMDJiNWQ5YTUyMjc0NDg1YTFjNzVmY2ExMzU4NDUzNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjczMzI4MjUsLTc5LjQxOTc0OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDVhNzJmMjRiMmM4NGRhZGE1ZTYxOWJhYWM5MDk4ZDUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDE5ZDliMWQyZDdlNDFjNWJjNDAxNGIzOWI3YmNhOGQgPSAkKCc8ZGl2IGlkPSJodG1sXzAxOWQ5YjFkMmQ3ZTQxYzViYzQwMTRiMzliN2JjYThkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWRmb3JkIFBhcmssTGF3cmVuY2UgTWFub3IgRWFzdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQ1YTcyZjI0YjJjODRkYWRhNWU2MTliYWFjOTA5OGQ1LnNldENvbnRlbnQoaHRtbF8wMTlkOWIxZDJkN2U0MWM1YmM0MDE0YjM5YjdiY2E4ZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xMDJiNWQ5YTUyMjc0NDg1YTFjNzVmY2ExMzU4NDUzNy5iaW5kUG9wdXAocG9wdXBfNDVhNzJmMjRiMmM4NGRhZGE1ZTYxOWJhYWM5MDk4ZDUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDA4OTgwMWMyYTg0NDY5ZWJhNDVmYWIzNzdiNjJlZjQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MTE2OTQ4LC03OS40MTY5MzU1OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iZjk4YTlhZDhkYmY0YWFlYmE1M2MxNTM2MTc3ZDk5MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xMjIxNGY2ZDFjY2M0YWYxOGFmNzc5YmRkNzNiMjJkNyA9ICQoJzxkaXYgaWQ9Imh0bWxfMTIyMTRmNmQxY2NjNGFmMThhZjc3OWJkZDczYjIyZDciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJvc2VsYXduIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYmY5OGE5YWQ4ZGJmNGFhZWJhNTNjMTUzNjE3N2Q5OTIuc2V0Q29udGVudChodG1sXzEyMjE0ZjZkMWNjYzRhZjE4YWY3NzliZGQ3M2IyMmQ3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzAwODk4MDFjMmE4NDQ2OWViYTQ1ZmFiMzc3YjYyZWY0LmJpbmRQb3B1cChwb3B1cF9iZjk4YTlhZDhkYmY0YWFlYmE1M2MxNTM2MTc3ZDk5Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MmI2YjU1NzVmMDQ0NWQ4YWZlNDJhOTYyOGRlOTc4ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5Njk0NzYsLTc5LjQxMTMwNzIwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2VhMjgxNjg1ZWNjMjRkMmY5ZjBiMjc5NjA4NzU0ODhiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzgzMWQzOWQxYzY2ZTQyMTE5ZDYyZjc3NzY4ODg1MGZhID0gJCgnPGRpdiBpZD0iaHRtbF84MzFkMzlkMWM2NmU0MjExOWQ2MmY3Nzc2ODg4NTBmYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rm9yZXN0IEhpbGwgTm9ydGgsRm9yZXN0IEhpbGwgV2VzdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2VhMjgxNjg1ZWNjMjRkMmY5ZjBiMjc5NjA4NzU0ODhiLnNldENvbnRlbnQoaHRtbF84MzFkMzlkMWM2NmU0MjExOWQ2MmY3Nzc2ODg4NTBmYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MmI2YjU1NzVmMDQ0NWQ4YWZlNDJhOTYyOGRlOTc4ZS5iaW5kUG9wdXAocG9wdXBfZWEyODE2ODVlY2MyNGQyZjlmMGIyNzk2MDg3NTQ4OGIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTlkZjc2YTVkNjEwNDIyM2JlOWU4YjMwYmVjNjMzYmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NzI3MDk3LC03OS40MDU2Nzg0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iYjE3ODgzODY4NDk0OGU0YmMzZGQxMGQwNTY2YjU2ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85MmQxNzEwNTgwZjE0M2RlYmY4MTRkZjIwNDViZjA5NSA9ICQoJzxkaXYgaWQ9Imh0bWxfOTJkMTcxMDU4MGYxNDNkZWJmODE0ZGYyMDQ1YmYwOTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRoZSBBbm5leCxOb3J0aCBNaWR0b3duLFlvcmt2aWxsZSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2JiMTc4ODM4Njg0OTQ4ZTRiYzNkZDEwZDA1NjZiNTZmLnNldENvbnRlbnQoaHRtbF85MmQxNzEwNTgwZjE0M2RlYmY4MTRkZjIwNDViZjA5NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lOWRmNzZhNWQ2MTA0MjIzYmU5ZThiMzBiZWM2MzNiYi5iaW5kUG9wdXAocG9wdXBfYmIxNzg4Mzg2ODQ5NDhlNGJjM2RkMTBkMDU2NmI1NmYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTY0MGIyNjI5ZDQ0NGE3MGE2ODY3MDQ2NmNkZDhmYmYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjI2OTU2LC03OS40MDAwNDkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk4Y2UwN2JlNDNmNTQ4NTdhOTAwYmFhYzYxOGU4YTVlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JjZTMxZGYwNDkyMjQyY2U5ODJhOThkZjk5NmU4YzcxID0gJCgnPGRpdiBpZD0iaHRtbF9iY2UzMWRmMDQ5MjI0MmNlOTgyYTk4ZGY5OTZlOGM3MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGFyYm9yZCxVbml2ZXJzaXR5IG9mIFRvcm9udG8gQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85OGNlMDdiZTQzZjU0ODU3YTkwMGJhYWM2MThlOGE1ZS5zZXRDb250ZW50KGh0bWxfYmNlMzFkZjA0OTIyNDJjZTk4MmE5OGRmOTk2ZThjNzEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTY0MGIyNjI5ZDQ0NGE3MGE2ODY3MDQ2NmNkZDhmYmYuYmluZFBvcHVwKHBvcHVwXzk4Y2UwN2JlNDNmNTQ4NTdhOTAwYmFhYzYxOGU4YTVlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U4ZDQ1YWNjYzE4NzRkNDdhNTk3YzY5ZWRiNjY5YjFjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUzMjA1NywtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jYTY2YTE1YmQ2YzM0ZWVjYmJkNTFmZjgxZjFkZTAyNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mOTJlMzc0ZDkwMDg0N2IyOTA5MTlkYWIzOWMzNTZjZCA9ICQoJzxkaXYgaWQ9Imh0bWxfZjkyZTM3NGQ5MDA4NDdiMjkwOTE5ZGFiMzljMzU2Y2QiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNoaW5hdG93bixHcmFuZ2UgUGFyayxLZW5zaW5ndG9uIE1hcmtldCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2NhNjZhMTViZDZjMzRlZWNiYmQ1MWZmODFmMWRlMDI1LnNldENvbnRlbnQoaHRtbF9mOTJlMzc0ZDkwMDg0N2IyOTA5MTlkYWIzOWMzNTZjZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lOGQ0NWFjY2MxODc0ZDQ3YTU5N2M2OWVkYjY2OWIxYy5iaW5kUG9wdXAocG9wdXBfY2E2NmExNWJkNmMzNGVlY2JiZDUxZmY4MWYxZGUwMjUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMGI0MDk3NjAxNWU3NDViNzk4OGIwNDA2MmMxZDM4YWQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Mjg5NDY3LC03OS4zOTQ0MTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2ZkY2YwMGQ2MjhiNTRkZmJiODcwMGQ3MjYzMWE0ZWFkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzM0NmVkNjhkYjU5MzRlNTJiN2I4NTkzMWFiMTUwYmI2ID0gJCgnPGRpdiBpZD0iaHRtbF8zNDZlZDY4ZGI1OTM0ZTUyYjdiODU5MzFhYjE1MGJiNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q04gVG93ZXIsQmF0aHVyc3QgUXVheSxJc2xhbmQgYWlycG9ydCxIYXJib3VyZnJvbnQgV2VzdCxLaW5nIGFuZCBTcGFkaW5hLFJhaWx3YXkgTGFuZHMsU291dGggTmlhZ2FyYSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZkY2YwMGQ2MjhiNTRkZmJiODcwMGQ3MjYzMWE0ZWFkLnNldENvbnRlbnQoaHRtbF8zNDZlZDY4ZGI1OTM0ZTUyYjdiODU5MzFhYjE1MGJiNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wYjQwOTc2MDE1ZTc0NWI3OTg4YjA0MDYyYzFkMzhhZC5iaW5kUG9wdXAocG9wdXBfZmRjZjAwZDYyOGI1NGRmYmI4NzAwZDcyNjMxYTRlYWQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZWM3MzNhNDlhZWQ0NDY5NDg0YTgzYjJhMzg3ZmI3OTUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDY0MzUyLC03OS4zNzQ4NDU5OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82MTc4NGMxMDY0MjA0ODAwYjY1YTUwMWIyYjVhMjE0ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jN2YzNDk4MTc1ZmI0NTEyYjNmYTUyMDNjYjViMzZiNCA9ICQoJzxkaXYgaWQ9Imh0bWxfYzdmMzQ5ODE3NWZiNDUxMmIzZmE1MjAzY2I1YjM2YjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlN0biBBIFBPIEJveGVzIDI1IFRoZSBFc3BsYW5hZGUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82MTc4NGMxMDY0MjA0ODAwYjY1YTUwMWIyYjVhMjE0ZC5zZXRDb250ZW50KGh0bWxfYzdmMzQ5ODE3NWZiNDUxMmIzZmE1MjAzY2I1YjM2YjQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZWM3MzNhNDlhZWQ0NDY5NDg0YTgzYjJhMzg3ZmI3OTUuYmluZFBvcHVwKHBvcHVwXzYxNzg0YzEwNjQyMDQ4MDBiNjVhNTAxYjJiNWEyMTRkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNmMzdiNzgzMmY0NzQwMDQ5MWY0OGNlOTY3Y2Y5M2UyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ4NDI5MiwtNzkuMzgyMjgwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lNTJiMjFmZjBmNzI0ZTMxYjgzYjcyYmRmNDhhMjk0ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kY2Y5ZTk1YWZiODg0YmI3YWE1MjE2ZDA5NTJkYjA5MyA9ICQoJzxkaXYgaWQ9Imh0bWxfZGNmOWU5NWFmYjg4NGJiN2FhNTIxNmQwOTUyZGIwOTMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZpcnN0IENhbmFkaWFuIFBsYWNlLFVuZGVyZ3JvdW5kIGNpdHkgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lNTJiMjFmZjBmNzI0ZTMxYjgzYjcyYmRmNDhhMjk0ZC5zZXRDb250ZW50KGh0bWxfZGNmOWU5NWFmYjg4NGJiN2FhNTIxNmQwOTUyZGIwOTMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2YzN2I3ODMyZjQ3NDAwNDkxZjQ4Y2U5NjdjZjkzZTIuYmluZFBvcHVwKHBvcHVwX2U1MmIyMWZmMGY3MjRlMzFiODNiNzJiZGY0OGEyOTRkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBkZDhlYTQ1ZjYyYjQ0YTQ5OGFkZDdiMjgxZmJlZjAxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE4NTE3OTk5OTk5OTk2LC03OS40NjQ3NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80YjNmYmRhODlmYjk0MjQyODY5NWEyN2QxYmNiOTFiYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84ODQ3ODMwNDliNzE0NTEzYjdiNGZiMzI3MTViOTljZSA9ICQoJzxkaXYgaWQ9Imh0bWxfODg0NzgzMDQ5YjcxNDUxM2I3YjRmYjMyNzE1Yjk5Y2UiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIEhlaWdodHMsTGF3cmVuY2UgTWFub3IgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80YjNmYmRhODlmYjk0MjQyODY5NWEyN2QxYmNiOTFiYS5zZXRDb250ZW50KGh0bWxfODg0NzgzMDQ5YjcxNDUxM2I3YjRmYjMyNzE1Yjk5Y2UpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMGRkOGVhNDVmNjJiNDRhNDk4YWRkN2IyODFmYmVmMDEuYmluZFBvcHVwKHBvcHVwXzRiM2ZiZGE4OWZiOTQyNDI4Njk1YTI3ZDFiY2I5MWJhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk1NGNjYjg0NWRiNzRiZjM4MDYxYTE5Mzg0ZDZkNzNiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA5NTc3LC03OS40NDUwNzI1OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mNTVhZDUyNjBjYjI0MGM2YmFhNDIyY2JlNGY5NjJlNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84ODljZjY1MzI5YTQ0MDI2ODg2Mjg3YWJiMDliNDQwZCA9ICQoJzxkaXYgaWQ9Imh0bWxfODg5Y2Y2NTMyOWE0NDAyNjg4NjI4N2FiYjA5YjQ0MGQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdsZW5jYWlybiBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y1NWFkNTI2MGNiMjQwYzZiYWE0MjJjYmU0Zjk2MmU0LnNldENvbnRlbnQoaHRtbF84ODljZjY1MzI5YTQ0MDI2ODg2Mjg3YWJiMDliNDQwZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85NTRjY2I4NDVkYjc0YmYzODA2MWExOTM4NGQ2ZDczYi5iaW5kUG9wdXAocG9wdXBfZjU1YWQ1MjYwY2IyNDBjNmJhYTQyMmNiZTRmOTYyZTQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmY4Nzc3ZDMxNTVlNGI3ZTk5OWVlOTM1ODQ1Mzg2OTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTM3ODEzLC03OS40MjgxOTE0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mZjk0OWZiOTIwODA0ZmZiYWE1ZTQ4N2FhZDVmMzg1NiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85ZWZlMTk4OTRkMmI0NDlkODAzMmJhYzVhYTQ5NzBmZCA9ICQoJzxkaXYgaWQ9Imh0bWxfOWVmZTE5ODk0ZDJiNDQ5ZDgwMzJiYWM1YWE0OTcwZmQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWV3b29kLUNlZGFydmFsZSBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZmOTQ5ZmI5MjA4MDRmZmJhYTVlNDg3YWFkNWYzODU2LnNldENvbnRlbnQoaHRtbF85ZWZlMTk4OTRkMmI0NDlkODAzMmJhYzVhYTQ5NzBmZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yZjg3NzdkMzE1NWU0YjdlOTk5ZWU5MzU4NDUzODY5MC5iaW5kUG9wdXAocG9wdXBfZmY5NDlmYjkyMDgwNGZmYmFhNWU0ODdhYWQ1ZjM4NTYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTBkZDlmYjEzNWM0NDlhYTgyMzYxNTliNTg2M2ZiYzIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42ODkwMjU2LC03OS40NTM1MTJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGFlYTYzZDAyOWUxNDg2Nzk1ZWNjMDQ4NTY0ZGFiMWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTRjZGFlNDdhMzEwNDZiZWFiOTlhNmJkZmZlYTc1YTUgPSAkKCc8ZGl2IGlkPSJodG1sXzE0Y2RhZTQ3YTMxMDQ2YmVhYjk5YTZiZGZmZWE3NWE1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYWxlZG9uaWEtRmFpcmJhbmtzIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGFlYTYzZDAyOWUxNDg2Nzk1ZWNjMDQ4NTY0ZGFiMWMuc2V0Q29udGVudChodG1sXzE0Y2RhZTQ3YTMxMDQ2YmVhYjk5YTZiZGZmZWE3NWE1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkwZGQ5ZmIxMzVjNDQ5YWE4MjM2MTU5YjU4NjNmYmMyLmJpbmRQb3B1cChwb3B1cF84YWVhNjNkMDI5ZTE0ODY3OTVlY2MwNDg1NjRkYWIxYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mZTE3NGZkNTk2YWM0ZWI0OTkxMGVkNzdmYTlhNDM0OSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2OTU0MiwtNzkuNDIyNTYzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83M2ExNWY3ZjRlOTg0MzIxOWY3NTE3NzNiZDU3ZDQ0MSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iYzc1OWZmN2M2ZWU0ZWE2YjQ5YzJlOGNmZWM1ZDQzOCA9ICQoJzxkaXYgaWQ9Imh0bWxfYmM3NTlmZjdjNmVlNGVhNmI0OWMyZThjZmVjNWQ0MzgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNocmlzdGllIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzNhMTVmN2Y0ZTk4NDMyMTlmNzUxNzczYmQ1N2Q0NDEuc2V0Q29udGVudChodG1sX2JjNzU5ZmY3YzZlZTRlYTZiNDljMmU4Y2ZlYzVkNDM4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZlMTc0ZmQ1OTZhYzRlYjQ5OTEwZWQ3N2ZhOWE0MzQ5LmJpbmRQb3B1cChwb3B1cF83M2ExNWY3ZjRlOTg0MzIxOWY3NTE3NzNiZDU3ZDQ0MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kZTk2NDIzYjkwNjY0YzU0OWIyMjQzMjAyMDI3YzU3ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2OTAwNTEwMDAwMDAxLC03OS40NDIyNTkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2EwMzU1MTE4MGEzMjRlYmNiYWY1ZDkwMmU0ODY0ZGJhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzlmNWY0NmVlMDJmMjRjYjc4ZGQ1NDU2NzE1NmZhMmI0ID0gJCgnPGRpdiBpZD0iaHRtbF85ZjVmNDZlZTAyZjI0Y2I3OGRkNTQ1NjcxNTZmYTJiNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG92ZXJjb3VydCBWaWxsYWdlLER1ZmZlcmluIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTAzNTUxMTgwYTMyNGViY2JhZjVkOTAyZTQ4NjRkYmEuc2V0Q29udGVudChodG1sXzlmNWY0NmVlMDJmMjRjYjc4ZGQ1NDU2NzE1NmZhMmI0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2RlOTY0MjNiOTA2NjRjNTQ5YjIyNDMyMDIwMjdjNTdlLmJpbmRQb3B1cChwb3B1cF9hMDM1NTExODBhMzI0ZWJjYmFmNWQ5MDJlNDg2NGRiYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kYTI0YmYyMDQ5MzI0NDA1YjRkY2YxOWQ2YTk0YjZkNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY0NzkyNjcwMDAwMDAwNiwtNzkuNDE5NzQ5N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zNzM3Njg0NDE5ZjQ0NWQ2ODA4ZTdiY2MxMzdlMDhkOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zYzU3ZTBjNzU1ODc0ZDFiYWMzNDAwYjJjM2U3ZmRiYyA9ICQoJzxkaXYgaWQ9Imh0bWxfM2M1N2UwYzc1NTg3NGQxYmFjMzQwMGIyYzNlN2ZkYmMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxpdHRsZSBQb3J0dWdhbCxUcmluaXR5IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzczNzY4NDQxOWY0NDVkNjgwOGU3YmNjMTM3ZTA4ZDkuc2V0Q29udGVudChodG1sXzNjNTdlMGM3NTU4NzRkMWJhYzM0MDBiMmMzZTdmZGJjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2RhMjRiZjIwNDkzMjQ0MDViNGRjZjE5ZDZhOTRiNmQ3LmJpbmRQb3B1cChwb3B1cF8zNzM3Njg0NDE5ZjQ0NWQ2ODA4ZTdiY2MxMzdlMDhkOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mMjhiYWQ0ODk3ODA0ZTQ3YmFiZDdkNTI1MTE0M2JlOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYzNjg0NzIsLTc5LjQyODE5MTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFkY2E3MDBiYWM1ZDQwMjE5ZTYwYTRhZGYzZjZjM2EyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRiM2JhYTk0Y2UxYzQ2NjE5ZGRmM2VkNjBkNzg5NWVmID0gJCgnPGRpdiBpZD0iaHRtbF80YjNiYWE5NGNlMWM0NjYxOWRkZjNlZDYwZDc4OTVlZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnJvY2t0b24sRXhoaWJpdGlvbiBQbGFjZSxQYXJrZGFsZSBWaWxsYWdlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWRjYTcwMGJhYzVkNDAyMTllNjBhNGFkZjNmNmMzYTIuc2V0Q29udGVudChodG1sXzRiM2JhYTk0Y2UxYzQ2NjE5ZGRmM2VkNjBkNzg5NWVmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2YyOGJhZDQ4OTc4MDRlNDdiYWJkN2Q1MjUxMTQzYmU4LmJpbmRQb3B1cChwb3B1cF8xZGNhNzAwYmFjNWQ0MDIxOWU2MGE0YWRmM2Y2YzNhMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yMDg4MDU2NmE2ZTM0MWM0OWRjZmJlMTVmNzE2MzAzNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcxMzc1NjIwMDAwMDAwNiwtNzkuNDkwMDczOF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85NGNkMmNjMmY0M2U0ODRmOTJiMzhhZDFlNjFmMTRiNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82MjI3ODVjNGQyNTQ0ZTQ0OTYyOTgxMDRiMTAxNGE3OSA9ICQoJzxkaXYgaWQ9Imh0bWxfNjIyNzg1YzRkMjU0NGU0NDk2Mjk4MTA0YjEwMTRhNzkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvd25zdmlldyxOb3J0aCBQYXJrLFVwd29vZCBQYXJrIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTRjZDJjYzJmNDNlNDg0ZjkyYjM4YWQxZTYxZjE0YjQuc2V0Q29udGVudChodG1sXzYyMjc4NWM0ZDI1NDRlNDQ5NjI5ODEwNGIxMDE0YTc5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzIwODgwNTY2YTZlMzQxYzQ5ZGNmYmUxNWY3MTYzMDM3LmJpbmRQb3B1cChwb3B1cF85NGNkMmNjMmY0M2U0ODRmOTJiMzhhZDFlNjFmMTRiNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82YjZmMjg0MzExYWQ0NTEwOTBhYjQzMDUxNTYwMjcyNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5MTExNTgsLTc5LjQ3NjAxMzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFkMDA0YTAyYzM3YTRlNzVhZjhhZWMxNWZjYjg5YTI5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzBlNjY2ZjgzNTcyMTQ3MWU5MjNkOGIyZTIyMzFiZGIzID0gJCgnPGRpdiBpZD0iaHRtbF8wZTY2NmY4MzU3MjE0NzFlOTIzZDhiMmUyMjMxYmRiMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RGVsIFJheSxLZWVsZXNkYWxlLE1vdW50IERlbm5pcyxTaWx2ZXJ0aG9ybiBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFkMDA0YTAyYzM3YTRlNzVhZjhhZWMxNWZjYjg5YTI5LnNldENvbnRlbnQoaHRtbF8wZTY2NmY4MzU3MjE0NzFlOTIzZDhiMmUyMjMxYmRiMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82YjZmMjg0MzExYWQ0NTEwOTBhYjQzMDUxNTYwMjcyNC5iaW5kUG9wdXAocG9wdXBfMWQwMDRhMDJjMzdhNGU3NWFmOGFlYzE1ZmNiODlhMjkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzBiODA2ZjY5M2NiNDljY2I5NWNkNjU3M2Y1N2Q3ODQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NzMxODUyOTk5OTk5OSwtNzkuNDg3MjYxOTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzAxMWQ2OTViMTJmNGQ3OTkwOTY4ZjQ3YzI1ZGY3ZjQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDZiMTU2OGUxYWFkNDBjMmE2NTI5Mjg4ZDhjMjgwYjMgPSAkKCc8ZGl2IGlkPSJodG1sXzQ2YjE1NjhlMWFhZDQwYzJhNjUyOTI4OGQ4YzI4MGIzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgSnVuY3Rpb24gTm9ydGgsUnVubnltZWRlIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzAxMWQ2OTViMTJmNGQ3OTkwOTY4ZjQ3YzI1ZGY3ZjQuc2V0Q29udGVudChodG1sXzQ2YjE1NjhlMWFhZDQwYzJhNjUyOTI4OGQ4YzI4MGIzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzMwYjgwNmY2OTNjYjQ5Y2NiOTVjZDY1NzNmNTdkNzg0LmJpbmRQb3B1cChwb3B1cF83MDExZDY5NWIxMmY0ZDc5OTA5NjhmNDdjMjVkZjdmNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jOTc1OTY2MGVjODg0OTlhODc1NDZmOTJmNzRjN2U4MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MTYwODMsLTc5LjQ2NDc2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RlNjM5MDJkYmYzOTQ1YmFhYzc2ODA1ZWE1NDE3MjA5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJlNDZmOWNmODk3NzQ5OTFhOTQ3YTJiMzNjOWE0YjBiID0gJCgnPGRpdiBpZD0iaHRtbF8yZTQ2ZjljZjg5Nzc0OTkxYTk0N2EyYjMzYzlhNGIwYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaCBQYXJrLFRoZSBKdW5jdGlvbiBTb3V0aCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RlNjM5MDJkYmYzOTQ1YmFhYzc2ODA1ZWE1NDE3MjA5LnNldENvbnRlbnQoaHRtbF8yZTQ2ZjljZjg5Nzc0OTkxYTk0N2EyYjMzYzlhNGIwYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jOTc1OTY2MGVjODg0OTlhODc1NDZmOTJmNzRjN2U4MC5iaW5kUG9wdXAocG9wdXBfZGU2MzkwMmRiZjM5NDViYWFjNzY4MDVlYTU0MTcyMDkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTVjMDdlY2E4NjViNDdkNzk5OGIxZmJmY2FmZGZiZDYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDg5NTk3LC03OS40NTYzMjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjYyNjdjNDFkMjliNGVkOGFiYjA3MmI3ZDY5ODMzZTUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYWVkOWI4ZmMxOGU4NGE1NmIzNTU2YjBhMjQ0MDczMmEgPSAkKCc8ZGl2IGlkPSJodG1sX2FlZDliOGZjMThlODRhNTZiMzU1NmIwYTI0NDA3MzJhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrZGFsZSxSb25jZXN2YWxsZXMgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNjI2N2M0MWQyOWI0ZWQ4YWJiMDcyYjdkNjk4MzNlNS5zZXRDb250ZW50KGh0bWxfYWVkOWI4ZmMxOGU4NGE1NmIzNTU2YjBhMjQ0MDczMmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTVjMDdlY2E4NjViNDdkNzk5OGIxZmJmY2FmZGZiZDYuYmluZFBvcHVwKHBvcHVwX2Y2MjY3YzQxZDI5YjRlZDhhYmIwNzJiN2Q2OTgzM2U1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzU1ZTc3MTFkYTdhYzQ0ZDhiM2M3M2FkZTg4M2MyZTVhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUxNTcwNiwtNzkuNDg0NDQ5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMWE5N2UyMmQyZGU0ZGUxYTZmYTNjOTQwNDIzMTY3YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84MmE3ZTgzMzQ1MTk0ZDk0YTZiYzczMzRiNDJiOTRmOCA9ICQoJzxkaXYgaWQ9Imh0bWxfODJhN2U4MzM0NTE5NGQ5NGE2YmM3MzM0YjQyYjk0ZjgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJ1bm55bWVkZSxTd2Fuc2VhIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjFhOTdlMjJkMmRlNGRlMWE2ZmEzYzk0MDQyMzE2N2Euc2V0Q29udGVudChodG1sXzgyYTdlODMzNDUxOTRkOTRhNmJjNzMzNGI0MmI5NGY4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzU1ZTc3MTFkYTdhYzQ0ZDhiM2M3M2FkZTg4M2MyZTVhLmJpbmRQb3B1cChwb3B1cF9mMWE5N2UyMmQyZGU0ZGUxYTZmYTNjOTQwNDIzMTY3YSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zNDY3OThmYmY3OTk0Zjc1OWZjMzkyMjg0NTRmZjdjZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MjMwMTUsLTc5LjM4OTQ5MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmFhYjEzZjY5YTM4NDM2MjhkMzM2NzlmNmIzMjY4ZTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzFiOTdiMzRhMGI2NGYwY2JjZmNlYTQ5MDMwNWUzODAgPSAkKCc8ZGl2IGlkPSJodG1sXzcxYjk3YjM0YTBiNjRmMGNiY2ZjZWE0OTAzMDVlMzgwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5RdWVlbiYjMzk7cyBQYXJrIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmFhYjEzZjY5YTM4NDM2MjhkMzM2NzlmNmIzMjY4ZTcuc2V0Q29udGVudChodG1sXzcxYjk3YjM0YTBiNjRmMGNiY2ZjZWE0OTAzMDVlMzgwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzM0Njc5OGZiZjc5OTRmNzU5ZmMzOTIyODQ1NGZmN2NlLmJpbmRQb3B1cChwb3B1cF9mYWFiMTNmNjlhMzg0MzYyOGQzMzY3OWY2YjMyNjhlNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81M2M0NjgyMzYyOWI0MTEzOTczZWQyYjE0NTg4NGZkYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYzNjk2NTYsLTc5LjYxNTgxODk5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFjOTVjZTA4YTM4MjQ3NGU5ZmU1MTdmOGQ2YmEzYjVhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2M1OWQzNjYxZmE2ZTQxZDhhMTg4YzExYzMxZTdlYWYzID0gJCgnPGRpdiBpZD0iaHRtbF9jNTlkMzY2MWZhNmU0MWQ4YTE4OGMxMWMzMWU3ZWFmMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FuYWRhIFBvc3QgR2F0ZXdheSBQcm9jZXNzaW5nIENlbnRyZSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFjOTVjZTA4YTM4MjQ3NGU5ZmU1MTdmOGQ2YmEzYjVhLnNldENvbnRlbnQoaHRtbF9jNTlkMzY2MWZhNmU0MWQ4YTE4OGMxMWMzMWU3ZWFmMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81M2M0NjgyMzYyOWI0MTEzOTczZWQyYjE0NTg4NGZkYy5iaW5kUG9wdXAocG9wdXBfMWM5NWNlMDhhMzgyNDc0ZTlmZTUxN2Y4ZDZiYTNiNWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTAxYmI3MGY2MmY3NGIxZGI1M2FkZWZkNjZkY2NmZjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjI3NDM5LC03OS4zMjE1NThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGFjZDM4YmNlOTEzNDNhMjk2NmU1ZDI5M2VhMjY5NDQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYzkyYTY0NGExZmVjNDk4OWI1ODEwNzY3ZGE2NjRkZDIgPSAkKCc8ZGl2IGlkPSJodG1sX2M5MmE2NDRhMWZlYzQ5ODliNTgxMDc2N2RhNjY0ZGQyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CdXNpbmVzcyBSZXBseSBNYWlsIFByb2Nlc3NpbmcgQ2VudHJlIDk2OSBFYXN0ZXJuIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGFjZDM4YmNlOTEzNDNhMjk2NmU1ZDI5M2VhMjY5NDQuc2V0Q29udGVudChodG1sX2M5MmE2NDRhMWZlYzQ5ODliNTgxMDc2N2RhNjY0ZGQyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2EwMWJiNzBmNjJmNzRiMWRiNTNhZGVmZDY2ZGNjZmY3LmJpbmRQb3B1cChwb3B1cF9kYWNkMzhiY2U5MTM0M2EyOTY2ZTVkMjkzZWEyNjk0NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81YTgyZjg0NTIxODA0N2Y2OTI1ZTY4YzhiOTRjY2RhYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYwNTY0NjYsLTc5LjUwMTMyMDcwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzllMjgzZTYxODUxZTQwYzI4M2QwOTI0ZGFhNDQwYTQyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzdhYjUzYTQ0NDQ1ZjQ3ZTdhMGQ1MWM0NWE4N2FhMzQ5ID0gJCgnPGRpdiBpZD0iaHRtbF83YWI1M2E0NDQ0NWY0N2U3YTBkNTFjNDVhODdhYTM0OSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtYmVyIEJheSBTaG9yZXMsTWltaWNvIFNvdXRoLE5ldyBUb3JvbnRvIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWUyODNlNjE4NTFlNDBjMjgzZDA5MjRkYWE0NDBhNDIuc2V0Q29udGVudChodG1sXzdhYjUzYTQ0NDQ1ZjQ3ZTdhMGQ1MWM0NWE4N2FhMzQ5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzVhODJmODQ1MjE4MDQ3ZjY5MjVlNjhjOGI5NGNjZGFiLmJpbmRQb3B1cChwb3B1cF85ZTI4M2U2MTg1MWU0MGMyODNkMDkyNGRhYTQ0MGE0Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iMDc1NzhjZjZhMzM0MjZkOWQ0YzkxNWUwNTJiNTMxZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYwMjQxMzcwMDAwMDAxLC03OS41NDM0ODQwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84NTYyYTFmOTEzYjI0OTMzOTM0NjE2NTI0NGQzNWNkNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hODk5MWJiNzYzMTc0ZDdjYTlmMzNiM2RmMDIxN2I5MiA9ICQoJzxkaXYgaWQ9Imh0bWxfYTg5OTFiYjc2MzE3NGQ3Y2E5ZjMzYjNkZjAyMTdiOTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFsZGVyd29vZCxMb25nIEJyYW5jaCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg1NjJhMWY5MTNiMjQ5MzM5MzQ2MTY1MjQ0ZDM1Y2Q1LnNldENvbnRlbnQoaHRtbF9hODk5MWJiNzYzMTc0ZDdjYTlmMzNiM2RmMDIxN2I5Mik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iMDc1NzhjZjZhMzM0MjZkOWQ0YzkxNWUwNTJiNTMxZi5iaW5kUG9wdXAocG9wdXBfODU2MmExZjkxM2IyNDkzMzkzNDYxNjUyNDRkMzVjZDUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzhjYjQyZDg5YTU0NGNjZGI0YmQ4YTk0MWI4ODI3YWQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTM2NTM2MDAwMDAwMDUsLTc5LjUwNjk0MzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTkzMWI1NzU5NTE4NDAyZjg0MGZhODEzYjk0ZDZiNzMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzQ1ZWMwNmNkN2Y4NDQ0MTllOTRkODQ1MjNhZGJmYWIgPSAkKCc8ZGl2IGlkPSJodG1sXzM0NWVjMDZjZDdmODQ0NDE5ZTk0ZDg0NTIzYWRiZmFiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgS2luZ3N3YXksTW9udGdvbWVyeSBSb2FkLE9sZCBNaWxsIE5vcnRoIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTkzMWI1NzU5NTE4NDAyZjg0MGZhODEzYjk0ZDZiNzMuc2V0Q29udGVudChodG1sXzM0NWVjMDZjZDdmODQ0NDE5ZTk0ZDg0NTIzYWRiZmFiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M4Y2I0MmQ4OWE1NDRjY2RiNGJkOGE5NDFiODgyN2FkLmJpbmRQb3B1cChwb3B1cF9hOTMxYjU3NTk1MTg0MDJmODQwZmE4MTNiOTRkNmI3Myk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNDA2ZWMyY2U2MDU0YzljODI5MDE0NTkwZGI3NDM3YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYzNjI1NzksLTc5LjQ5ODUwOTA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE1NTUxYTZkMjhkNTQyYzhhYmQ0YjI3YzNjOTlmOWE5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzM2ZjQ0ZGJjODdiZDQyZDlhM2U2NDMxYWRjZWVjZThiID0gJCgnPGRpdiBpZD0iaHRtbF8zNmY0NGRiYzg3YmQ0MmQ5YTNlNjQzMWFkY2VlY2U4YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtYmVyIEJheSxLaW5nJiMzOTtzIE1pbGwgUGFyayxLaW5nc3dheSBQYXJrIFNvdXRoIEVhc3QsTWltaWNvIE5FLE9sZCBNaWxsIFNvdXRoLFRoZSBRdWVlbnN3YXkgRWFzdCxSb3lhbCBZb3JrIFNvdXRoIEVhc3QsU3VubnlsZWEgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNTU1MWE2ZDI4ZDU0MmM4YWJkNGIyN2MzYzk5ZjlhOS5zZXRDb250ZW50KGh0bWxfMzZmNDRkYmM4N2JkNDJkOWEzZTY0MzFhZGNlZWNlOGIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDQwNmVjMmNlNjA1NGM5YzgyOTAxNDU5MGRiNzQzN2EuYmluZFBvcHVwKHBvcHVwXzE1NTUxYTZkMjhkNTQyYzhhYmQ0YjI3YzNjOTlmOWE5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M5ZWZmZWE1NGI2ODQ5ZTg5YzgwNTExOGQ1OWMzM2UzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjI4ODQwOCwtNzkuNTIwOTk5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzI1Yzk3YTIzMDU3NDZkY2FmNGU2NmRmZjhlOTczZjEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmRiZDEyMzMwYWQ3NDI3MGIyNGQ5Y2VkMjZkODI3NTggPSAkKCc8ZGl2IGlkPSJodG1sX2ZkYmQxMjMzMGFkNzQyNzBiMjRkOWNlZDI2ZDgyNzU4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc3dheSBQYXJrIFNvdXRoIFdlc3QsTWltaWNvIE5XLFRoZSBRdWVlbnN3YXkgV2VzdCxSb3lhbCBZb3JrIFNvdXRoIFdlc3QsU291dGggb2YgQmxvb3IgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zMjVjOTdhMjMwNTc0NmRjYWY0ZTY2ZGZmOGU5NzNmMS5zZXRDb250ZW50KGh0bWxfZmRiZDEyMzMwYWQ3NDI3MGIyNGQ5Y2VkMjZkODI3NTgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzllZmZlYTU0YjY4NDllODljODA1MTE4ZDU5YzMzZTMuYmluZFBvcHVwKHBvcHVwXzMyNWM5N2EyMzA1NzQ2ZGNhZjRlNjZkZmY4ZTk3M2YxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UzNzU4MDZmZDdiYTRmNmJiZDM2ZDNiODViZmJlZmEzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQzNTE1MiwtNzkuNTc3MjAwNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDBhOTUzZTBjOTU3NDEwZTk5OTQwNzlmYjAzNTlhYjQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTMzZWQwZTU1NzRhNDY4YTgxYjRhMjRkM2Y1NGNlMTIgPSAkKCc8ZGl2IGlkPSJodG1sX2UzM2VkMGU1NTc0YTQ2OGE4MWI0YTI0ZDNmNTRjZTEyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CbG9vcmRhbGUgR2FyZGVucyxFcmluZ2F0ZSxNYXJrbGFuZCBXb29kLE9sZCBCdXJuaGFtdGhvcnBlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDBhOTUzZTBjOTU3NDEwZTk5OTQwNzlmYjAzNTlhYjQuc2V0Q29udGVudChodG1sX2UzM2VkMGU1NTc0YTQ2OGE4MWI0YTI0ZDNmNTRjZTEyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UzNzU4MDZmZDdiYTRmNmJiZDM2ZDNiODViZmJlZmEzLmJpbmRQb3B1cChwb3B1cF8wMGE5NTNlMGM5NTc0MTBlOTk5NDA3OWZiMDM1OWFiNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80ZTNmMzYxYTAxNTY0ZTJmOGYwNDFiMTdhODA5ZTY3YiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1NjMwMzMsLTc5LjU2NTk2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2JiZjY1MDA0ODQ0ZTRjOTQ5NDhmMzBhMDdiNDIwMTUyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2NiZjUxNjU0ZjJhMjQ3NzY5MWQwYjhkZGJhNDMyZmM3ID0gJCgnPGRpdiBpZD0iaHRtbF9jYmY1MTY1NGYyYTI0Nzc2OTFkMGI4ZGRiYTQzMmZjNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtYmVyIFN1bW1pdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2JiZjY1MDA0ODQ0ZTRjOTQ5NDhmMzBhMDdiNDIwMTUyLnNldENvbnRlbnQoaHRtbF9jYmY1MTY1NGYyYTI0Nzc2OTFkMGI4ZGRiYTQzMmZjNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80ZTNmMzYxYTAxNTY0ZTJmOGYwNDFiMTdhODA5ZTY3Yi5iaW5kUG9wdXAocG9wdXBfYmJmNjUwMDQ4NDRlNGM5NDk0OGYzMGEwN2I0MjAxNTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzk0YjdlMWJmYmU4NGVhYmJiYWE2MmRlMzlmYjU3ZDEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MjQ3NjU5LC03OS41MzIyNDI0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODBmZmI0IiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwZmZiNCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NzBlOGQ3MmU3OWI0NjQzYjAxNmFmZTczNmQ5NzIxYik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yNjY2Y2Q2OGQzMzQ0MGI1YTA5NDQzZGU1ZTY3ZjM0OCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84ODQzNjFiYWE5YWY0NDQ2YjliN2IwZTlhMmU1OTZkZCA9ICQoJzxkaXYgaWQ9Imh0bWxfODg0MzYxYmFhOWFmNDQ0NmI5YjdiMGU5YTJlNTk2ZGQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVtZXJ5LEh1bWJlcmxlYSBDbHVzdGVyIDM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI2NjZjZDY4ZDMzNDQwYjVhMDk0NDNkZTVlNjdmMzQ4LnNldENvbnRlbnQoaHRtbF84ODQzNjFiYWE5YWY0NDQ2YjliN2IwZTlhMmU1OTZkZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83OTRiN2UxYmZiZTg0ZWFiYmJhYTYyZGUzOWZiNTdkMS5iaW5kUG9wdXAocG9wdXBfMjY2NmNkNjhkMzM0NDBiNWEwOTQ0M2RlNWU2N2YzNDgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjQxZDY5Zjg3NTI3NGNlMjgyNjE0OWFjOTM3MDE5YWMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MDY4NzYsLTc5LjUxODE4ODQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzZmMzU3Y2UzODdjMjQzZTA4Yjk2YzAxOTE0ZTkxNThjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FkMzg5ZGE0YmU2ODQ2ZDY5OWRhMmM1MTVkNmRiNzczID0gJCgnPGRpdiBpZD0iaHRtbF9hZDM4OWRhNGJlNjg0NmQ2OTlkYTJjNTE1ZDZkYjc3MyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2VzdG9uIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmYzNTdjZTM4N2MyNDNlMDhiOTZjMDE5MTRlOTE1OGMuc2V0Q29udGVudChodG1sX2FkMzg5ZGE0YmU2ODQ2ZDY5OWRhMmM1MTVkNmRiNzczKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzI0MWQ2OWY4NzUyNzRjZTI4MjYxNDlhYzkzNzAxOWFjLmJpbmRQb3B1cChwb3B1cF82ZjM1N2NlMzg3YzI0M2UwOGI5NmMwMTkxNGU5MTU4Yyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mMTQyNDVjYTNiZjk0N2Q0YTkzODVhOGZjZDdhYWYzOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5NjMxOSwtNzkuNTMyMjQyNDAwMDAwMDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDRlMTJmMmY3MmYwNDRiNWFhNzNlZDRiNzQ4ZWYzM2UgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjUxNWZmNTlmNjNhNDcwZTk1ZDhlZjRjMzJkMjU5MGYgPSAkKCc8ZGl2IGlkPSJodG1sX2I1MTVmZjU5ZjYzYTQ3MGU5NWQ4ZWY0YzMyZDI1OTBmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0bW91bnQgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kNGUxMmYyZjcyZjA0NGI1YWE3M2VkNGI3NDhlZjMzZS5zZXRDb250ZW50KGh0bWxfYjUxNWZmNTlmNjNhNDcwZTk1ZDhlZjRjMzJkMjU5MGYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjE0MjQ1Y2EzYmY5NDdkNGE5Mzg1YThmY2Q3YWFmMzguYmluZFBvcHVwKHBvcHVwX2Q0ZTEyZjJmNzJmMDQ0YjVhYTczZWQ0Yjc0OGVmMzNlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIxNjQ2ZTM5N2E0MzRkODdhZWM2OWRlY2JhZmQ3OTA5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg4OTA1NCwtNzkuNTU0NzI0NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWJhODM0NDFkZTVjNDUzZjg2OTEzZGIxNjYzMzM3MjQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTg1OTdhYzM2ZjJkNGU5NjllZjNlNjI2NjI2YTBkMzUgPSAkKCc8ZGl2IGlkPSJodG1sXzk4NTk3YWMzNmYyZDRlOTY5ZWYzZTYyNjYyNmEwZDM1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc3ZpZXcgVmlsbGFnZSxNYXJ0aW4gR3JvdmUgR2FyZGVucyxSaWNodmlldyBHYXJkZW5zLFN0LiBQaGlsbGlwcyBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FiYTgzNDQxZGU1YzQ1M2Y4NjkxM2RiMTY2MzMzNzI0LnNldENvbnRlbnQoaHRtbF85ODU5N2FjMzZmMmQ0ZTk2OWVmM2U2MjY2MjZhMGQzNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yMTY0NmUzOTdhNDM0ZDg3YWVjNjlkZWNiYWZkNzkwOS5iaW5kUG9wdXAocG9wdXBfYWJhODM0NDFkZTVjNDUzZjg2OTEzZGIxNjYzMzM3MjQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTk0OThiYjg1MDk2NDVlY2JmYzQwMTllNWQ3NWRjY2UgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Mzk0MTYzOTk5OTk5OTYsLTc5LjU4ODQzNjldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTcwZThkNzJlNzliNDY0M2IwMTZhZmU3MzZkOTcyMWIpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTVhYWNmMmQ0ZTlhNDY3M2IwNzQxYTYyZTdjYTlhYTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTNjMDJlYTdkNGRmNDUwMDkwOGQ1ZTU2ZWVlMDE1NGIgPSAkKCc8ZGl2IGlkPSJodG1sXzUzYzAyZWE3ZDRkZjQ1MDA5MDhkNWU1NmVlZTAxNTRiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BbGJpb24gR2FyZGVucyxCZWF1bW9uZCBIZWlnaHRzLEh1bWJlcmdhdGUsSmFtZXN0b3duLE1vdW50IE9saXZlLFNpbHZlcnN0b25lLFNvdXRoIFN0ZWVsZXMsVGhpc3RsZXRvd24gQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81NWFhY2YyZDRlOWE0NjczYjA3NDFhNjJlN2NhOWFhOC5zZXRDb250ZW50KGh0bWxfNTNjMDJlYTdkNGRmNDUwMDkwOGQ1ZTU2ZWVlMDE1NGIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTk0OThiYjg1MDk2NDVlY2JmYzQwMTllNWQ3NWRjY2UuYmluZFBvcHVwKHBvcHVwXzU1YWFjZjJkNGU5YTQ2NzNiMDc0MWE2MmU3Y2E5YWE4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2MyZmNmY2NiMjUxZjQ2NmZhYjFmMDZjOTlkNTJkMWQxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA2NzQ4Mjk5OTk5OTk0LC03OS41OTQwNTQ0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk3MGU4ZDcyZTc5YjQ2NDNiMDE2YWZlNzM2ZDk3MjFiKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2QwMTQ1ZTEzMGIyNTRlOGFiNmQzNWI3NjNmYTljNDA0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzAzMmFjYTBlMWUzNzQzNmY4N2Q2ZjNhNDE2NjUyYzZlID0gJCgnPGRpdiBpZD0iaHRtbF8wMzJhY2EwZTFlMzc0MzZmODdkNmYzYTQxNjY1MmM2ZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Tm9ydGh3ZXN0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDAxNDVlMTMwYjI1NGU4YWI2ZDM1Yjc2M2ZhOWM0MDQuc2V0Q29udGVudChodG1sXzAzMmFjYTBlMWUzNzQzNmY4N2Q2ZjNhNDE2NjUyYzZlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2MyZmNmY2NiMjUxZjQ2NmZhYjFmMDZjOTlkNTJkMWQxLmJpbmRQb3B1cChwb3B1cF9kMDE0NWUxMzBiMjU0ZThhYjZkMzViNzYzZmE5YzQwNCk7CgogICAgICAgICAgICAKICAgICAgICAKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



Now we examine the clusters to see the distinguishing venues


```python
toronto_merged.loc[toronto_merged['Cluster Labels'] == 0, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]
```




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




```python
toronto_merged.loc[toronto_merged['Cluster Labels'] == 1, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]
```




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




```python
toronto_merged.loc[toronto_merged['Cluster Labels'] == 2, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]
```




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




```python
toronto_merged.loc[toronto_merged['Cluster Labels'] == 3, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]
```




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




```python
toronto_merged.loc[toronto_merged['Cluster Labels'] == 4, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]
```




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
