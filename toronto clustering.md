
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




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmIiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5ZiA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5ZicsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDMuNjUzOTYzLC03OS4zODcyMDddLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTAsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzI3NjMzMDEzZjc3ZTRjNDA4ZDIyYjJhNWNlNzYzNTQ0ID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICJtYXhab29tIjogMTgsCiAgIm1pblpvb20iOiAxLAogICJub1dyYXAiOiBmYWxzZSwKICAic3ViZG9tYWlucyI6ICJhYmMiCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wYTI2MGZlNDUzMzU0YWE2YWZhODI1N2U3ZDdmMTJmNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjgwNjY4NjI5OTk5OTk5NiwtNzkuMTk0MzUzNDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTI1ZGZlYzRiNjVhNDQ1MWE4YzlmN2QzNGUyODJiYTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDZmYTA0MjZjOWFmNGVmNjlkY2M3MTgxZDg3NzA3YTYgPSAkKCc8ZGl2IGlkPSJodG1sX2Q2ZmEwNDI2YzlhZjRlZjY5ZGNjNzE4MWQ4NzcwN2E2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3VnZSxNYWx2ZXJuLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTI1ZGZlYzRiNjVhNDQ1MWE4YzlmN2QzNGUyODJiYTcuc2V0Q29udGVudChodG1sX2Q2ZmEwNDI2YzlhZjRlZjY5ZGNjNzE4MWQ4NzcwN2E2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBhMjYwZmU0NTMzNTRhYTZhZmE4MjU3ZTdkN2YxMmY3LmJpbmRQb3B1cChwb3B1cF8xMjVkZmVjNGI2NWE0NDUxYThjOWY3ZDM0ZTI4MmJhNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kMGVlOGZmMTlkZjE0NmU4OThiYjRjODE4NGQzMTg3YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4NDUzNTEsLTc5LjE2MDQ5NzA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI0NmRlMzNhMmUyYjQxY2NiNTgwYzk3MWNhOTA2MTEwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU3NzA4OTc5ODU1NzQ4YzU4MmYzYWU2ZmNhMTZhYTBlID0gJCgnPGRpdiBpZD0iaHRtbF81NzcwODk3OTg1NTc0OGM1ODJmM2FlNmZjYTE2YWEwZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaGxhbmQgQ3JlZWssUm91Z2UgSGlsbCxQb3J0IFVuaW9uLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjQ2ZGUzM2EyZTJiNDFjY2I1ODBjOTcxY2E5MDYxMTAuc2V0Q29udGVudChodG1sXzU3NzA4OTc5ODU1NzQ4YzU4MmYzYWU2ZmNhMTZhYTBlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2QwZWU4ZmYxOWRmMTQ2ZTg5OGJiNGM4MTg0ZDMxODdhLmJpbmRQb3B1cChwb3B1cF8yNDZkZTMzYTJlMmI0MWNjYjU4MGM5NzFjYTkwNjExMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85MjhkMDA2Y2ExNmQ0ZjkyYWM2MWE4M2VkNzMyNmM4NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc2MzU3MjYsLTc5LjE4ODcxMTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjRlMWM5NzM5MjU2NDZiYTllOTBlYjE2YmIyZTQ4MjEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDkyZGE3NjBjZTFhNGFmMDkwNTk0YWQ0ZmFiZTE4NWEgPSAkKCc8ZGl2IGlkPSJodG1sX2Q5MmRhNzYwY2UxYTRhZjA5MDU5NGFkNGZhYmUxODVhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HdWlsZHdvb2QsTW9ybmluZ3NpZGUsV2VzdCBIaWxsLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjRlMWM5NzM5MjU2NDZiYTllOTBlYjE2YmIyZTQ4MjEuc2V0Q29udGVudChodG1sX2Q5MmRhNzYwY2UxYTRhZjA5MDU5NGFkNGZhYmUxODVhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkyOGQwMDZjYTE2ZDRmOTJhYzYxYTgzZWQ3MzI2Yzg3LmJpbmRQb3B1cChwb3B1cF82NGUxYzk3MzkyNTY0NmJhOWU5MGViMTZiYjJlNDgyMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zZDhiYzQ0MGVkNWU0ZDJlYWQwZjNmNTY1MDJhYjI1YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MDk5MjEsLTc5LjIxNjkxNzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzlmNDEwMzAzODlmNzRiYmE4NWNlZWE2NTA0MDJiMjNlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FmM2E2YmNmMDVhMDRlY2VhOTQ2ZDFhYmU2ZjU1ZjZkID0gJCgnPGRpdiBpZD0iaHRtbF9hZjNhNmJjZjA1YTA0ZWNlYTk0NmQxYWJlNmY1NWY2ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V29idXJuLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWY0MTAzMDM4OWY3NGJiYTg1Y2VlYTY1MDQwMmIyM2Uuc2V0Q29udGVudChodG1sX2FmM2E2YmNmMDVhMDRlY2VhOTQ2ZDFhYmU2ZjU1ZjZkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNkOGJjNDQwZWQ1ZTRkMmVhZDBmM2Y1NjUwMmFiMjVjLmJpbmRQb3B1cChwb3B1cF85ZjQxMDMwMzg5Zjc0YmJhODVjZWVhNjUwNDAyYjIzZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yZDdhMTc5ZjQwYjE0MTU2YTc1MWY3NzMzYTE1ZGQxMyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MzEzNiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWQ0MGIxYjNjMDlmNGZiM2FlMjI4MWJiYzNkNTRmN2YgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGM1OWY1MTIxYjMyNDE4ZWJhZTU4NTFjZDA5NWZlN2IgPSAkKCc8ZGl2IGlkPSJodG1sXzRjNTlmNTEyMWIzMjQxOGViYWU1ODUxY2QwOTVmZTdiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZWRhcmJyYWUsIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xZDQwYjFiM2MwOWY0ZmIzYWUyMjgxYmJjM2Q1NGY3Zi5zZXRDb250ZW50KGh0bWxfNGM1OWY1MTIxYjMyNDE4ZWJhZTU4NTFjZDA5NWZlN2IpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmQ3YTE3OWY0MGIxNDE1NmE3NTFmNzczM2ExNWRkMTMuYmluZFBvcHVwKHBvcHVwXzFkNDBiMWIzYzA5ZjRmYjNhZTIyODFiYmMzZDU0ZjdmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M2ZGZmZWI1MDZlMTQzYzA5ZWVmYWEyNjk1NTQwZDQwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ0NzM0MiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjg2NzNhODExOTlhNDg2ODk0NzNkYmUzNWNlYzA0ODUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2RmOWQzODgyOTMwNGM0YmIzNjA0OGYxMTYzOTkxMGMgPSAkKCc8ZGl2IGlkPSJodG1sX2NkZjlkMzg4MjkzMDRjNGJiMzYwNDhmMTE2Mzk5MTBjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TY2FyYm9yb3VnaCBWaWxsYWdlLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjg2NzNhODExOTlhNDg2ODk0NzNkYmUzNWNlYzA0ODUuc2V0Q29udGVudChodG1sX2NkZjlkMzg4MjkzMDRjNGJiMzYwNDhmMTE2Mzk5MTBjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M2ZGZmZWI1MDZlMTQzYzA5ZWVmYWEyNjk1NTQwZDQwLmJpbmRQb3B1cChwb3B1cF9iODY3M2E4MTE5OWE0ODY4OTQ3M2RiZTM1Y2VjMDQ4NSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNmRmMTljMDcxZDY0YjJiYjQ4MTk4OGM3NGMyYjRiOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNzkyOTIsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzlkNzc3NTQ5ZmE5YTQwODI4NmVmMTkyZWNmOTEyYmZjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNiN2FmNzExZTBkMTQ3ODJhZTk3NmIyYWRjZjY3ZmZkID0gJCgnPGRpdiBpZD0iaHRtbF8zYjdhZjcxMWUwZDE0NzgyYWU5NzZiMmFkY2Y2N2ZmZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdCBCaXJjaG1vdW50IFBhcmssSW9udmlldyxLZW5uZWR5IFBhcmssIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85ZDc3NzU0OWZhOWE0MDgyODZlZjE5MmVjZjkxMmJmYy5zZXRDb250ZW50KGh0bWxfM2I3YWY3MTFlMGQxNDc4MmFlOTc2YjJhZGNmNjdmZmQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTZkZjE5YzA3MWQ2NGIyYmI0ODE5ODhjNzRjMmI0YjkuYmluZFBvcHVwKHBvcHVwXzlkNzc3NTQ5ZmE5YTQwODI4NmVmMTkyZWNmOTEyYmZjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdjNjg0ZGI3NDYwYjRiNDY5Mjg1NjUwMmY0NGZjNDMwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzExMTExNzAwMDAwMDA0LC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y3NzU1ZDQ5MjQwNDRjOGZhNmM4NzE5Mjg4MWEzMmRmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQ2ZTkzMmQ0MGIzZDQxNTA4Y2VhYjJhOWI1YjY5NzM1ID0gJCgnPGRpdiBpZD0iaHRtbF80NmU5MzJkNDBiM2Q0MTUwOGNlYWIyYTliNWI2OTczNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2xhaXJsZWEsR29sZGVuIE1pbGUsT2FrcmlkZ2UsIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNzc1NWQ0OTI0MDQ0YzhmYTZjODcxOTI4ODFhMzJkZi5zZXRDb250ZW50KGh0bWxfNDZlOTMyZDQwYjNkNDE1MDhjZWFiMmE5YjViNjk3MzUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2M2ODRkYjc0NjBiNGI0NjkyODU2NTAyZjQ0ZmM0MzAuYmluZFBvcHVwKHBvcHVwX2Y3NzU1ZDQ5MjQwNDRjOGZhNmM4NzE5Mjg4MWEzMmRmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZhZjQ3MTU4NjNiMzQ5Zjc4MGJmNGE5NDc5NWVlOWJkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE2MzE2LC03OS4yMzk0NzYwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81ODQzZGYxZDY1YWE0ODNlODUyNjRiYzMxMWU0ZTgyMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mZjhlNjNhYjgxNDE0OTFmOWIyZDU4MjJlZWFhNzA5MiA9ICQoJzxkaXYgaWQ9Imh0bWxfZmY4ZTYzYWI4MTQxNDkxZjliMmQ1ODIyZWVhYTcwOTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsaWZmY3Jlc3QsQ2xpZmZzaWRlLFNjYXJib3JvdWdoIFZpbGxhZ2UgV2VzdCwgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU4NDNkZjFkNjVhYTQ4M2U4NTI2NGJjMzExZTRlODIyLnNldENvbnRlbnQoaHRtbF9mZjhlNjNhYjgxNDE0OTFmOWIyZDU4MjJlZWFhNzA5Mik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mYWY0NzE1ODYzYjM0OWY3ODBiZjRhOTQ3OTVlZTliZC5iaW5kUG9wdXAocG9wdXBfNTg0M2RmMWQ2NWFhNDgzZTg1MjY0YmMzMTFlNGU4MjIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzAyNTQ3OWQwODllNGIyMThjOGZmZDY5MGE1OGM0NDIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTI2NTcwMDAwMDAwMDQsLTc5LjI2NDg0ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDk0NzQzZGM2M2ZmNGIxZWI0YWQ3YWNmZjI2MTA5ZjMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTE2YTZlMmExM2U1NGRlMWE3NjRjNTJhNmY0ZmRjYzQgPSAkKCc8ZGl2IGlkPSJodG1sXzUxNmE2ZTJhMTNlNTRkZTFhNzY0YzUyYTZmNGZkY2M0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CaXJjaCBDbGlmZixDbGlmZnNpZGUgV2VzdCwgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzA5NDc0M2RjNjNmZjRiMWViNGFkN2FjZmYyNjEwOWYzLnNldENvbnRlbnQoaHRtbF81MTZhNmUyYTEzZTU0ZGUxYTc2NGM1MmE2ZjRmZGNjNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83MDI1NDc5ZDA4OWU0YjIxOGM4ZmZkNjkwYTU4YzQ0Mi5iaW5kUG9wdXAocG9wdXBfMDk0NzQzZGM2M2ZmNGIxZWI0YWQ3YWNmZjI2MTA5ZjMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjFiOWYxNzEwNzQ4NGIxMTg4NWM3YjE1YTA4YjEzMzMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTc0MDk2LC03OS4yNzMzMDQwMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNjIyZGFiMGIzNzk0ZWNlYWUyOWMyZGM3MjRmZGNiNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jOGFkY2U3NjcwOTI0MWE3YjU3ODRkOGFkOTgwMGM3YiA9ICQoJzxkaXYgaWQ9Imh0bWxfYzhhZGNlNzY3MDkyNDFhN2I1Nzg0ZDhhZDk4MDBjN2IiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvcnNldCBQYXJrLFNjYXJib3JvdWdoIFRvd24gQ2VudHJlLFdleGZvcmQgSGVpZ2h0cywgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2E2MjJkYWIwYjM3OTRlY2VhZTI5YzJkYzcyNGZkY2I1LnNldENvbnRlbnQoaHRtbF9jOGFkY2U3NjcwOTI0MWE3YjU3ODRkOGFkOTgwMGM3Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mMWI5ZjE3MTA3NDg0YjExODg1YzdiMTVhMDhiMTMzMy5iaW5kUG9wdXAocG9wdXBfYTYyMmRhYjBiMzc5NGVjZWFlMjljMmRjNzI0ZmRjYjUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmE4NmIzNmFkZWIxNGYyMDhhYTY4NzFlZGIzMzEyMjIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTAwNzE1MDAwMDAwMDQsLTc5LjI5NTg0OTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWRkYTNmNDkwMzIzNDE1OGIyOGM0ODRkM2MzNTQxNGMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTI1ZDM3Y2Q5YmRjNDY0Y2JmYmQwOTcyOTk4MDUwMGQgPSAkKCc8ZGl2IGlkPSJodG1sXzUyNWQzN2NkOWJkYzQ2NGNiZmJkMDk3Mjk5ODA1MDBkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJ5dmFsZSxXZXhmb3JkLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWRkYTNmNDkwMzIzNDE1OGIyOGM0ODRkM2MzNTQxNGMuc2V0Q29udGVudChodG1sXzUyNWQzN2NkOWJkYzQ2NGNiZmJkMDk3Mjk5ODA1MDBkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZhODZiMzZhZGViMTRmMjA4YWE2ODcxZWRiMzMxMjIyLmJpbmRQb3B1cChwb3B1cF8xZGRhM2Y0OTAzMjM0MTU4YjI4YzQ4NGQzYzM1NDE0Yyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81YTY1NzBlNmMxMTE0M2M4YjQzYTU2OTlkNWE0Y2I2MyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5NDIwMDMsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2E0YjgzNWVmNjE1NzQ0ODY4NDVmM2Q2YTg5ZGIyYTgyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JkODVlYTYwZTVmNDQ0Mzg4NTk2ZWNjMDEwOTQxZmVkID0gJCgnPGRpdiBpZD0iaHRtbF9iZDg1ZWE2MGU1ZjQ0NDM4ODU5NmVjYzAxMDk0MWZlZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0LCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTRiODM1ZWY2MTU3NDQ4Njg0NWYzZDZhODlkYjJhODIuc2V0Q29udGVudChodG1sX2JkODVlYTYwZTVmNDQ0Mzg4NTk2ZWNjMDEwOTQxZmVkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzVhNjU3MGU2YzExMTQzYzhiNDNhNTY5OWQ1YTRjYjYzLmJpbmRQb3B1cChwb3B1cF9hNGI4MzVlZjYxNTc0NDg2ODQ1ZjNkNmE4OWRiMmE4Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hZjlhMzg2ZTgzNTI0MmYzYTU5ZWEyZjZiYTY4MWEzMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4MTYzNzUsLTc5LjMwNDMwMjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTU2ZmU4ODM1MGVjNDQ3ZGE0MzBjMTZiZDExYjQ5MDAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzFkYWU4OTU5YzdhNDI1NWIzN2RhZmRlYjI2NDAwYWYgPSAkKCc8ZGl2IGlkPSJodG1sXzMxZGFlODk1OWM3YTQyNTViMzdkYWZkZWIyNjQwMGFmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGFya3MgQ29ybmVycyxTdWxsaXZhbixUYW0gTyYjMzk7U2hhbnRlciwgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU1NmZlODgzNTBlYzQ0N2RhNDMwYzE2YmQxMWI0OTAwLnNldENvbnRlbnQoaHRtbF8zMWRhZTg5NTljN2E0MjU1YjM3ZGFmZGViMjY0MDBhZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hZjlhMzg2ZTgzNTI0MmYzYTU5ZWEyZjZiYTY4MWEzMi5iaW5kUG9wdXAocG9wdXBfNTU2ZmU4ODM1MGVjNDQ3ZGE0MzBjMTZiZDExYjQ5MDApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjZkMGM3MjhjODM1NDEwODg2Mjg3ZjE3YTg5OWY1OTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My44MTUyNTIyLC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzM0NzlhNGNiYzBhYzRjN2RhYTc2MGRiMzE3NTY4MzY2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJlODMyMzk0MThkMTRhNjliYjg1MGQ2ZTZjMzJiYmQ3ID0gJCgnPGRpdiBpZD0iaHRtbF8yZTgzMjM5NDE4ZDE0YTY5YmI4NTBkNmU2YzMyYmJkNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0IE5vcnRoLEwmIzM5O0Ftb3JlYXV4IEVhc3QsTWlsbGlrZW4sU3RlZWxlcyBFYXN0LCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzQ3OWE0Y2JjMGFjNGM3ZGFhNzYwZGIzMTc1NjgzNjYuc2V0Q29udGVudChodG1sXzJlODMyMzk0MThkMTRhNjliYjg1MGQ2ZTZjMzJiYmQ3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzY2ZDBjNzI4YzgzNTQxMDg4NjI4N2YxN2E4OTlmNTk4LmJpbmRQb3B1cChwb3B1cF8zNDc5YTRjYmMwYWM0YzdkYWE3NjBkYjMxNzU2ODM2Nik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jZjM4N2Q1YjA1Mzc0MWU4YTFjOTYyNmE0YzFlMmUzNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5OTUyNTIwMDAwMDAwNSwtNzkuMzE4Mzg4N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ZjU5YjExNjE1YzE0ZmQxYmQwMDNiMGZiY2Y0MTIxMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNTZmODM4NzlhZTQ0MmJmYWU2MTJmN2IyNTllYWMxNyA9ICQoJzxkaXYgaWQ9Imh0bWxfMzU2ZjgzODc5YWU0NDJiZmFlNjEyZjdiMjU5ZWFjMTciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkwmIzM5O0Ftb3JlYXV4IFdlc3QsIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83ZjU5YjExNjE1YzE0ZmQxYmQwMDNiMGZiY2Y0MTIxMC5zZXRDb250ZW50KGh0bWxfMzU2ZjgzODc5YWU0NDJiZmFlNjEyZjdiMjU5ZWFjMTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfY2YzODdkNWIwNTM3NDFlOGExYzk2MjZhNGMxZTJlMzQuYmluZFBvcHVwKHBvcHVwXzdmNTliMTE2MTVjMTRmZDFiZDAwM2IwZmJjZjQxMjEwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VjMmVjMjEzMDAxZTQ1ODU5ZjNhMGFiOWZhMTIxZTJhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuODM2MTI0NzAwMDAwMDA2LC03OS4yMDU2MzYwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jNWU2Nzc2M2E1Yzk0ZTc4Yjk5MTkxYzUwNDEzOWNiMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kNWUyM2IwOWM1YjM0MzY5YjhkNzEwOTU1Y2NhMWUwOSA9ICQoJzxkaXYgaWQ9Imh0bWxfZDVlMjNiMDljNWIzNDM2OWI4ZDcxMDk1NWNjYTFlMDkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlVwcGVyIFJvdWdlLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzVlNjc3NjNhNWM5NGU3OGI5OTE5MWM1MDQxMzljYjIuc2V0Q29udGVudChodG1sX2Q1ZTIzYjA5YzViMzQzNjliOGQ3MTA5NTVjY2ExZTA5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2VjMmVjMjEzMDAxZTQ1ODU5ZjNhMGFiOWZhMTIxZTJhLmJpbmRQb3B1cChwb3B1cF9jNWU2Nzc2M2E1Yzk0ZTc4Yjk5MTkxYzUwNDEzOWNiMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81NzhlODA5YmIzNGE0OTIwYWJlN2Y4ODU4MmMzMjZlYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjgwMzc2MjIsLTc5LjM2MzQ1MTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODg4ZGFkZjU4MjU4NDIyYWFiZGYxODIzYWMyMDczMDAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGVhZTBkZDY1YTY4NDY2OWIwNTIyMzY3YmM2NGFhNmQgPSAkKCc8ZGl2IGlkPSJodG1sXzRlYWUwZGQ2NWE2ODQ2NjliMDUyMjM2N2JjNjRhYTZkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IaWxsY3Jlc3QgVmlsbGFnZSwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84ODhkYWRmNTgyNTg0MjJhYWJkZjE4MjNhYzIwNzMwMC5zZXRDb250ZW50KGh0bWxfNGVhZTBkZDY1YTY4NDY2OWIwNTIyMzY3YmM2NGFhNmQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTc4ZTgwOWJiMzRhNDkyMGFiZTdmODg1ODJjMzI2ZWMuYmluZFBvcHVwKHBvcHVwXzg4OGRhZGY1ODI1ODQyMmFhYmRmMTgyM2FjMjA3MzAwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhiYjZiYTM5NjI3NTRiM2RhY2Q3NzM4N2M0NWVhYWQzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzc4NTE3NSwtNzkuMzQ2NTU1N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84YWVhNWZlZmQ5MGQ0OGU5OWIzYmJlMjQ2ZDY4YWNhZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80OTBlYzM0ZTU4NjI0NWU0OGRkMjNjNjI1NWMxOTUyZSA9ICQoJzxkaXYgaWQ9Imh0bWxfNDkwZWMzNGU1ODYyNDVlNDhkZDIzYzYyNTVjMTk1MmUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZhaXJ2aWV3LEhlbnJ5IEZhcm0sT3Jpb2xlLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhhZWE1ZmVmZDkwZDQ4ZTk5YjNiYmUyNDZkNjhhY2FlLnNldENvbnRlbnQoaHRtbF80OTBlYzM0ZTU4NjI0NWU0OGRkMjNjNjI1NWMxOTUyZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84YmI2YmEzOTYyNzU0YjNkYWNkNzczODdjNDVlYWFkMy5iaW5kUG9wdXAocG9wdXBfOGFlYTVmZWZkOTBkNDhlOTliM2JiZTI0NmQ2OGFjYWUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzQ0YWU4NjY0OWZhNDgzMzhjYjBiYWEyNWE0ZjVlOTQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43ODY5NDczLC03OS4zODU5NzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGIyZWRkYWQ3NWE4NDQ4N2JiNTcxMmUzMzYxZmU0MzUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTlhZDZmNzBlYTQ4NDk2OWEwZDM4ZDNlMDUxZTQxMTcgPSAkKCc8ZGl2IGlkPSJodG1sX2E5YWQ2ZjcwZWE0ODQ5NjlhMGQzOGQzZTA1MWU0MTE3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXl2aWV3IFZpbGxhZ2UsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZGIyZWRkYWQ3NWE4NDQ4N2JiNTcxMmUzMzYxZmU0MzUuc2V0Q29udGVudChodG1sX2E5YWQ2ZjcwZWE0ODQ5NjlhMGQzOGQzZTA1MWU0MTE3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc0NGFlODY2NDlmYTQ4MzM4Y2IwYmFhMjVhNGY1ZTk0LmJpbmRQb3B1cChwb3B1cF9kYjJlZGRhZDc1YTg0NDg3YmI1NzEyZTMzNjFmZTQzNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84Y2M4MDc0YzZiNzA0MjlmYTAwOTIxZGU1ZTk4NGExNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1NzQ5MDIsLTc5LjM3NDcxNDA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzQzYmIxOGZkMDMzMTQzMGFhMjVmYjRjZmVjYzI4M2M4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2NkMWViNzYxOGZlNDRlNmFhNzU5M2EyZGE1OGYxOWE2ID0gJCgnPGRpdiBpZD0iaHRtbF9jZDFlYjc2MThmZTQ0ZTZhYTc1OTNhMmRhNThmMTlhNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U2lsdmVyIEhpbGxzLFlvcmsgTWlsbHMsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDNiYjE4ZmQwMzMxNDMwYWEyNWZiNGNmZWNjMjgzYzguc2V0Q29udGVudChodG1sX2NkMWViNzYxOGZlNDRlNmFhNzU5M2EyZGE1OGYxOWE2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhjYzgwNzRjNmI3MDQyOWZhMDA5MjFkZTVlOTg0YTE3LmJpbmRQb3B1cChwb3B1cF80M2JiMThmZDAzMzE0MzBhYTI1ZmI0Y2ZlY2MyODNjOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xYzNhZDcwMzUxMzU0ZDQxYWI3OTQ0OWFhMzM5ZWMxZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4OTA1MywtNzkuNDA4NDkyNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzQ1M2MyZjQxZjdkNGE3MTk5NmE5NWNjZDQ5MDMzZGYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDQwZGFlYmQxZjU1NDgzMzg4YmE1YTAwM2I1MGYwMzYgPSAkKCc8ZGl2IGlkPSJodG1sX2Q0MGRhZWJkMWY1NTQ4MzM4OGJhNWEwMDNiNTBmMDM2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5OZXd0b25icm9vayxXaWxsb3dkYWxlLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc0NTNjMmY0MWY3ZDRhNzE5OTZhOTVjY2Q0OTAzM2RmLnNldENvbnRlbnQoaHRtbF9kNDBkYWViZDFmNTU0ODMzODhiYTVhMDAzYjUwZjAzNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xYzNhZDcwMzUxMzU0ZDQxYWI3OTQ0OWFhMzM5ZWMxZS5iaW5kUG9wdXAocG9wdXBfNzQ1M2MyZjQxZjdkNGE3MTk5NmE5NWNjZDQ5MDMzZGYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmE5MjJiNWNmY2NhNGQ2Y2JlMmFjMjFiZDFjNTkwZWQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NzAxMTk5LC03OS40MDg0OTI3OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ZWJiMDliYjUyNjM0MzM3YjRiM2Y1ZjhkYzllYjY0ZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mNmY5MTJmMGQ0M2Y0YTVjOTk2ZDBhNzlkNTRkOTFmZSA9ICQoJzxkaXYgaWQ9Imh0bWxfZjZmOTEyZjBkNDNmNGE1Yzk5NmQwYTc5ZDU0ZDkxZmUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxvd2RhbGUgU291dGgsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNGViYjA5YmI1MjYzNDMzN2I0YjNmNWY4ZGM5ZWI2NGUuc2V0Q29udGVudChodG1sX2Y2ZjkxMmYwZDQzZjRhNWM5OTZkMGE3OWQ1NGQ5MWZlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZhOTIyYjVjZmNjYTRkNmNiZTJhYzIxYmQxYzU5MGVkLmJpbmRQb3B1cChwb3B1cF80ZWJiMDliYjUyNjM0MzM3YjRiM2Y1ZjhkYzllYjY0ZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85ZTY3OTkzNzMwMDY0Y2VlOTVjYjVjMTAwMWJiYmUzZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1Mjc1ODI5OTk5OTk5NiwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wNzc1YjNmZTY0YzA0MmI1YTYzNDk5NTYyNTQ2YTdjZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84MzQxMjM5YmViNTQ0YWM4YTM0ZGZmNGNjZjM3YmZjMSA9ICQoJzxkaXYgaWQ9Imh0bWxfODM0MTIzOWJlYjU0NGFjOGEzNGRmZjRjY2YzN2JmYzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPllvcmsgTWlsbHMgV2VzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wNzc1YjNmZTY0YzA0MmI1YTYzNDk5NTYyNTQ2YTdjZS5zZXRDb250ZW50KGh0bWxfODM0MTIzOWJlYjU0NGFjOGEzNGRmZjRjY2YzN2JmYzEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWU2Nzk5MzczMDA2NGNlZTk1Y2I1YzEwMDFiYmJlM2QuYmluZFBvcHVwKHBvcHVwXzA3NzViM2ZlNjRjMDQyYjVhNjM0OTk1NjI1NDZhN2NlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RmZjEyMGI3OGU0ODQ2OWY4Nzk2MjljZTgzN2NjNjAyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzgyNzM2NCwtNzkuNDQyMjU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82OGVlZjliYzQzNGM0ZjI5OWZjMTdlN2QwODI0YmQ1YiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNjgyMzkwMzMyYTk0YjNkYWYwMmU5Yjk4Y2EzY2QyZiA9ICQoJzxkaXYgaWQ9Imh0bWxfMzY4MjM5MDMzMmE5NGIzZGFmMDJlOWI5OGNhM2NkMmYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxvd2RhbGUgV2VzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82OGVlZjliYzQzNGM0ZjI5OWZjMTdlN2QwODI0YmQ1Yi5zZXRDb250ZW50KGh0bWxfMzY4MjM5MDMzMmE5NGIzZGFmMDJlOWI5OGNhM2NkMmYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGZmMTIwYjc4ZTQ4NDY5Zjg3OTYyOWNlODM3Y2M2MDIuYmluZFBvcHVwKHBvcHVwXzY4ZWVmOWJjNDM0YzRmMjk5ZmMxN2U3ZDA4MjRiZDViKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIzOTFiYTMyMDQ4ODQyYjQ4ODg1MmNjNDQzMTQwMGU1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzUzMjU4NiwtNzkuMzI5NjU2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jMGQ0M2RjNmYyZDA0MTE3ODU3ZmRmZjQ5ZmY5NzIwMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xMDVmOTllZjc2ZWM0NDgwOGUxYmFkMDc1NDhjNmM3MCA9ICQoJzxkaXYgaWQ9Imh0bWxfMTA1Zjk5ZWY3NmVjNDQ4MDhlMWJhZDA3NTQ4YzZjNzAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBhcmt3b29kcywgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jMGQ0M2RjNmYyZDA0MTE3ODU3ZmRmZjQ5ZmY5NzIwMC5zZXRDb250ZW50KGh0bWxfMTA1Zjk5ZWY3NmVjNDQ4MDhlMWJhZDA3NTQ4YzZjNzApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjM5MWJhMzIwNDg4NDJiNDg4ODUyY2M0NDMxNDAwZTUuYmluZFBvcHVwKHBvcHVwX2MwZDQzZGM2ZjJkMDQxMTc4NTdmZGZmNDlmZjk3MjAwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJhMzIyNDBiZmY3ZTRjM2FiYzI2MGZhYTM3NTMxODc5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ1OTA1Nzk5OTk5OTk2LC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzA2OTY3YTBjMjk4NDI1MTljNWM3N2ViOWU0NGU1NTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDkzODZjMmRhMjZkNDFlOGFmY2Q3N2U4NmIzMWY2MjcgPSAkKCc8ZGl2IGlkPSJodG1sXzA5Mzg2YzJkYTI2ZDQxZThhZmNkNzdlODZiMzFmNjI3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb24gTWlsbHMgTm9ydGgsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzA2OTY3YTBjMjk4NDI1MTljNWM3N2ViOWU0NGU1NTYuc2V0Q29udGVudChodG1sXzA5Mzg2YzJkYTI2ZDQxZThhZmNkNzdlODZiMzFmNjI3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJhMzIyNDBiZmY3ZTRjM2FiYzI2MGZhYTM3NTMxODc5LmJpbmRQb3B1cChwb3B1cF9jMDY5NjdhMGMyOTg0MjUxOWM1Yzc3ZWI5ZTQ0ZTU1Nik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lZjNiMWQ3OTZiNjU0MGQ5OGM5ZGU3ZmQwYjY0ZTgyNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNTg5OTcwMDAwMDAxLC03OS4zNDA5MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTkyNjk5Y2YyNWM3NDNiMzk4NWNkMGE2ZDVlNzEwNjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODQ3ZTYzOWJhYTkyNDgxMThiMTU5NjQxZjcyYmZiYzcgPSAkKCc8ZGl2IGlkPSJodG1sXzg0N2U2MzliYWE5MjQ4MTE4YjE1OTY0MWY3MmJmYmM3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GbGVtaW5nZG9uIFBhcmssRG9uIE1pbGxzIFNvdXRoLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU5MjY5OWNmMjVjNzQzYjM5ODVjZDBhNmQ1ZTcxMDY1LnNldENvbnRlbnQoaHRtbF84NDdlNjM5YmFhOTI0ODExOGIxNTk2NDFmNzJiZmJjNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lZjNiMWQ3OTZiNjU0MGQ5OGM5ZGU3ZmQwYjY0ZTgyNS5iaW5kUG9wdXAocG9wdXBfNTkyNjk5Y2YyNWM3NDNiMzk4NWNkMGE2ZDVlNzEwNjUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzA0ZmJjNDZiYzk2NGVlYTkxOTBlZDZlYjljOWNkNjQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTQzMjgzLC03OS40NDIyNTkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzNiMWIyZDhhZWIxZjQ1ZThhM2E1NWQ3NWNjYWQ2MWJmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2RmNjU0ZGVjNDg2ZDQ2YzI4NTVmOTExMGIxMTAzZjk4ID0gJCgnPGRpdiBpZD0iaHRtbF9kZjY1NGRlYzQ4NmQ0NmMyODU1ZjkxMTBiMTEwM2Y5OCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmF0aHVyc3QgTWFub3IsRG93bnN2aWV3IE5vcnRoLFdpbHNvbiBIZWlnaHRzLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNiMWIyZDhhZWIxZjQ1ZThhM2E1NWQ3NWNjYWQ2MWJmLnNldENvbnRlbnQoaHRtbF9kZjY1NGRlYzQ4NmQ0NmMyODU1ZjkxMTBiMTEwM2Y5OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMDRmYmM0NmJjOTY0ZWVhOTE5MGVkNmViOWM5Y2Q2NC5iaW5kUG9wdXAocG9wdXBfM2IxYjJkOGFlYjFmNDVlOGEzYTU1ZDc1Y2NhZDYxYmYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2VmMmNhNDBmYjFhNGJiYzk5YjQ3ODBmNjRmMGNjY2EgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Njc5ODAzLC03OS40ODcyNjE5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85MjNkNTYzODZkN2M0YTAzYjUxODJlY2ZjOThkZjY1OSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lZGE1ZDI3ZmVkNzE0NDc1YmIzYWQyMTk5YjAwZDU0ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfZWRhNWQyN2ZlZDcxNDQ3NWJiM2FkMjE5OWIwMGQ1NGUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vcnRod29vZCBQYXJrLFlvcmsgVW5pdmVyc2l0eSwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85MjNkNTYzODZkN2M0YTAzYjUxODJlY2ZjOThkZjY1OS5zZXRDb250ZW50KGh0bWxfZWRhNWQyN2ZlZDcxNDQ3NWJiM2FkMjE5OWIwMGQ1NGUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfY2VmMmNhNDBmYjFhNGJiYzk5YjQ3ODBmNjRmMGNjY2EuYmluZFBvcHVwKHBvcHVwXzkyM2Q1NjM4NmQ3YzRhMDNiNTE4MmVjZmM5OGRmNjU5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RmYTZmN2JlZTllMDQ1N2RiZWVjMmE1MmM3YTM3ZmIwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzM3NDczMjAwMDAwMDA0LC03OS40NjQ3NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81OThjYzIzZTBmMjU0M2M5YWY3YWZhOTI2MWIzNTk1OSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84YzI5NGI0N2IyMjc0ODc5ODI1ZDVkZjBlYTU1ODIxNSA9ICQoJzxkaXYgaWQ9Imh0bWxfOGMyOTRiNDdiMjI3NDg3OTgyNWQ1ZGYwZWE1NTgyMTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNGQiBUb3JvbnRvLERvd25zdmlldyBFYXN0LCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU5OGNjMjNlMGYyNTQzYzlhZjdhZmE5MjYxYjM1OTU5LnNldENvbnRlbnQoaHRtbF84YzI5NGI0N2IyMjc0ODc5ODI1ZDVkZjBlYTU1ODIxNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kZmE2ZjdiZWU5ZTA0NTdkYmVlYzJhNTJjN2EzN2ZiMC5iaW5kUG9wdXAocG9wdXBfNTk4Y2MyM2UwZjI1NDNjOWFmN2FmYTkyNjFiMzU5NTkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWQyNGFlNWE4ODg3NGNjZGFjMGQ1MjdjMjFmMGRmYTkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MzkwMTQ2LC03OS41MDY5NDM2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y4NGIyMWNlZjQwYzRiM2E5OTE1YmQwMzZjMzRkMTEwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzkxZDc1M2YwZGQwOTQzMzk4ZThmZGU1MWQ4YjdiODYxID0gJCgnPGRpdiBpZD0iaHRtbF85MWQ3NTNmMGRkMDk0MzM5OGU4ZmRlNTFkOGI3Yjg2MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IFdlc3QsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjg0YjIxY2VmNDBjNGIzYTk5MTViZDAzNmMzNGQxMTAuc2V0Q29udGVudChodG1sXzkxZDc1M2YwZGQwOTQzMzk4ZThmZGU1MWQ4YjdiODYxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2FkMjRhZTVhODg4NzRjY2RhYzBkNTI3YzIxZjBkZmE5LmJpbmRQb3B1cChwb3B1cF9mODRiMjFjZWY0MGM0YjNhOTkxNWJkMDM2YzM0ZDExMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mNTc0MWVmNzRmYjA0MTIwYmI0MTBlYzk1OTEzZDBiOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyODQ5NjQsLTc5LjQ5NTY5NzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2UyNzVlZmZhOGEzMTQ0N2Y5MTE0YmI3ODVlOTQwNDBmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FmZmQ0ODhkNDRiNjQyYTZhN2EzYzgxYTlhNTU5ZjQ3ID0gJCgnPGRpdiBpZD0iaHRtbF9hZmZkNDg4ZDQ0YjY0MmE2YTdhM2M4MWE5YTU1OWY0NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IENlbnRyYWwsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTI3NWVmZmE4YTMxNDQ3ZjkxMTRiYjc4NWU5NDA0MGYuc2V0Q29udGVudChodG1sX2FmZmQ0ODhkNDRiNjQyYTZhN2EzYzgxYTlhNTU5ZjQ3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y1NzQxZWY3NGZiMDQxMjBiYjQxMGVjOTU5MTNkMGI5LmJpbmRQb3B1cChwb3B1cF9lMjc1ZWZmYThhMzE0NDdmOTExNGJiNzg1ZTk0MDQwZik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wNDZiMGM2MjZjZjM0Yjc4YWEwZjI4OTBiMzc0YTRmNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc2MTYzMTMsLTc5LjUyMDk5OTQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NhYzE2YjExNDljNjRjODU5NWYxMDg1NWZiY2QyMTIyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Y4Y2Q5ZjVkODEyNTRhZTU5MGUxZDkyYzFkNWY3MTY0ID0gJCgnPGRpdiBpZD0iaHRtbF9mOGNkOWY1ZDgxMjU0YWU1OTBlMWQ5MmMxZDVmNzE2NCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IE5vcnRod2VzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jYWMxNmIxMTQ5YzY0Yzg1OTVmMTA4NTVmYmNkMjEyMi5zZXRDb250ZW50KGh0bWxfZjhjZDlmNWQ4MTI1NGFlNTkwZTFkOTJjMWQ1ZjcxNjQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDQ2YjBjNjI2Y2YzNGI3OGFhMGYyODkwYjM3NGE0ZjcuYmluZFBvcHVwKHBvcHVwX2NhYzE2YjExNDljNjRjODU5NWYxMDg1NWZiY2QyMTIyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzUzZDdiNTBiYzUwZTQzZDdhZjI2OTM2MTk1N2QyYTc4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI1ODgyMjk5OTk5OTk1LC03OS4zMTU1NzE1OTk5OTk5OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zMmI3ZmRiMWVkMDI0NTdmYmE1ODE1ODllYzU2ZTdmMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yODE0OGRhMTNjODU0YWZlYmZkZDkxYWYwNjI4MmUxNiA9ICQoJzxkaXYgaWQ9Imh0bWxfMjgxNDhkYTEzYzg1NGFmZWJmZGQ5MWFmMDYyODJlMTYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlZpY3RvcmlhIFZpbGxhZ2UsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzJiN2ZkYjFlZDAyNDU3ZmJhNTgxNTg5ZWM1NmU3ZjAuc2V0Q29udGVudChodG1sXzI4MTQ4ZGExM2M4NTRhZmViZmRkOTFhZjA2MjgyZTE2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzUzZDdiNTBiYzUwZTQzZDdhZjI2OTM2MTk1N2QyYTc4LmJpbmRQb3B1cChwb3B1cF8zMmI3ZmRiMWVkMDI0NTdmYmE1ODE1ODllYzU2ZTdmMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zNWZlNTM4ZjMwNjc0OTE0ODQwNDcwMzIzMzMzZWQ3NiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcwNjM5NzIsLTc5LjMwOTkzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xODllMzJmNTRiOWQ0MzgxOTU1OWU3YzRlNzg1ZjJlMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84YTI3YWUzNmFlNGQ0ODZhODE3YzExYTJjMTdkZWI2NyA9ICQoJzxkaXYgaWQ9Imh0bWxfOGEyN2FlMzZhZTRkNDg2YTgxN2MxMWEyYzE3ZGViNjciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldvb2RiaW5lIEdhcmRlbnMsUGFya3ZpZXcgSGlsbCwgRWFzdFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzE4OWUzMmY1NGI5ZDQzODE5NTU5ZTdjNGU3ODVmMmUzLnNldENvbnRlbnQoaHRtbF84YTI3YWUzNmFlNGQ0ODZhODE3YzExYTJjMTdkZWI2Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zNWZlNTM4ZjMwNjc0OTE0ODQwNDcwMzIzMzMzZWQ3Ni5iaW5kUG9wdXAocG9wdXBfMTg5ZTMyZjU0YjlkNDM4MTk1NTllN2M0ZTc4NWYyZTMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmM1N2I1NGU3ZDNhNDBkYTgzMDZkYzc2NWUwYjVkNTMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTUzNDM5MDAwMDAwMDUsLTc5LjMxODM4ODddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMGJlZWU5YmFhZDg3NDE0YmEyY2IzNDg2NWZiYWMzMGUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjczZDE1NGY1MmEwNGNjZWEwZDM1YzU4ODIwMzk0MzEgPSAkKCc8ZGl2IGlkPSJodG1sXzY3M2QxNTRmNTJhMDRjY2VhMGQzNWM1ODgyMDM5NDMxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Xb29kYmluZSBIZWlnaHRzLCBFYXN0WW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMGJlZWU5YmFhZDg3NDE0YmEyY2IzNDg2NWZiYWMzMGUuc2V0Q29udGVudChodG1sXzY3M2QxNTRmNTJhMDRjY2VhMGQzNWM1ODgyMDM5NDMxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZjNTdiNTRlN2QzYTQwZGE4MzA2ZGM3NjVlMGI1ZDUzLmJpbmRQb3B1cChwb3B1cF8wYmVlZTliYWFkODc0MTRiYTJjYjM0ODY1ZmJhYzMwZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yNGZhMzUyMDhiNWI0ZmQwYTdjYTI1ZjkwNzRjZDFiMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY3NjM1NzM5OTk5OTk5LC03OS4yOTMwMzEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y1NzYwMzljN2IxYzQ3YWViN2JmZTQ3NmJkYWQyZTg0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Y4NTRmZTJhZDdjNDRhZDNhODZlMDFkZmZiODQ5MjA5ID0gJCgnPGRpdiBpZD0iaHRtbF9mODU0ZmUyYWQ3YzQ0YWQzYTg2ZTAxZGZmYjg0OTIwOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhlIEJlYWNoZXMsIEVhc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNTc2MDM5YzdiMWM0N2FlYjdiZmU0NzZiZGFkMmU4NC5zZXRDb250ZW50KGh0bWxfZjg1NGZlMmFkN2M0NGFkM2E4NmUwMWRmZmI4NDkyMDkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjRmYTM1MjA4YjViNGZkMGE3Y2EyNWY5MDc0Y2QxYjEuYmluZFBvcHVwKHBvcHVwX2Y1NzYwMzljN2IxYzQ3YWViN2JmZTQ3NmJkYWQyZTg0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2MwNTFkYTUzZDk3NjQ4NmM5ZTZmYjI3NGJmMjM3Y2YzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA5MDYwNCwtNzkuMzYzNDUxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lYmMzZDI1NjY5NTU0NzMyYjc4MDQzODMyYjhmY2FiMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zODgzMTgwMmMzZDU0MWQwOTI2YzA2MmZmMWE4MzAwZiA9ICQoJzxkaXYgaWQ9Imh0bWxfMzg4MzE4MDJjM2Q1NDFkMDkyNmMwNjJmZjFhODMwMGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxlYXNpZGUsIEVhc3RZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lYmMzZDI1NjY5NTU0NzMyYjc4MDQzODMyYjhmY2FiMi5zZXRDb250ZW50KGh0bWxfMzg4MzE4MDJjM2Q1NDFkMDkyNmMwNjJmZjFhODMwMGYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzA1MWRhNTNkOTc2NDg2YzllNmZiMjc0YmYyMzdjZjMuYmluZFBvcHVwKHBvcHVwX2ViYzNkMjU2Njk1NTQ3MzJiNzgwNDM4MzJiOGZjYWIyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzgxMzQzMGI1MjhkODQwZWQ5OGVhYTM2ZjMzOTg2MGZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA1MzY4OSwtNzkuMzQ5MzcxOTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmZkYzE5NWYwNzE1NGVjOTk1ODcyZGM3ZWYwNzdhNTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWQyYTBkZmQ1NDc2NGRmYjg4ZjhiYWQzNmJlNWI3ZTkgPSAkKCc8ZGl2IGlkPSJodG1sX2VkMmEwZGZkNTQ3NjRkZmI4OGY4YmFkMzZiZTViN2U5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaG9ybmNsaWZmZSBQYXJrLCBFYXN0WW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmZkYzE5NWYwNzE1NGVjOTk1ODcyZGM3ZWYwNzdhNTIuc2V0Q29udGVudChodG1sX2VkMmEwZGZkNTQ3NjRkZmI4OGY4YmFkMzZiZTViN2U5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzgxMzQzMGI1MjhkODQwZWQ5OGVhYTM2ZjMzOTg2MGZhLmJpbmRQb3B1cChwb3B1cF9mZmRjMTk1ZjA3MTU0ZWM5OTU4NzJkYzdlZjA3N2E1Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mZGE2MTcxODk1NWU0NjE0OTg5N2Y2NGQ0MTI4NjgwMyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY4NTM0NywtNzkuMzM4MTA2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85MzE5YmVkMTAzNTM0YmNmYjkyZGUzZTVmNGY1ODdiZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xZGYxZTBmZjMxMzY0YTI5YWY5MDExNDdiM2YyYTExOCA9ICQoJzxkaXYgaWQ9Imh0bWxfMWRmMWUwZmYzMTM2NGEyOWFmOTAxMTQ3YjNmMmExMTgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgVG9yb250bywgRWFzdFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzkzMTliZWQxMDM1MzRiY2ZiOTJkZTNlNWY0ZjU4N2JmLnNldENvbnRlbnQoaHRtbF8xZGYxZTBmZjMxMzY0YTI5YWY5MDExNDdiM2YyYTExOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mZGE2MTcxODk1NWU0NjE0OTg5N2Y2NGQ0MTI4NjgwMy5iaW5kUG9wdXAocG9wdXBfOTMxOWJlZDEwMzUzNGJjZmI5MmRlM2U1ZjRmNTg3YmYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2YxMWI4OTI3MTY5NGFkYWI1MzRjYzQxZDYzZTI5ZmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Nzk1NTcxLC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzUwOTI1ZTIzZDhmNGMzMDk2MjUxY2Q0ZDg0ZmFmYmMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDFmYTAwYTU5MTYwNDk2MDliYjg5YmJkMjcwYzk3MjIgPSAkKCc8ZGl2IGlkPSJodG1sXzAxZmEwMGE1OTE2MDQ5NjA5YmI4OWJiZDI3MGM5NzIyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgRGFuZm9ydGggV2VzdCxSaXZlcmRhbGUsIEVhc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jNTA5MjVlMjNkOGY0YzMwOTYyNTFjZDRkODRmYWZiYy5zZXRDb250ZW50KGh0bWxfMDFmYTAwYTU5MTYwNDk2MDliYjg5YmJkMjcwYzk3MjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2YxMWI4OTI3MTY5NGFkYWI1MzRjYzQxZDYzZTI5ZmIuYmluZFBvcHVwKHBvcHVwX2M1MDkyNWUyM2Q4ZjRjMzA5NjI1MWNkNGQ4NGZhZmJjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNmZWExMjQwOWEwYTQ5Y2JiZDM3NzY1MDZjMjdlMzNlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY4OTk4NSwtNzkuMzE1NTcxNTk5OTk5OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGExNjM2MjI1NTA4NGQ0OGEwN2FjMDA2ZGY3ZmVjMDggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDUwZGRhMjhkOGQxNDFjOWE1YWY0MDFlMjFkODYzMjggPSAkKCc8ZGl2IGlkPSJodG1sX2Q1MGRkYTI4ZDhkMTQxYzlhNWFmNDAxZTIxZDg2MzI4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgQmVhY2hlcyBXZXN0LEluZGlhIEJhemFhciwgRWFzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzhhMTYzNjIyNTUwODRkNDhhMDdhYzAwNmRmN2ZlYzA4LnNldENvbnRlbnQoaHRtbF9kNTBkZGEyOGQ4ZDE0MWM5YTVhZjQwMWUyMWQ4NjMyOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zZmVhMTI0MDlhMGE0OWNiYmQzNzc2NTA2YzI3ZTMzZS5iaW5kUG9wdXAocG9wdXBfOGExNjM2MjI1NTA4NGQ0OGEwN2FjMDA2ZGY3ZmVjMDgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2UyOWIyNjRkN2ZiNGZjZDgwOGI3MmIyNGRmMDM1NjQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTk1MjU1LC03OS4zNDA5MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjQyMDcwZDQ0ZjQyNDQzNWFhZjE5MDU1Y2I5YzkyY2MgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjUyODUxNzY2MThhNDBjOWEzZTEyMTJjYjZlYmVlZDUgPSAkKCc8ZGl2IGlkPSJodG1sX2Y1Mjg1MTc2NjE4YTQwYzlhM2UxMjEyY2I2ZWJlZWQ1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdHVkaW8gRGlzdHJpY3QsIEVhc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNDIwNzBkNDRmNDI0NDM1YWFmMTkwNTVjYjljOTJjYy5zZXRDb250ZW50KGh0bWxfZjUyODUxNzY2MThhNDBjOWEzZTEyMTJjYjZlYmVlZDUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2UyOWIyNjRkN2ZiNGZjZDgwOGI3MmIyNGRmMDM1NjQuYmluZFBvcHVwKHBvcHVwX2Y0MjA3MGQ0NGY0MjQ0MzVhYWYxOTA1NWNiOWM5MmNjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY5OWFiMzBjMGM4YTRjNWQ4ZTdjMzBkMjhjYjE1MTAyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI4MDIwNSwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hZWMzMzkyYmFiZGY0ZjlhODEwNWZkY2NjYmFjYzY3ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84MjA0NDYxYWQzMmY0OWMyYTVjNmQyMGU4NzFhZDM4ZCA9ICQoJzxkaXYgaWQ9Imh0bWxfODIwNDQ2MWFkMzJmNDljMmE1YzZkMjBlODcxYWQzOGQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIFBhcmssIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hZWMzMzkyYmFiZGY0ZjlhODEwNWZkY2NjYmFjYzY3ZC5zZXRDb250ZW50KGh0bWxfODIwNDQ2MWFkMzJmNDljMmE1YzZkMjBlODcxYWQzOGQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjk5YWIzMGMwYzhhNGM1ZDhlN2MzMGQyOGNiMTUxMDIuYmluZFBvcHVwKHBvcHVwX2FlYzMzOTJiYWJkZjRmOWE4MTA1ZmRjY2NiYWNjNjdkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2QxN2YwNGQ2OTRiNTRlNTc5MzJhODI4NjEzYWQwNWQ4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzEyNzUxMSwtNzkuMzkwMTk3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNDhiODg2NTJiODA0OTgwYmNhOGI3ZDY0ZmYzYjFmMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82OWVlZmMwNDM3NzA0ZmMwYmNmMmRmYzUyZGE1YjRmNiA9ICQoJzxkaXYgaWQ9Imh0bWxfNjllZWZjMDQzNzcwNGZjMGJjZjJkZmM1MmRhNWI0ZjYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUgTm9ydGgsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hNDhiODg2NTJiODA0OTgwYmNhOGI3ZDY0ZmYzYjFmMS5zZXRDb250ZW50KGh0bWxfNjllZWZjMDQzNzcwNGZjMGJjZjJkZmM1MmRhNWI0ZjYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDE3ZjA0ZDY5NGI1NGU1NzkzMmE4Mjg2MTNhZDA1ZDguYmluZFBvcHVwKHBvcHVwX2E0OGI4ODY1MmI4MDQ5ODBiY2E4YjdkNjRmZjNiMWYxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2YwOWU2N2YzNzAwZDQ3Mzk5YzIzN2ZmMzE4ZmJjYjkzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE1MzgzNCwtNzkuNDA1Njc4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzU3MGUzMjc0NzdjNGY0YmExNzY2OGY1YWNhZjk5NDEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjM1N2FhMmI0ZWQ3NGJhOWFkYzc4ZWQwNDc4YzgzZTEgPSAkKCc8ZGl2IGlkPSJodG1sX2IzNTdhYTJiNGVkNzRiYTlhZGM3OGVkMDQ3OGM4M2UxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aCBUb3JvbnRvIFdlc3QsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zNTcwZTMyNzQ3N2M0ZjRiYTE3NjY4ZjVhY2FmOTk0MS5zZXRDb250ZW50KGh0bWxfYjM1N2FhMmI0ZWQ3NGJhOWFkYzc4ZWQwNDc4YzgzZTEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjA5ZTY3ZjM3MDBkNDczOTljMjM3ZmYzMThmYmNiOTMuYmluZFBvcHVwKHBvcHVwXzM1NzBlMzI3NDc3YzRmNGJhMTc2NjhmNWFjYWY5OTQxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VjNmIyZWJjOGMxMDRiNDJhYmJmMTkzZjAxNThjY2FlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA0MzI0NCwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mNWU1ZThhYWJhZTU0YTliOGVkZGM1Yjk2YTJiZmJkYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83ZWYwMmZkZmVlNzA0ZTVjOTlhOTFjNDdiMmQ1MjFhMiA9ICQoJzxkaXYgaWQ9Imh0bWxfN2VmMDJmZGZlZTcwNGU1Yzk5YTkxYzQ3YjJkNTIxYTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNWU1ZThhYWJhZTU0YTliOGVkZGM1Yjk2YTJiZmJkYy5zZXRDb250ZW50KGh0bWxfN2VmMDJmZGZlZTcwNGU1Yzk5YTkxYzQ3YjJkNTIxYTIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZWM2YjJlYmM4YzEwNGI0MmFiYmYxOTNmMDE1OGNjYWUuYmluZFBvcHVwKHBvcHVwX2Y1ZTVlOGFhYmFlNTRhOWI4ZWRkYzViOTZhMmJmYmRjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzA5MzUyYjAxYjc3OTQ0MmJiZWEwODcwNmRkNDcxMjc5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg5NTc0MywtNzkuMzgzMTU5OTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWU5YmMxM2NmNDE1NDkzN2I3MWMwYjE5Y2VkNDY1ZWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjVjYjE3ODI0N2UyNGExNDkwMWE1MWIzZTk1NDA2YjggPSAkKCc8ZGl2IGlkPSJodG1sX2Y1Y2IxNzgyNDdlMjRhMTQ5MDFhNTFiM2U5NTQwNmI4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb29yZSBQYXJrLFN1bW1lcmhpbGwgRWFzdCwgQ2VudHJhbFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzllOWJjMTNjZjQxNTQ5MzdiNzFjMGIxOWNlZDQ2NWVjLnNldENvbnRlbnQoaHRtbF9mNWNiMTc4MjQ3ZTI0YTE0OTAxYTUxYjNlOTU0MDZiOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wOTM1MmIwMWI3Nzk0NDJiYmVhMDg3MDZkZDQ3MTI3OS5iaW5kUG9wdXAocG9wdXBfOWU5YmMxM2NmNDE1NDkzN2I3MWMwYjE5Y2VkNDY1ZWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOTA2Y2U5YjQ1NDVhNDc1NGFiOWMwMTc4NTk4NDdjZjQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42ODY0MTIyOTk5OTk5OSwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hZWEzYzU2NzQzMzA0OGI3OGI1YTMyM2M0MmVlZTI0NyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iNzcxMDVjYWEzMGE0YmY4Yjk2Y2I0N2E4NThmNmEyNSA9ICQoJzxkaXYgaWQ9Imh0bWxfYjc3MTA1Y2FhMzBhNGJmOGI5NmNiNDdhODU4ZjZhMjUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRlZXIgUGFyayxGb3Jlc3QgSGlsbCBTRSxSYXRobmVsbHksU291dGggSGlsbCxTdW1tZXJoaWxsIFdlc3QsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hZWEzYzU2NzQzMzA0OGI3OGI1YTMyM2M0MmVlZTI0Ny5zZXRDb250ZW50KGh0bWxfYjc3MTA1Y2FhMzBhNGJmOGI5NmNiNDdhODU4ZjZhMjUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTA2Y2U5YjQ1NDVhNDc1NGFiOWMwMTc4NTk4NDdjZjQuYmluZFBvcHVwKHBvcHVwX2FlYTNjNTY3NDMzMDQ4Yjc4YjVhMzIzYzQyZWVlMjQ3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRmNTgwNjIxMjNmZjQyOGRhZmQ1ZmQ5MGJlOTdiMDlkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjc5NTYyNiwtNzkuMzc3NTI5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzliMjk1N2ExNzFjNDZlOTk5YzI4OTM4ZDhiMWIyNDMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTVkMTUwZWNkYWJmNDVjMTgzODJiZTMzOGQxMzlmMjUgPSAkKCc8ZGl2IGlkPSJodG1sXzk1ZDE1MGVjZGFiZjQ1YzE4MzgyYmUzMzhkMTM5ZjI1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlZGFsZSwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zOWIyOTU3YTE3MWM0NmU5OTljMjg5MzhkOGIxYjI0My5zZXRDb250ZW50KGh0bWxfOTVkMTUwZWNkYWJmNDVjMTgzODJiZTMzOGQxMzlmMjUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNGY1ODA2MjEyM2ZmNDI4ZGFmZDVmZDkwYmU5N2IwOWQuYmluZFBvcHVwKHBvcHVwXzM5YjI5NTdhMTcxYzQ2ZTk5OWMyODkzOGQ4YjFiMjQzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y1Y2U2YThjNDAyMDRkMjY4MDJmNjZkMTI0MWZjMTk3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY3OTY3LC03OS4zNjc2NzUzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzYxMzBlMDdmMWMyYTQzMWQ5MDdlM2JmNmJiZDc3OGUxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQwZTU5Y2I2MTAwOTQxM2FhNWE3M2UzNGE2NjNiZGMzID0gJCgnPGRpdiBpZD0iaHRtbF80MGU1OWNiNjEwMDk0MTNhYTVhNzNlMzRhNjYzYmRjMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FiYmFnZXRvd24sU3QuIEphbWVzIFRvd24sIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjEzMGUwN2YxYzJhNDMxZDkwN2UzYmY2YmJkNzc4ZTEuc2V0Q29udGVudChodG1sXzQwZTU5Y2I2MTAwOTQxM2FhNWE3M2UzNGE2NjNiZGMzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y1Y2U2YThjNDAyMDRkMjY4MDJmNjZkMTI0MWZjMTk3LmJpbmRQb3B1cChwb3B1cF82MTMwZTA3ZjFjMmE0MzFkOTA3ZTNiZjZiYmQ3NzhlMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hNjZhYmUyNGMzY2U0OGYzYTU5MTczMjUzNDFhNzZhNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2NTg1OTksLTc5LjM4MzE1OTkwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE2YjQwYjRlZGY3ZTRhZGZhOTk5OGM3MmQ2MDA1ZmIwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2IzNTMyNjdjMjhjNjRkZWI4MTRiZDRhMTlkM2Y0ZDhiID0gJCgnPGRpdiBpZD0iaHRtbF9iMzUzMjY3YzI4YzY0ZGViODE0YmQ0YTE5ZDNmNGQ4YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2h1cmNoIGFuZCBXZWxsZXNsZXksIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTZiNDBiNGVkZjdlNGFkZmE5OTk4YzcyZDYwMDVmYjAuc2V0Q29udGVudChodG1sX2IzNTMyNjdjMjhjNjRkZWI4MTRiZDRhMTlkM2Y0ZDhiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2E2NmFiZTI0YzNjZTQ4ZjNhNTkxNzMyNTM0MWE3NmE3LmJpbmRQb3B1cChwb3B1cF8xNmI0MGI0ZWRmN2U0YWRmYTk5OThjNzJkNjAwNWZiMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mYzBjM2NjYzNlY2U0YjU5YmE4YjQ1NTY2ZTk4YTIxOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1NDI1OTksLTc5LjM2MDYzNTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmVlYWZiMTdjZDgwNDFjMTk4OWI0ZDBiNTM3YmQ3Y2YgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDU5NjNjMDc1ZDE3NDk1YTg4MjlkOWY5NDQ5YTFmNDQgPSAkKCc8ZGl2IGlkPSJodG1sXzQ1OTYzYzA3NWQxNzQ5NWE4ODI5ZDlmOTQ0OWExZjQ0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQsUmVnZW50IFBhcmssIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmVlYWZiMTdjZDgwNDFjMTk4OWI0ZDBiNTM3YmQ3Y2Yuc2V0Q29udGVudChodG1sXzQ1OTYzYzA3NWQxNzQ5NWE4ODI5ZDlmOTQ0OWExZjQ0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZjMGMzY2NjM2VjZTRiNTliYThiNDU1NjZlOThhMjE5LmJpbmRQb3B1cChwb3B1cF8yZWVhZmIxN2NkODA0MWMxOTg5YjRkMGI1MzdiZDdjZik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iMWEyYWYwZjk3NDk0NGRhYTAxNmE2NjVjOTkxNDBhOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1NzE2MTgsLTc5LjM3ODkzNzA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U4NTJiNjMxYjYxNTRlOTBhZWI5NDdkOTU4YWNjMmQ0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY1ZGUxYmM3NTY5ZDRjZDI5OWM4NjgzYjZlOWEwMGQ4ID0gJCgnPGRpdiBpZD0iaHRtbF82NWRlMWJjNzU2OWQ0Y2QyOTljODY4M2I2ZTlhMDBkOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UnllcnNvbixHYXJkZW4gRGlzdHJpY3QsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTg1MmI2MzFiNjE1NGU5MGFlYjk0N2Q5NThhY2MyZDQuc2V0Q29udGVudChodG1sXzY1ZGUxYmM3NTY5ZDRjZDI5OWM4NjgzYjZlOWEwMGQ4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2IxYTJhZjBmOTc0OTQ0ZGFhMDE2YTY2NWM5OTE0MGE4LmJpbmRQb3B1cChwb3B1cF9lODUyYjYzMWI2MTU0ZTkwYWViOTQ3ZDk1OGFjYzJkNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNmRlODU3ODljNDg0OTYzOWEwZmVmOTIwYTA2NzY4MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1MTQ5MzksLTc5LjM3NTQxNzldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDI3NGViYTc5NWUwNGY1ZmI5MDI4N2FhOGU4NzAxMjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDJhZTk4MzIxZTQwNDlhOWFlMDgxYzk4YmZlYzE3YTAgPSAkKCc8ZGl2IGlkPSJodG1sXzAyYWU5ODMyMWU0MDQ5YTlhZTA4MWM5OGJmZWMxN2EwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdC4gSmFtZXMgVG93biwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wMjc0ZWJhNzk1ZTA0ZjVmYjkwMjg3YWE4ZTg3MDEyNS5zZXRDb250ZW50KGh0bWxfMDJhZTk4MzIxZTQwNDlhOWFlMDgxYzk4YmZlYzE3YTApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTZkZTg1Nzg5YzQ4NDk2MzlhMGZlZjkyMGEwNjc2ODAuYmluZFBvcHVwKHBvcHVwXzAyNzRlYmE3OTVlMDRmNWZiOTAyODdhYThlODcwMTI1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzlmMTM5MGQxNjk5MzQwNmZiZjRiODY1YzM0NzJkNmY1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ0NzcwNzk5OTk5OTk2LC03OS4zNzMzMDY0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzJjYzBiZmNhZGYwOTRmNWZhOTFiMDNjNjVlNWVlZjI0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU4YmYwYjUxNzdiZjRmZDc4OWE3ZTIyNmY1MDE1MjRkID0gJCgnPGRpdiBpZD0iaHRtbF81OGJmMGI1MTc3YmY0ZmQ3ODlhN2UyMjZmNTAxNTI0ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVyY3p5IFBhcmssIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmNjMGJmY2FkZjA5NGY1ZmE5MWIwM2M2NWU1ZWVmMjQuc2V0Q29udGVudChodG1sXzU4YmYwYjUxNzdiZjRmZDc4OWE3ZTIyNmY1MDE1MjRkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzlmMTM5MGQxNjk5MzQwNmZiZjRiODY1YzM0NzJkNmY1LmJpbmRQb3B1cChwb3B1cF8yY2MwYmZjYWRmMDk0ZjVmYTkxYjAzYzY1ZTVlZWYyNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jZjY2MmM3OWJlMzY0NmVjYmMwYTU1Y2Y4ZGUwMDdkNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1Nzk1MjQsLTc5LjM4NzM4MjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTdhZjcwZjcwYTEzNDhmYmJlMmZjY2ZlZWE3ZjRlY2IgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMzEzYzFjYzJiYjEzNDY0Nzg3OTViNTJjNDA1MWZmZDIgPSAkKCc8ZGl2IGlkPSJodG1sXzMxM2MxY2MyYmIxMzQ2NDc4Nzk1YjUyYzQwNTFmZmQyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZW50cmFsIEJheSBTdHJlZXQsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTdhZjcwZjcwYTEzNDhmYmJlMmZjY2ZlZWE3ZjRlY2Iuc2V0Q29udGVudChodG1sXzMxM2MxY2MyYmIxMzQ2NDc4Nzk1YjUyYzQwNTFmZmQyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NmNjYyYzc5YmUzNjQ2ZWNiYzBhNTVjZjhkZTAwN2Q0LmJpbmRQb3B1cChwb3B1cF9lN2FmNzBmNzBhMTM0OGZiYmUyZmNjZmVlYTdmNGVjYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jYTBmYzA5OTAzMDg0YWE0YjJlYTE0NmVlOWM2MGNjNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1MDU3MTIwMDAwMDAxLC03OS4zODQ1Njc1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzVhMWUwZGI5ZTRiYjQ4YmNhZDEwMzk2ZmVkM2U2N2JhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2VjNWU4ZmZmOTQ1MTQ1YTA4MWZmZjA2N2Q1M2IzZmY4ID0gJCgnPGRpdiBpZD0iaHRtbF9lYzVlOGZmZjk0NTE0NWEwODFmZmYwNjdkNTNiM2ZmOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWRlbGFpZGUsS2luZyxSaWNobW9uZCwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81YTFlMGRiOWU0YmI0OGJjYWQxMDM5NmZlZDNlNjdiYS5zZXRDb250ZW50KGh0bWxfZWM1ZThmZmY5NDUxNDVhMDgxZmZmMDY3ZDUzYjNmZjgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfY2EwZmMwOTkwMzA4NGFhNGIyZWExNDZlZTljNjBjYzQuYmluZFBvcHVwKHBvcHVwXzVhMWUwZGI5ZTRiYjQ4YmNhZDEwMzk2ZmVkM2U2N2JhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk4MTgwMWUzMmJjMjRlZDA4ZDBmMzJkYjhhYmQxMDZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQwODE1NywtNzkuMzgxNzUyMjk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDRiOWMwZjdmOWZlNGQ2MGI3NzgyMmQ0N2IxMjQ3YWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTFjMmQyYzVlNmY3NDBhNjhjNTM3ZTU0MzE5N2ZmNzIgPSAkKCc8ZGl2IGlkPSJodG1sX2ExYzJkMmM1ZTZmNzQwYTY4YzUzN2U1NDMxOTdmZjcyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQgRWFzdCxUb3JvbnRvIElzbGFuZHMsVW5pb24gU3RhdGlvbiwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kNGI5YzBmN2Y5ZmU0ZDYwYjc3ODIyZDQ3YjEyNDdhYy5zZXRDb250ZW50KGh0bWxfYTFjMmQyYzVlNmY3NDBhNjhjNTM3ZTU0MzE5N2ZmNzIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTgxODAxZTMyYmMyNGVkMDhkMGYzMmRiOGFiZDEwNmEuYmluZFBvcHVwKHBvcHVwX2Q0YjljMGY3ZjlmZTRkNjBiNzc4MjJkNDdiMTI0N2FjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIxNDIxMDQ0ZWU5ZDQ4NmU5OTRhYjQyNDdiMDFiYzlhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ3MTc2OCwtNzkuMzgxNTc2NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmJkOWI0NTJhY2U0NDgyMDg3MzQ4N2Q0MmYwOThlMTUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2VhODkwZTQ4ZDBkNDdiOTgwYjg3ZWJlNjM1ZDkwOTEgPSAkKCc8ZGl2IGlkPSJodG1sXzdlYTg5MGU0OGQwZDQ3Yjk4MGI4N2ViZTYzNWQ5MDkxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5EZXNpZ24gRXhjaGFuZ2UsVG9yb250byBEb21pbmlvbiBDZW50cmUsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYmJkOWI0NTJhY2U0NDgyMDg3MzQ4N2Q0MmYwOThlMTUuc2V0Q29udGVudChodG1sXzdlYTg5MGU0OGQwZDQ3Yjk4MGI4N2ViZTYzNWQ5MDkxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzIxNDIxMDQ0ZWU5ZDQ4NmU5OTRhYjQyNDdiMDFiYzlhLmJpbmRQb3B1cChwb3B1cF9iYmQ5YjQ1MmFjZTQ0ODIwODczNDg3ZDQyZjA5OGUxNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iZTRlZTA2NzgxNGE0ZTNlOTk4MTQ3MzViYjQxZjMyZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY0ODE5ODUsLTc5LjM3OTgxNjkwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE2M2RkZmE3NTk2OTRkYTBiM2E1NjQyY2M5Y2Q5YTgwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzZkMDAxNzU5MzA3MDRmMzk5ZTJlM2Y0ZWY5MmY3ZDA1ID0gJCgnPGRpdiBpZD0iaHRtbF82ZDAwMTc1OTMwNzA0ZjM5OWUyZTNmNGVmOTJmN2QwNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q29tbWVyY2UgQ291cnQsVmljdG9yaWEgSG90ZWwsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTYzZGRmYTc1OTY5NGRhMGIzYTU2NDJjYzljZDlhODAuc2V0Q29udGVudChodG1sXzZkMDAxNzU5MzA3MDRmMzk5ZTJlM2Y0ZWY5MmY3ZDA1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2JlNGVlMDY3ODE0YTRlM2U5OTgxNDczNWJiNDFmMzJlLmJpbmRQb3B1cChwb3B1cF8xNjNkZGZhNzU5Njk0ZGEwYjNhNTY0MmNjOWNkOWE4MCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xZGI3ZmZlYjAyOGE0OTNjODhhOWM2YjY2ZjZmMDRiMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjczMzI4MjUsLTc5LjQxOTc0OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2U2MDVjMDY2ODBhNDM3ZjlhMGQ0YzhhZDg4MTM5YjYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODI5N2M2MjBlOGJjNDMwOThlNGQ1ZTQ4MDBmOGI0YWUgPSAkKCc8ZGl2IGlkPSJodG1sXzgyOTdjNjIwZThiYzQzMDk4ZTRkNWU0ODAwZjhiNGFlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWRmb3JkIFBhcmssTGF3cmVuY2UgTWFub3IgRWFzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83ZTYwNWMwNjY4MGE0MzdmOWEwZDRjOGFkODgxMzliNi5zZXRDb250ZW50KGh0bWxfODI5N2M2MjBlOGJjNDMwOThlNGQ1ZTQ4MDBmOGI0YWUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMWRiN2ZmZWIwMjhhNDkzYzg4YTljNmI2NmY2ZjA0YjAuYmluZFBvcHVwKHBvcHVwXzdlNjA1YzA2NjgwYTQzN2Y5YTBkNGM4YWQ4ODEzOWI2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2JmM2MyNDcwMmQxZDRkMzA5ZWYxZTM1MGUwMmI1Mzg2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzExNjk0OCwtNzkuNDE2OTM1NTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDNlMTBiMjc5MjgxNDgyYWEyZjBhNTRjZTcwY2FiNmIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjFjNTViOGNhNjY3NGQ2NDk3N2IwNmRkYjI5YWRjODcgPSAkKCc8ZGl2IGlkPSJodG1sX2YxYzU1YjhjYTY2NzRkNjQ5NzdiMDZkZGIyOWFkYzg3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlbGF3biwgQ2VudHJhbFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2QzZTEwYjI3OTI4MTQ4MmFhMmYwYTU0Y2U3MGNhYjZiLnNldENvbnRlbnQoaHRtbF9mMWM1NWI4Y2E2Njc0ZDY0OTc3YjA2ZGRiMjlhZGM4Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iZjNjMjQ3MDJkMWQ0ZDMwOWVmMWUzNTBlMDJiNTM4Ni5iaW5kUG9wdXAocG9wdXBfZDNlMTBiMjc5MjgxNDgyYWEyZjBhNTRjZTcwY2FiNmIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZGRmNjI5YWU2MjMwNGQ4MThlOTAzYzFiZWYyYTlhNDcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTY5NDc2LC03OS40MTEzMDcyMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wNjljOTBlMGQ3Y2M0Yzg4OGQ2YTQ1MTc2N2JlMTJjMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zZDg2N2QxZTk2NDg0NWU2OTRhMDgxZGIzZjMzZTI2NiA9ICQoJzxkaXYgaWQ9Imh0bWxfM2Q4NjdkMWU5NjQ4NDVlNjk0YTA4MWRiM2YzM2UyNjYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZvcmVzdCBIaWxsIE5vcnRoLEZvcmVzdCBIaWxsIFdlc3QsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wNjljOTBlMGQ3Y2M0Yzg4OGQ2YTQ1MTc2N2JlMTJjMS5zZXRDb250ZW50KGh0bWxfM2Q4NjdkMWU5NjQ4NDVlNjk0YTA4MWRiM2YzM2UyNjYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGRmNjI5YWU2MjMwNGQ4MThlOTAzYzFiZWYyYTlhNDcuYmluZFBvcHVwKHBvcHVwXzA2OWM5MGUwZDdjYzRjODg4ZDZhNDUxNzY3YmUxMmMxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBmN2ZiOGI1NjA3NTQwZjA4NzdmMzFmNDBhZmZkNzQwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjcyNzA5NywtNzkuNDA1Njc4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzM2NjIxYzZkYWFlNGIxN2E2ZmQyYjQ0MjI5N2VjOWIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMGJiYzM2ODE4OTEzNGI3Y2JmY2NkZDgzMjNmYmY4MjMgPSAkKCc8ZGl2IGlkPSJodG1sXzBiYmMzNjgxODkxMzRiN2NiZmNjZGQ4MzIzZmJmODIzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgQW5uZXgsTm9ydGggTWlkdG93bixZb3JrdmlsbGUsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zMzY2MjFjNmRhYWU0YjE3YTZmZDJiNDQyMjk3ZWM5Yi5zZXRDb250ZW50KGh0bWxfMGJiYzM2ODE4OTEzNGI3Y2JmY2NkZDgzMjNmYmY4MjMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMGY3ZmI4YjU2MDc1NDBmMDg3N2YzMWY0MGFmZmQ3NDAuYmluZFBvcHVwKHBvcHVwXzMzNjYyMWM2ZGFhZTRiMTdhNmZkMmI0NDIyOTdlYzliKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y0NmY4MTczYzU2YzRhZDU5NGIyNDNjOWQ4NDk2MjIzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjYyNjk1NiwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ZjkwMGU1NTYyOTQ0MzMyODUyOTZkNTQ3OTAxYjk0NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84NGE3ZTEwMGY4NDQ0ZmM1YTVmZTBjZDZmYzk3ZWMzNiA9ICQoJzxkaXYgaWQ9Imh0bWxfODRhN2UxMDBmODQ0NGZjNWE1ZmUwY2Q2ZmM5N2VjMzYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhhcmJvcmQsVW5pdmVyc2l0eSBvZiBUb3JvbnRvLCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdmOTAwZTU1NjI5NDQzMzI4NTI5NmQ1NDc5MDFiOTQ0LnNldENvbnRlbnQoaHRtbF84NGE3ZTEwMGY4NDQ0ZmM1YTVmZTBjZDZmYzk3ZWMzNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mNDZmODE3M2M1NmM0YWQ1OTRiMjQzYzlkODQ5NjIyMy5iaW5kUG9wdXAocG9wdXBfN2Y5MDBlNTU2Mjk0NDMzMjg1Mjk2ZDU0NzkwMWI5NDQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWVmMGM4NDY0YmMxNDk1MGFhMzA3NWE4N2JmYWE4MjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTMyMDU3LC03OS40MDAwNDkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NhODRlZjJkMzZhMzRiZGY4NzE0OGRjZmQ3ZjE4OWFkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQ5Mjc5YWY1MDY0ODQ4NGRiNGNiZjZjN2MxNzlkZWU5ID0gJCgnPGRpdiBpZD0iaHRtbF80OTI3OWFmNTA2NDg0ODRkYjRjYmY2YzdjMTc5ZGVlOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2hpbmF0b3duLEdyYW5nZSBQYXJrLEtlbnNpbmd0b24gTWFya2V0LCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2NhODRlZjJkMzZhMzRiZGY4NzE0OGRjZmQ3ZjE4OWFkLnNldENvbnRlbnQoaHRtbF80OTI3OWFmNTA2NDg0ODRkYjRjYmY2YzdjMTc5ZGVlOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hZWYwYzg0NjRiYzE0OTUwYWEzMDc1YTg3YmZhYTgyOC5iaW5kUG9wdXAocG9wdXBfY2E4NGVmMmQzNmEzNGJkZjg3MTQ4ZGNmZDdmMTg5YWQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDhhNWQzYzA4YThjNDY5Yjk5NjBhYzhiODQ2YzJmY2EgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Mjg5NDY3LC03OS4zOTQ0MTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2QyNWJhMTJjMDVmNjRlM2I5MjEyZGMyMGM3MmNjNGU0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Y5N2MwYjExOGFlYzQ1NTk5OTQ5YzVlYTM0MDQ3YjU2ID0gJCgnPGRpdiBpZD0iaHRtbF9mOTdjMGIxMThhZWM0NTU5OTk0OWM1ZWEzNDA0N2I1NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q04gVG93ZXIsQmF0aHVyc3QgUXVheSxJc2xhbmQgYWlycG9ydCxIYXJib3VyZnJvbnQgV2VzdCxLaW5nIGFuZCBTcGFkaW5hLFJhaWx3YXkgTGFuZHMsU291dGggTmlhZ2FyYSwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kMjViYTEyYzA1ZjY0ZTNiOTIxMmRjMjBjNzJjYzRlNC5zZXRDb250ZW50KGh0bWxfZjk3YzBiMTE4YWVjNDU1OTk5NDljNWVhMzQwNDdiNTYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDhhNWQzYzA4YThjNDY5Yjk5NjBhYzhiODQ2YzJmY2EuYmluZFBvcHVwKHBvcHVwX2QyNWJhMTJjMDVmNjRlM2I5MjEyZGMyMGM3MmNjNGU0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY0NzE4YjllMTdhMjRhMTliNDQ3NWYwZTQ1MzZjZjM2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ2NDM1MiwtNzkuMzc0ODQ1OTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODkwZGNlNTA1ZDQzNGU1NjhiYzcwZDIzY2Y5NTAwNjEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWUxZmVlZGNkYjkyNGE3OTk0MmY2YmNjZTc2MTY0ZGMgPSAkKCc8ZGl2IGlkPSJodG1sXzVlMWZlZWRjZGI5MjRhNzk5NDJmNmJjY2U3NjE2NGRjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdG4gQSBQTyBCb3hlcyAyNSBUaGUgRXNwbGFuYWRlLCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg5MGRjZTUwNWQ0MzRlNTY4YmM3MGQyM2NmOTUwMDYxLnNldENvbnRlbnQoaHRtbF81ZTFmZWVkY2RiOTI0YTc5OTQyZjZiY2NlNzYxNjRkYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82NDcxOGI5ZTE3YTI0YTE5YjQ0NzVmMGU0NTM2Y2YzNi5iaW5kUG9wdXAocG9wdXBfODkwZGNlNTA1ZDQzNGU1NjhiYzcwZDIzY2Y5NTAwNjEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWJhMTI3MTQxMzYxNDgzZWE3ZWY2MDJmOGIzZjcwYzQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDg0MjkyLC03OS4zODIyODAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzIxMTIwZjBjZDNmMjQ4OWU4YTg3OGYxM2JmMzFlOWJiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzUxNjg0M2E2N2VmZjRjMjI4NjcxNTczZTJiZDNjOThiID0gJCgnPGRpdiBpZD0iaHRtbF81MTY4NDNhNjdlZmY0YzIyODY3MTU3M2UyYmQzYzk4YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rmlyc3QgQ2FuYWRpYW4gUGxhY2UsVW5kZXJncm91bmQgY2l0eSwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yMTEyMGYwY2QzZjI0ODllOGE4NzhmMTNiZjMxZTliYi5zZXRDb250ZW50KGh0bWxfNTE2ODQzYTY3ZWZmNGMyMjg2NzE1NzNlMmJkM2M5OGIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWJhMTI3MTQxMzYxNDgzZWE3ZWY2MDJmOGIzZjcwYzQuYmluZFBvcHVwKHBvcHVwXzIxMTIwZjBjZDNmMjQ4OWU4YTg3OGYxM2JmMzFlOWJiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFhYTJhNTI4NWJjZjQ2NGQ4MjI0ZjBmNzhiOGQ4MGM4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE4NTE3OTk5OTk5OTk2LC03OS40NjQ3NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mNzBmZjcyY2M3ZGE0ODY0OTQ2MjUyOTZkODQ3YjU4ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zNDY0NTY2MWI2N2M0YTZjOTM1NTczMGQ3ZjBlNzkwZSA9ICQoJzxkaXYgaWQ9Imh0bWxfMzQ2NDU2NjFiNjdjNGE2YzkzNTU3MzBkN2YwZTc5MGUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIEhlaWdodHMsTGF3cmVuY2UgTWFub3IsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjcwZmY3MmNjN2RhNDg2NDk0NjI1Mjk2ZDg0N2I1OGYuc2V0Q29udGVudChodG1sXzM0NjQ1NjYxYjY3YzRhNmM5MzU1NzMwZDdmMGU3OTBlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFhYTJhNTI4NWJjZjQ2NGQ4MjI0ZjBmNzhiOGQ4MGM4LmJpbmRQb3B1cChwb3B1cF9mNzBmZjcyY2M3ZGE0ODY0OTQ2MjUyOTZkODQ3YjU4Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85OWZjYzI5ODMwZjQ0NWY4OWI3MmFkYzRhZjVkNTdkYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcwOTU3NywtNzkuNDQ1MDcyNTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjgyMDZhNjg2YWI1NDBkMGEzYTU0MmUyOGQ4NjUyMDUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTA5MjJmNjVlYjE5NGJiMDk5YjcxN2Y4ODc2ZjVhZTYgPSAkKCc8ZGl2IGlkPSJodG1sXzUwOTIyZjY1ZWIxOTRiYjA5OWI3MTdmODg3NmY1YWU2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HbGVuY2Fpcm4sIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjgyMDZhNjg2YWI1NDBkMGEzYTU0MmUyOGQ4NjUyMDUuc2V0Q29udGVudChodG1sXzUwOTIyZjY1ZWIxOTRiYjA5OWI3MTdmODg3NmY1YWU2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk5ZmNjMjk4MzBmNDQ1Zjg5YjcyYWRjNGFmNWQ1N2RhLmJpbmRQb3B1cChwb3B1cF9iODIwNmE2ODZhYjU0MGQwYTNhNTQyZTI4ZDg2NTIwNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNjdlZjgzOGE5NDE0ZTZiOWM4MzQ1ZWEzMDE1OTE5YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5Mzc4MTMsLTc5LjQyODE5MTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzU3MDRhYTJhYWQwZDRiY2NiMGZkZTRiZDhjMzQxODM5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJlMmJiYTVlZjQ3MjRhMjNiODZhNjFjN2IyMjk3YzVkID0gJCgnPGRpdiBpZD0iaHRtbF8yZTJiYmE1ZWY0NzI0YTIzYjg2YTYxYzdiMjI5N2M1ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtZXdvb2QtQ2VkYXJ2YWxlLCBZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81NzA0YWEyYWFkMGQ0YmNjYjBmZGU0YmQ4YzM0MTgzOS5zZXRDb250ZW50KGh0bWxfMmUyYmJhNWVmNDcyNGEyM2I4NmE2MWM3YjIyOTdjNWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDY3ZWY4MzhhOTQxNGU2YjljODM0NWVhMzAxNTkxOWMuYmluZFBvcHVwKHBvcHVwXzU3MDRhYTJhYWQwZDRiY2NiMGZkZTRiZDhjMzQxODM5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzlhNmI0ZjgwMjhmZDQzZWM5Y2ZjN2E4ZTlkY2JjOTdlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg5MDI1NiwtNzkuNDUzNTEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzM5NDEwNDIwYTE5ZDQ3MmE4NWYyNWZjMTIwMTkwZmQ4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzUxNjU4ODFmZTRkMDQxMDBiZDg4ODAxM2MwMWZlNWQxID0gJCgnPGRpdiBpZD0iaHRtbF81MTY1ODgxZmU0ZDA0MTAwYmQ4ODgwMTNjMDFmZTVkMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FsZWRvbmlhLUZhaXJiYW5rcywgWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzk0MTA0MjBhMTlkNDcyYTg1ZjI1ZmMxMjAxOTBmZDguc2V0Q29udGVudChodG1sXzUxNjU4ODFmZTRkMDQxMDBiZDg4ODAxM2MwMWZlNWQxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzlhNmI0ZjgwMjhmZDQzZWM5Y2ZjN2E4ZTlkY2JjOTdlLmJpbmRQb3B1cChwb3B1cF8zOTQxMDQyMGExOWQ0NzJhODVmMjVmYzEyMDE5MGZkOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yZTc3YzM4MmEzZTk0MGQ2YWE4ZDczZTYzMmI0YmVjOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2OTU0MiwtNzkuNDIyNTYzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mNzIxMzM2NjA0Mzk0MGJjOWM4NzM3YmEwMDUzMDM2ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xYzc4OTlkNDk1NzI0MWFhYWI1ZTUyYjY3YTU4M2ZkMyA9ICQoJzxkaXYgaWQ9Imh0bWxfMWM3ODk5ZDQ5NTcyNDFhYWFiNWU1MmI2N2E1ODNmZDMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNocmlzdGllLCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y3MjEzMzY2MDQzOTQwYmM5Yzg3MzdiYTAwNTMwMzZkLnNldENvbnRlbnQoaHRtbF8xYzc4OTlkNDk1NzI0MWFhYWI1ZTUyYjY3YTU4M2ZkMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yZTc3YzM4MmEzZTk0MGQ2YWE4ZDczZTYzMmI0YmVjOS5iaW5kUG9wdXAocG9wdXBfZjcyMTMzNjYwNDM5NDBiYzljODczN2JhMDA1MzAzNmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzBhN2JjOGY2MjRkNDJmYmE1NzVlYzU5MTNhNjBiYzAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjkwMDUxMDAwMDAwMSwtNzkuNDQyMjU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wN2U1NzI3NDNmYjM0NjI4OTQwYzdiYzQ3MzI1YjllMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MjZiZDVlNGQzMzk0ZmU0YWFiZTFhZjBlMGUyYjAwNCA9ICQoJzxkaXYgaWQ9Imh0bWxfNTI2YmQ1ZTRkMzM5NGZlNGFhYmUxYWYwZTBlMmIwMDQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvdmVyY291cnQgVmlsbGFnZSxEdWZmZXJpbiwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzA3ZTU3Mjc0M2ZiMzQ2Mjg5NDBjN2JjNDczMjViOWUyLnNldENvbnRlbnQoaHRtbF81MjZiZDVlNGQzMzk0ZmU0YWFiZTFhZjBlMGUyYjAwNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMGE3YmM4ZjYyNGQ0MmZiYTU3NWVjNTkxM2E2MGJjMC5iaW5kUG9wdXAocG9wdXBfMDdlNTcyNzQzZmIzNDYyODk0MGM3YmM0NzMyNWI5ZTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTgxMmUzYjU3N2EzNGQyZWFiZjZlOTJkYjA2NTk0OWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDc5MjY3MDAwMDAwMDYsLTc5LjQxOTc0OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmRhNmYxZDNkZTZmNDk5MDgwZWU5ODhkY2QyYWQ1NDggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWQxZTRlYTkwOThkNDg2YjhhOTNjNDYwYmM2MzgwNWQgPSAkKCc8ZGl2IGlkPSJodG1sXzVkMWU0ZWE5MDk4ZDQ4NmI4YTkzYzQ2MGJjNjM4MDVkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5MaXR0bGUgUG9ydHVnYWwsVHJpbml0eSwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2JkYTZmMWQzZGU2ZjQ5OTA4MGVlOTg4ZGNkMmFkNTQ4LnNldENvbnRlbnQoaHRtbF81ZDFlNGVhOTA5OGQ0ODZiOGE5M2M0NjBiYzYzODA1ZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hODEyZTNiNTc3YTM0ZDJlYWJmNmU5MmRiMDY1OTQ5Yi5iaW5kUG9wdXAocG9wdXBfYmRhNmYxZDNkZTZmNDk5MDgwZWU5ODhkY2QyYWQ1NDgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzYyZDY2MDFiOWJkNGUzNWE3ZmE0NDUyMjdkM2Q2MmUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MzY4NDcyLC03OS40MjgxOTE0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yY2IzM2Y5MmNmMGQ0ZmZkODU4NjhmOGViOWM3ZDA4YyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kOWY1NzQ1ZjUwOTU0NWY2YmUyMjBlNThkNjc5N2FiOCA9ICQoJzxkaXYgaWQ9Imh0bWxfZDlmNTc0NWY1MDk1NDVmNmJlMjIwZTU4ZDY3OTdhYjgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJyb2NrdG9uLEV4aGliaXRpb24gUGxhY2UsUGFya2RhbGUgVmlsbGFnZSwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzJjYjMzZjkyY2YwZDRmZmQ4NTg2OGY4ZWI5YzdkMDhjLnNldENvbnRlbnQoaHRtbF9kOWY1NzQ1ZjUwOTU0NWY2YmUyMjBlNThkNjc5N2FiOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83NjJkNjYwMWI5YmQ0ZTM1YTdmYTQ0NTIyN2QzZDYyZS5iaW5kUG9wdXAocG9wdXBfMmNiMzNmOTJjZjBkNGZmZDg1ODY4ZjhlYjljN2QwOGMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWI3NjI3ZjgxMzNiNDQxNTk5NDdiNzQwZTE2YjU2NGEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MTM3NTYyMDAwMDAwMDYsLTc5LjQ5MDA3MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTgzNjhjYTBkOTE0NDhhZGExMDYxMDhkY2I4NmIxNjYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDcwMmI3NzQ3NmMxNDY1ZWJhYjY3YTY3YmZhMjliYmUgPSAkKCc8ZGl2IGlkPSJodG1sXzA3MDJiNzc0NzZjMTQ2NWViYWI2N2E2N2JmYTI5YmJlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb3duc3ZpZXcsTm9ydGggUGFyayxVcHdvb2QgUGFyaywgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lODM2OGNhMGQ5MTQ0OGFkYTEwNjEwOGRjYjg2YjE2Ni5zZXRDb250ZW50KGh0bWxfMDcwMmI3NzQ3NmMxNDY1ZWJhYjY3YTY3YmZhMjliYmUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWI3NjI3ZjgxMzNiNDQxNTk5NDdiNzQwZTE2YjU2NGEuYmluZFBvcHVwKHBvcHVwX2U4MzY4Y2EwZDkxNDQ4YWRhMTA2MTA4ZGNiODZiMTY2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IyOGIyZWUzYTc2NTQxM2Y5NGMyNmQzZTA3OTVmN2FkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjkxMTE1OCwtNzkuNDc2MDEzMjk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODVkOTM1YzNjNTI3NDliZGI5ZjY5NjkzYTJlOTcwNTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTQ4MWE3OWFhZTU1NGJjYjhiMjdlNGYyZjg4OTRkNzYgPSAkKCc8ZGl2IGlkPSJodG1sXzE0ODFhNzlhYWU1NTRiY2I4YjI3ZTRmMmY4ODk0ZDc2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5EZWwgUmF5LEtlZWxlc2RhbGUsTW91bnQgRGVubmlzLFNpbHZlcnRob3JuLCBZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84NWQ5MzVjM2M1Mjc0OWJkYjlmNjk2OTNhMmU5NzA1OC5zZXRDb250ZW50KGh0bWxfMTQ4MWE3OWFhZTU1NGJjYjhiMjdlNGYyZjg4OTRkNzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjI4YjJlZTNhNzY1NDEzZjk0YzI2ZDNlMDc5NWY3YWQuYmluZFBvcHVwKHBvcHVwXzg1ZDkzNWMzYzUyNzQ5YmRiOWY2OTY5M2EyZTk3MDU4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2QzOGU4MmU3ODkwYzQzMGU5YjI2YzJiOTkyYWMxZWNkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjczMTg1Mjk5OTk5OTksLTc5LjQ4NzI2MTkwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzliZDRhOTlhNmY2ZDQ0OGU5MzZjNTk4ZDgyMTJmNmQ2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzJkYzIxOWNkYjRkZjQyYzU4NGIwZjU0MTQ0ZjQzNmNjID0gJCgnPGRpdiBpZD0iaHRtbF8yZGMyMTljZGI0ZGY0MmM1ODRiMGY1NDE0NGY0MzZjYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhlIEp1bmN0aW9uIE5vcnRoLFJ1bm55bWVkZSwgWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWJkNGE5OWE2ZjZkNDQ4ZTkzNmM1OThkODIxMmY2ZDYuc2V0Q29udGVudChodG1sXzJkYzIxOWNkYjRkZjQyYzU4NGIwZjU0MTQ0ZjQzNmNjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2QzOGU4MmU3ODkwYzQzMGU5YjI2YzJiOTkyYWMxZWNkLmJpbmRQb3B1cChwb3B1cF85YmQ0YTk5YTZmNmQ0NDhlOTM2YzU5OGQ4MjEyZjZkNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kYjI0NWFhZTFiYzg0MTczODBjYmEzNDdkOTVkM2Q5OCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MTYwODMsLTc5LjQ2NDc2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI1N2Y4MTFhMDlmMTQ4ZjlhMmEzZmY3MDYxZTY1YWE5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2YyZTEwNzkwNzE4NzQzODQ5MDU2MDUzYTUxNDcxZGZlID0gJCgnPGRpdiBpZD0iaHRtbF9mMmUxMDc5MDcxODc0Mzg0OTA1NjA1M2E1MTQ3MWRmZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaCBQYXJrLFRoZSBKdW5jdGlvbiBTb3V0aCwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI1N2Y4MTFhMDlmMTQ4ZjlhMmEzZmY3MDYxZTY1YWE5LnNldENvbnRlbnQoaHRtbF9mMmUxMDc5MDcxODc0Mzg0OTA1NjA1M2E1MTQ3MWRmZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kYjI0NWFhZTFiYzg0MTczODBjYmEzNDdkOTVkM2Q5OC5iaW5kUG9wdXAocG9wdXBfMjU3ZjgxMWEwOWYxNDhmOWEyYTNmZjcwNjFlNjVhYTkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDYzMDYwZTEyNjk5NDExODlmNDM5ZmM3ZDg4MWY1NWEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDg5NTk3LC03OS40NTYzMjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTA0MWI2NTliNWIyNDM1MjhmMDMxNjA1MDM0NmU3Y2QgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWY3Y2U2YTlhM2YzNDE3ZTkyNjg2M2VhODliMTY3NTkgPSAkKCc8ZGl2IGlkPSJodG1sXzVmN2NlNmE5YTNmMzQxN2U5MjY4NjNlYTg5YjE2NzU5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrZGFsZSxSb25jZXN2YWxsZXMsIFdlc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85MDQxYjY1OWI1YjI0MzUyOGYwMzE2MDUwMzQ2ZTdjZC5zZXRDb250ZW50KGh0bWxfNWY3Y2U2YTlhM2YzNDE3ZTkyNjg2M2VhODliMTY3NTkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDYzMDYwZTEyNjk5NDExODlmNDM5ZmM3ZDg4MWY1NWEuYmluZFBvcHVwKHBvcHVwXzkwNDFiNjU5YjViMjQzNTI4ZjAzMTYwNTAzNDZlN2NkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y1MzM2MjFiMGI2ZDQzNDg5YTdmNTdiMzk1NzQ4MWU1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUxNTcwNiwtNzkuNDg0NDQ5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zOGI1YTljN2JiYzY0OTU0YmRkMWU0ZTBmYzU0NDg4MSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81ZjFmNGIyNWFlNDY0ZTk1YjhjZjhiOWZjMDFmMzE3YSA9ICQoJzxkaXYgaWQ9Imh0bWxfNWYxZjRiMjVhZTQ2NGU5NWI4Y2Y4YjlmYzAxZjMxN2EiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJ1bm55bWVkZSxTd2Fuc2VhLCBXZXN0VG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzhiNWE5YzdiYmM2NDk1NGJkZDFlNGUwZmM1NDQ4ODEuc2V0Q29udGVudChodG1sXzVmMWY0YjI1YWU0NjRlOTViOGNmOGI5ZmMwMWYzMTdhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y1MzM2MjFiMGI2ZDQzNDg5YTdmNTdiMzk1NzQ4MWU1LmJpbmRQb3B1cChwb3B1cF8zOGI1YTljN2JiYzY0OTU0YmRkMWU0ZTBmYzU0NDg4MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zODc1MDA4ZjA5MDk0ZGZkOWEwMzAwOWIzZTdlMDY5OCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MjMwMTUsLTc5LjM4OTQ5MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWVjYjhiYzJhNzZiNDZjYzk5MjVmZDVkYmE0OWViNDggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTM2OGEyODg3Zjc2NDNkMmEzNzcxMDJhNTc3OGIyMTAgPSAkKCc8ZGl2IGlkPSJodG1sXzEzNjhhMjg4N2Y3NjQzZDJhMzc3MTAyYTU3NzhiMjEwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5RdWVlbiYjMzk7cyBQYXJrLCBRdWVlbiYjMzk7c1Bhcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFlY2I4YmMyYTc2YjQ2Y2M5OTI1ZmQ1ZGJhNDllYjQ4LnNldENvbnRlbnQoaHRtbF8xMzY4YTI4ODdmNzY0M2QyYTM3NzEwMmE1Nzc4YjIxMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zODc1MDA4ZjA5MDk0ZGZkOWEwMzAwOWIzZTdlMDY5OC5iaW5kUG9wdXAocG9wdXBfMWVjYjhiYzJhNzZiNDZjYzk5MjVmZDVkYmE0OWViNDgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTEwZjVkNjBjOWFlNGQ4Njk5ZDQ2N2VlZjhkZDgyZjIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MzY5NjU2LC03OS42MTU4MTg5OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kZDc0NmRmMjhjNTI0ODVmOGE4NGJhYWI0YmJjNWVmMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yMDAwNTc4OTcwYjI0YWM4YjYyNWFjNTY5MGZmOTBhMCA9ICQoJzxkaXYgaWQ9Imh0bWxfMjAwMDU3ODk3MGIyNGFjOGI2MjVhYzU2OTBmZjkwYTAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNhbmFkYSBQb3N0IEdhdGV3YXkgUHJvY2Vzc2luZyBDZW50cmUsIE1pc3Npc3NhdWdhPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kZDc0NmRmMjhjNTI0ODVmOGE4NGJhYWI0YmJjNWVmMy5zZXRDb250ZW50KGh0bWxfMjAwMDU3ODk3MGIyNGFjOGI2MjVhYzU2OTBmZjkwYTApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTEwZjVkNjBjOWFlNGQ4Njk5ZDQ2N2VlZjhkZDgyZjIuYmluZFBvcHVwKHBvcHVwX2RkNzQ2ZGYyOGM1MjQ4NWY4YTg0YmFhYjRiYmM1ZWYzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M2YWY1MjE5ZGNlMjRiYWZiZjRiN2EwZWRhNDJmMzY1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjYyNzQzOSwtNzkuMzIxNTU4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2FiNzBjNjUyMGJiZDRlODFiZmVhZDZkZDZjZjA2OWZjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU2NWQyZTFhODdhNDQzNGY5MGM3MWE4YjU4NmIyYmFmID0gJCgnPGRpdiBpZD0iaHRtbF81NjVkMmUxYTg3YTQ0MzRmOTBjNzFhOGI1ODZiMmJhZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnVzaW5lc3MgUmVwbHkgTWFpbCBQcm9jZXNzaW5nIENlbnRyZSA5NjkgRWFzdGVybiwgRWFzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FiNzBjNjUyMGJiZDRlODFiZmVhZDZkZDZjZjA2OWZjLnNldENvbnRlbnQoaHRtbF81NjVkMmUxYTg3YTQ0MzRmOTBjNzFhOGI1ODZiMmJhZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jNmFmNTIxOWRjZTI0YmFmYmY0YjdhMGVkYTQyZjM2NS5iaW5kUG9wdXAocG9wdXBfYWI3MGM2NTIwYmJkNGU4MWJmZWFkNmRkNmNmMDY5ZmMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODlhZGFkZDRmOTZkNDJmZjlmMDI1NWNhOWNmN2FlMTkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MDU2NDY2LC03OS41MDEzMjA3MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80MTA2YjM0ZjRiYzU0MjA1ODNiYTZiY2RjY2JkY2YyYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jNjI1Y2E1ZjRiNTA0MDBmYTVlYmVkMmMxOWJjNTAxMiA9ICQoJzxkaXYgaWQ9Imh0bWxfYzYyNWNhNWY0YjUwNDAwZmE1ZWJlZDJjMTliYzUwMTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWJlciBCYXkgU2hvcmVzLE1pbWljbyBTb3V0aCxOZXcgVG9yb250bywgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80MTA2YjM0ZjRiYzU0MjA1ODNiYTZiY2RjY2JkY2YyYy5zZXRDb250ZW50KGh0bWxfYzYyNWNhNWY0YjUwNDAwZmE1ZWJlZDJjMTliYzUwMTIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODlhZGFkZDRmOTZkNDJmZjlmMDI1NWNhOWNmN2FlMTkuYmluZFBvcHVwKHBvcHVwXzQxMDZiMzRmNGJjNTQyMDU4M2JhNmJjZGNjYmRjZjJjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzgxN2VjZTZjMzU2MDQxMGI4MDc2YzQ2ODM0ZTQ0NDQ5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjAyNDEzNzAwMDAwMDEsLTc5LjU0MzQ4NDA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzgwMjFjYjQzNDk4YzQzNzFiMjdiZWQ0OGM2ZDM0NzYzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzllOTY4NGZiM2YwZjQxNDQ4MWYyNTA1ZjM2OWYzMzIyID0gJCgnPGRpdiBpZD0iaHRtbF85ZTk2ODRmYjNmMGY0MTQ0ODFmMjUwNWYzNjlmMzMyMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWxkZXJ3b29kLExvbmcgQnJhbmNoLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzgwMjFjYjQzNDk4YzQzNzFiMjdiZWQ0OGM2ZDM0NzYzLnNldENvbnRlbnQoaHRtbF85ZTk2ODRmYjNmMGY0MTQ0ODFmMjUwNWYzNjlmMzMyMik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84MTdlY2U2YzM1NjA0MTBiODA3NmM0NjgzNGU0NDQ0OS5iaW5kUG9wdXAocG9wdXBfODAyMWNiNDM0OThjNDM3MWIyN2JlZDQ4YzZkMzQ3NjMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNWJiZTUxNDdmMDY3NDYyMmFkYTgxY2MzOWM1MjJhZGQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTM2NTM2MDAwMDAwMDUsLTc5LjUwNjk0MzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGIwZjU2N2JjMmEwNGJmODlhYTBmYjg0NjViNjAzZGMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjdmN2E4YmY5YWNjNDc5YmIyNDQxN2I0YzFmYzc5MzggPSAkKCc8ZGl2IGlkPSJodG1sX2Y3ZjdhOGJmOWFjYzQ3OWJiMjQ0MTdiNGMxZmM3OTM4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgS2luZ3N3YXksTW9udGdvbWVyeSBSb2FkLE9sZCBNaWxsIE5vcnRoLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RiMGY1NjdiYzJhMDRiZjg5YWEwZmI4NDY1YjYwM2RjLnNldENvbnRlbnQoaHRtbF9mN2Y3YThiZjlhY2M0NzliYjI0NDE3YjRjMWZjNzkzOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81YmJlNTE0N2YwNjc0NjIyYWRhODFjYzM5YzUyMmFkZC5iaW5kUG9wdXAocG9wdXBfZGIwZjU2N2JjMmEwNGJmODlhYTBmYjg0NjViNjAzZGMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODM4NzA2NmI2NjVmNDkwNmIyOWU0ODRhY2ZiNzAwODkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MzYyNTc5LC03OS40OTg1MDkwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hMGE5NmFiODU2Y2I0ZjBhYjU2OTRhZmE1YmUzZTI3MyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hYTBhNDcwMjU1Mjc0NzRmODgwZWUwYWE2ZGE2ZjljMSA9ICQoJzxkaXYgaWQ9Imh0bWxfYWEwYTQ3MDI1NTI3NDc0Zjg4MGVlMGFhNmRhNmY5YzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWJlciBCYXksS2luZyYjMzk7cyBNaWxsIFBhcmssS2luZ3N3YXkgUGFyayBTb3V0aCBFYXN0LE1pbWljbyBORSxPbGQgTWlsbCBTb3V0aCxUaGUgUXVlZW5zd2F5IEVhc3QsUm95YWwgWW9yayBTb3V0aCBFYXN0LFN1bm55bGVhLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2EwYTk2YWI4NTZjYjRmMGFiNTY5NGFmYTViZTNlMjczLnNldENvbnRlbnQoaHRtbF9hYTBhNDcwMjU1Mjc0NzRmODgwZWUwYWE2ZGE2ZjljMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84Mzg3MDY2YjY2NWY0OTA2YjI5ZTQ4NGFjZmI3MDA4OS5iaW5kUG9wdXAocG9wdXBfYTBhOTZhYjg1NmNiNGYwYWI1Njk0YWZhNWJlM2UyNzMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMWM4OWQ2MGNkMDFmNDhmZjlkMDVlYzUyNGQ1N2U5NDEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Mjg4NDA4LC03OS41MjA5OTk0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lNDE2YWI5NDRjMzE0YjE0YjBhZmI2MTJkYjk2NmIwZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84MTdiOTBiNmQwYTc0NWJlOTYwYmQwNWJhMTQ1ZjBhMyA9ICQoJzxkaXYgaWQ9Imh0bWxfODE3YjkwYjZkMGE3NDViZTk2MGJkMDViYTE0NWYwYTMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPktpbmdzd2F5IFBhcmsgU291dGggV2VzdCxNaW1pY28gTlcsVGhlIFF1ZWVuc3dheSBXZXN0LFJveWFsIFlvcmsgU291dGggV2VzdCxTb3V0aCBvZiBCbG9vciwgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lNDE2YWI5NDRjMzE0YjE0YjBhZmI2MTJkYjk2NmIwZC5zZXRDb250ZW50KGh0bWxfODE3YjkwYjZkMGE3NDViZTk2MGJkMDViYTE0NWYwYTMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMWM4OWQ2MGNkMDFmNDhmZjlkMDVlYzUyNGQ1N2U5NDEuYmluZFBvcHVwKHBvcHVwX2U0MTZhYjk0NGMzMTRiMTRiMGFmYjYxMmRiOTY2YjBkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI0NWIxMjkzZjczNjRhMjdiN2M0NDA2MDEzZTQxYTU3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY3ODU1NiwtNzkuNTMyMjQyNDAwMDAwMDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWQyY2MzYWZiMjQzNGM0MGEwYTBkODJmNmZkNzJkZDkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2FiNzViMTdhZDM2NDVmNDg3NWI3YmJiZTcxNzU5MzYgPSAkKCc8ZGl2IGlkPSJodG1sXzNhYjc1YjE3YWQzNjQ1ZjQ4NzViN2JiYmU3MTc1OTM2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Jc2xpbmd0b24gQXZlbnVlLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzVkMmNjM2FmYjI0MzRjNDBhMGEwZDgyZjZmZDcyZGQ5LnNldENvbnRlbnQoaHRtbF8zYWI3NWIxN2FkMzY0NWY0ODc1YjdiYmJlNzE3NTkzNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yNDViMTI5M2Y3MzY0YTI3YjdjNDQwNjAxM2U0MWE1Ny5iaW5kUG9wdXAocG9wdXBfNWQyY2MzYWZiMjQzNGM0MGEwYTBkODJmNmZkNzJkZDkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjBkNTQ0NzFhNDM0NDQ2YzgxY2I3YmVjMDI1NDNkM2YgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTA5NDMyLC03OS41NTQ3MjQ0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84MjIyZGU3MTFiZjI0NzgyYTQ5MTFhYjcxNzI2N2MzZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83YTc2YTdlNTI4M2M0YTY5YTU1MmUzZGNkYzc3MDJjYiA9ICQoJzxkaXYgaWQ9Imh0bWxfN2E3NmE3ZTUyODNjNGE2OWE1NTJlM2RjZGM3NzAyY2IiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsb3ZlcmRhbGUsSXNsaW5ndG9uLE1hcnRpbiBHcm92ZSxQcmluY2VzcyBHYXJkZW5zLFdlc3QgRGVhbmUgUGFyaywgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84MjIyZGU3MTFiZjI0NzgyYTQ5MTFhYjcxNzI2N2MzZi5zZXRDb250ZW50KGh0bWxfN2E3NmE3ZTUyODNjNGE2OWE1NTJlM2RjZGM3NzAyY2IpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjBkNTQ0NzFhNDM0NDQ2YzgxY2I3YmVjMDI1NDNkM2YuYmluZFBvcHVwKHBvcHVwXzgyMjJkZTcxMWJmMjQ3ODJhNDkxMWFiNzE3MjY3YzNmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VlMjcyOTY4NjU0ZjQzOWFhOTgxNGM3MWNhMTNjMDg0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQzNTE1MiwtNzkuNTc3MjAwNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZWQ4Yzg4YTQ4OWJhNGZkYmJiMTMzY2MzNWY4NGRlODMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjU0OGY4OWQzODg0NDc3ZWI4MzdkY2ZhY2JhNzcwMDQgPSAkKCc8ZGl2IGlkPSJodG1sX2I1NDhmODlkMzg4NDQ3N2ViODM3ZGNmYWNiYTc3MDA0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CbG9vcmRhbGUgR2FyZGVucyxFcmluZ2F0ZSxNYXJrbGFuZCBXb29kLE9sZCBCdXJuaGFtdGhvcnBlLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2VkOGM4OGE0ODliYTRmZGJiYjEzM2NjMzVmODRkZTgzLnNldENvbnRlbnQoaHRtbF9iNTQ4Zjg5ZDM4ODQ0NzdlYjgzN2RjZmFjYmE3NzAwNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lZTI3Mjk2ODY1NGY0MzlhYTk4MTRjNzFjYTEzYzA4NC5iaW5kUG9wdXAocG9wdXBfZWQ4Yzg4YTQ4OWJhNGZkYmJiMTMzY2MzNWY4NGRlODMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2U4MGRjNGJjNjdlNDczZTlkNmMzZTJlYjViOWY0NGUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTYzMDMzLC03OS41NjU5NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84NDU2Nzc3ODBlYzg0NGFjYTRkZWJjYmE5YjUzYTE5ZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85N2YzNjM2NTYyYjY0ODkzOWRjM2YyYjY2NGMwMmVmZCA9ICQoJzxkaXYgaWQ9Imh0bWxfOTdmMzYzNjU2MmI2NDg5MzlkYzNmMmI2NjRjMDJlZmQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWJlciBTdW1taXQsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODQ1Njc3NzgwZWM4NDRhY2E0ZGViY2JhOWI1M2ExOWUuc2V0Q29udGVudChodG1sXzk3ZjM2MzY1NjJiNjQ4OTM5ZGMzZjJiNjY0YzAyZWZkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NlODBkYzRiYzY3ZTQ3M2U5ZDZjM2UyZWI1YjlmNDRlLmJpbmRQb3B1cChwb3B1cF84NDU2Nzc3ODBlYzg0NGFjYTRkZWJjYmE5YjUzYTE5ZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jYzRhNzg0NjJlZDI0OThkYjhkN2Q0NWUxYWQ4NmViMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNDc2NTksLTc5LjUzMjI0MjQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RkOTFmZmNlOTM5YjQ0MTliOGUxMzFlNTExOWUyM2E0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzQ5MjU2ZTlmMGI1MjQ3ZGZhNWE5YWMyMmRkNzg1NWNkID0gJCgnPGRpdiBpZD0iaHRtbF80OTI1NmU5ZjBiNTI0N2RmYTVhOWFjMjJkZDc4NTVjZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RW1lcnksSHVtYmVybGVhLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RkOTFmZmNlOTM5YjQ0MTliOGUxMzFlNTExOWUyM2E0LnNldENvbnRlbnQoaHRtbF80OTI1NmU5ZjBiNTI0N2RmYTVhOWFjMjJkZDc4NTVjZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jYzRhNzg0NjJlZDI0OThkYjhkN2Q0NWUxYWQ4NmViMS5iaW5kUG9wdXAocG9wdXBfZGQ5MWZmY2U5MzliNDQxOWI4ZTEzMWU1MTE5ZTIzYTQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2I0M2MyMGEwZjFjNDFlZDg2MjZjZDkxYTg0OGM3ODUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MDY4NzYsLTc5LjUxODE4ODQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzhhYjk5YTcyYzc0YjQzNmFhOTM4OWVkNWIzNTFkMDhkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzhlZDVmOGNhZTY4ODQzMGY5MDg1NTYzNzNhYzkwOTIwID0gJCgnPGRpdiBpZD0iaHRtbF84ZWQ1ZjhjYWU2ODg0MzBmOTA4NTU2MzczYWM5MDkyMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2VzdG9uLCBZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84YWI5OWE3MmM3NGI0MzZhYTkzODllZDViMzUxZDA4ZC5zZXRDb250ZW50KGh0bWxfOGVkNWY4Y2FlNjg4NDMwZjkwODU1NjM3M2FjOTA5MjApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfY2I0M2MyMGEwZjFjNDFlZDg2MjZjZDkxYTg0OGM3ODUuYmluZFBvcHVwKHBvcHVwXzhhYjk5YTcyYzc0YjQzNmFhOTM4OWVkNWIzNTFkMDhkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q0Mzk2ZTU3Mjc5ZDRhOGE5MGY0ODA5N2UzZDVhMDYzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjk2MzE5LC03OS41MzIyNDI0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJtYWdlbnRhIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF9hNTNjZWI1ZjlkMGU0ZDU0OTJmOTk5MWI4YzRjZjA5Zik7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wNmY2NDAzOGUwYjI0ZGNkOTAwNzJiNDhjNWQ5NzE2MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hZWJjMzZmMTVmM2Y0NTNkYWE4MmNjYmNiNzgyNDMwMyA9ICQoJzxkaXYgaWQ9Imh0bWxfYWViYzM2ZjE1ZjNmNDUzZGFhODJjY2JjYjc4MjQzMDMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldlc3Rtb3VudCwgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wNmY2NDAzOGUwYjI0ZGNkOTAwNzJiNDhjNWQ5NzE2Mi5zZXRDb250ZW50KGh0bWxfYWViYzM2ZjE1ZjNmNDUzZGFhODJjY2JjYjc4MjQzMDMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDQzOTZlNTcyNzlkNGE4YTkwZjQ4MDk3ZTNkNWEwNjMuYmluZFBvcHVwKHBvcHVwXzA2ZjY0MDM4ZTBiMjRkY2Q5MDA3MmI0OGM1ZDk3MTYyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ4OTBlMWNlY2VkNDRkZTlhMGFjNTY1MzIyZWUxNmRjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg4OTA1NCwtNzkuNTU0NzI0NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzZiYmQ3OTc1NGI4NDA1M2I4ODhkNGRhMmNhZDRjYzggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWY4MGQzZGQ0ZGQ3NGE1YjhiZTVjMTRiMzU0NGQ3OTggPSAkKCc8ZGl2IGlkPSJodG1sX2VmODBkM2RkNGRkNzRhNWI4YmU1YzE0YjM1NDRkNzk4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc3ZpZXcgVmlsbGFnZSxNYXJ0aW4gR3JvdmUgR2FyZGVucyxSaWNodmlldyBHYXJkZW5zLFN0LiBQaGlsbGlwcywgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83NmJiZDc5NzU0Yjg0MDUzYjg4OGQ0ZGEyY2FkNGNjOC5zZXRDb250ZW50KGh0bWxfZWY4MGQzZGQ0ZGQ3NGE1YjhiZTVjMTRiMzU0NGQ3OTgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDg5MGUxY2VjZWQ0NGRlOWEwYWM1NjUzMjJlZTE2ZGMuYmluZFBvcHVwKHBvcHVwXzc2YmJkNzk3NTRiODQwNTNiODg4ZDRkYTJjYWQ0Y2M4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NjOTQ1OTEwNjEwZjQxMDRhYjM4ZDA5MDFkZjMyZTAyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzM5NDE2Mzk5OTk5OTk2LC03OS41ODg0MzY5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIm1hZ2VudGEiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwX2E1M2NlYjVmOWQwZTRkNTQ5MmY5OTkxYjhjNGNmMDlmKTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2ZjY2U3ZDQ0ZTAwMDQ0ZjlhZWU2ZGJhNjllODYxZGU0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzkwODU2ZGI4MjQwNDQ1YzZiY2IyZjU5NDVmNTk1NWU2ID0gJCgnPGRpdiBpZD0iaHRtbF85MDg1NmRiODI0MDQ0NWM2YmNiMmY1OTQ1ZjU5NTVlNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWxiaW9uIEdhcmRlbnMsQmVhdW1vbmQgSGVpZ2h0cyxIdW1iZXJnYXRlLEphbWVzdG93bixNb3VudCBPbGl2ZSxTaWx2ZXJzdG9uZSxTb3V0aCBTdGVlbGVzLFRoaXN0bGV0b3duLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZjY2U3ZDQ0ZTAwMDQ0ZjlhZWU2ZGJhNjllODYxZGU0LnNldENvbnRlbnQoaHRtbF85MDg1NmRiODI0MDQ0NWM2YmNiMmY1OTQ1ZjU5NTVlNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jYzk0NTkxMDYxMGY0MTA0YWIzOGQwOTAxZGYzMmUwMi5iaW5kUG9wdXAocG9wdXBfZmNjZTdkNDRlMDAwNDRmOWFlZTZkYmE2OWU4NjFkZTQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2I5ZjM5YzM4YjEwNGYyNThiNDIxZGEwMTU0MjUyZWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MDY3NDgyOTk5OTk5OTQsLTc5LjU5NDA1NDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAibWFnZW50YSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfYTUzY2ViNWY5ZDBlNGQ1NDkyZjk5OTFiOGM0Y2YwOWYpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTgxMGM4MTk1YTc2NGM1YmE1Y2UxMjQxNGU5MWRhMzggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTZkMTUyZTM0Y2VjNDNlZDg3ZGJhZDM5NmJmZjE3YzEgPSAkKCc8ZGl2IGlkPSJodG1sXzU2ZDE1MmUzNGNlYzQzZWQ4N2RiYWQzOTZiZmYxN2MxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aHdlc3QsIEV0b2JpY29rZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTgxMGM4MTk1YTc2NGM1YmE1Y2UxMjQxNGU5MWRhMzguc2V0Q29udGVudChodG1sXzU2ZDE1MmUzNGNlYzQzZWQ4N2RiYWQzOTZiZmYxN2MxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NiOWYzOWMzOGIxMDRmMjU4YjQyMWRhMDE1NDI1MmViLmJpbmRQb3B1cChwb3B1cF9hODEwYzgxOTVhNzY0YzViYTVjZTEyNDE0ZTkxZGEzOCk7CgogICAgICAgICAgICAKICAgICAgICAKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



# Using Foursquare API to explore the neighborhoods


```python
# @hidden_cell
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




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0IiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCcsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDMuNjUzOTYzLC03OS4zODcyMDddLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTEsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyX2UyMGNhMzJkYmUzZDQ2ZmJiMDU3YjQ4YWEwYzQyYWUxID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICJtYXhab29tIjogMTgsCiAgIm1pblpvb20iOiAxLAogICJub1dyYXAiOiBmYWxzZSwKICAic3ViZG9tYWlucyI6ICJhYmMiCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iMTczNTFiMDMyYjI0ZWZlOTEzMjQ3NDAwYTFkZjA1ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjgwNjY4NjI5OTk5OTk5NiwtNzkuMTk0MzUzNDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDNlNTI2MmVkM2U4NGMzZGFkMDRjYjI0ZWMwYjk2NTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYzUzZTkwZjBhNTE3NGIxNTg2MjBhMDkxZGNjMDA0ZjMgPSAkKCc8ZGl2IGlkPSJodG1sX2M1M2U5MGYwYTUxNzRiMTU4NjIwYTA5MWRjYzAwNGYzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3VnZSxNYWx2ZXJuIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDNlNTI2MmVkM2U4NGMzZGFkMDRjYjI0ZWMwYjk2NTguc2V0Q29udGVudChodG1sX2M1M2U5MGYwYTUxNzRiMTU4NjIwYTA5MWRjYzAwNGYzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2IxNzM1MWIwMzJiMjRlZmU5MTMyNDc0MDBhMWRmMDVkLmJpbmRQb3B1cChwb3B1cF80M2U1MjYyZWQzZTg0YzNkYWQwNGNiMjRlYzBiOTY1OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82ZDE4YmE2NGE5ZDc0OWIxYWE3ODBjYWIzNGVjMjUwZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4NDUzNTEsLTc5LjE2MDQ5NzA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzEwYWYyOGJlYzNkZDRhZGE4NTM0M2ExMWE3YzEyOWIwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2M5NDQ2OTkwNjlhMjQyODlhYjM1YzQ1ODRiYmU2ZDI2ID0gJCgnPGRpdiBpZD0iaHRtbF9jOTQ0Njk5MDY5YTI0Mjg5YWIzNWM0NTg0YmJlNmQyNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaGxhbmQgQ3JlZWssUm91Z2UgSGlsbCxQb3J0IFVuaW9uIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTBhZjI4YmVjM2RkNGFkYTg1MzQzYTExYTdjMTI5YjAuc2V0Q29udGVudChodG1sX2M5NDQ2OTkwNjlhMjQyODlhYjM1YzQ1ODRiYmU2ZDI2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZkMThiYTY0YTlkNzQ5YjFhYTc4MGNhYjM0ZWMyNTBkLmJpbmRQb3B1cChwb3B1cF8xMGFmMjhiZWMzZGQ0YWRhODUzNDNhMTFhN2MxMjliMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jMmYwYTI0YmE2OTE0ZTcxYWYxOTc2M2YxMmFiMWZhOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc2MzU3MjYsLTc5LjE4ODcxMTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfN2FmYzI3NDk1YTkwNDI3MGE5OWY1NjQyYmM0NzM5ZWUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGI5MzhmZWVlNWJjNDY4YzkzMTI3MWYyM2FmZmVkOWQgPSAkKCc8ZGl2IGlkPSJodG1sXzhiOTM4ZmVlZTViYzQ2OGM5MzEyNzFmMjNhZmZlZDlkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HdWlsZHdvb2QsTW9ybmluZ3NpZGUsV2VzdCBIaWxsIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfN2FmYzI3NDk1YTkwNDI3MGE5OWY1NjQyYmM0NzM5ZWUuc2V0Q29udGVudChodG1sXzhiOTM4ZmVlZTViYzQ2OGM5MzEyNzFmMjNhZmZlZDlkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2MyZjBhMjRiYTY5MTRlNzFhZjE5NzYzZjEyYWIxZmE4LmJpbmRQb3B1cChwb3B1cF83YWZjMjc0OTVhOTA0MjcwYTk5ZjU2NDJiYzQ3MzllZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83OGRhZTc3ZGZiNzM0NzAyODY2ODg2MDE3ODU4MTg1YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MDk5MjEsLTc5LjIxNjkxNzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzM5ZTYxZTE3MGVmYzQwOTA4NmQ2ZmZiYzdmZWQ4OGM5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZmMmE0OWJkMTA3MzQ5Y2M5NmZjZjk1MzY2ZjgyMTdhID0gJCgnPGRpdiBpZD0iaHRtbF9mZjJhNDliZDEwNzM0OWNjOTZmY2Y5NTM2NmY4MjE3YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V29idXJuIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzllNjFlMTcwZWZjNDA5MDg2ZDZmZmJjN2ZlZDg4Yzkuc2V0Q29udGVudChodG1sX2ZmMmE0OWJkMTA3MzQ5Y2M5NmZjZjk1MzY2ZjgyMTdhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc4ZGFlNzdkZmI3MzQ3MDI4NjY4ODYwMTc4NTgxODVhLmJpbmRQb3B1cChwb3B1cF8zOWU2MWUxNzBlZmM0MDkwODZkNmZmYmM3ZmVkODhjOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MzE4ZGYwM2ZhNjA0NzFlYTY2Yzc2ODAzZmE5Y2ZlMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MzEzNiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfM2FiNWFhNjQyMzdjNDQ1NGEwOTA0MWQwZjY4NGY5MjAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2UyODNjZTU5MTNhNDFjNWE2MDg3MTUzZmE5MWE2ODEgPSAkKCc8ZGl2IGlkPSJodG1sX2NlMjgzY2U1OTEzYTQxYzVhNjA4NzE1M2ZhOTFhNjgxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZWRhcmJyYWUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zYWI1YWE2NDIzN2M0NDU0YTA5MDQxZDBmNjg0ZjkyMC5zZXRDb250ZW50KGh0bWxfY2UyODNjZTU5MTNhNDFjNWE2MDg3MTUzZmE5MWE2ODEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDMxOGRmMDNmYTYwNDcxZWE2NmM3NjgwM2ZhOWNmZTIuYmluZFBvcHVwKHBvcHVwXzNhYjVhYTY0MjM3YzQ0NTRhMDkwNDFkMGY2ODRmOTIwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y5ZTZiMjA3NmIzNDQ2NGY5NTNlMWFkNzQzODgzNjZiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ0NzM0MiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDIxNmVmZDNmOTM2NDg3OGEwZjQ5NGNhMWMzMDMzZmMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTJiYTY4MzY5YWU1NDE0OWE4Njk0N2I3MDFiMTJjNDEgPSAkKCc8ZGl2IGlkPSJodG1sX2UyYmE2ODM2OWFlNTQxNDlhODY5NDdiNzAxYjEyYzQxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TY2FyYm9yb3VnaCBWaWxsYWdlIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDIxNmVmZDNmOTM2NDg3OGEwZjQ5NGNhMWMzMDMzZmMuc2V0Q29udGVudChodG1sX2UyYmE2ODM2OWFlNTQxNDlhODY5NDdiNzAxYjEyYzQxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y5ZTZiMjA3NmIzNDQ2NGY5NTNlMWFkNzQzODgzNjZiLmJpbmRQb3B1cChwb3B1cF9kMjE2ZWZkM2Y5MzY0ODc4YTBmNDk0Y2ExYzMwMzNmYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83MDE0MGU4ZDkzNTA0YjgwYmVmNjQyYTM2N2IwZmVmNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNzkyOTIsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2E2MGZkOTA5Njc2YTQ1Yzk4ZDAyYmYyNmE4NjI2NjE1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU3NDEyODllMzIyZTRiOTI5OWZlZjRjOTA3NjEyMWRiID0gJCgnPGRpdiBpZD0iaHRtbF81NzQxMjg5ZTMyMmU0YjkyOTlmZWY0YzkwNzYxMjFkYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdCBCaXJjaG1vdW50IFBhcmssSW9udmlldyxLZW5uZWR5IFBhcmsgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hNjBmZDkwOTY3NmE0NWM5OGQwMmJmMjZhODYyNjYxNS5zZXRDb250ZW50KGh0bWxfNTc0MTI4OWUzMjJlNGI5Mjk5ZmVmNGM5MDc2MTIxZGIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzAxNDBlOGQ5MzUwNGI4MGJlZjY0MmEzNjdiMGZlZjUuYmluZFBvcHVwKHBvcHVwX2E2MGZkOTA5Njc2YTQ1Yzk4ZDAyYmYyNmE4NjI2NjE1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzllN2I5N2FhOTFhNzRjYzFhZWE4YjE1NzU5OTYxNDIxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzExMTExNzAwMDAwMDA0LC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzEyMTg1OGQ3OTAxODQ0ZWJiYzFlYWVkM2Q5ODZhYTkxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNhNjhiOGNmMDBmYzRlNDQ4NGEwNWQ0MGQyNGIyMTIyID0gJCgnPGRpdiBpZD0iaHRtbF8zYTY4YjhjZjAwZmM0ZTQ0ODRhMDVkNDBkMjRiMjEyMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2xhaXJsZWEsR29sZGVuIE1pbGUsT2FrcmlkZ2UgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xMjE4NThkNzkwMTg0NGViYmMxZWFlZDNkOTg2YWE5MS5zZXRDb250ZW50KGh0bWxfM2E2OGI4Y2YwMGZjNGU0NDg0YTA1ZDQwZDI0YjIxMjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWU3Yjk3YWE5MWE3NGNjMWFlYThiMTU3NTk5NjE0MjEuYmluZFBvcHVwKHBvcHVwXzEyMTg1OGQ3OTAxODQ0ZWJiYzFlYWVkM2Q5ODZhYTkxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzA0YjZlYTI0OGQ1ZTQ5ZjI4NjYxZWE1ZWY3MjYxYTU1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE2MzE2LC03OS4yMzk0NzYwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wMWJkNmEyOGUyZDY0ZWRmYWVlZTdjY2VmYWVjYzFjYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hNWU5OTNjYjA4NmU0YTc3OTUwOTM0NDcyNzgzYTA3NSA9ICQoJzxkaXYgaWQ9Imh0bWxfYTVlOTkzY2IwODZlNGE3Nzk1MDkzNDQ3Mjc4M2EwNzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsaWZmY3Jlc3QsQ2xpZmZzaWRlLFNjYXJib3JvdWdoIFZpbGxhZ2UgV2VzdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzAxYmQ2YTI4ZTJkNjRlZGZhZWVlN2NjZWZhZWNjMWNiLnNldENvbnRlbnQoaHRtbF9hNWU5OTNjYjA4NmU0YTc3OTUwOTM0NDcyNzgzYTA3NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wNGI2ZWEyNDhkNWU0OWYyODY2MWVhNWVmNzI2MWE1NS5iaW5kUG9wdXAocG9wdXBfMDFiZDZhMjhlMmQ2NGVkZmFlZWU3Y2NlZmFlY2MxY2IpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMGJhNmRjZDE5YjdmNGNkNmFjNzg4Njk4ZTNhMzEwZDEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTI2NTcwMDAwMDAwMDQsLTc5LjI2NDg0ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNmVlZDI3YzVmOGQyNDEzNDkxYWE4NmU5Y2YzMmE3MWQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTg1ZGZlM2ExYjlhNDM5Nzg2NWNmYWI2Yjc3ZGFiNjAgPSAkKCc8ZGl2IGlkPSJodG1sX2U4NWRmZTNhMWI5YTQzOTc4NjVjZmFiNmI3N2RhYjYwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CaXJjaCBDbGlmZixDbGlmZnNpZGUgV2VzdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZlZWQyN2M1ZjhkMjQxMzQ5MWFhODZlOWNmMzJhNzFkLnNldENvbnRlbnQoaHRtbF9lODVkZmUzYTFiOWE0Mzk3ODY1Y2ZhYjZiNzdkYWI2MCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wYmE2ZGNkMTliN2Y0Y2Q2YWM3ODg2OThlM2EzMTBkMS5iaW5kUG9wdXAocG9wdXBfNmVlZDI3YzVmOGQyNDEzNDkxYWE4NmU5Y2YzMmE3MWQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGE5MWZmNWU4YTcyNGJmZWE4MDRhZWVjMTQyNjY0OTAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTc0MDk2LC03OS4yNzMzMDQwMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83NDlhMTlmYmViOGQ0ZDMxYjA2OTIwNzdmNjYyNWM4OCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85MmFhN2E5MDY2ZjU0MmQ4ODU5NWQ0MThmZWM4MWVjZSA9ICQoJzxkaXYgaWQ9Imh0bWxfOTJhYTdhOTA2NmY1NDJkODg1OTVkNDE4ZmVjODFlY2UiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvcnNldCBQYXJrLFNjYXJib3JvdWdoIFRvd24gQ2VudHJlLFdleGZvcmQgSGVpZ2h0cyBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc0OWExOWZiZWI4ZDRkMzFiMDY5MjA3N2Y2NjI1Yzg4LnNldENvbnRlbnQoaHRtbF85MmFhN2E5MDY2ZjU0MmQ4ODU5NWQ0MThmZWM4MWVjZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80YTkxZmY1ZThhNzI0YmZlYTgwNGFlZWMxNDI2NjQ5MC5iaW5kUG9wdXAocG9wdXBfNzQ5YTE5ZmJlYjhkNGQzMWIwNjkyMDc3ZjY2MjVjODgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDIxZDY2NTY4YzQ1NGI5YWFkNTIzN2RiMTY5M2FmY2MgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTAwNzE1MDAwMDAwMDQsLTc5LjI5NTg0OTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODVmM2NhNmMyY2NlNGZlYjkxNDc1NTZjNGRkMzg1ZWUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2FlYWQ3YjFkMDMzNGI5NmFhMTQ3ZjQyMDBlN2QwZmQgPSAkKCc8ZGl2IGlkPSJodG1sXzdhZWFkN2IxZDAzMzRiOTZhYTE0N2Y0MjAwZTdkMGZkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJ5dmFsZSxXZXhmb3JkIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODVmM2NhNmMyY2NlNGZlYjkxNDc1NTZjNGRkMzg1ZWUuc2V0Q29udGVudChodG1sXzdhZWFkN2IxZDAzMzRiOTZhYTE0N2Y0MjAwZTdkMGZkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQyMWQ2NjU2OGM0NTRiOWFhZDUyMzdkYjE2OTNhZmNjLmJpbmRQb3B1cChwb3B1cF84NWYzY2E2YzJjY2U0ZmViOTE0NzU1NmM0ZGQzODVlZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xMjAxYjViMjMzYjU0Njc1ODlhMTAxMTA5NzRjMGUwYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5NDIwMDMsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2MxNTY2ODIxMjM5ZjRkYzhhZDNhMzJmOGU5MjExNzIxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2U5Y2UxZTk4ZTkxYjQ3ZjRhNTJkNDdiZjQ5NTQ5Y2ZmID0gJCgnPGRpdiBpZD0iaHRtbF9lOWNlMWU5OGU5MWI0N2Y0YTUyZDQ3YmY0OTU0OWNmZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzE1NjY4MjEyMzlmNGRjOGFkM2EzMmY4ZTkyMTE3MjEuc2V0Q29udGVudChodG1sX2U5Y2UxZTk4ZTkxYjQ3ZjRhNTJkNDdiZjQ5NTQ5Y2ZmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzEyMDFiNWIyMzNiNTQ2NzU4OWExMDExMDk3NGMwZTBhLmJpbmRQb3B1cChwb3B1cF9jMTU2NjgyMTIzOWY0ZGM4YWQzYTMyZjhlOTIxMTcyMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80NmM5YTEwMGYzNTY0NTQ3OGM2OGEwMmU0OTZiZTIxNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4MTYzNzUsLTc5LjMwNDMwMjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODQzNTQwMTBlYjM0NDc2MWIwMmJlNDBhYTFlMGYzN2IgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTIwYmNiMTU5NTJlNDg5Njk1ZDYyOTEwNWZmNjNhYTQgPSAkKCc8ZGl2IGlkPSJodG1sX2UyMGJjYjE1OTUyZTQ4OTY5NWQ2MjkxMDVmZjYzYWE0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGFya3MgQ29ybmVycyxTdWxsaXZhbixUYW0gTyYjMzk7U2hhbnRlciBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg0MzU0MDEwZWIzNDQ3NjFiMDJiZTQwYWExZTBmMzdiLnNldENvbnRlbnQoaHRtbF9lMjBiY2IxNTk1MmU0ODk2OTVkNjI5MTA1ZmY2M2FhNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80NmM5YTEwMGYzNTY0NTQ3OGM2OGEwMmU0OTZiZTIxNy5iaW5kUG9wdXAocG9wdXBfODQzNTQwMTBlYjM0NDc2MWIwMmJlNDBhYTFlMGYzN2IpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzZmYzY1MzZhN2NkNDdkYWFkNTVkYmYyMzQxZTIzMGEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My44MTUyNTIyLC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzYxYTA2MDViNzQyNjRlMTlhN2VmNmQwY2Y4NzZjOWFmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2MxMDU3OGExYzMwNDQxMGY5NWYzOTlmYTYyZjFiY2IwID0gJCgnPGRpdiBpZD0iaHRtbF9jMTA1NzhhMWMzMDQ0MTBmOTVmMzk5ZmE2MmYxYmNiMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0IE5vcnRoLEwmIzM5O0Ftb3JlYXV4IEVhc3QsTWlsbGlrZW4sU3RlZWxlcyBFYXN0IENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjFhMDYwNWI3NDI2NGUxOWE3ZWY2ZDBjZjg3NmM5YWYuc2V0Q29udGVudChodG1sX2MxMDU3OGExYzMwNDQxMGY5NWYzOTlmYTYyZjFiY2IwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M2ZmM2NTM2YTdjZDQ3ZGFhZDU1ZGJmMjM0MWUyMzBhLmJpbmRQb3B1cChwb3B1cF82MWEwNjA1Yjc0MjY0ZTE5YTdlZjZkMGNmODc2YzlhZik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNGIyYzVhOTNlMGU0NjJjOTYwYzQ1MjE3YmExOWJlMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5OTUyNTIwMDAwMDAwNSwtNzkuMzE4Mzg4N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83YzJjZjk2NTJmYmQ0YzNjYWU4YzhkMTE4Y2I0ZmUyMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82Y2Q3MGY5OTI3ZWQ0YzM4ODQwNWFhM2M4NTYwZWE5ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfNmNkNzBmOTkyN2VkNGMzODg0MDVhYTNjODU2MGVhOWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkwmIzM5O0Ftb3JlYXV4IFdlc3QgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83YzJjZjk2NTJmYmQ0YzNjYWU4YzhkMTE4Y2I0ZmUyMS5zZXRDb250ZW50KGh0bWxfNmNkNzBmOTkyN2VkNGMzODg0MDVhYTNjODU2MGVhOWYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDRiMmM1YTkzZTBlNDYyYzk2MGM0NTIxN2JhMTliZTAuYmluZFBvcHVwKHBvcHVwXzdjMmNmOTY1MmZiZDRjM2NhZThjOGQxMThjYjRmZTIxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBkOGEzNTBiYzhkNDQ4NzhiZDVmNzFjZjEyNTkxMTNkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuODAzNzYyMiwtNzkuMzYzNDUxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hZjY0ZDU1NTdhYTQ0MTMyYTYwYTE0MThkYzM1Y2RlNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iNjBjMzFmMTc5YTk0ZTQyYTdmZWYzM2MxNDliN2EzYiA9ICQoJzxkaXYgaWQ9Imh0bWxfYjYwYzMxZjE3OWE5NGU0MmE3ZmVmMzNjMTQ5YjdhM2IiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhpbGxjcmVzdCBWaWxsYWdlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWY2NGQ1NTU3YWE0NDEzMmE2MGExNDE4ZGMzNWNkZTYuc2V0Q29udGVudChodG1sX2I2MGMzMWYxNzlhOTRlNDJhN2ZlZjMzYzE0OWI3YTNiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBkOGEzNTBiYzhkNDQ4NzhiZDVmNzFjZjEyNTkxMTNkLmJpbmRQb3B1cChwb3B1cF9hZjY0ZDU1NTdhYTQ0MTMyYTYwYTE0MThkYzM1Y2RlNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mODc3NjI1MTJlZjM0YzJlYWM5MTZjNzY5YTMxYmViMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3ODUxNzUsLTc5LjM0NjU1NTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNmE1YmU2ZDAzYWE4NDcwMzlmYzAzYjk2YzEyNzc5OGUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYmI0ZGZlZGQyZjYzNDgyOWIzYTUxMjdmNzU3MzRjNTMgPSAkKCc8ZGl2IGlkPSJodG1sX2JiNGRmZWRkMmY2MzQ4MjliM2E1MTI3Zjc1NzM0YzUzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GYWlydmlldyxIZW5yeSBGYXJtLE9yaW9sZSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZhNWJlNmQwM2FhODQ3MDM5ZmMwM2I5NmMxMjc3OThlLnNldENvbnRlbnQoaHRtbF9iYjRkZmVkZDJmNjM0ODI5YjNhNTEyN2Y3NTczNGM1Myk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mODc3NjI1MTJlZjM0YzJlYWM5MTZjNzY5YTMxYmViMC5iaW5kUG9wdXAocG9wdXBfNmE1YmU2ZDAzYWE4NDcwMzlmYzAzYjk2YzEyNzc5OGUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTNkMzcxM2E4ODU4NDg4YzljZTcyZWRmNDdjZjkyNjggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43ODY5NDczLC03OS4zODU5NzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTY2NzlhMTI4ZDNiNDVhMDlhYzIyYzA4MGRhMjg3YmQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTQxNzgzZDgyNGE0NDBhMThjOGI3ZDBiMzFiYjhhNDUgPSAkKCc8ZGl2IGlkPSJodG1sX2E0MTc4M2Q4MjRhNDQwYTE4YzhiN2QwYjMxYmI4YTQ1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXl2aWV3IFZpbGxhZ2UgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hNjY3OWExMjhkM2I0NWEwOWFjMjJjMDgwZGEyODdiZC5zZXRDb250ZW50KGh0bWxfYTQxNzgzZDgyNGE0NDBhMThjOGI3ZDBiMzFiYjhhNDUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTNkMzcxM2E4ODU4NDg4YzljZTcyZWRmNDdjZjkyNjguYmluZFBvcHVwKHBvcHVwX2E2Njc5YTEyOGQzYjQ1YTA5YWMyMmMwODBkYTI4N2JkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFiNDYxNjJkOTM4ZTQ5Mjk4M2ZkNWIyMWZjMmFlY2I3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzg5MDUzLC03OS40MDg0OTI3OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84ZWFmYzE3ZWY4Y2Y0OTNlODVmZjM5NjcxZjY5OTJmNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lNTQ2OTVkMGQwNzA0YzJkYjlmMmNkMDNmNWNiNDY0YiA9ICQoJzxkaXYgaWQ9Imh0bWxfZTU0Njk1ZDBkMDcwNGMyZGI5ZjJjZDAzZjVjYjQ2NGIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5ld3RvbmJyb29rLFdpbGxvd2RhbGUgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84ZWFmYzE3ZWY4Y2Y0OTNlODVmZjM5NjcxZjY5OTJmNi5zZXRDb250ZW50KGh0bWxfZTU0Njk1ZDBkMDcwNGMyZGI5ZjJjZDAzZjVjYjQ2NGIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMWI0NjE2MmQ5MzhlNDkyOTgzZmQ1YjIxZmMyYWVjYjcuYmluZFBvcHVwKHBvcHVwXzhlYWZjMTdlZjhjZjQ5M2U4NWZmMzk2NzFmNjk5MmY2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZlMTI5MDBmMjIyOTQxMDc4NjU0YmI4MWEyZjZlMDAxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzcwMTE5OSwtNzkuNDA4NDkyNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjc5MGFkNDIwZWYzNGEyMzg0MGQ4MTQxNzgxZmRjZTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTE0MWFiMjBlMzVkNGVmNWI1YzkxMzdkMjEwYWRiN2IgPSAkKCc8ZGl2IGlkPSJodG1sX2UxNDFhYjIwZTM1ZDRlZjViNWM5MTM3ZDIxMGFkYjdiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XaWxsb3dkYWxlIFNvdXRoIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjc5MGFkNDIwZWYzNGEyMzg0MGQ4MTQxNzgxZmRjZTcuc2V0Q29udGVudChodG1sX2UxNDFhYjIwZTM1ZDRlZjViNWM5MTM3ZDIxMGFkYjdiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZlMTI5MDBmMjIyOTQxMDc4NjU0YmI4MWEyZjZlMDAxLmJpbmRQb3B1cChwb3B1cF9mNzkwYWQ0MjBlZjM0YTIzODQwZDgxNDE3ODFmZGNlNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jZmQ2YjhkZDJhZTg0MTJlYWUzMzI0ZjZiNzJkNjE1ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1Mjc1ODI5OTk5OTk5NiwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85MzM3OWVkNWY0M2M0YWMzOGY5MTU3Nzk5NTNlZGMyNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83MGE4YzBlYWFkYzA0ZjBiYmJiMTU2MGFjM2NiYTRlNiA9ICQoJzxkaXYgaWQ9Imh0bWxfNzBhOGMwZWFhZGMwNGYwYmJiYjE1NjBhYzNjYmE0ZTYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPllvcmsgTWlsbHMgV2VzdCBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzkzMzc5ZWQ1ZjQzYzRhYzM4ZjkxNTc3OTk1M2VkYzI1LnNldENvbnRlbnQoaHRtbF83MGE4YzBlYWFkYzA0ZjBiYmJiMTU2MGFjM2NiYTRlNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jZmQ2YjhkZDJhZTg0MTJlYWUzMzI0ZjZiNzJkNjE1ZS5iaW5kUG9wdXAocG9wdXBfOTMzNzllZDVmNDNjNGFjMzhmOTE1Nzc5OTUzZWRjMjUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDc3Yjg5Y2I5MmYyNDE0NzhhNWU3NDgzODZhOWIzMzggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43ODI3MzY0LC03OS40NDIyNTkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk4ZGFhMDg3MDM1NTQ1MDU5MzI4YTg1MjhlOThmYjNiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRhOWY4MDExMWUxYTQyNmU4MWY2M2FjZTEwNjQzOGFmID0gJCgnPGRpdiBpZD0iaHRtbF80YTlmODAxMTFlMWE0MjZlODFmNjNhY2UxMDY0MzhhZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2lsbG93ZGFsZSBXZXN0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOThkYWEwODcwMzU1NDUwNTkzMjhhODUyOGU5OGZiM2Iuc2V0Q29udGVudChodG1sXzRhOWY4MDExMWUxYTQyNmU4MWY2M2FjZTEwNjQzOGFmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q3N2I4OWNiOTJmMjQxNDc4YTVlNzQ4Mzg2YTliMzM4LmJpbmRQb3B1cChwb3B1cF85OGRhYTA4NzAzNTU0NTA1OTMyOGE4NTI4ZTk4ZmIzYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85ODYzYmEwZTNhYjg0Y2MyODg3ZGUyY2JmZGUxZjI4NyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1MzI1ODYsLTc5LjMyOTY1NjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzhmZTg3YjAwMjcwNDE3ZWFiOTAyNjA2NmM1NGM3MGMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMmFhZTRmNDY4YTIzNDMzMmI4YThjNjA2NjU4NTVlMmIgPSAkKCc8ZGl2IGlkPSJodG1sXzJhYWU0ZjQ2OGEyMzQzMzJiOGE4YzYwNjY1ODU1ZTJiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrd29vZHMgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jOGZlODdiMDAyNzA0MTdlYWI5MDI2MDY2YzU0YzcwYy5zZXRDb250ZW50KGh0bWxfMmFhZTRmNDY4YTIzNDMzMmI4YThjNjA2NjU4NTVlMmIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTg2M2JhMGUzYWI4NGNjMjg4N2RlMmNiZmRlMWYyODcuYmluZFBvcHVwKHBvcHVwX2M4ZmU4N2IwMDI3MDQxN2VhYjkwMjYwNjZjNTRjNzBjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdjOWE1MTUxZmE2YjQ3ZjM5ZTVhYWEyMTY2YTNjNzUyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ1OTA1Nzk5OTk5OTk2LC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDIwYzFhNzE3ZDU0NGJhNGIyMzliMGE1MDQ4Nzg4MTMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYzYwZjMwZTEwZDZkNDgwMTgwZGQxMjJiMDdmNjZmNGMgPSAkKCc8ZGl2IGlkPSJodG1sX2M2MGYzMGUxMGQ2ZDQ4MDE4MGRkMTIyYjA3ZjY2ZjRjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb24gTWlsbHMgTm9ydGggQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80MjBjMWE3MTdkNTQ0YmE0YjIzOWIwYTUwNDg3ODgxMy5zZXRDb250ZW50KGh0bWxfYzYwZjMwZTEwZDZkNDgwMTgwZGQxMjJiMDdmNjZmNGMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2M5YTUxNTFmYTZiNDdmMzllNWFhYTIxNjZhM2M3NTIuYmluZFBvcHVwKHBvcHVwXzQyMGMxYTcxN2Q1NDRiYTRiMjM5YjBhNTA0ODc4ODEzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2JjZDllYjlmN2ZmZjRmYzI5NWY0ODI1YzRmZGMwNjY1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI1ODk5NzAwMDAwMDEsLTc5LjM0MDkyM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ZTk2YTYwZjAzM2U0MGFjOGM1NWQ0YjY5MDdjOGM5NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81Yzg0NDE0OGY3MDQ0YTUxYWI4ZGMyZjQ3YWRhODM0ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfNWM4NDQxNDhmNzA0NGE1MWFiOGRjMmY0N2FkYTgzNGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZsZW1pbmdkb24gUGFyayxEb24gTWlsbHMgU291dGggQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83ZTk2YTYwZjAzM2U0MGFjOGM1NWQ0YjY5MDdjOGM5NC5zZXRDb250ZW50KGh0bWxfNWM4NDQxNDhmNzA0NGE1MWFiOGRjMmY0N2FkYTgzNGYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYmNkOWViOWY3ZmZmNGZjMjk1ZjQ4MjVjNGZkYzA2NjUuYmluZFBvcHVwKHBvcHVwXzdlOTZhNjBmMDMzZTQwYWM4YzU1ZDRiNjkwN2M4Yzk0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I0MDE0ODJiNzg4NTRmOTI4MGZjNTMyZDQyZTczN2Y2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzU0MzI4MywtNzkuNDQyMjU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80YzM4M2RhNzI0YWM0NmJlODA2Y2UyMWMxNjIzMjVlZSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wMzI5MDU2YzM5NWE0YWQwOGZhNzUwY2IzYzUzYzEwYiA9ICQoJzxkaXYgaWQ9Imh0bWxfMDMyOTA1NmMzOTVhNGFkMDhmYTc1MGNiM2M1M2MxMGIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJhdGh1cnN0IE1hbm9yLERvd25zdmlldyBOb3J0aCxXaWxzb24gSGVpZ2h0cyBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzRjMzgzZGE3MjRhYzQ2YmU4MDZjZTIxYzE2MjMyNWVlLnNldENvbnRlbnQoaHRtbF8wMzI5MDU2YzM5NWE0YWQwOGZhNzUwY2IzYzUzYzEwYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iNDAxNDgyYjc4ODU0ZjkyODBmYzUzMmQ0MmU3MzdmNi5iaW5kUG9wdXAocG9wdXBfNGMzODNkYTcyNGFjNDZiZTgwNmNlMjFjMTYyMzI1ZWUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2Y3ZGRkOWVhZjQzNGNmOThjMWFkZTU4M2MwYjE1ZGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Njc5ODAzLC03OS40ODcyNjE5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ZTEzZDAxODE2MTY0YWNkYTMyYzNiMjQyYTQ5NTkxNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNjJjYzkwNjY2ZjM0NDc0YjAzYWY1ZmUzMzVmOWQ0ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfMTYyY2M5MDY2NmYzNDQ3NGIwM2FmNWZlMzM1ZjlkNGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vcnRod29vZCBQYXJrLFlvcmsgVW5pdmVyc2l0eSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdlMTNkMDE4MTYxNjRhY2RhMzJjM2IyNDJhNDk1OTE0LnNldENvbnRlbnQoaHRtbF8xNjJjYzkwNjY2ZjM0NDc0YjAzYWY1ZmUzMzVmOWQ0Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83ZjdkZGQ5ZWFmNDM0Y2Y5OGMxYWRlNTgzYzBiMTVkZi5iaW5kUG9wdXAocG9wdXBfN2UxM2QwMTgxNjE2NGFjZGEzMmMzYjI0MmE0OTU5MTQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNWY0MjA1MDY0ZjNlNDBjNWE1NWYwMGU0OWJiYzljM2EgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Mzc0NzMyMDAwMDAwMDQsLTc5LjQ2NDc2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2VkMDZmZjcyNWM3NjQxYjhhMjkxOTZlYjc5NzVjYWRiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzliYWVlMGI4MDYxNzQwMGU5NmNlZGVhNGVhYjIxM2QzID0gJCgnPGRpdiBpZD0iaHRtbF85YmFlZTBiODA2MTc0MDBlOTZjZWRlYTRlYWIyMTNkMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q0ZCIFRvcm9udG8sRG93bnN2aWV3IEVhc3QgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lZDA2ZmY3MjVjNzY0MWI4YTI5MTk2ZWI3OTc1Y2FkYi5zZXRDb250ZW50KGh0bWxfOWJhZWUwYjgwNjE3NDAwZTk2Y2VkZWE0ZWFiMjEzZDMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNWY0MjA1MDY0ZjNlNDBjNWE1NWYwMGU0OWJiYzljM2EuYmluZFBvcHVwKHBvcHVwX2VkMDZmZjcyNWM3NjQxYjhhMjkxOTZlYjc5NzVjYWRiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhiODkzZGI1MjYyMjQxNzE5NjZmMDFlZDliMTE1N2U3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzM5MDE0NiwtNzkuNTA2OTQzNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xNTc1ZDFhZDFmYTA0OWNiYjMxZThiNjI3ZmEwN2I4NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82ZjVmODc5M2VjMDk0YzcwOWJmMDllMGExYmEyOGI3MSA9ICQoJzxkaXYgaWQ9Imh0bWxfNmY1Zjg3OTNlYzA5NGM3MDliZjA5ZTBhMWJhMjhiNzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvd25zdmlldyBXZXN0IENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTU3NWQxYWQxZmEwNDljYmIzMWU4YjYyN2ZhMDdiODQuc2V0Q29udGVudChodG1sXzZmNWY4NzkzZWMwOTRjNzA5YmYwOWUwYTFiYTI4YjcxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhiODkzZGI1MjYyMjQxNzE5NjZmMDFlZDliMTE1N2U3LmJpbmRQb3B1cChwb3B1cF8xNTc1ZDFhZDFmYTA0OWNiYjMxZThiNjI3ZmEwN2I4NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wZGMwMGQ1MzliNDE0NTJkYTAzMjM0MmRkZDhmNTUxZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyODQ5NjQsLTc5LjQ5NTY5NzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MGZmYjQiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODBmZmI0IiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE1NjAxZjhkZDk4OTRkNzBhMTFhMDcyY2E0YWE4ODI1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzg1NjkwMmQ4NDM3MjRjMTE4ODMyZjAxYjIwNWEwNzgzID0gJCgnPGRpdiBpZD0iaHRtbF84NTY5MDJkODQzNzI0YzExODgzMmYwMWIyMDVhMDc4MyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IENlbnRyYWwgQ2x1c3RlciAzPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNTYwMWY4ZGQ5ODk0ZDcwYTExYTA3MmNhNGFhODgyNS5zZXRDb250ZW50KGh0bWxfODU2OTAyZDg0MzcyNGMxMTg4MzJmMDFiMjA1YTA3ODMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMGRjMDBkNTM5YjQxNDUyZGEwMzIzNDJkZGQ4ZjU1MWUuYmluZFBvcHVwKHBvcHVwXzE1NjAxZjhkZDk4OTRkNzBhMTFhMDcyY2E0YWE4ODI1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2YzZDdkZDJkMzU5MzRlZjViMDAyYmNiZWI5MDlmYzhmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzYxNjMxMywtNzkuNTIwOTk5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTFhZmY1NjgxYmQxNDExNjgwMDc2ZWVmMjU5ZThlNzkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTgwYjE3ZWM0ZmFkNDliNjhlZmJmYzdmYWNjOWNhNzcgPSAkKCc8ZGl2IGlkPSJodG1sXzE4MGIxN2VjNGZhZDQ5YjY4ZWZiZmM3ZmFjYzljYTc3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb3duc3ZpZXcgTm9ydGh3ZXN0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTFhZmY1NjgxYmQxNDExNjgwMDc2ZWVmMjU5ZThlNzkuc2V0Q29udGVudChodG1sXzE4MGIxN2VjNGZhZDQ5YjY4ZWZiZmM3ZmFjYzljYTc3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2YzZDdkZDJkMzU5MzRlZjViMDAyYmNiZWI5MDlmYzhmLmJpbmRQb3B1cChwb3B1cF9hMWFmZjU2ODFiZDE0MTE2ODAwNzZlZWYyNTllOGU3OSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNzlkZTE3MjQ5NmU0ZGU5OGNkZTZjYTMyNDU0YWEwMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNTg4MjI5OTk5OTk5NSwtNzkuMzE1NTcxNTk5OTk5OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODgxNGYyM2EzMDZlNDBkOGE1MzJjMzE2MTA1NmZkMzUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDMyYmZmMjVkNTVkNGYxY2ExMDM1MWViYTBjMzgxMWUgPSAkKCc8ZGl2IGlkPSJodG1sXzQzMmJmZjI1ZDU1ZDRmMWNhMTAzNTFlYmEwYzM4MTFlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5WaWN0b3JpYSBWaWxsYWdlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODgxNGYyM2EzMDZlNDBkOGE1MzJjMzE2MTA1NmZkMzUuc2V0Q29udGVudChodG1sXzQzMmJmZjI1ZDU1ZDRmMWNhMTAzNTFlYmEwYzM4MTFlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzE3OWRlMTcyNDk2ZTRkZTk4Y2RlNmNhMzI0NTRhYTAyLmJpbmRQb3B1cChwb3B1cF84ODE0ZjIzYTMwNmU0MGQ4YTUzMmMzMTYxMDU2ZmQzNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNWI0OTc4MTIzNjQ0NzRmYjI5OGU3ZTgzNmYyMmRlNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcwNjM5NzIsLTc5LjMwOTkzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81YjI0MjJhMTMwMTI0M2JmYWM3NDVlMjg4YzliODY5OCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hMzQyYzdmMTZhNzk0Y2RmOGVjNzFlMjE0NzZjZmFkZiA9ICQoJzxkaXYgaWQ9Imh0bWxfYTM0MmM3ZjE2YTc5NGNkZjhlYzcxZTIxNDc2Y2ZhZGYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldvb2RiaW5lIEdhcmRlbnMsUGFya3ZpZXcgSGlsbCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzViMjQyMmExMzAxMjQzYmZhYzc0NWUyODhjOWI4Njk4LnNldENvbnRlbnQoaHRtbF9hMzQyYzdmMTZhNzk0Y2RmOGVjNzFlMjE0NzZjZmFkZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kNWI0OTc4MTIzNjQ0NzRmYjI5OGU3ZTgzNmYyMmRlNi5iaW5kUG9wdXAocG9wdXBfNWIyNDIyYTEzMDEyNDNiZmFjNzQ1ZTI4OGM5Yjg2OTgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmRmNmRlMDFjMmFlNGJlZjk1NzNmNmZmMzZiZWUyZTQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTUzNDM5MDAwMDAwMDUsLTc5LjMxODM4ODddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODIzNjY1MjM5MTQ2NDliZmFhODE1NDYyYzg2MDAxZTEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjhhNGQzMTQ1ZTFlNDZmYWI0ZGVlMTQ5OTg1MTExZWEgPSAkKCc8ZGl2IGlkPSJodG1sX2Y4YTRkMzE0NWUxZTQ2ZmFiNGRlZTE0OTk4NTExMWVhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Xb29kYmluZSBIZWlnaHRzIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODIzNjY1MjM5MTQ2NDliZmFhODE1NDYyYzg2MDAxZTEuc2V0Q29udGVudChodG1sX2Y4YTRkMzE0NWUxZTQ2ZmFiNGRlZTE0OTk4NTExMWVhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZkZjZkZTAxYzJhZTRiZWY5NTczZjZmZjM2YmVlMmU0LmJpbmRQb3B1cChwb3B1cF84MjM2NjUyMzkxNDY0OWJmYWE4MTU0NjJjODYwMDFlMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mM2UzOGFmMWEyMTU0ZWZiODZjYjRlYzNiZTk5ZGMwZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY3NjM1NzM5OTk5OTk5LC03OS4yOTMwMzEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE0OTk4MmU0YjFlNDRlOThhNmM0NDQ0NDI5ZjlmMTA0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRlOTJhNDdiZTVjZjRiMzI4YmE0OWRiOGM5ZGRjMTEwID0gJCgnPGRpdiBpZD0iaHRtbF80ZTkyYTQ3YmU1Y2Y0YjMyOGJhNDlkYjhjOWRkYzExMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhlIEJlYWNoZXMgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNDk5ODJlNGIxZTQ0ZTk4YTZjNDQ0NDQyOWY5ZjEwNC5zZXRDb250ZW50KGh0bWxfNGU5MmE0N2JlNWNmNGIzMjhiYTQ5ZGI4YzlkZGMxMTApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjNlMzhhZjFhMjE1NGVmYjg2Y2I0ZWMzYmU5OWRjMGUuYmluZFBvcHVwKHBvcHVwXzE0OTk4MmU0YjFlNDRlOThhNmM0NDQ0NDI5ZjlmMTA0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IxOWU4NmExNWYzMzQ5MGU4MmQzNTg1ODc1YjI1Yjk1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA5MDYwNCwtNzkuMzYzNDUxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hNjAxMzg3NjlkMjk0MWM1OWZhMTdmYmM2ZmFmOTU2MSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85YzdhMDI4MDUxYWM0MGVlOWY1OGI5MmNlYjIxODAxZiA9ICQoJzxkaXYgaWQ9Imh0bWxfOWM3YTAyODA1MWFjNDBlZTlmNThiOTJjZWIyMTgwMWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxlYXNpZGUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hNjAxMzg3NjlkMjk0MWM1OWZhMTdmYmM2ZmFmOTU2MS5zZXRDb250ZW50KGh0bWxfOWM3YTAyODA1MWFjNDBlZTlmNThiOTJjZWIyMTgwMWYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjE5ZTg2YTE1ZjMzNDkwZTgyZDM1ODU4NzViMjViOTUuYmluZFBvcHVwKHBvcHVwX2E2MDEzODc2OWQyOTQxYzU5ZmExN2ZiYzZmYWY5NTYxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E4N2NkOTI4MjdkNjQ2ZjU4Y2MzN2ExOGNkY2I5MmQ3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA1MzY4OSwtNzkuMzQ5MzcxOTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNGM0NmZjMWM4MGQ3NGU2MGE4NzU5NjJlN2M0ZjdiYWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzgzNmM2OWNiY2VhNDIzOGExMGJkYjUyZTg5MDk2ZTEgPSAkKCc8ZGl2IGlkPSJodG1sXzc4MzZjNjljYmNlYTQyMzhhMTBiZGI1MmU4OTA5NmUxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaG9ybmNsaWZmZSBQYXJrIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNGM0NmZjMWM4MGQ3NGU2MGE4NzU5NjJlN2M0ZjdiYWEuc2V0Q29udGVudChodG1sXzc4MzZjNjljYmNlYTQyMzhhMTBiZGI1MmU4OTA5NmUxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2E4N2NkOTI4MjdkNjQ2ZjU4Y2MzN2ExOGNkY2I5MmQ3LmJpbmRQb3B1cChwb3B1cF80YzQ2ZmMxYzgwZDc0ZTYwYTg3NTk2MmU3YzRmN2JhYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jMjA0MGZiYmViN2U0OTA1YmNmOWU2ZTU5N2JjMjczNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY4NTM0NywtNzkuMzM4MTA2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82NzZiOGFkMDYxMzQ0M2E2YjQ5ZDVhZjRiNWZlZGMwMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kOWVhN2E3NDFhYjE0Mzk5OWVkNDljNWExYTJkNmQyMyA9ICQoJzxkaXYgaWQ9Imh0bWxfZDllYTdhNzQxYWIxNDM5OTllZDQ5YzVhMWEyZDZkMjMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgVG9yb250byBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzY3NmI4YWQwNjEzNDQzYTZiNDlkNWFmNGI1ZmVkYzAzLnNldENvbnRlbnQoaHRtbF9kOWVhN2E3NDFhYjE0Mzk5OWVkNDljNWExYTJkNmQyMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jMjA0MGZiYmViN2U0OTA1YmNmOWU2ZTU5N2JjMjczNi5iaW5kUG9wdXAocG9wdXBfNjc2YjhhZDA2MTM0NDNhNmI0OWQ1YWY0YjVmZWRjMDMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfM2EyNGIwNDZhODg3NDRmYWE2NmJmOGUzNWMxMmRjMWQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Nzk1NTcxLC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWRhODlhMWRkNjg5NDVkMjhjNTJlZTQ1ZmRmYzM4YzEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWQwZTFlYjllOWMwNDg0NjljNTE2MmYxNTdhNTgwOTYgPSAkKCc8ZGl2IGlkPSJodG1sXzVkMGUxZWI5ZTljMDQ4NDY5YzUxNjJmMTU3YTU4MDk2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgRGFuZm9ydGggV2VzdCxSaXZlcmRhbGUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xZGE4OWExZGQ2ODk0NWQyOGM1MmVlNDVmZGZjMzhjMS5zZXRDb250ZW50KGh0bWxfNWQwZTFlYjllOWMwNDg0NjljNTE2MmYxNTdhNTgwOTYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfM2EyNGIwNDZhODg3NDRmYWE2NmJmOGUzNWMxMmRjMWQuYmluZFBvcHVwKHBvcHVwXzFkYTg5YTFkZDY4OTQ1ZDI4YzUyZWU0NWZkZmMzOGMxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzM5N2Q2ZWIzY2E1OTQxOTY4ZmI0MDllYTA4OGY4YWJiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY4OTk4NSwtNzkuMzE1NTcxNTk5OTk5OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWJiNTIzYmZiZTQyNDkxNmJmYjU3MTU2NTIyYTUxNWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDM0OTg5MmNhYWY4NDE3NWE3MzA4ODM0MzY4Mjc1YzUgPSAkKCc8ZGl2IGlkPSJodG1sXzQzNDk4OTJjYWFmODQxNzVhNzMwODgzNDM2ODI3NWM1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgQmVhY2hlcyBXZXN0LEluZGlhIEJhemFhciBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFiYjUyM2JmYmU0MjQ5MTZiZmI1NzE1NjUyMmE1MTVhLnNldENvbnRlbnQoaHRtbF80MzQ5ODkyY2FhZjg0MTc1YTczMDg4MzQzNjgyNzVjNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zOTdkNmViM2NhNTk0MTk2OGZiNDA5ZWEwODhmOGFiYi5iaW5kUG9wdXAocG9wdXBfMWJiNTIzYmZiZTQyNDkxNmJmYjU3MTU2NTIyYTUxNWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmY1N2U3NzcxM2UwNGRkODk4M2JlM2U5ZGY2MTVjZDcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTk1MjU1LC03OS4zNDA5MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWMwYmIxYjE3NjJkNDk1MWE3OWVlZTI3YmVlYmZkOGIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTY1MDI2YzYxNDE5NDAwY2FlOWM3ZWE1ZTE5YzEzYjkgPSAkKCc8ZGl2IGlkPSJodG1sX2U2NTAyNmM2MTQxOTQwMGNhZTljN2VhNWUxOWMxM2I5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdHVkaW8gRGlzdHJpY3QgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hYzBiYjFiMTc2MmQ0OTUxYTc5ZWVlMjdiZWViZmQ4Yi5zZXRDb250ZW50KGh0bWxfZTY1MDI2YzYxNDE5NDAwY2FlOWM3ZWE1ZTE5YzEzYjkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmY1N2U3NzcxM2UwNGRkODk4M2JlM2U5ZGY2MTVjZDcuYmluZFBvcHVwKHBvcHVwX2FjMGJiMWIxNzYyZDQ5NTFhNzllZWUyN2JlZWJmZDhiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzQ2NzViYjMxYmM1YTQxNDNiYzBlMTc2Y2E2MGFhYzY4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI4MDIwNSwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81MmVhMjk3ZjY0Mjk0NjYwYTc3ZDZmM2I5NDhjYjA1YyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wMjc4OGI4MTY1ODM0MmM3OWU0MjdmMzk1NGVkMGYyMiA9ICQoJzxkaXYgaWQ9Imh0bWxfMDI3ODhiODE2NTgzNDJjNzllNDI3ZjM5NTRlZDBmMjIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIFBhcmsgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81MmVhMjk3ZjY0Mjk0NjYwYTc3ZDZmM2I5NDhjYjA1Yy5zZXRDb250ZW50KGh0bWxfMDI3ODhiODE2NTgzNDJjNzllNDI3ZjM5NTRlZDBmMjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNDY3NWJiMzFiYzVhNDE0M2JjMGUxNzZjYTYwYWFjNjguYmluZFBvcHVwKHBvcHVwXzUyZWEyOTdmNjQyOTQ2NjBhNzdkNmYzYjk0OGNiMDVjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q3M2ZiZDhmYjQ5YTRmZDk5NTdlM2EzNmYxMDMzNGM3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzEyNzUxMSwtNzkuMzkwMTk3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82ODMxZDVmNGRjYzU0NjIxYmUzOGM1MjJiZDc3ZjdhYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lMjg1YTE5NGU5M2I0NGZhYjRhZTYwZDljYWM2ZmVjNSA9ICQoJzxkaXYgaWQ9Imh0bWxfZTI4NWExOTRlOTNiNDRmYWI0YWU2MGQ5Y2FjNmZlYzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUgTm9ydGggQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82ODMxZDVmNGRjYzU0NjIxYmUzOGM1MjJiZDc3ZjdhYS5zZXRDb250ZW50KGh0bWxfZTI4NWExOTRlOTNiNDRmYWI0YWU2MGQ5Y2FjNmZlYzUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDczZmJkOGZiNDlhNGZkOTk1N2UzYTM2ZjEwMzM0YzcuYmluZFBvcHVwKHBvcHVwXzY4MzFkNWY0ZGNjNTQ2MjFiZTM4YzUyMmJkNzdmN2FhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzAxZjI2OTZlZGIwNjRlYWRiNjVhOTQ2OTMzYWQ1YmUzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE1MzgzNCwtNzkuNDA1Njc4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDA0NGQwZjMzMTEwNDA2NGE3NDA1MjA5MDMxZWY1MGMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDJkNzk0ZjU1MmY4NDEwZmJmYTk0MmI5NDFmZWY0YjQgPSAkKCc8ZGl2IGlkPSJodG1sXzAyZDc5NGY1NTJmODQxMGZiZmE5NDJiOTQxZmVmNGI0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aCBUb3JvbnRvIFdlc3QgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kMDQ0ZDBmMzMxMTA0MDY0YTc0MDUyMDkwMzFlZjUwYy5zZXRDb250ZW50KGh0bWxfMDJkNzk0ZjU1MmY4NDEwZmJmYTk0MmI5NDFmZWY0YjQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDFmMjY5NmVkYjA2NGVhZGI2NWE5NDY5MzNhZDViZTMuYmluZFBvcHVwKHBvcHVwX2QwNDRkMGYzMzExMDQwNjRhNzQwNTIwOTAzMWVmNTBjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzAwMjk5YTJmNWJlYTRiOTc4ZTVmNjA5YmJjOWZkYWI4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA0MzI0NCwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82YjUwMjYzYWZjN2E0MDFjOGYzMTZiY2I1NDNiODFjOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83OTIyZjcxODhhN2M0YmViOTU0YzhkMmEwZTJlMDNkYiA9ICQoJzxkaXYgaWQ9Imh0bWxfNzkyMmY3MTg4YTdjNGJlYjk1NGM4ZDJhMGUyZTAzZGIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82YjUwMjYzYWZjN2E0MDFjOGYzMTZiY2I1NDNiODFjOC5zZXRDb250ZW50KGh0bWxfNzkyMmY3MTg4YTdjNGJlYjk1NGM4ZDJhMGUyZTAzZGIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDAyOTlhMmY1YmVhNGI5NzhlNWY2MDliYmM5ZmRhYjguYmluZFBvcHVwKHBvcHVwXzZiNTAyNjNhZmM3YTQwMWM4ZjMxNmJjYjU0M2I4MWM4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY1OWZjNTI0ZGNiZjQ2OWU4NjJjNDhjZGNiYWVkYzJlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg5NTc0MywtNzkuMzgzMTU5OTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjFjMWQwZGI3ZmQyNDNkYmEwN2JhNjVlNDlkYTdmOWQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYmFjYjBkNjUwZDQ1NDgyNzgxYjBiYjY1MWQ1MzY1ZTAgPSAkKCc8ZGl2IGlkPSJodG1sX2JhY2IwZDY1MGQ0NTQ4Mjc4MWIwYmI2NTFkNTM2NWUwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb29yZSBQYXJrLFN1bW1lcmhpbGwgRWFzdCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2IxYzFkMGRiN2ZkMjQzZGJhMDdiYTY1ZTQ5ZGE3ZjlkLnNldENvbnRlbnQoaHRtbF9iYWNiMGQ2NTBkNDU0ODI3ODFiMGJiNjUxZDUzNjVlMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82NTlmYzUyNGRjYmY0NjllODYyYzQ4Y2RjYmFlZGMyZS5iaW5kUG9wdXAocG9wdXBfYjFjMWQwZGI3ZmQyNDNkYmEwN2JhNjVlNDlkYTdmOWQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOGFmNmJlZmYzZTAwNGQ1Mzg1OGU4NmQ1MjdlNTk5YzYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42ODY0MTIyOTk5OTk5OSwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kYzc2NWY0NzM2MGU0NjljOTY1MTRhNjRmOTM0NTAyZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wNDJmNTYwMDM0MTU0NjQ3YWJjM2NhMTRmNjk4NWNlZCA9ICQoJzxkaXYgaWQ9Imh0bWxfMDQyZjU2MDAzNDE1NDY0N2FiYzNjYTE0ZjY5ODVjZWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRlZXIgUGFyayxGb3Jlc3QgSGlsbCBTRSxSYXRobmVsbHksU291dGggSGlsbCxTdW1tZXJoaWxsIFdlc3QgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kYzc2NWY0NzM2MGU0NjljOTY1MTRhNjRmOTM0NTAyZC5zZXRDb250ZW50KGh0bWxfMDQyZjU2MDAzNDE1NDY0N2FiYzNjYTE0ZjY5ODVjZWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGFmNmJlZmYzZTAwNGQ1Mzg1OGU4NmQ1MjdlNTk5YzYuYmluZFBvcHVwKHBvcHVwX2RjNzY1ZjQ3MzYwZTQ2OWM5NjUxNGE2NGY5MzQ1MDJkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZmYTdmOTY3YjVjYjQyNjY4NGJhYmEzYWE3YmJkNzY4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjc5NTYyNiwtNzkuMzc3NTI5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOTI2YTE2YjhkMWYwNDYwNThhMTgwMGUwM2JiMjBkY2UgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYmFmODc1NTEwYzhmNGRjNWJjOGZlMzFjMmY5Mzk5YTAgPSAkKCc8ZGl2IGlkPSJodG1sX2JhZjg3NTUxMGM4ZjRkYzViYzhmZTMxYzJmOTM5OWEwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlZGFsZSBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzkyNmExNmI4ZDFmMDQ2MDU4YTE4MDBlMDNiYjIwZGNlLnNldENvbnRlbnQoaHRtbF9iYWY4NzU1MTBjOGY0ZGM1YmM4ZmUzMWMyZjkzOTlhMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mZmE3Zjk2N2I1Y2I0MjY2ODRiYWJhM2FhN2JiZDc2OC5iaW5kUG9wdXAocG9wdXBfOTI2YTE2YjhkMWYwNDYwNThhMTgwMGUwM2JiMjBkY2UpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfY2Y1ZjUyYzNmYmM1NGFmMTkxN2JlOTA3OWEzZGZkYmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Njc5NjcsLTc5LjM2NzY3NTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDA2NDNhMTNiZGU0NDg0Zjg2ZjUwMTM5YzAyMzhhZjMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2VkYzUxMzE1OWE4NDQxNDllOTQ4YzNhOWExZjUwM2UgPSAkKCc8ZGl2IGlkPSJodG1sXzdlZGM1MTMxNTlhODQ0MTQ5ZTk0OGMzYTlhMWY1MDNlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYWJiYWdldG93bixTdC4gSmFtZXMgVG93biBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQwNjQzYTEzYmRlNDQ4NGY4NmY1MDEzOWMwMjM4YWYzLnNldENvbnRlbnQoaHRtbF83ZWRjNTEzMTU5YTg0NDE0OWU5NDhjM2E5YTFmNTAzZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jZjVmNTJjM2ZiYzU0YWYxOTE3YmU5MDc5YTNkZmRiYi5iaW5kUG9wdXAocG9wdXBfNDA2NDNhMTNiZGU0NDg0Zjg2ZjUwMTM5YzAyMzhhZjMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDQ2MDliOGNhZTRmNGExYzg0NzNiNWJhYzlhZmY5NDggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjU4NTk5LC03OS4zODMxNTk5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xYzY2ODFhN2JmOWI0MTkzODNiY2UxYTI1MWViZjVjYiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82YzRjZTgxZGU4MzQ0NDU3YTllNTk3N2JlNWFjNGYyMCA9ICQoJzxkaXYgaWQ9Imh0bWxfNmM0Y2U4MWRlODM0NDQ1N2E5ZTU5NzdiZTVhYzRmMjAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNodXJjaCBhbmQgV2VsbGVzbGV5IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWM2NjgxYTdiZjliNDE5MzgzYmNlMWEyNTFlYmY1Y2Iuc2V0Q29udGVudChodG1sXzZjNGNlODFkZTgzNDQ0NTdhOWU1OTc3YmU1YWM0ZjIwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q0NjA5YjhjYWU0ZjRhMWM4NDczYjViYWM5YWZmOTQ4LmJpbmRQb3B1cChwb3B1cF8xYzY2ODFhN2JmOWI0MTkzODNiY2UxYTI1MWViZjVjYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yM2E3MGU1ZDNlNDE0NTQ5ODIwYmY4NjE0ZGVlNDEwMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1NDI1OTksLTc5LjM2MDYzNTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTZmOGNkMTU0ODc5NDlhMjhmMTU3YjA2NzA4ZTI5MjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWI1NTZmZWIwOTU2NGUzNGI5NzM5YjA3NzJlYzk1NWEgPSAkKCc8ZGl2IGlkPSJodG1sX2ViNTU2ZmViMDk1NjRlMzRiOTczOWIwNzcyZWM5NTVhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQsUmVnZW50IFBhcmsgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lNmY4Y2QxNTQ4Nzk0OWEyOGYxNTdiMDY3MDhlMjkyNS5zZXRDb250ZW50KGh0bWxfZWI1NTZmZWIwOTU2NGUzNGI5NzM5YjA3NzJlYzk1NWEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjNhNzBlNWQzZTQxNDU0OTgyMGJmODYxNGRlZTQxMDEuYmluZFBvcHVwKHBvcHVwX2U2ZjhjZDE1NDg3OTQ5YTI4ZjE1N2IwNjcwOGUyOTI1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzA0NGM0MjNiMzViOTQyNWE5ZTgyMjljMTYzOWU4Y2MwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjU3MTYxOCwtNzkuMzc4OTM3MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzk3MGVhOGRhN2EzNDU4ZWFhY2RhYzZmZDI0YWE1NDYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2I2ZDQ2NTNiMmQwNGQ2MmEzMzI5NGRlNmFmNzY5ODIgPSAkKCc8ZGl2IGlkPSJodG1sXzdiNmQ0NjUzYjJkMDRkNjJhMzMyOTRkZTZhZjc2OTgyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SeWVyc29uLEdhcmRlbiBEaXN0cmljdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M5NzBlYThkYTdhMzQ1OGVhYWNkYWM2ZmQyNGFhNTQ2LnNldENvbnRlbnQoaHRtbF83YjZkNDY1M2IyZDA0ZDYyYTMzMjk0ZGU2YWY3Njk4Mik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wNDRjNDIzYjM1Yjk0MjVhOWU4MjI5YzE2MzllOGNjMC5iaW5kUG9wdXAocG9wdXBfYzk3MGVhOGRhN2EzNDU4ZWFhY2RhYzZmZDI0YWE1NDYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjRmNjM3Y2EwZTY4NDM2MGE0NmU3NDE2N2EzNTE5ZTkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTE0OTM5LC03OS4zNzU0MTc5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzUzOWZhNWM1M2JlZDQ5YTRhOTkzZTBlZDRjMGM1ZWZhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY0MzM5ODQxNDgyNTRlZTc4YTU4NGZjZjA3YmExMjc5ID0gJCgnPGRpdiBpZD0iaHRtbF82NDMzOTg0MTQ4MjU0ZWU3OGE1ODRmY2YwN2JhMTI3OSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3QuIEphbWVzIFRvd24gQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81MzlmYTVjNTNiZWQ0OWE0YTk5M2UwZWQ0YzBjNWVmYS5zZXRDb250ZW50KGh0bWxfNjQzMzk4NDE0ODI1NGVlNzhhNTg0ZmNmMDdiYTEyNzkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjRmNjM3Y2EwZTY4NDM2MGE0NmU3NDE2N2EzNTE5ZTkuYmluZFBvcHVwKHBvcHVwXzUzOWZhNWM1M2JlZDQ5YTRhOTkzZTBlZDRjMGM1ZWZhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJhY2Q3MzExNjE4MzQ2OWU4ZWQyNWNkNDA5MDMwMDk2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ0NzcwNzk5OTk5OTk2LC03OS4zNzMzMDY0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk5MGE3MzA2MzUzZjQzNTlhMWE3OTg5ZjY1ODI2YzAzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzAxODlhNzI3NDgxNzRjN2ZhOTZkY2MzY2EyMjliMGY1ID0gJCgnPGRpdiBpZD0iaHRtbF8wMTg5YTcyNzQ4MTc0YzdmYTk2ZGNjM2NhMjI5YjBmNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVyY3p5IFBhcmsgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85OTBhNzMwNjM1M2Y0MzU5YTFhNzk4OWY2NTgyNmMwMy5zZXRDb250ZW50KGh0bWxfMDE4OWE3Mjc0ODE3NGM3ZmE5NmRjYzNjYTIyOWIwZjUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmFjZDczMTE2MTgzNDY5ZThlZDI1Y2Q0MDkwMzAwOTYuYmluZFBvcHVwKHBvcHVwXzk5MGE3MzA2MzUzZjQzNTlhMWE3OTg5ZjY1ODI2YzAzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VmZTE3NGZlZTllMzRlYjZhMWQ1ZTgzMDU3ZmFhZjgzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjU3OTUyNCwtNzkuMzg3MzgyNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83N2FlZWJjZTgyMTM0MzY0OWJhNDI4YTFlMzFmNTQ0ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iODgzYWZjYmU4ODA0OWU1YmU2NTFlNGI1NGZjY2MxMiA9ICQoJzxkaXYgaWQ9Imh0bWxfYjg4M2FmY2JlODgwNDllNWJlNjUxZTRiNTRmY2NjMTIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNlbnRyYWwgQmF5IFN0cmVldCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc3YWVlYmNlODIxMzQzNjQ5YmE0MjhhMWUzMWY1NDRmLnNldENvbnRlbnQoaHRtbF9iODgzYWZjYmU4ODA0OWU1YmU2NTFlNGI1NGZjY2MxMik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lZmUxNzRmZWU5ZTM0ZWI2YTFkNWU4MzA1N2ZhYWY4My5iaW5kUG9wdXAocG9wdXBfNzdhZWViY2U4MjEzNDM2NDliYTQyOGExZTMxZjU0NGYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDBiMzg1ZWJlYjFmNDE2OWEwMTBhMzczMmVlYjljNjIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTA1NzEyMDAwMDAwMSwtNzkuMzg0NTY3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82YjQxZWE4ZDFkYjM0NDEyOGI2M2E5YmMwZjQxYmUxOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jYTE2YjViMmQ5ZGY0OTk3OGNkNmUxYWQ4ODUyYTFmNCA9ICQoJzxkaXYgaWQ9Imh0bWxfY2ExNmI1YjJkOWRmNDk5NzhjZDZlMWFkODg1MmExZjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZWxhaWRlLEtpbmcsUmljaG1vbmQgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82YjQxZWE4ZDFkYjM0NDEyOGI2M2E5YmMwZjQxYmUxOS5zZXRDb250ZW50KGh0bWxfY2ExNmI1YjJkOWRmNDk5NzhjZDZlMWFkODg1MmExZjQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDBiMzg1ZWJlYjFmNDE2OWEwMTBhMzczMmVlYjljNjIuYmluZFBvcHVwKHBvcHVwXzZiNDFlYThkMWRiMzQ0MTI4YjYzYTliYzBmNDFiZTE5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E0NDUzMTVhM2VkYjRkZGZiOWM0ODRkZmRlMGEyMjcwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQwODE1NywtNzkuMzgxNzUyMjk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWIwMWRhYTA2OGQ5NDEzMWI4ZjIyNzg5NWQzN2U4ZTEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODBlNjRkM2UwOWQ0NDg4Yzk1ZWJiOWFlYWM3ODViNDcgPSAkKCc8ZGl2IGlkPSJodG1sXzgwZTY0ZDNlMDlkNDQ4OGM5NWViYjlhZWFjNzg1YjQ3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQgRWFzdCxUb3JvbnRvIElzbGFuZHMsVW5pb24gU3RhdGlvbiBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzViMDFkYWEwNjhkOTQxMzFiOGYyMjc4OTVkMzdlOGUxLnNldENvbnRlbnQoaHRtbF84MGU2NGQzZTA5ZDQ0ODhjOTVlYmI5YWVhYzc4NWI0Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hNDQ1MzE1YTNlZGI0ZGRmYjljNDg0ZGZkZTBhMjI3MC5iaW5kUG9wdXAocG9wdXBfNWIwMWRhYTA2OGQ5NDEzMWI4ZjIyNzg5NWQzN2U4ZTEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZWQ3NDNlN2IwMDBmNDZmZmFlYWIxMTUzZWEwZTgzZWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDcxNzY4LC03OS4zODE1NzY0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hMzVmMGVjZWI0OWU0ZTAzOGNjOGVmNzY2MGI3Y2ViZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lNzVmMzk0YjAzN2Q0NjQ2OGY2MzNmZDBiMDc4YzUxZiA9ICQoJzxkaXYgaWQ9Imh0bWxfZTc1ZjM5NGIwMzdkNDY0NjhmNjMzZmQwYjA3OGM1MWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRlc2lnbiBFeGNoYW5nZSxUb3JvbnRvIERvbWluaW9uIENlbnRyZSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2EzNWYwZWNlYjQ5ZTRlMDM4Y2M4ZWY3NjYwYjdjZWJkLnNldENvbnRlbnQoaHRtbF9lNzVmMzk0YjAzN2Q0NjQ2OGY2MzNmZDBiMDc4YzUxZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lZDc0M2U3YjAwMGY0NmZmYWVhYjExNTNlYTBlODNlZS5iaW5kUG9wdXAocG9wdXBfYTM1ZjBlY2ViNDllNGUwMzhjYzhlZjc2NjBiN2NlYmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDE5NGFjMWFlZGI5NDFlYTk2ZDQwNDY1NmIyM2Q1NzIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDgxOTg1LC03OS4zNzk4MTY5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wZmMwZDRhMjljMDk0ZWExYTFjMDE2YjViZTJlZjk3MyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kOGY0OWJlZTNmOTc0OWRjYmQ3NTVhMjQ0M2RmMzFiOCA9ICQoJzxkaXYgaWQ9Imh0bWxfZDhmNDliZWUzZjk3NDlkY2JkNzU1YTI0NDNkZjMxYjgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvbW1lcmNlIENvdXJ0LFZpY3RvcmlhIEhvdGVsIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMGZjMGQ0YTI5YzA5NGVhMWExYzAxNmI1YmUyZWY5NzMuc2V0Q29udGVudChodG1sX2Q4ZjQ5YmVlM2Y5NzQ5ZGNiZDc1NWEyNDQzZGYzMWI4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQxOTRhYzFhZWRiOTQxZWE5NmQ0MDQ2NTZiMjNkNTcyLmJpbmRQb3B1cChwb3B1cF8wZmMwZDRhMjljMDk0ZWExYTFjMDE2YjViZTJlZjk3Myk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xMWU0MDM1ODBhMzQ0ZDk0OWNmZTc0NmQwOGEzYjZjZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjczMzI4MjUsLTc5LjQxOTc0OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmNlNzU4N2JlNTI3NDg3Yzk1YTU1NmVlYWY4ZTM4YTYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTBkYjdkMzZjNTZiNDVmZWJjMjY1ODlhY2EwZjc5ODMgPSAkKCc8ZGl2IGlkPSJodG1sXzEwZGI3ZDM2YzU2YjQ1ZmViYzI2NTg5YWNhMGY3OTgzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWRmb3JkIFBhcmssTGF3cmVuY2UgTWFub3IgRWFzdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZjZTc1ODdiZTUyNzQ4N2M5NWE1NTZlZWFmOGUzOGE2LnNldENvbnRlbnQoaHRtbF8xMGRiN2QzNmM1NmI0NWZlYmMyNjU4OWFjYTBmNzk4Myk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xMWU0MDM1ODBhMzQ0ZDk0OWNmZTc0NmQwOGEzYjZjZS5iaW5kUG9wdXAocG9wdXBfZmNlNzU4N2JlNTI3NDg3Yzk1YTU1NmVlYWY4ZTM4YTYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzg4ODg4OWU2NGNlNGJjYzhmYmY2YzZkNmYwOGQ2OTYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MTE2OTQ4LC03OS40MTY5MzU1OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81YWU4MDI1NDQxMTE0OTIyOWMyOTY4OWVhMTM2M2QyNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82MDhiZDFmNWFhMzM0MTA3ODY1YmI5YWY0ZjI2NDEzMiA9ICQoJzxkaXYgaWQ9Imh0bWxfNjA4YmQxZjVhYTMzNDEwNzg2NWJiOWFmNGYyNjQxMzIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJvc2VsYXduIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNWFlODAyNTQ0MTExNDkyMjljMjk2ODllYTEzNjNkMjUuc2V0Q29udGVudChodG1sXzYwOGJkMWY1YWEzMzQxMDc4NjViYjlhZjRmMjY0MTMyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc4ODg4ODllNjRjZTRiY2M4ZmJmNmM2ZDZmMDhkNjk2LmJpbmRQb3B1cChwb3B1cF81YWU4MDI1NDQxMTE0OTIyOWMyOTY4OWVhMTM2M2QyNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jNDA3MzM5YzQyMDY0NWNjOWFmNjQwYjNkZTgxMzlmZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5Njk0NzYsLTc5LjQxMTMwNzIwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2VjNDk0ODI5OGQyOTQwYWZhMDE2ZWZhZTE2MDkxYWMxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzMxODU5NTk3ZTFiNjRkMjM5NDllNWU0NmZmZTQzY2FhID0gJCgnPGRpdiBpZD0iaHRtbF8zMTg1OTU5N2UxYjY0ZDIzOTQ5ZTVlNDZmZmU0M2NhYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rm9yZXN0IEhpbGwgTm9ydGgsRm9yZXN0IEhpbGwgV2VzdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2VjNDk0ODI5OGQyOTQwYWZhMDE2ZWZhZTE2MDkxYWMxLnNldENvbnRlbnQoaHRtbF8zMTg1OTU5N2UxYjY0ZDIzOTQ5ZTVlNDZmZmU0M2NhYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jNDA3MzM5YzQyMDY0NWNjOWFmNjQwYjNkZTgxMzlmZS5iaW5kUG9wdXAocG9wdXBfZWM0OTQ4Mjk4ZDI5NDBhZmEwMTZlZmFlMTYwOTFhYzEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWM5NTMzMTM4ZjI5NGZmZmI3ZWYwMDNlYzZhNDg4N2MgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NzI3MDk3LC03OS40MDU2Nzg0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zYjYyM2IzNWZjMWQ0YWU2YTQzYjUwZmY4M2FhYWQxNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84NDY3NTQxZDMwNmI0NzJhODI3NmJiOTAyYzFlNTExZiA9ICQoJzxkaXYgaWQ9Imh0bWxfODQ2NzU0MWQzMDZiNDcyYTgyNzZiYjkwMmMxZTUxMWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRoZSBBbm5leCxOb3J0aCBNaWR0b3duLFlvcmt2aWxsZSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNiNjIzYjM1ZmMxZDRhZTZhNDNiNTBmZjgzYWFhZDE1LnNldENvbnRlbnQoaHRtbF84NDY3NTQxZDMwNmI0NzJhODI3NmJiOTAyYzFlNTExZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hYzk1MzMxMzhmMjk0ZmZmYjdlZjAwM2VjNmE0ODg3Yy5iaW5kUG9wdXAocG9wdXBfM2I2MjNiMzVmYzFkNGFlNmE0M2I1MGZmODNhYWFkMTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDQ5Y2M0MTMzZGFmNGRkMTg3NGVlYjY2M2U0NDRmYjYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjI2OTU2LC03OS40MDAwNDkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzQ2ZmE2OWUyZjA0MzQ0ODE4M2Y2ZDUzYmEzY2Y1Nzk0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JiODhiZTBjZmQzNTQxNWViMjYxYWUxMzUyNzE2YWM4ID0gJCgnPGRpdiBpZD0iaHRtbF9iYjg4YmUwY2ZkMzU0MTVlYjI2MWFlMTM1MjcxNmFjOCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGFyYm9yZCxVbml2ZXJzaXR5IG9mIFRvcm9udG8gQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80NmZhNjllMmYwNDM0NDgxODNmNmQ1M2JhM2NmNTc5NC5zZXRDb250ZW50KGh0bWxfYmI4OGJlMGNmZDM1NDE1ZWIyNjFhZTEzNTI3MTZhYzgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDQ5Y2M0MTMzZGFmNGRkMTg3NGVlYjY2M2U0NDRmYjYuYmluZFBvcHVwKHBvcHVwXzQ2ZmE2OWUyZjA0MzQ0ODE4M2Y2ZDUzYmEzY2Y1Nzk0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzlkOGJiOTIwYzY4NDRjNGJiMjgwMWQ3ZmMyNzFhOTJjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUzMjA1NywtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80NjQ4NTYzM2UxN2Y0MTEzYjc4YzE1MWNiZWU0ODRmMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lOThkNTcyNGEwYTM0MmUzYjJhOTMzOThjZGRjM2EyOSA9ICQoJzxkaXYgaWQ9Imh0bWxfZTk4ZDU3MjRhMGEzNDJlM2IyYTkzMzk4Y2RkYzNhMjkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNoaW5hdG93bixHcmFuZ2UgUGFyayxLZW5zaW5ndG9uIE1hcmtldCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQ2NDg1NjMzZTE3ZjQxMTNiNzhjMTUxY2JlZTQ4NGYzLnNldENvbnRlbnQoaHRtbF9lOThkNTcyNGEwYTM0MmUzYjJhOTMzOThjZGRjM2EyOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85ZDhiYjkyMGM2ODQ0YzRiYjI4MDFkN2ZjMjcxYTkyYy5iaW5kUG9wdXAocG9wdXBfNDY0ODU2MzNlMTdmNDExM2I3OGMxNTFjYmVlNDg0ZjMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDI3OTA0NWRlMTg0NDI3NjgzMDY5Y2EwMjE2YTZjMmQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Mjg5NDY3LC03OS4zOTQ0MTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2VlNDAwZGI1OGI4NTRlOTQ4NDljMzEwYjE0MmIzYmY2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY4NjMxMWE5MGM2YTQ3OGJhYjVkZWU2YzJjMzQ4MzNiID0gJCgnPGRpdiBpZD0iaHRtbF82ODYzMTFhOTBjNmE0NzhiYWI1ZGVlNmMyYzM0ODMzYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q04gVG93ZXIsQmF0aHVyc3QgUXVheSxJc2xhbmQgYWlycG9ydCxIYXJib3VyZnJvbnQgV2VzdCxLaW5nIGFuZCBTcGFkaW5hLFJhaWx3YXkgTGFuZHMsU291dGggTmlhZ2FyYSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2VlNDAwZGI1OGI4NTRlOTQ4NDljMzEwYjE0MmIzYmY2LnNldENvbnRlbnQoaHRtbF82ODYzMTFhOTBjNmE0NzhiYWI1ZGVlNmMyYzM0ODMzYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wMjc5MDQ1ZGUxODQ0Mjc2ODMwNjljYTAyMTZhNmMyZC5iaW5kUG9wdXAocG9wdXBfZWU0MDBkYjU4Yjg1NGU5NDg0OWMzMTBiMTQyYjNiZjYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMjRiZDkwZmJmNTEyNGQwOGEyZjIwYTVmN2U2NGE4NDEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDY0MzUyLC03OS4zNzQ4NDU5OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zNTk3NmRjYTU2Nzg0ODZlYTQzYzlmMGE3YTllNTM4OSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81MjY1YTZjNzk2MDg0MDBmYWE2NDNhOTgwYTU5NDUzNSA9ICQoJzxkaXYgaWQ9Imh0bWxfNTI2NWE2Yzc5NjA4NDAwZmFhNjQzYTk4MGE1OTQ1MzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlN0biBBIFBPIEJveGVzIDI1IFRoZSBFc3BsYW5hZGUgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zNTk3NmRjYTU2Nzg0ODZlYTQzYzlmMGE3YTllNTM4OS5zZXRDb250ZW50KGh0bWxfNTI2NWE2Yzc5NjA4NDAwZmFhNjQzYTk4MGE1OTQ1MzUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjRiZDkwZmJmNTEyNGQwOGEyZjIwYTVmN2U2NGE4NDEuYmluZFBvcHVwKHBvcHVwXzM1OTc2ZGNhNTY3ODQ4NmVhNDNjOWYwYTdhOWU1Mzg5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzM4NzQxMTI4ZmI3MzRjMmU5ZGM2NmEyOTc2NGFmZWQ1ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ4NDI5MiwtNzkuMzgyMjgwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ZWVhMTNiNWZiMmY0ZmIwOWVmNWUzMzJmNzIyMTA1ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80MjFmYWVhNTY5M2I0NzRhYjUyMDBiMDQ3YzFjZGE3OSA9ICQoJzxkaXYgaWQ9Imh0bWxfNDIxZmFlYTU2OTNiNDc0YWI1MjAwYjA0N2MxY2RhNzkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZpcnN0IENhbmFkaWFuIFBsYWNlLFVuZGVyZ3JvdW5kIGNpdHkgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83ZWVhMTNiNWZiMmY0ZmIwOWVmNWUzMzJmNzIyMTA1ZC5zZXRDb250ZW50KGh0bWxfNDIxZmFlYTU2OTNiNDc0YWI1MjAwYjA0N2MxY2RhNzkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzg3NDExMjhmYjczNGMyZTlkYzY2YTI5NzY0YWZlZDUuYmluZFBvcHVwKHBvcHVwXzdlZWExM2I1ZmIyZjRmYjA5ZWY1ZTMzMmY3MjIxMDVkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2I4MGJmMDQ4MDA3ZDRkZDM5NjMzNzI0MWRhMGUyMzEyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE4NTE3OTk5OTk5OTk2LC03OS40NjQ3NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wNTNiOGNiNzZhYzc0ZTljOTAxYjUwMmM5MjZhODg3YyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kNTg5OGQ2NGU5NDk0M2VkOTFmZWU3Y2M2MDRmNzYyZiA9ICQoJzxkaXYgaWQ9Imh0bWxfZDU4OThkNjRlOTQ5NDNlZDkxZmVlN2NjNjA0Zjc2MmYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIEhlaWdodHMsTGF3cmVuY2UgTWFub3IgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wNTNiOGNiNzZhYzc0ZTljOTAxYjUwMmM5MjZhODg3Yy5zZXRDb250ZW50KGh0bWxfZDU4OThkNjRlOTQ5NDNlZDkxZmVlN2NjNjA0Zjc2MmYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjgwYmYwNDgwMDdkNGRkMzk2MzM3MjQxZGEwZTIzMTIuYmluZFBvcHVwKHBvcHVwXzA1M2I4Y2I3NmFjNzRlOWM5MDFiNTAyYzkyNmE4ODdjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzkwZmY0ODdlNDI5NzRkYzJiOTE2MjFlYzdiN2E2MjlhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA5NTc3LC03OS40NDUwNzI1OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zODM1YTIyMDE3NTA0NDAzYTZjZTA3NzRkZDFjMGEyOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hMWZkOWJkMTk4ZTk0MWY5YmQ3YzgzYjU5ODE5NzBmNCA9ICQoJzxkaXYgaWQ9Imh0bWxfYTFmZDliZDE5OGU5NDFmOWJkN2M4M2I1OTgxOTcwZjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdsZW5jYWlybiBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzM4MzVhMjIwMTc1MDQ0MDNhNmNlMDc3NGRkMWMwYTI5LnNldENvbnRlbnQoaHRtbF9hMWZkOWJkMTk4ZTk0MWY5YmQ3YzgzYjU5ODE5NzBmNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl85MGZmNDg3ZTQyOTc0ZGMyYjkxNjIxZWM3YjdhNjI5YS5iaW5kUG9wdXAocG9wdXBfMzgzNWEyMjAxNzUwNDQwM2E2Y2UwNzc0ZGQxYzBhMjkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2IwYmUzMzg1YzZmNDJhMGE1OGJjOGNlNzdjYTEwZDYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTM3ODEzLC03OS40MjgxOTE0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xZGE4M2Q0YjA2ZjM0NTY1OTQwY2YwYzgyNWQxZmU0ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kZDQ3YTBmYmQ5Njc0MzVlYWJkZDZiOTljZDUyNjM2ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfZGQ0N2EwZmJkOTY3NDM1ZWFiZGQ2Yjk5Y2Q1MjYzNmUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWV3b29kLUNlZGFydmFsZSBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFkYTgzZDRiMDZmMzQ1NjU5NDBjZjBjODI1ZDFmZTRkLnNldENvbnRlbnQoaHRtbF9kZDQ3YTBmYmQ5Njc0MzVlYWJkZDZiOTljZDUyNjM2ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83YjBiZTMzODVjNmY0MmEwYTU4YmM4Y2U3N2NhMTBkNi5iaW5kUG9wdXAocG9wdXBfMWRhODNkNGIwNmYzNDU2NTk0MGNmMGM4MjVkMWZlNGQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjIxMDliMWMwYjQzNGQ4ZTllMmYwM2UxN2Y3NzA2MzcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42ODkwMjU2LC03OS40NTM1MTJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNGM3NzQ2Y2I0NGZiNGI3MWE1MzU5M2U2OGFiNTUzZGIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmU0MmRjMmI5YTAzNGZlM2E4MzM4MTMxNTUxYTRkZTIgPSAkKCc8ZGl2IGlkPSJodG1sX2ZlNDJkYzJiOWEwMzRmZTNhODMzODEzMTU1MWE0ZGUyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYWxlZG9uaWEtRmFpcmJhbmtzIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNGM3NzQ2Y2I0NGZiNGI3MWE1MzU5M2U2OGFiNTUzZGIuc2V0Q29udGVudChodG1sX2ZlNDJkYzJiOWEwMzRmZTNhODMzODEzMTU1MWE0ZGUyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzYyMTA5YjFjMGI0MzRkOGU5ZTJmMDNlMTdmNzcwNjM3LmJpbmRQb3B1cChwb3B1cF80Yzc3NDZjYjQ0ZmI0YjcxYTUzNTkzZTY4YWI1NTNkYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iZmM1M2Q4NzQ4MTk0NWZjYWJjNjljYjA1N2UzYWIyZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2OTU0MiwtNzkuNDIyNTYzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lOWNjNjI0ZmI1NGM0MTRjYTE5ZTM1ZDU3NTRjODhiZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zYmVjOTJkY2EwNDg0ZjNhOGQxNTY4NjY3ZGNjOGY4ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfM2JlYzkyZGNhMDQ4NGYzYThkMTU2ODY2N2RjYzhmOGUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNocmlzdGllIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTljYzYyNGZiNTRjNDE0Y2ExOWUzNWQ1NzU0Yzg4YmYuc2V0Q29udGVudChodG1sXzNiZWM5MmRjYTA0ODRmM2E4ZDE1Njg2NjdkY2M4ZjhlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2JmYzUzZDg3NDgxOTQ1ZmNhYmM2OWNiMDU3ZTNhYjJmLmJpbmRQb3B1cChwb3B1cF9lOWNjNjI0ZmI1NGM0MTRjYTE5ZTM1ZDU3NTRjODhiZik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81N2YwYjcwNWM5ZmU0Zjk5YjY1NGY4YzRkMWE0ZmE3ZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2OTAwNTEwMDAwMDAxLC03OS40NDIyNTkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2ZjYmY4ZDBhNjc1MDQ0ZGJiNWU5OThkMDg1MWQ5YzRiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzZjZTU3NDRmYTJkZjQ4NWU4ODFmNzQ3ZmJlODM2MjM0ID0gJCgnPGRpdiBpZD0iaHRtbF82Y2U1NzQ0ZmEyZGY0ODVlODgxZjc0N2ZiZTgzNjIzNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG92ZXJjb3VydCBWaWxsYWdlLER1ZmZlcmluIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmNiZjhkMGE2NzUwNDRkYmI1ZTk5OGQwODUxZDljNGIuc2V0Q29udGVudChodG1sXzZjZTU3NDRmYTJkZjQ4NWU4ODFmNzQ3ZmJlODM2MjM0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzU3ZjBiNzA1YzlmZTRmOTliNjU0ZjhjNGQxYTRmYTdmLmJpbmRQb3B1cChwb3B1cF9mY2JmOGQwYTY3NTA0NGRiYjVlOTk4ZDA4NTFkOWM0Yik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNjdiYTUwYzdiYmU0Y2VjYTc5ZmE0ZTU5NDg2NDY1NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY0NzkyNjcwMDAwMDAwNiwtNzkuNDE5NzQ5N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mNjgxNTJmZmRjNzg0ZGE1YTlhMzJhYzg5Y2I2YjNlMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80ZDM2Y2QyODljNDI0OWY5OGI4NjY4ZTlkNjljYTk2ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfNGQzNmNkMjg5YzQyNDlmOThiODY2OGU5ZDY5Y2E5NmYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxpdHRsZSBQb3J0dWdhbCxUcmluaXR5IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjY4MTUyZmZkYzc4NGRhNWE5YTMyYWM4OWNiNmIzZTEuc2V0Q29udGVudChodG1sXzRkMzZjZDI4OWM0MjQ5Zjk4Yjg2NjhlOWQ2OWNhOTZmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzE2N2JhNTBjN2JiZTRjZWNhNzlmYTRlNTk0ODY0NjU0LmJpbmRQb3B1cChwb3B1cF9mNjgxNTJmZmRjNzg0ZGE1YTlhMzJhYzg5Y2I2YjNlMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zNDRhMTdmNDAyNDg0ZGJiYWMzNmFjMTM1N2FjNWRmNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYzNjg0NzIsLTc5LjQyODE5MTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NlZmQ1YWFiZWE4MzQ3OGE5ZThmYzc1YzFmYTZjNDcyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2NkYzMzYWVjOTYzYjRhMGFhNDE3YzE3ZWQzYzIwNWNkID0gJCgnPGRpdiBpZD0iaHRtbF9jZGMzM2FlYzk2M2I0YTBhYTQxN2MxN2VkM2MyMDVjZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnJvY2t0b24sRXhoaWJpdGlvbiBQbGFjZSxQYXJrZGFsZSBWaWxsYWdlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfY2VmZDVhYWJlYTgzNDc4YTllOGZjNzVjMWZhNmM0NzIuc2V0Q29udGVudChodG1sX2NkYzMzYWVjOTYzYjRhMGFhNDE3YzE3ZWQzYzIwNWNkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzM0NGExN2Y0MDI0ODRkYmJhYzM2YWMxMzU3YWM1ZGY3LmJpbmRQb3B1cChwb3B1cF9jZWZkNWFhYmVhODM0NzhhOWU4ZmM3NWMxZmE2YzQ3Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81NzQ2MDgwOWQyNDg0YjJlODU5MjkzNTQyNzZhOTM1YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcxMzc1NjIwMDAwMDAwNiwtNzkuNDkwMDczOF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmZiMzYwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmYjM2MCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wMzAyODMxNmVhMGM0Y2RkODJhZWQzNDM2NDYzMmRhMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mNDdkNDBlZmJlNzE0NGNkYmRmMzZjNmZiNmE4ZDBiYSA9ICQoJzxkaXYgaWQ9Imh0bWxfZjQ3ZDQwZWZiZTcxNDRjZGJkZjM2YzZmYjZhOGQwYmEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvd25zdmlldyxOb3J0aCBQYXJrLFVwd29vZCBQYXJrIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDMwMjgzMTZlYTBjNGNkZDgyYWVkMzQzNjQ2MzJkYTIuc2V0Q29udGVudChodG1sX2Y0N2Q0MGVmYmU3MTQ0Y2RiZGYzNmM2ZmI2YThkMGJhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzU3NDYwODA5ZDI0ODRiMmU4NTkyOTM1NDI3NmE5MzVhLmJpbmRQb3B1cChwb3B1cF8wMzAyODMxNmVhMGM0Y2RkODJhZWQzNDM2NDYzMmRhMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80NmZmODYwZGRlYzE0MzJmYTEyNDg3NGEzZGE2ZGM0ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5MTExNTgsLTc5LjQ3NjAxMzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U2NGVhNGUyZTQxYjQ0NTNhZWMxOTYwZTMyZTg3ZTU2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2VmNjY3MzI0ZWJhNjQxNTFhMTg2MzcxYmE2YzVjMzdhID0gJCgnPGRpdiBpZD0iaHRtbF9lZjY2NzMyNGViYTY0MTUxYTE4NjM3MWJhNmM1YzM3YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RGVsIFJheSxLZWVsZXNkYWxlLE1vdW50IERlbm5pcyxTaWx2ZXJ0aG9ybiBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2U2NGVhNGUyZTQxYjQ0NTNhZWMxOTYwZTMyZTg3ZTU2LnNldENvbnRlbnQoaHRtbF9lZjY2NzMyNGViYTY0MTUxYTE4NjM3MWJhNmM1YzM3YSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80NmZmODYwZGRlYzE0MzJmYTEyNDg3NGEzZGE2ZGM0ZC5iaW5kUG9wdXAocG9wdXBfZTY0ZWE0ZTJlNDFiNDQ1M2FlYzE5NjBlMzJlODdlNTYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzAzOTY1ODI4NjZiNDZlOGE1NzY3NTIyODlkZGZlMGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NzMxODUyOTk5OTk5OSwtNzkuNDg3MjYxOTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYmNiYTU5YzI3MzY1NDI2ZjkwNWU4YTA5MWJjMDQyNTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGVkOGFiNjNlYzc4NDdiOTgyM2RlMTY5OTQ0YjA3OTAgPSAkKCc8ZGl2IGlkPSJodG1sXzRlZDhhYjYzZWM3ODQ3Yjk4MjNkZTE2OTk0NGIwNzkwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgSnVuY3Rpb24gTm9ydGgsUnVubnltZWRlIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYmNiYTU5YzI3MzY1NDI2ZjkwNWU4YTA5MWJjMDQyNTguc2V0Q29udGVudChodG1sXzRlZDhhYjYzZWM3ODQ3Yjk4MjNkZTE2OTk0NGIwNzkwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2MwMzk2NTgyODY2YjQ2ZThhNTc2NzUyMjg5ZGRmZTBiLmJpbmRQb3B1cChwb3B1cF9iY2JhNTljMjczNjU0MjZmOTA1ZThhMDkxYmMwNDI1OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kMWE5ZmI3YTQ5NTE0OWVmYjQ2NGVhOGE0YzBjYThmMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MTYwODMsLTc5LjQ2NDc2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzBhYjdiOGRiZjg3MTRkMDViYTQyZDljZjQyMzIzNzg2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2M4YTBlZDZjNTU2ZTQyZmJhMzdjMzU4YmU0M2MyZjcyID0gJCgnPGRpdiBpZD0iaHRtbF9jOGEwZWQ2YzU1NmU0MmZiYTM3YzM1OGJlNDNjMmY3MiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaCBQYXJrLFRoZSBKdW5jdGlvbiBTb3V0aCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzBhYjdiOGRiZjg3MTRkMDViYTQyZDljZjQyMzIzNzg2LnNldENvbnRlbnQoaHRtbF9jOGEwZWQ2YzU1NmU0MmZiYTM3YzM1OGJlNDNjMmY3Mik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kMWE5ZmI3YTQ5NTE0OWVmYjQ2NGVhOGE0YzBjYThmMC5iaW5kUG9wdXAocG9wdXBfMGFiN2I4ZGJmODcxNGQwNWJhNDJkOWNmNDIzMjM3ODYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZGQzZmQ1MWE0OGYxNDlhMDgzMGZmMDE0YzVhODU1NzMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDg5NTk3LC03OS40NTYzMjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjk5N2JhMjkwODNlNGYzOTg0N2I1MTRiMjdlMmUwNDYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDY2NTM5ZjgwYTM3NGQxZGE0ZGMzYzFlMGM3MzNlMzYgPSAkKCc8ZGl2IGlkPSJodG1sXzA2NjUzOWY4MGEzNzRkMWRhNGRjM2MxZTBjNzMzZTM2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrZGFsZSxSb25jZXN2YWxsZXMgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82OTk3YmEyOTA4M2U0ZjM5ODQ3YjUxNGIyN2UyZTA0Ni5zZXRDb250ZW50KGh0bWxfMDY2NTM5ZjgwYTM3NGQxZGE0ZGMzYzFlMGM3MzNlMzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGQzZmQ1MWE0OGYxNDlhMDgzMGZmMDE0YzVhODU1NzMuYmluZFBvcHVwKHBvcHVwXzY5OTdiYTI5MDgzZTRmMzk4NDdiNTE0YjI3ZTJlMDQ2KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzExZTE3YjA4OGVhOTQ0NTE4YTMyYjI5YTc3NWRjOGEzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUxNTcwNiwtNzkuNDg0NDQ5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84ZGQxZDJmNzNjYjM0YWYyYjEwMzU4NzM3NDQyM2Q5NyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yYzdmNGU2MDRmNzY0MmQxOTdiZDNlZTVjNGJlMDRkOCA9ICQoJzxkaXYgaWQ9Imh0bWxfMmM3ZjRlNjA0Zjc2NDJkMTk3YmQzZWU1YzRiZTA0ZDgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJ1bm55bWVkZSxTd2Fuc2VhIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGRkMWQyZjczY2IzNGFmMmIxMDM1ODczNzQ0MjNkOTcuc2V0Q29udGVudChodG1sXzJjN2Y0ZTYwNGY3NjQyZDE5N2JkM2VlNWM0YmUwNGQ4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzExZTE3YjA4OGVhOTQ0NTE4YTMyYjI5YTc3NWRjOGEzLmJpbmRQb3B1cChwb3B1cF84ZGQxZDJmNzNjYjM0YWYyYjEwMzU4NzM3NDQyM2Q5Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xYzE5N2Y0NTc0YmQ0ZjIxYjhjYTdmNWYwMWFkYWY3YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MjMwMTUsLTc5LjM4OTQ5MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDg2N2EyNzY0YWZlNGZhMmI5ZDRlMTdjN2RiOWJhNWQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDJlMTQ5YzU2ZDI2NDhjMGExYjljMjgzYjM0MWIxMjkgPSAkKCc8ZGl2IGlkPSJodG1sX2QyZTE0OWM1NmQyNjQ4YzBhMWI5YzI4M2IzNDFiMTI5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5RdWVlbiYjMzk7cyBQYXJrIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDg2N2EyNzY0YWZlNGZhMmI5ZDRlMTdjN2RiOWJhNWQuc2V0Q29udGVudChodG1sX2QyZTE0OWM1NmQyNjQ4YzBhMWI5YzI4M2IzNDFiMTI5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFjMTk3ZjQ1NzRiZDRmMjFiOGNhN2Y1ZjAxYWRhZjdhLmJpbmRQb3B1cChwb3B1cF9kODY3YTI3NjRhZmU0ZmEyYjlkNGUxN2M3ZGI5YmE1ZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jZGI3OTI4OGFiM2I0MzZkOGVlZmYwOGQyMDFmYzA0ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYzNjk2NTYsLTc5LjYxNTgxODk5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2RiY2YzZWNlN2RlZDQyN2Y4OGVmNGNjYjc0ZTRkZjIwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzM1YzBmZmVjYjVlMjQ0MGI4MzhjYWQyMDdlNTdkNzExID0gJCgnPGRpdiBpZD0iaHRtbF8zNWMwZmZlY2I1ZTI0NDBiODM4Y2FkMjA3ZTU3ZDcxMSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FuYWRhIFBvc3QgR2F0ZXdheSBQcm9jZXNzaW5nIENlbnRyZSBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RiY2YzZWNlN2RlZDQyN2Y4OGVmNGNjYjc0ZTRkZjIwLnNldENvbnRlbnQoaHRtbF8zNWMwZmZlY2I1ZTI0NDBiODM4Y2FkMjA3ZTU3ZDcxMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jZGI3OTI4OGFiM2I0MzZkOGVlZmYwOGQyMDFmYzA0ZS5iaW5kUG9wdXAocG9wdXBfZGJjZjNlY2U3ZGVkNDI3Zjg4ZWY0Y2NiNzRlNGRmMjApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjRhZTJmZTdjMzBhNDQ5OThiZTc1YjI2Nzg4ZDllOWIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjI3NDM5LC03OS4zMjE1NThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWMxNjhhNzEwMTA5NGQyNDgyZDk4NTE4MTkyZmVmOWYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGVlYmU1ODUyMDU0NDkzOWEwNDYyZmNmMzcyNGQ5MDEgPSAkKCc8ZGl2IGlkPSJodG1sXzhlZWJlNTg1MjA1NDQ5MzlhMDQ2MmZjZjM3MjRkOTAxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CdXNpbmVzcyBSZXBseSBNYWlsIFByb2Nlc3NpbmcgQ2VudHJlIDk2OSBFYXN0ZXJuIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWMxNjhhNzEwMTA5NGQyNDgyZDk4NTE4MTkyZmVmOWYuc2V0Q29udGVudChodG1sXzhlZWJlNTg1MjA1NDQ5MzlhMDQ2MmZjZjM3MjRkOTAxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2I0YWUyZmU3YzMwYTQ0OTk4YmU3NWIyNjc4OGQ5ZTliLmJpbmRQb3B1cChwb3B1cF8xYzE2OGE3MTAxMDk0ZDI0ODJkOTg1MTgxOTJmZWY5Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yY2IyN2IwZWM5OWU0MTI2ODEyMzQyMzRjNzc5YjUyZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYwNTY0NjYsLTc5LjUwMTMyMDcwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2ExM2I2MjMzMTE1ZTQ2MWI4ZTMxNTc5OTRiZWY4YzJiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNkYzFjMjYyYWJmYjRlZWM4MGFhMTg1ZTIwZDcyMDIwID0gJCgnPGRpdiBpZD0iaHRtbF8zZGMxYzI2MmFiZmI0ZWVjODBhYTE4NWUyMGQ3MjAyMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtYmVyIEJheSBTaG9yZXMsTWltaWNvIFNvdXRoLE5ldyBUb3JvbnRvIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTEzYjYyMzMxMTVlNDYxYjhlMzE1Nzk5NGJlZjhjMmIuc2V0Q29udGVudChodG1sXzNkYzFjMjYyYWJmYjRlZWM4MGFhMTg1ZTIwZDcyMDIwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJjYjI3YjBlYzk5ZTQxMjY4MTIzNDIzNGM3NzliNTJlLmJpbmRQb3B1cChwb3B1cF9hMTNiNjIzMzExNWU0NjFiOGUzMTU3OTk0YmVmOGMyYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yZGUwYTViYTNhNTk0YzRmODViNGE4YjQ2YTA1N2Q5MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYwMjQxMzcwMDAwMDAxLC03OS41NDM0ODQwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMjkzMjg3ODZlNTY0NTczOWUwNDc0N2ZjMTk3NTEwMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80MmNlOWM1OThmY2Q0NmNmYWU2NGQ5MzA3MmU4YzBmZSA9ICQoJzxkaXYgaWQ9Imh0bWxfNDJjZTljNTk4ZmNkNDZjZmFlNjRkOTMwNzJlOGMwZmUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFsZGVyd29vZCxMb25nIEJyYW5jaCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2YyOTMyODc4NmU1NjQ1NzM5ZTA0NzQ3ZmMxOTc1MTAxLnNldENvbnRlbnQoaHRtbF80MmNlOWM1OThmY2Q0NmNmYWU2NGQ5MzA3MmU4YzBmZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yZGUwYTViYTNhNTk0YzRmODViNGE4YjQ2YTA1N2Q5MC5iaW5kUG9wdXAocG9wdXBfZjI5MzI4Nzg2ZTU2NDU3MzllMDQ3NDdmYzE5NzUxMDEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDEwNmZjZDA1NWIzNDgwMDk2YzZmNTBiY2E4OTEwNzggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTM2NTM2MDAwMDAwMDUsLTc5LjUwNjk0MzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTBhODkyMzY1OTMzNDllM2EzY2U3ZDFmYTAwY2FkODggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTkwMzRmOWZkNzJmNDg1MWI0MDhhMDAyZmVkODFiZWIgPSAkKCc8ZGl2IGlkPSJodG1sXzU5MDM0ZjlmZDcyZjQ4NTFiNDA4YTAwMmZlZDgxYmViIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgS2luZ3N3YXksTW9udGdvbWVyeSBSb2FkLE9sZCBNaWxsIE5vcnRoIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNTBhODkyMzY1OTMzNDllM2EzY2U3ZDFmYTAwY2FkODguc2V0Q29udGVudChodG1sXzU5MDM0ZjlmZDcyZjQ4NTFiNDA4YTAwMmZlZDgxYmViKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzAxMDZmY2QwNTViMzQ4MDA5NmM2ZjUwYmNhODkxMDc4LmJpbmRQb3B1cChwb3B1cF81MGE4OTIzNjU5MzM0OWUzYTNjZTdkMWZhMDBjYWQ4OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83YTgxMzY1YjFlYTc0NTdhYmE2YTk0YmRiNmZlNzk4MCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYzNjI1NzksLTc5LjQ5ODUwOTA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzlhZjY1M2RmNjE0NDQ4YWNiNWYxODUzNTEyMjliYjUxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzE0NmU0ZmQwY2NlNjRjNmViMjQyYTkzMzlkN2Y4NDJlID0gJCgnPGRpdiBpZD0iaHRtbF8xNDZlNGZkMGNjZTY0YzZlYjI0MmE5MzM5ZDdmODQyZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtYmVyIEJheSxLaW5nJiMzOTtzIE1pbGwgUGFyayxLaW5nc3dheSBQYXJrIFNvdXRoIEVhc3QsTWltaWNvIE5FLE9sZCBNaWxsIFNvdXRoLFRoZSBRdWVlbnN3YXkgRWFzdCxSb3lhbCBZb3JrIFNvdXRoIEVhc3QsU3VubnlsZWEgQ2x1c3RlciA0PC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85YWY2NTNkZjYxNDQ0OGFjYjVmMTg1MzUxMjI5YmI1MS5zZXRDb250ZW50KGh0bWxfMTQ2ZTRmZDBjY2U2NGM2ZWIyNDJhOTMzOWQ3Zjg0MmUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2E4MTM2NWIxZWE3NDU3YWJhNmE5NGJkYjZmZTc5ODAuYmluZFBvcHVwKHBvcHVwXzlhZjY1M2RmNjE0NDQ4YWNiNWYxODUzNTEyMjliYjUxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzE2YWJhYzMzODBlZTQwYWY4YTNhOWM3YmExOTExYjMyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjI4ODQwOCwtNzkuNTIwOTk5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNGM2NjE5YmY1YTU4NDY4NTk2ZjYzMjQzOWQxZDgyODcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGFkZWY1MmYzMDM0NDllODg4N2VkZjlkMTNiZTJhMzQgPSAkKCc8ZGl2IGlkPSJodG1sXzRhZGVmNTJmMzAzNDQ5ZTg4ODdlZGY5ZDEzYmUyYTM0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc3dheSBQYXJrIFNvdXRoIFdlc3QsTWltaWNvIE5XLFRoZSBRdWVlbnN3YXkgV2VzdCxSb3lhbCBZb3JrIFNvdXRoIFdlc3QsU291dGggb2YgQmxvb3IgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80YzY2MTliZjVhNTg0Njg1OTZmNjMyNDM5ZDFkODI4Ny5zZXRDb250ZW50KGh0bWxfNGFkZWY1MmYzMDM0NDllODg4N2VkZjlkMTNiZTJhMzQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTZhYmFjMzM4MGVlNDBhZjhhM2E5YzdiYTE5MTFiMzIuYmluZFBvcHVwKHBvcHVwXzRjNjYxOWJmNWE1ODQ2ODU5NmY2MzI0MzlkMWQ4Mjg3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzY1OTUzOWI0Njk4YzQyNTRhM2EyM2MyMjE4OGI2ZTY5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQzNTE1MiwtNzkuNTc3MjAwNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzQ5N2NlOTMwZjJiNDNiZDg3MmVlNjRjZGFjODU3MDUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjUyNTlkZjY0YzRiNDZlYzkyMWMxZDU2ZDQ3NTEzNTMgPSAkKCc8ZGl2IGlkPSJodG1sXzI1MjU5ZGY2NGM0YjQ2ZWM5MjFjMWQ1NmQ0NzUxMzUzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CbG9vcmRhbGUgR2FyZGVucyxFcmluZ2F0ZSxNYXJrbGFuZCBXb29kLE9sZCBCdXJuaGFtdGhvcnBlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzQ5N2NlOTMwZjJiNDNiZDg3MmVlNjRjZGFjODU3MDUuc2V0Q29udGVudChodG1sXzI1MjU5ZGY2NGM0YjQ2ZWM5MjFjMWQ1NmQ0NzUxMzUzKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzY1OTUzOWI0Njk4YzQyNTRhM2EyM2MyMjE4OGI2ZTY5LmJpbmRQb3B1cChwb3B1cF8zNDk3Y2U5MzBmMmI0M2JkODcyZWU2NGNkYWM4NTcwNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yZGI4NTEwNjFkZTA0ZGQyOWY3ZTRhODkyODkwYzU4YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1NjMwMzMsLTc5LjU2NTk2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2QyNGI0NDM2ZmJlZjQwNTRhODU5YjBmOGU1Mzc2NjM2ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzBjMmE3MDczNmMyMjQxZjliYTQwYmIwZjljMjk1ZmYzID0gJCgnPGRpdiBpZD0iaHRtbF8wYzJhNzA3MzZjMjI0MWY5YmE0MGJiMGY5YzI5NWZmMyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtYmVyIFN1bW1pdCBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2QyNGI0NDM2ZmJlZjQwNTRhODU5YjBmOGU1Mzc2NjM2LnNldENvbnRlbnQoaHRtbF8wYzJhNzA3MzZjMjI0MWY5YmE0MGJiMGY5YzI5NWZmMyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yZGI4NTEwNjFkZTA0ZGQyOWY3ZTRhODkyODkwYzU4YS5iaW5kUG9wdXAocG9wdXBfZDI0YjQ0MzZmYmVmNDA1NGE4NTliMGY4ZTUzNzY2MzYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzYzZDNmNGU2ZTg5NDY3ZTk3ZGE1ODI3OTdjM2IwN2EgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MjQ3NjU5LC03OS41MzIyNDI0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODBmZmI0IiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwZmZiNCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF81NGY1ZmI5YmY0OTI0MDJmYjBhNWJjOWQzZTE2NWY3NCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85ZGNkZjg1YjRiN2M0OTZjOTczMTNkZjkyY2VjMWUyNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kYjMwNGNhNmI1OWY0MTgxOTgzODk4OTE2MjJhZDU5NSA9ICQoJzxkaXYgaWQ9Imh0bWxfZGIzMDRjYTZiNTlmNDE4MTk4Mzg5ODkxNjIyYWQ1OTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVtZXJ5LEh1bWJlcmxlYSBDbHVzdGVyIDM8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzlkY2RmODViNGI3YzQ5NmM5NzMxM2RmOTJjZWMxZTI1LnNldENvbnRlbnQoaHRtbF9kYjMwNGNhNmI1OWY0MTgxOTgzODk4OTE2MjJhZDU5NSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83NjNkM2Y0ZTZlODk0NjdlOTdkYTU4Mjc5N2MzYjA3YS5iaW5kUG9wdXAocG9wdXBfOWRjZGY4NWI0YjdjNDk2Yzk3MzEzZGY5MmNlYzFlMjUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmIzMjA3YWIzZTU3NDBhZDgyYjZjZGVkMWQ2OWFlZGEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MDY4NzYsLTc5LjUxODE4ODQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzU4OWFjZDRiYmM2YzQ4MmE4MjA5YjkxZWQ4YWQwNjlmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY3ZWZhMGYxZWQ2MjQzMDI5Mzk1MjkyNDE4MzVlNzU1ID0gJCgnPGRpdiBpZD0iaHRtbF82N2VmYTBmMWVkNjI0MzAyOTM5NTI5MjQxODM1ZTc1NSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2VzdG9uIENsdXN0ZXIgNDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNTg5YWNkNGJiYzZjNDgyYTgyMDliOTFlZDhhZDA2OWYuc2V0Q29udGVudChodG1sXzY3ZWZhMGYxZWQ2MjQzMDI5Mzk1MjkyNDE4MzVlNzU1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZiMzIwN2FiM2U1NzQwYWQ4MmI2Y2RlZDFkNjlhZWRhLmJpbmRQb3B1cChwb3B1cF81ODlhY2Q0YmJjNmM0ODJhODIwOWI5MWVkOGFkMDY5Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iNjA0MTA5ZGY4ZmI0YjZmYmU3MzlkM2E5MDlkYjMwNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5NjMxOSwtNzkuNTMyMjQyNDAwMDAwMDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZWMyOWVjOGZlMjVjNGQzMDkzYzk0OWEwOGYyZGY0MTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfY2IwYzA2M2IxNzczNDUyNWIyNjVhZjNjNTc0YmExNjAgPSAkKCc8ZGl2IGlkPSJodG1sX2NiMGMwNjNiMTc3MzQ1MjViMjY1YWYzYzU3NGJhMTYwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0bW91bnQgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lYzI5ZWM4ZmUyNWM0ZDMwOTNjOTQ5YTA4ZjJkZjQxOC5zZXRDb250ZW50KGh0bWxfY2IwYzA2M2IxNzczNDUyNWIyNjVhZjNjNTc0YmExNjApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjYwNDEwOWRmOGZiNGI2ZmJlNzM5ZDNhOTA5ZGIzMDYuYmluZFBvcHVwKHBvcHVwX2VjMjllYzhmZTI1YzRkMzA5M2M5NDlhMDhmMmRmNDE4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2E4MWYwZDRkZDljMjQxZTdhYzcxODY2Nzk2NGZlYjNhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg4OTA1NCwtNzkuNTU0NzI0NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmYjM2MCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZmIzNjAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDAzOGUxYmMyMjlkNDliZDhhNjk1ZmQwYzFkMTA1NjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTUxNDQ3NTNhY2Y4NDA0YWEyMDU0MmIyZWYxMTAyNzIgPSAkKCc8ZGl2IGlkPSJodG1sXzU1MTQ0NzUzYWNmODQwNGFhMjA1NDJiMmVmMTEwMjcyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc3ZpZXcgVmlsbGFnZSxNYXJ0aW4gR3JvdmUgR2FyZGVucyxSaWNodmlldyBHYXJkZW5zLFN0LiBQaGlsbGlwcyBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzAwMzhlMWJjMjI5ZDQ5YmQ4YTY5NWZkMGMxZDEwNTY1LnNldENvbnRlbnQoaHRtbF81NTE0NDc1M2FjZjg0MDRhYTIwNTQyYjJlZjExMDI3Mik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hODFmMGQ0ZGQ5YzI0MWU3YWM3MTg2Njc5NjRmZWIzYS5iaW5kUG9wdXAocG9wdXBfMDAzOGUxYmMyMjlkNDliZDhhNjk1ZmQwYzFkMTA1NjUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTk0OGFkZWM4OWU5NDZhNDkzMjQzYjU3YmExYzgzMzQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Mzk0MTYzOTk5OTk5OTYsLTc5LjU4ODQzNjldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfNTRmNWZiOWJmNDkyNDAyZmIwYTViYzlkM2UxNjVmNzQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfY2RjZmExMzI5NTgzNGY3NzhjNTM3ZDBkZmU4MTYyMDAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjljY2M1NTg0MDVmNDdlZWE3MjFkODg5NjBhYTg3M2EgPSAkKCc8ZGl2IGlkPSJodG1sXzY5Y2NjNTU4NDA1ZjQ3ZWVhNzIxZDg4OTYwYWE4NzNhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BbGJpb24gR2FyZGVucyxCZWF1bW9uZCBIZWlnaHRzLEh1bWJlcmdhdGUsSmFtZXN0b3duLE1vdW50IE9saXZlLFNpbHZlcnN0b25lLFNvdXRoIFN0ZWVsZXMsVGhpc3RsZXRvd24gQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jZGNmYTEzMjk1ODM0Zjc3OGM1MzdkMGRmZTgxNjIwMC5zZXRDb250ZW50KGh0bWxfNjljY2M1NTg0MDVmNDdlZWE3MjFkODg5NjBhYTg3M2EpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTk0OGFkZWM4OWU5NDZhNDkzMjQzYjU3YmExYzgzMzQuYmluZFBvcHVwKHBvcHVwX2NkY2ZhMTMyOTU4MzRmNzc4YzUzN2QwZGZlODE2MjAwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2VhYTNkMjViYWQ1NzQ5M2FhNTA1OGJkNDgwNDdjMzBhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA2NzQ4Mjk5OTk5OTk0LC03OS41OTQwNTQ0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzU0ZjVmYjliZjQ5MjQwMmZiMGE1YmM5ZDNlMTY1Zjc0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2UyNDFiMWVmNzE3OTRmMDU4ZTVkZmM2MTNkZDJmODBkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzVhNTI2NmRmMDZjOTQ2ODhiZWI5ZjIwODJkZjlhNDFiID0gJCgnPGRpdiBpZD0iaHRtbF81YTUyNjZkZjA2Yzk0Njg4YmViOWYyMDgyZGY5YTQxYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Tm9ydGh3ZXN0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTI0MWIxZWY3MTc5NGYwNThlNWRmYzYxM2RkMmY4MGQuc2V0Q29udGVudChodG1sXzVhNTI2NmRmMDZjOTQ2ODhiZWI5ZjIwODJkZjlhNDFiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2VhYTNkMjViYWQ1NzQ5M2FhNTA1OGJkNDgwNDdjMzBhLmJpbmRQb3B1cChwb3B1cF9lMjQxYjFlZjcxNzk0ZjA1OGU1ZGZjNjEzZGQyZjgwZCk7CgogICAgICAgICAgICAKICAgICAgICAKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



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
