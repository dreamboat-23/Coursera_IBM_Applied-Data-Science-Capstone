# Segmentation and Clustering
Firstly, I downloaded the data into an excel file.


```python
#Importing libraries
!conda install -c anaconda xlrd --yes
```

    Solving environment: done
    
    
    ==> WARNING: A newer version of conda exists. <==
      current version: 4.5.11
      latest version: 4.7.12
    
    Please update conda by running
    
        $ conda update -n base -c defaults conda
    
    
    
    ## Package Plan ##
    
      environment location: /home/jupyterlab/conda/envs/python
    
      added / updated specs: 
        - xlrd
    
    
    The following packages will be downloaded:
    
        package                    |            build
        ---------------------------|-----------------
        openssl-1.1.1              |       h7b6447c_0         5.0 MB  anaconda
        certifi-2019.9.11          |           py36_0         154 KB  anaconda
        xlrd-1.2.0                 |           py36_0         188 KB  anaconda
        ------------------------------------------------------------
                                               Total:         5.4 MB
    
    The following packages will be UPDATED:
    
        certifi: 2019.6.16-py36_1  conda-forge --> 2019.9.11-py36_0 anaconda
        openssl: 1.1.1c-h516909a_0 conda-forge --> 1.1.1-h7b6447c_0 anaconda
        xlrd:    1.1.0-py37_1                  --> 1.2.0-py36_0     anaconda
    
    
    Downloading and Extracting Packages
    openssl-1.1.1        | 5.0 MB    | ##################################### | 100% 
    certifi-2019.9.11    | 154 KB    | ##################################### | 100% 
    xlrd-1.2.0           | 188 KB    | ##################################### | 100% 
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done


# Importing the libraries


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


```python
df = pd.read_excel(r'Canada neighborhood data.xlsx')
```

Let us examine what our data frame looks like:


```python
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
      <td>0</td>
      <td>M1A</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>1</td>
      <td>M2A</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>2</td>
      <td>M3A</td>
      <td>North York</td>
      <td>Parkwoods</td>
    </tr>
    <tr>
      <td>3</td>
      <td>M4A</td>
      <td>North York</td>
      <td>Victoria Village</td>
    </tr>
    <tr>
      <td>4</td>
      <td>M5A</td>
      <td>Downtown Toronto</td>
      <td>Harbourfront</td>
    </tr>
    <tr>
      <td>5</td>
      <td>M5A</td>
      <td>Downtown Toronto</td>
      <td>Regent Park</td>
    </tr>
    <tr>
      <td>6</td>
      <td>M6A</td>
      <td>North York</td>
      <td>Lawrence Heights</td>
    </tr>
    <tr>
      <td>7</td>
      <td>M6A</td>
      <td>North York</td>
      <td>Lawrence Manor</td>
    </tr>
    <tr>
      <td>8</td>
      <td>M7A</td>
      <td>Queen's Park</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>9</td>
      <td>M8A</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>10</td>
      <td>M9A</td>
      <td>Etobicoke</td>
      <td>Islington Avenue</td>
    </tr>
    <tr>
      <td>11</td>
      <td>M1B</td>
      <td>Scarborough</td>
      <td>Rouge</td>
    </tr>
  </tbody>
</table>
</div>



Evaluating for missing data


```python
missing_data = df.isnull()
missing_data.head(5)
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
      <td>0</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>1</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <td>2</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>3</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <td>4</td>
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
    


As we can see from above, we will drop the 77 true values that are missing in Borough column.


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
      <td>0</td>
      <td>M3A</td>
      <td>North York</td>
      <td>Parkwoods</td>
    </tr>
    <tr>
      <td>1</td>
      <td>M4A</td>
      <td>North York</td>
      <td>Victoria Village</td>
    </tr>
    <tr>
      <td>2</td>
      <td>M5A</td>
      <td>Downtown Toronto</td>
      <td>Harbourfront</td>
    </tr>
    <tr>
      <td>3</td>
      <td>M5A</td>
      <td>Downtown Toronto</td>
      <td>Regent Park</td>
    </tr>
    <tr>
      <td>4</td>
      <td>M6A</td>
      <td>North York</td>
      <td>Lawrence Heights</td>
    </tr>
    <tr>
      <td>5</td>
      <td>M6A</td>
      <td>North York</td>
      <td>Lawrence Manor</td>
    </tr>
    <tr>
      <td>6</td>
      <td>M7A</td>
      <td>Queen's Park</td>
      <td>NaN</td>
    </tr>
    <tr>
      <td>7</td>
      <td>M9A</td>
      <td>Etobicoke</td>
      <td>Islington Avenue</td>
    </tr>
    <tr>
      <td>8</td>
      <td>M1B</td>
      <td>Scarborough</td>
      <td>Rouge</td>
    </tr>
    <tr>
      <td>9</td>
      <td>M1B</td>
      <td>Scarborough</td>
      <td>Malvern</td>
    </tr>
    <tr>
      <td>10</td>
      <td>M3B</td>
      <td>North York</td>
      <td>Don Mills North</td>
    </tr>
    <tr>
      <td>11</td>
      <td>M4B</td>
      <td>East York</td>
      <td>Woodbine Gardens</td>
    </tr>
  </tbody>
</table>
</div>



Assign missing neighborhoods to name of corresponding borough


```python
df['Neighbourhood'].replace(np.nan, df['Borough'], inplace=True)
```


```python
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
      <td>0</td>
      <td>M3A</td>
      <td>North York</td>
      <td>Parkwoods</td>
    </tr>
    <tr>
      <td>1</td>
      <td>M4A</td>
      <td>North York</td>
      <td>Victoria Village</td>
    </tr>
    <tr>
      <td>2</td>
      <td>M5A</td>
      <td>Downtown Toronto</td>
      <td>Harbourfront</td>
    </tr>
    <tr>
      <td>3</td>
      <td>M5A</td>
      <td>Downtown Toronto</td>
      <td>Regent Park</td>
    </tr>
    <tr>
      <td>4</td>
      <td>M6A</td>
      <td>North York</td>
      <td>Lawrence Heights</td>
    </tr>
    <tr>
      <td>5</td>
      <td>M6A</td>
      <td>North York</td>
      <td>Lawrence Manor</td>
    </tr>
    <tr>
      <td>6</td>
      <td>M7A</td>
      <td>Queen's Park</td>
      <td>Queen's Park</td>
    </tr>
    <tr>
      <td>7</td>
      <td>M9A</td>
      <td>Etobicoke</td>
      <td>Islington Avenue</td>
    </tr>
    <tr>
      <td>8</td>
      <td>M1B</td>
      <td>Scarborough</td>
      <td>Rouge</td>
    </tr>
    <tr>
      <td>9</td>
      <td>M1B</td>
      <td>Scarborough</td>
      <td>Malvern</td>
    </tr>
    <tr>
      <td>10</td>
      <td>M3B</td>
      <td>North York</td>
      <td>Don Mills North</td>
    </tr>
    <tr>
      <td>11</td>
      <td>M4B</td>
      <td>East York</td>
      <td>Woodbine Gardens</td>
    </tr>
  </tbody>
</table>
</div>



Group neighborhoods by Postcode


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
      <td>0</td>
      <td>M1B</td>
      <td>Scarborough</td>
      <td>Rouge,Malvern</td>
    </tr>
    <tr>
      <td>1</td>
      <td>M1C</td>
      <td>Scarborough</td>
      <td>Highland Creek,Rouge Hill,Port Union</td>
    </tr>
    <tr>
      <td>2</td>
      <td>M1E</td>
      <td>Scarborough</td>
      <td>Guildwood,Morningside,West Hill</td>
    </tr>
    <tr>
      <td>3</td>
      <td>M1G</td>
      <td>Scarborough</td>
      <td>Woburn</td>
    </tr>
    <tr>
      <td>4</td>
      <td>M1H</td>
      <td>Scarborough</td>
      <td>Cedarbrae</td>
    </tr>
    <tr>
      <td>5</td>
      <td>M1J</td>
      <td>Scarborough</td>
      <td>Scarborough Village</td>
    </tr>
    <tr>
      <td>6</td>
      <td>M1K</td>
      <td>Scarborough</td>
      <td>East Birchmount Park,Ionview,Kennedy Park</td>
    </tr>
    <tr>
      <td>7</td>
      <td>M1L</td>
      <td>Scarborough</td>
      <td>Clairlea,Golden Mile,Oakridge</td>
    </tr>
    <tr>
      <td>8</td>
      <td>M1M</td>
      <td>Scarborough</td>
      <td>Cliffcrest,Cliffside,Scarborough Village West</td>
    </tr>
    <tr>
      <td>9</td>
      <td>M1N</td>
      <td>Scarborough</td>
      <td>Birch Cliff,Cliffside West</td>
    </tr>
    <tr>
      <td>10</td>
      <td>M1P</td>
      <td>Scarborough</td>
      <td>Dorset Park,Scarborough Town Centre,Wexford He...</td>
    </tr>
    <tr>
      <td>11</td>
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



The data frame has 103 columns and 3 rows!

# Geo-coding Exercise

Using the CSV data to merge it to the the cleaned table from the previous section. First examine what the data frame looks like. 


```python
filepath = "https://cocl.us/Geospatial_data"
df_3 = pd.read_csv('https://cocl.us/Geospatial_data')
```


```python
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
      <td>0</td>
      <td>M1B</td>
      <td>43.806686</td>
      <td>-79.194353</td>
    </tr>
    <tr>
      <td>1</td>
      <td>M1C</td>
      <td>43.784535</td>
      <td>-79.160497</td>
    </tr>
    <tr>
      <td>2</td>
      <td>M1E</td>
      <td>43.763573</td>
      <td>-79.188711</td>
    </tr>
    <tr>
      <td>3</td>
      <td>M1G</td>
      <td>43.770992</td>
      <td>-79.216917</td>
    </tr>
    <tr>
      <td>4</td>
      <td>M1H</td>
      <td>43.773136</td>
      <td>-79.239476</td>
    </tr>
  </tbody>
</table>
</div>



Rename the field "Postal Code" to Postcode to match the previous section


```python
df_3.rename(columns={'Postal Code': 'Postcode'}, inplace=True)
```

Merge the two data sets to get the required 5 column data frame


```python
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
      <td>0</td>
      <td>M1B</td>
      <td>43.806686</td>
      <td>-79.194353</td>
      <td>Scarborough</td>
      <td>Rouge,Malvern</td>
    </tr>
    <tr>
      <td>1</td>
      <td>M1C</td>
      <td>43.784535</td>
      <td>-79.160497</td>
      <td>Scarborough</td>
      <td>Highland Creek,Rouge Hill,Port Union</td>
    </tr>
    <tr>
      <td>2</td>
      <td>M1E</td>
      <td>43.763573</td>
      <td>-79.188711</td>
      <td>Scarborough</td>
      <td>Guildwood,Morningside,West Hill</td>
    </tr>
    <tr>
      <td>3</td>
      <td>M1G</td>
      <td>43.770992</td>
      <td>-79.216917</td>
      <td>Scarborough</td>
      <td>Woburn</td>
    </tr>
    <tr>
      <td>4</td>
      <td>M1H</td>
      <td>43.773136</td>
      <td>-79.239476</td>
      <td>Scarborough</td>
      <td>Cedarbrae</td>
    </tr>
  </tbody>
</table>
</div>



Fixing the column order


```python
column_order = ['Postcode',
 'Borough',
 'Neighbourhood',
 'Latitude',
 'Longitude']
column_order
```




    ['Postcode', 'Borough', 'Neighbourhood', 'Latitude', 'Longitude']




```python
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
      <td>0</td>
      <td>M1B</td>
      <td>Scarborough</td>
      <td>Rouge,Malvern</td>
      <td>43.806686</td>
      <td>-79.194353</td>
    </tr>
    <tr>
      <td>1</td>
      <td>M1C</td>
      <td>Scarborough</td>
      <td>Highland Creek,Rouge Hill,Port Union</td>
      <td>43.784535</td>
      <td>-79.160497</td>
    </tr>
    <tr>
      <td>2</td>
      <td>M1E</td>
      <td>Scarborough</td>
      <td>Guildwood,Morningside,West Hill</td>
      <td>43.763573</td>
      <td>-79.188711</td>
    </tr>
    <tr>
      <td>3</td>
      <td>M1G</td>
      <td>Scarborough</td>
      <td>Woburn</td>
      <td>43.770992</td>
      <td>-79.216917</td>
    </tr>
    <tr>
      <td>4</td>
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

Import required libraries


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
    
    
    ==> WARNING: A newer version of conda exists. <==
      current version: 4.5.11
      latest version: 4.7.12
    
    Please update conda by running
    
        $ conda update -n base -c defaults conda
    
    
    
    ## Package Plan ##
    
      environment location: /home/jupyterlab/conda/envs/python
    
      added / updated specs: 
        - geopy
    
    
    The following packages will be downloaded:
    
        package                    |            build
        ---------------------------|-----------------
        geopy-1.20.0               |             py_0          57 KB  conda-forge
        geographiclib-1.50         |             py_0          34 KB  conda-forge
        certifi-2019.9.11          |           py36_0         147 KB  conda-forge
        ------------------------------------------------------------
                                               Total:         238 KB
    
    The following NEW packages will be INSTALLED:
    
        geographiclib: 1.50-py_0        conda-forge
        geopy:         1.20.0-py_0      conda-forge
    
    The following packages will be UPDATED:
    
        certifi:       2019.9.11-py36_0 anaconda    --> 2019.9.11-py36_0  conda-forge
    
    The following packages will be DOWNGRADED:
    
        openssl:       1.1.1-h7b6447c_0 anaconda    --> 1.1.1c-h516909a_0 conda-forge
    
    
    Downloading and Extracting Packages
    geopy-1.20.0         | 57 KB     | ##################################### | 100% 
    geographiclib-1.50   | 34 KB     | ##################################### | 100% 
    certifi-2019.9.11    | 147 KB    | ##################################### | 100% 
    Preparing transaction: done
    Verifying transaction: done
    Executing transaction: done
    Solving environment: done
    
    
    ==> WARNING: A newer version of conda exists. <==
      current version: 4.5.11
      latest version: 4.7.12
    
    Please update conda by running
    
        $ conda update -n base -c defaults conda
    
    
    
    # All requested packages already installed.
    
    Libraries imported.


Using Geopy library to get the latitude and longitude of Toronto, Canada


```python
address = 'Toronto, Ontario'

geolocator = Nominatim(user_agent="TO_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Toronto, Ontario are {}, {}.'.format(latitude, longitude))
```

    The geograpical coordinate of Toronto, Ontario are 43.653963, -79.387207.


# Map of Toronto Ontario with neighborhoods


```python
map_toronto = folium.Map(location=[latitude, longitude], zoom_start=10)

for lat, lng, borough, neighbourhood in zip(df_5['Latitude'], df_5['Longitude'], df_5['Borough'], df_5['Neighbourhood']):
    label = '{}, {}'.format(neighbourhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=4,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)  
    
map_toronto
```




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0IiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCcsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDMuNjUzOTYzLC03OS4zODcyMDddLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTAsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyXzNhOTBhOWQ1ZTg0YzQ4MDJiYTkzZWUyMjc5MDA5M2MxID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICJtYXhab29tIjogMTgsCiAgIm1pblpvb20iOiAxLAogICJub1dyYXAiOiBmYWxzZSwKICAic3ViZG9tYWlucyI6ICJhYmMiCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yYmYxYWJhNWJjZTY0ODgyYTcxYmRhMzIyYzFkYjQ2ZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjgwNjY4NjI5OTk5OTk5NiwtNzkuMTk0MzUzNDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTA0YWI4ZmY5ODU3NDc4YTg0NTQxYzAwY2Y0MGMyZmEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTY4MmM5NjIyNmViNDE0YTg5YzFmNzU2YjEyMGI5YjIgPSAkKCc8ZGl2IGlkPSJodG1sXzk2ODJjOTYyMjZlYjQxNGE4OWMxZjc1NmIxMjBiOWIyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3VnZSxNYWx2ZXJuLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTA0YWI4ZmY5ODU3NDc4YTg0NTQxYzAwY2Y0MGMyZmEuc2V0Q29udGVudChodG1sXzk2ODJjOTYyMjZlYjQxNGE4OWMxZjc1NmIxMjBiOWIyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJiZjFhYmE1YmNlNjQ4ODJhNzFiZGEzMjJjMWRiNDZkLmJpbmRQb3B1cChwb3B1cF8xMDRhYjhmZjk4NTc0NzhhODQ1NDFjMDBjZjQwYzJmYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yYjYzZWY3ZGNhNTc0MGZhYjhkZTgzNWU1MzNlMjVkYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4NDUzNTEsLTc5LjE2MDQ5NzA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzZkMDcyODUwMjI3NjQyODRiNjI2NzA1OTdlMzU0ZWRkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU0OTEwMGNkZDFiNzRjZThhYmIwMWNlNTU3NzM1ZWM2ID0gJCgnPGRpdiBpZD0iaHRtbF81NDkxMDBjZGQxYjc0Y2U4YWJiMDFjZTU1NzczNWVjNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaGxhbmQgQ3JlZWssUm91Z2UgSGlsbCxQb3J0IFVuaW9uLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmQwNzI4NTAyMjc2NDI4NGI2MjY3MDU5N2UzNTRlZGQuc2V0Q29udGVudChodG1sXzU0OTEwMGNkZDFiNzRjZThhYmIwMWNlNTU3NzM1ZWM2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzJiNjNlZjdkY2E1NzQwZmFiOGRlODM1ZTUzM2UyNWRjLmJpbmRQb3B1cChwb3B1cF82ZDA3Mjg1MDIyNzY0Mjg0YjYyNjcwNTk3ZTM1NGVkZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83MzdmMDQ4ODFjYmM0NmI3ODVjNzA2ZTU2NTFlNWM1MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc2MzU3MjYsLTc5LjE4ODcxMTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzU0OTgwNTc4NjljNDE3MGI4YjQxZWMzNjY5NmJjODIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjNlMjZlNTg0YzE2NDhhN2JiZmU0ZDgxN2EyODZkZWQgPSAkKCc8ZGl2IGlkPSJodG1sX2IzZTI2ZTU4NGMxNjQ4YTdiYmZlNGQ4MTdhMjg2ZGVkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HdWlsZHdvb2QsTW9ybmluZ3NpZGUsV2VzdCBIaWxsLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzU0OTgwNTc4NjljNDE3MGI4YjQxZWMzNjY5NmJjODIuc2V0Q29udGVudChodG1sX2IzZTI2ZTU4NGMxNjQ4YTdiYmZlNGQ4MTdhMjg2ZGVkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzczN2YwNDg4MWNiYzQ2Yjc4NWM3MDZlNTY1MWU1YzUxLmJpbmRQb3B1cChwb3B1cF8zNTQ5ODA1Nzg2OWM0MTcwYjhiNDFlYzM2Njk2YmM4Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80YmJlNjk5ZThlZWI0Mzg2YTJhZTM1YzQwZWE0YzI2MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MDk5MjEsLTc5LjIxNjkxNzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFhY2FhZWFhMDc1OTQ1MTk5NGVmMWMwM2Q4Zjc1MDhhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzYyMDQyYWZkNTdjZDQ1Nzk5ODJlZjgzYmFhOTY2N2FjID0gJCgnPGRpdiBpZD0iaHRtbF82MjA0MmFmZDU3Y2Q0NTc5OTgyZWY4M2JhYTk2NjdhYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V29idXJuLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWFjYWFlYWEwNzU5NDUxOTk0ZWYxYzAzZDhmNzUwOGEuc2V0Q29udGVudChodG1sXzYyMDQyYWZkNTdjZDQ1Nzk5ODJlZjgzYmFhOTY2N2FjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzRiYmU2OTllOGVlYjQzODZhMmFlMzVjNDBlYTRjMjYyLmJpbmRQb3B1cChwb3B1cF8xYWNhYWVhYTA3NTk0NTE5OTRlZjFjMDNkOGY3NTA4YSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wOTc0MTQ3ZDUzZTA0OTUwOTNmYTk3MjAyYWI2MDdmMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MzEzNiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTRjNTg5YzA1OTg5NDQ3OWE0NTQ0YmMzNjczNjdmNzIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGIyMWY2Y2NmOWRlNDEyOGFjOWQ1ODlhMmRlOTA1MzcgPSAkKCc8ZGl2IGlkPSJodG1sX2RiMjFmNmNjZjlkZTQxMjhhYzlkNTg5YTJkZTkwNTM3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZWRhcmJyYWUsIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hNGM1ODljMDU5ODk0NDc5YTQ1NDRiYzM2NzM2N2Y3Mi5zZXRDb250ZW50KGh0bWxfZGIyMWY2Y2NmOWRlNDEyOGFjOWQ1ODlhMmRlOTA1MzcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDk3NDE0N2Q1M2UwNDk1MDkzZmE5NzIwMmFiNjA3ZjIuYmluZFBvcHVwKHBvcHVwX2E0YzU4OWMwNTk4OTQ0NzlhNDU0NGJjMzY3MzY3ZjcyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2YwYzAxZDdkYWY1MjQwMjRiZTAzZTY1YmY3OGRiOTA4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ0NzM0MiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWUxYWFhMDJmMGJlNDcyOWJlMDJkZDhiMGY4NTdhMDggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYmU3Y2U5OWRmMTk5NDU1Yjk5ZDkyNzEzZTM0OGVlMTIgPSAkKCc8ZGl2IGlkPSJodG1sX2JlN2NlOTlkZjE5OTQ1NWI5OWQ5MjcxM2UzNDhlZTEyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TY2FyYm9yb3VnaCBWaWxsYWdlLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWUxYWFhMDJmMGJlNDcyOWJlMDJkZDhiMGY4NTdhMDguc2V0Q29udGVudChodG1sX2JlN2NlOTlkZjE5OTQ1NWI5OWQ5MjcxM2UzNDhlZTEyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2YwYzAxZDdkYWY1MjQwMjRiZTAzZTY1YmY3OGRiOTA4LmJpbmRQb3B1cChwb3B1cF9hZTFhYWEwMmYwYmU0NzI5YmUwMmRkOGIwZjg1N2EwOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83YjdjOTEyYjQ2NTQ0NzhmODZhY2ExNDdkMDlhYTA5YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNzkyOTIsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA5ODkzOGIzOTNlZjQ4MDFhOGQyNDYwYjk5ZTVhMjJiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2I2NDU2YzU4MGJjOTRjZGJiNTAwNmVjOWUyYWJmNmI5ID0gJCgnPGRpdiBpZD0iaHRtbF9iNjQ1NmM1ODBiYzk0Y2RiYjUwMDZlYzllMmFiZjZiOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdCBCaXJjaG1vdW50IFBhcmssSW9udmlldyxLZW5uZWR5IFBhcmssIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wOTg5MzhiMzkzZWY0ODAxYThkMjQ2MGI5OWU1YTIyYi5zZXRDb250ZW50KGh0bWxfYjY0NTZjNTgwYmM5NGNkYmI1MDA2ZWM5ZTJhYmY2YjkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2I3YzkxMmI0NjU0NDc4Zjg2YWNhMTQ3ZDA5YWEwOWMuYmluZFBvcHVwKHBvcHVwXzA5ODkzOGIzOTNlZjQ4MDFhOGQyNDYwYjk5ZTVhMjJiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzg2YjlkNWQ2NzRhZjQzZGJiMDlmYmI1YmZkMDU2NTJiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzExMTExNzAwMDAwMDA0LC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzE3MjAyYzZmZmFmYjRmZTE5MjQ2NTExYWFmYzcwYmM3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Q5YjM2ZjFhM2ZjNTRjZGRiYTE5M2QyNDk2NmQ0MGZhID0gJCgnPGRpdiBpZD0iaHRtbF9kOWIzNmYxYTNmYzU0Y2RkYmExOTNkMjQ5NjZkNDBmYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2xhaXJsZWEsR29sZGVuIE1pbGUsT2FrcmlkZ2UsIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xNzIwMmM2ZmZhZmI0ZmUxOTI0NjUxMWFhZmM3MGJjNy5zZXRDb250ZW50KGh0bWxfZDliMzZmMWEzZmM1NGNkZGJhMTkzZDI0OTY2ZDQwZmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODZiOWQ1ZDY3NGFmNDNkYmIwOWZiYjViZmQwNTY1MmIuYmluZFBvcHVwKHBvcHVwXzE3MjAyYzZmZmFmYjRmZTE5MjQ2NTExYWFmYzcwYmM3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U1ZjE5YTQxZjEyOTQwOGM4ZmZmMzJkM2UwYmJkNGJkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE2MzE2LC03OS4yMzk0NzYwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iNjUwYjZlOTdhNjY0NmY4OTgxM2U0NTMyZTNkNWUxNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lNTJhMmViMTJjNmI0YmZhYjdhMDI1MzE5Zjk1NTZmNCA9ICQoJzxkaXYgaWQ9Imh0bWxfZTUyYTJlYjEyYzZiNGJmYWI3YTAyNTMxOWY5NTU2ZjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsaWZmY3Jlc3QsQ2xpZmZzaWRlLFNjYXJib3JvdWdoIFZpbGxhZ2UgV2VzdCwgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2I2NTBiNmU5N2E2NjQ2Zjg5ODEzZTQ1MzJlM2Q1ZTE3LnNldENvbnRlbnQoaHRtbF9lNTJhMmViMTJjNmI0YmZhYjdhMDI1MzE5Zjk1NTZmNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNWYxOWE0MWYxMjk0MDhjOGZmZjMyZDNlMGJiZDRiZC5iaW5kUG9wdXAocG9wdXBfYjY1MGI2ZTk3YTY2NDZmODk4MTNlNDUzMmUzZDVlMTcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzZlNzZkNzhiOTQ4NGQ1NTkwMzE3NDZmM2EwODJkNWUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTI2NTcwMDAwMDAwMDQsLTc5LjI2NDg0ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDY4ZTAzZjgyMWVkNGU2ZWJiNzViMTYwMGRkZjcyOWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWI3NTI4YjJlOTAzNGZmNjkyZGIwNTc1M2Q0OGU3ODMgPSAkKCc8ZGl2IGlkPSJodG1sXzViNzUyOGIyZTkwMzRmZjY5MmRiMDU3NTNkNDhlNzgzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CaXJjaCBDbGlmZixDbGlmZnNpZGUgV2VzdCwgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q2OGUwM2Y4MjFlZDRlNmViYjc1YjE2MDBkZGY3MjlhLnNldENvbnRlbnQoaHRtbF81Yjc1MjhiMmU5MDM0ZmY2OTJkYjA1NzUzZDQ4ZTc4Myk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jNmU3NmQ3OGI5NDg0ZDU1OTAzMTc0NmYzYTA4MmQ1ZS5iaW5kUG9wdXAocG9wdXBfZDY4ZTAzZjgyMWVkNGU2ZWJiNzViMTYwMGRkZjcyOWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzI3OTk4MWU0OWQyNDQ5YmE2MjI1N2E5Y2YxMjRlZmMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTc0MDk2LC03OS4yNzMzMDQwMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lOWYwOGZhZjNhZjQ0N2RhYTljYjUxNWE5ZTgxODFlYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iMWY3ZTZkNzNhZDg0YzgxOGNiYjc1NWE1MzAwMWNlYiA9ICQoJzxkaXYgaWQ9Imh0bWxfYjFmN2U2ZDczYWQ4NGM4MThjYmI3NTVhNTMwMDFjZWIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvcnNldCBQYXJrLFNjYXJib3JvdWdoIFRvd24gQ2VudHJlLFdleGZvcmQgSGVpZ2h0cywgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2U5ZjA4ZmFmM2FmNDQ3ZGFhOWNiNTE1YTllODE4MWVjLnNldENvbnRlbnQoaHRtbF9iMWY3ZTZkNzNhZDg0YzgxOGNiYjc1NWE1MzAwMWNlYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jMjc5OTgxZTQ5ZDI0NDliYTYyMjU3YTljZjEyNGVmYy5iaW5kUG9wdXAocG9wdXBfZTlmMDhmYWYzYWY0NDdkYWE5Y2I1MTVhOWU4MTgxZWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZTk4ZmI4MjJiY2ZiNGEwNTkyYTgyZjY2Yjg5Y2YwMGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTAwNzE1MDAwMDAwMDQsLTc5LjI5NTg0OTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjQ0ZTI4ZmJkYmY2NGIwMjhjNjZlNTlkMThkYWYzMWYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTI5NThmNmFiMjM4NDcxNzgzZjZkZTgzYmFiOGRhODQgPSAkKCc8ZGl2IGlkPSJodG1sX2UyOTU4ZjZhYjIzODQ3MTc4M2Y2ZGU4M2JhYjhkYTg0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJ5dmFsZSxXZXhmb3JkLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjQ0ZTI4ZmJkYmY2NGIwMjhjNjZlNTlkMThkYWYzMWYuc2V0Q29udGVudChodG1sX2UyOTU4ZjZhYjIzODQ3MTc4M2Y2ZGU4M2JhYjhkYTg0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2U5OGZiODIyYmNmYjRhMDU5MmE4MmY2NmI4OWNmMDBiLmJpbmRQb3B1cChwb3B1cF82NDRlMjhmYmRiZjY0YjAyOGM2NmU1OWQxOGRhZjMxZik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wNTQ1NzA3OTQzMjg0OTI1OTc3YWU1NGIwODE4ZjM3OCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5NDIwMDMsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzgxNzk3ZDNkNmZlMjQxMDRhOGEwNjM1NzU0NDRhYTg4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNmMGI3OGMyMDM2ZDRjMWViMjAzMGNlNGFhM2ZmYjcwID0gJCgnPGRpdiBpZD0iaHRtbF8zZjBiNzhjMjAzNmQ0YzFlYjIwMzBjZTRhYTNmZmI3MCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0LCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODE3OTdkM2Q2ZmUyNDEwNGE4YTA2MzU3NTQ0NGFhODguc2V0Q29udGVudChodG1sXzNmMGI3OGMyMDM2ZDRjMWViMjAzMGNlNGFhM2ZmYjcwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzA1NDU3MDc5NDMyODQ5MjU5NzdhZTU0YjA4MThmMzc4LmJpbmRQb3B1cChwb3B1cF84MTc5N2QzZDZmZTI0MTA0YThhMDYzNTc1NDQ0YWE4OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jYWMzYmM0ODUxM2Y0NmI1OTZkMzExYzAwNTRmMTM0MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4MTYzNzUsLTc5LjMwNDMwMjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzFjOWZmYjVjODYxNDY3Zjk1MGFiNzY5ZDdmYzZiMjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDJlYzZiZjgxYTMyNDEzZDk2MjZkNGZjYzBkMDJiMmYgPSAkKCc8ZGl2IGlkPSJodG1sX2QyZWM2YmY4MWEzMjQxM2Q5NjI2ZDRmY2MwZDAyYjJmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGFya3MgQ29ybmVycyxTdWxsaXZhbixUYW0gTyYjMzk7U2hhbnRlciwgU2NhcmJvcm91Z2g8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2MxYzlmZmI1Yzg2MTQ2N2Y5NTBhYjc2OWQ3ZmM2YjI1LnNldENvbnRlbnQoaHRtbF9kMmVjNmJmODFhMzI0MTNkOTYyNmQ0ZmNjMGQwMmIyZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jYWMzYmM0ODUxM2Y0NmI1OTZkMzExYzAwNTRmMTM0MS5iaW5kUG9wdXAocG9wdXBfYzFjOWZmYjVjODYxNDY3Zjk1MGFiNzY5ZDdmYzZiMjUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDNkZDkwYzliZjk1NGYwMzkwY2U5ZTM2MDI1MWRkMDAgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My44MTUyNTIyLC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzNjNzMyNzQ4ZDc5YzQ2NjlhNDQwZDFmODhkZDViMTM3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzZhNTY0MTIwODU5OTRiMWU5ODhlMTAzZjNiMWI3ZTIwID0gJCgnPGRpdiBpZD0iaHRtbF82YTU2NDEyMDg1OTk0YjFlOTg4ZTEwM2YzYjFiN2UyMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0IE5vcnRoLEwmIzM5O0Ftb3JlYXV4IEVhc3QsTWlsbGlrZW4sU3RlZWxlcyBFYXN0LCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfM2M3MzI3NDhkNzljNDY2OWE0NDBkMWY4OGRkNWIxMzcuc2V0Q29udGVudChodG1sXzZhNTY0MTIwODU5OTRiMWU5ODhlMTAzZjNiMWI3ZTIwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzAzZGQ5MGM5YmY5NTRmMDM5MGNlOWUzNjAyNTFkZDAwLmJpbmRQb3B1cChwb3B1cF8zYzczMjc0OGQ3OWM0NjY5YTQ0MGQxZjg4ZGQ1YjEzNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mNDZlNjI3NDJjNDY0NDQwYjgyMDI0MTgxZWVkZjJmZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5OTUyNTIwMDAwMDAwNSwtNzkuMzE4Mzg4N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lMTNlNzZlMDIzZjA0YzRlYTQwNjAyMWNkN2RlZmFmZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kNzc0OWQxNWI5NzQ0YWEzYmNmN2I0NzNmOTIwZDk5MSA9ICQoJzxkaXYgaWQ9Imh0bWxfZDc3NDlkMTViOTc0NGFhM2JjZjdiNDczZjkyMGQ5OTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkwmIzM5O0Ftb3JlYXV4IFdlc3QsIFNjYXJib3JvdWdoPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lMTNlNzZlMDIzZjA0YzRlYTQwNjAyMWNkN2RlZmFmZi5zZXRDb250ZW50KGh0bWxfZDc3NDlkMTViOTc0NGFhM2JjZjdiNDczZjkyMGQ5OTEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjQ2ZTYyNzQyYzQ2NDQ0MGI4MjAyNDE4MWVlZGYyZmUuYmluZFBvcHVwKHBvcHVwX2UxM2U3NmUwMjNmMDRjNGVhNDA2MDIxY2Q3ZGVmYWZmKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzUyMmExZmJlZGQ4NjRkMTI5MzA4YjZlNTc3ZTc4YmFmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuODM2MTI0NzAwMDAwMDA2LC03OS4yMDU2MzYwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zODNlYWYyNDcwNWQ0MzVjYWRjZDMzNzliMmM0MGMwYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kZDhjMjE3MzAyYjg0YTBkOTMyMzg4YmU2M2ZjYWZiNCA9ICQoJzxkaXYgaWQ9Imh0bWxfZGQ4YzIxNzMwMmI4NGEwZDkzMjM4OGJlNjNmY2FmYjQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlVwcGVyIFJvdWdlLCBTY2FyYm9yb3VnaDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzgzZWFmMjQ3MDVkNDM1Y2FkY2QzMzc5YjJjNDBjMGEuc2V0Q29udGVudChodG1sX2RkOGMyMTczMDJiODRhMGQ5MzIzODhiZTYzZmNhZmI0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzUyMmExZmJlZGQ4NjRkMTI5MzA4YjZlNTc3ZTc4YmFmLmJpbmRQb3B1cChwb3B1cF8zODNlYWYyNDcwNWQ0MzVjYWRjZDMzNzliMmM0MGMwYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lMjA3NzI2MTk0N2Q0Y2U5ODI2YTVjYjllYjZlMDAyYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjgwMzc2MjIsLTc5LjM2MzQ1MTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzU3MjQxMmZiMTU5NGE4N2I0MDM2MzE2Nzg4ZmE0ZDEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDYyMmY0NDBjYmYwNGNmMTkwN2Y0N2U2NDUzMGM0MzEgPSAkKCc8ZGl2IGlkPSJodG1sXzA2MjJmNDQwY2JmMDRjZjE5MDdmNDdlNjQ1MzBjNDMxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IaWxsY3Jlc3QgVmlsbGFnZSwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zNTcyNDEyZmIxNTk0YTg3YjQwMzYzMTY3ODhmYTRkMS5zZXRDb250ZW50KGh0bWxfMDYyMmY0NDBjYmYwNGNmMTkwN2Y0N2U2NDUzMGM0MzEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTIwNzcyNjE5NDdkNGNlOTgyNmE1Y2I5ZWI2ZTAwMmIuYmluZFBvcHVwKHBvcHVwXzM1NzI0MTJmYjE1OTRhODdiNDAzNjMxNjc4OGZhNGQxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2RhMGFkNzI5OTFlYTQ4ZjlhOTNlNmU3N2Y2YzM0OTUzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzc4NTE3NSwtNzkuMzQ2NTU1N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hM2I4NGYwNjg1Mzc0Y2Y0OWM1NjgxMTk3MDExZGI2ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82ZjJjOGQxYzRhMmM0NDI0YWVmZGE0YTI0YjAyOGRjMSA9ICQoJzxkaXYgaWQ9Imh0bWxfNmYyYzhkMWM0YTJjNDQyNGFlZmRhNGEyNGIwMjhkYzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZhaXJ2aWV3LEhlbnJ5IEZhcm0sT3Jpb2xlLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2EzYjg0ZjA2ODUzNzRjZjQ5YzU2ODExOTcwMTFkYjZkLnNldENvbnRlbnQoaHRtbF82ZjJjOGQxYzRhMmM0NDI0YWVmZGE0YTI0YjAyOGRjMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kYTBhZDcyOTkxZWE0OGY5YTkzZTZlNzdmNmMzNDk1My5iaW5kUG9wdXAocG9wdXBfYTNiODRmMDY4NTM3NGNmNDljNTY4MTE5NzAxMWRiNmQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTA4Yzk4MDgwNmJmNDYzMTllZDNlZGM2YmExYzVmYmEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43ODY5NDczLC03OS4zODU5NzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODczNWFmN2VkMmEzNDg5NDhlYjQ5NTE1NGQ4NTg3MzUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzA0YWUyMjc4ZGU2NDBhZGIwZDg3OWNjNDk1MGU5YTUgPSAkKCc8ZGl2IGlkPSJodG1sXzcwNGFlMjI3OGRlNjQwYWRiMGQ4NzljYzQ5NTBlOWE1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXl2aWV3IFZpbGxhZ2UsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODczNWFmN2VkMmEzNDg5NDhlYjQ5NTE1NGQ4NTg3MzUuc2V0Q29udGVudChodG1sXzcwNGFlMjI3OGRlNjQwYWRiMGQ4NzljYzQ5NTBlOWE1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzEwOGM5ODA4MDZiZjQ2MzE5ZWQzZWRjNmJhMWM1ZmJhLmJpbmRQb3B1cChwb3B1cF84NzM1YWY3ZWQyYTM0ODk0OGViNDk1MTU0ZDg1ODczNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kNDNlMTIyNmY5YjA0ZWM2OTBiNmFmNzljMzliMzdmOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1NzQ5MDIsLTc5LjM3NDcxNDA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2M1NWQzOGMzMjUyYzQ5YmVhYjgwMGE0MjgxMWFhM2FjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY1MGM0YmY0ODNlMDRkNTNhNDgyOGU0MjliYzk5MTY2ID0gJCgnPGRpdiBpZD0iaHRtbF82NTBjNGJmNDgzZTA0ZDUzYTQ4MjhlNDI5YmM5OTE2NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U2lsdmVyIEhpbGxzLFlvcmsgTWlsbHMsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzU1ZDM4YzMyNTJjNDliZWFiODAwYTQyODExYWEzYWMuc2V0Q29udGVudChodG1sXzY1MGM0YmY0ODNlMDRkNTNhNDgyOGU0MjliYzk5MTY2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q0M2UxMjI2ZjliMDRlYzY5MGI2YWY3OWMzOWIzN2Y5LmJpbmRQb3B1cChwb3B1cF9jNTVkMzhjMzI1MmM0OWJlYWI4MDBhNDI4MTFhYTNhYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zMDVjYzVjYjExNmY0MDVmYjAzNjk0NjBkM2FjY2Y3YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4OTA1MywtNzkuNDA4NDkyNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzYzMGQ1YjViNWM5NDhlYzhmMzhmNzUxMThjYWE2MjYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTdlYWQwMjgzZWRjNDk2NGFmYmU2YzdkMDkyMzRhOGIgPSAkKCc8ZGl2IGlkPSJodG1sX2U3ZWFkMDI4M2VkYzQ5NjRhZmJlNmM3ZDA5MjM0YThiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5OZXd0b25icm9vayxXaWxsb3dkYWxlLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc2MzBkNWI1YjVjOTQ4ZWM4ZjM4Zjc1MTE4Y2FhNjI2LnNldENvbnRlbnQoaHRtbF9lN2VhZDAyODNlZGM0OTY0YWZiZTZjN2QwOTIzNGE4Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMDVjYzVjYjExNmY0MDVmYjAzNjk0NjBkM2FjY2Y3YS5iaW5kUG9wdXAocG9wdXBfNzYzMGQ1YjViNWM5NDhlYzhmMzhmNzUxMThjYWE2MjYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjYwNzk3ZTQ1OTgzNGNiZWI0ZDFiMTkzMDBmZTk2ZDIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NzAxMTk5LC03OS40MDg0OTI3OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hYmE2ZGQ4NGUzZDU0NWIzYTMwODhiYTg3ZTI3MzQwMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84ZDZkZGQ2NzgwNTI0ZTkzYmU3ZjBlYTVlMWJiMGM3YSA9ICQoJzxkaXYgaWQ9Imh0bWxfOGQ2ZGRkNjc4MDUyNGU5M2JlN2YwZWE1ZTFiYjBjN2EiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxvd2RhbGUgU291dGgsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWJhNmRkODRlM2Q1NDViM2EzMDg4YmE4N2UyNzM0MDAuc2V0Q29udGVudChodG1sXzhkNmRkZDY3ODA1MjRlOTNiZTdmMGVhNWUxYmIwYzdhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzY2MDc5N2U0NTk4MzRjYmViNGQxYjE5MzAwZmU5NmQyLmJpbmRQb3B1cChwb3B1cF9hYmE2ZGQ4NGUzZDU0NWIzYTMwODhiYTg3ZTI3MzQwMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kZDQ0NzFmMjA4ZDA0ODhiYmI4MzE2MWJmODVhYWRiMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1Mjc1ODI5OTk5OTk5NiwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85YWUxMTkzNmI5YzU0MzhlYTdiYWFhNTYyMWJjMDU0MyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wOTJlM2M3NDMwMjc0NzhmYjA1NDY3ZTVkN2E3MTAzNiA9ICQoJzxkaXYgaWQ9Imh0bWxfMDkyZTNjNzQzMDI3NDc4ZmIwNTQ2N2U1ZDdhNzEwMzYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPllvcmsgTWlsbHMgV2VzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85YWUxMTkzNmI5YzU0MzhlYTdiYWFhNTYyMWJjMDU0My5zZXRDb250ZW50KGh0bWxfMDkyZTNjNzQzMDI3NDc4ZmIwNTQ2N2U1ZDdhNzEwMzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZGQ0NDcxZjIwOGQwNDg4YmJiODMxNjFiZjg1YWFkYjEuYmluZFBvcHVwKHBvcHVwXzlhZTExOTM2YjljNTQzOGVhN2JhYWE1NjIxYmMwNTQzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NiNjVmOWNhZDBiYTQ1ZjA4NmMzODlmYzI4MzI2OTVkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzgyNzM2NCwtNzkuNDQyMjU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xMjEzMmY0OGI3Nzc0YTMwOTI5YTU3NmU1OWVmYjMxNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mN2E0OWVmNTA1YmE0MTE2ODk3ZjM4MmU0MDg2ZmE1NSA9ICQoJzxkaXYgaWQ9Imh0bWxfZjdhNDllZjUwNWJhNDExNjg5N2YzODJlNDA4NmZhNTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldpbGxvd2RhbGUgV2VzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xMjEzMmY0OGI3Nzc0YTMwOTI5YTU3NmU1OWVmYjMxNS5zZXRDb250ZW50KGh0bWxfZjdhNDllZjUwNWJhNDExNjg5N2YzODJlNDA4NmZhNTUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfY2I2NWY5Y2FkMGJhNDVmMDg2YzM4OWZjMjgzMjY5NWQuYmluZFBvcHVwKHBvcHVwXzEyMTMyZjQ4Yjc3NzRhMzA5MjlhNTc2ZTU5ZWZiMzE1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UzZTk1MmIzOTg1MzRiZGZiYWI5M2Y2MTE1YWNhNzg0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzUzMjU4NiwtNzkuMzI5NjU2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jZTBiM2VhMmM3OWQ0OWJiOWQxZjhjNjcwNGI4ZTJlMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mNTkzMDcwMmQ4N2Q0N2NkYmVlNjExZjY1YTFmNTEyNyA9ICQoJzxkaXYgaWQ9Imh0bWxfZjU5MzA3MDJkODdkNDdjZGJlZTYxMWY2NWExZjUxMjciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlBhcmt3b29kcywgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jZTBiM2VhMmM3OWQ0OWJiOWQxZjhjNjcwNGI4ZTJlMS5zZXRDb250ZW50KGh0bWxfZjU5MzA3MDJkODdkNDdjZGJlZTYxMWY2NWExZjUxMjcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTNlOTUyYjM5ODUzNGJkZmJhYjkzZjYxMTVhY2E3ODQuYmluZFBvcHVwKHBvcHVwX2NlMGIzZWEyYzc5ZDQ5YmI5ZDFmOGM2NzA0YjhlMmUxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzkyZmRiODc2ZTcwNjRhNmY4YzU1YTBhYWRiZjJlMDFiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ1OTA1Nzk5OTk5OTk2LC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTliMDVjNzllYjliNGQ4MWEwZmNiNGYwMGM1MDQ1NTEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjAxNmMwZjcxNzU1NGQzMzliYjVlYzY0NTRmN2Y5MTggPSAkKCc8ZGl2IGlkPSJodG1sX2YwMTZjMGY3MTc1NTRkMzM5YmI1ZWM2NDU0ZjdmOTE4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb24gTWlsbHMgTm9ydGgsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYTliMDVjNzllYjliNGQ4MWEwZmNiNGYwMGM1MDQ1NTEuc2V0Q29udGVudChodG1sX2YwMTZjMGY3MTc1NTRkMzM5YmI1ZWM2NDU0ZjdmOTE4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkyZmRiODc2ZTcwNjRhNmY4YzU1YTBhYWRiZjJlMDFiLmJpbmRQb3B1cChwb3B1cF9hOWIwNWM3OWViOWI0ZDgxYTBmY2I0ZjAwYzUwNDU1MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iZTY4N2JlNmE2ZDI0NGU4YjU1YzUyOTY4MzJlMWExYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNTg5OTcwMDAwMDAxLC03OS4zNDA5MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZWZmMzllY2U2ZTgwNGM5MWI5YjI2ZmQyZTIzYTQ4ODMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjZhNmRjY2M0ZTMwNGU4YTk2NGZhZTNhOTIyNjRlYWUgPSAkKCc8ZGl2IGlkPSJodG1sX2I2YTZkY2NjNGUzMDRlOGE5NjRmYWUzYTkyMjY0ZWFlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GbGVtaW5nZG9uIFBhcmssRG9uIE1pbGxzIFNvdXRoLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2VmZjM5ZWNlNmU4MDRjOTFiOWIyNmZkMmUyM2E0ODgzLnNldENvbnRlbnQoaHRtbF9iNmE2ZGNjYzRlMzA0ZThhOTY0ZmFlM2E5MjI2NGVhZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iZTY4N2JlNmE2ZDI0NGU4YjU1YzUyOTY4MzJlMWExYi5iaW5kUG9wdXAocG9wdXBfZWZmMzllY2U2ZTgwNGM5MWI5YjI2ZmQyZTIzYTQ4ODMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmUyMzdiMWRiYjk3NDg1MGIyNzBiMWUzOWQ5YzQwZjUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTQzMjgzLC03OS40NDIyNTkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzc0NmY3NTYzNDRlMDRkY2FiOWFmZmIzMmIwMDZhZDg5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNhOWM2YmUxYWM3MDQwYTFhNDQwNDdkNDBmYTU3MzViID0gJCgnPGRpdiBpZD0iaHRtbF8zYTljNmJlMWFjNzA0MGExYTQ0MDQ3ZDQwZmE1NzM1YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmF0aHVyc3QgTWFub3IsRG93bnN2aWV3IE5vcnRoLFdpbHNvbiBIZWlnaHRzLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc0NmY3NTYzNDRlMDRkY2FiOWFmZmIzMmIwMDZhZDg5LnNldENvbnRlbnQoaHRtbF8zYTljNmJlMWFjNzA0MGExYTQ0MDQ3ZDQwZmE1NzM1Yik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iZTIzN2IxZGJiOTc0ODUwYjI3MGIxZTM5ZDljNDBmNS5iaW5kUG9wdXAocG9wdXBfNzQ2Zjc1NjM0NGUwNGRjYWI5YWZmYjMyYjAwNmFkODkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmM3ZjcwMDk2ODJjNDQ0Nzg4OWNjMTBhZTNlOTRlNmQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Njc5ODAzLC03OS40ODcyNjE5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wOWI3ODE4MDBhM2I0ZGI5OGU4Mzg5OTNjYTE2YzkwMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jNmYyNGExMzgxOWI0NDRkYWQxZWY2NmFkYzFhM2Q4NCA9ICQoJzxkaXYgaWQ9Imh0bWxfYzZmMjRhMTM4MTliNDQ0ZGFkMWVmNjZhZGMxYTNkODQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vcnRod29vZCBQYXJrLFlvcmsgVW5pdmVyc2l0eSwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wOWI3ODE4MDBhM2I0ZGI5OGU4Mzg5OTNjYTE2YzkwMC5zZXRDb250ZW50KGh0bWxfYzZmMjRhMTM4MTliNDQ0ZGFkMWVmNjZhZGMxYTNkODQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmM3ZjcwMDk2ODJjNDQ0Nzg4OWNjMTBhZTNlOTRlNmQuYmluZFBvcHVwKHBvcHVwXzA5Yjc4MTgwMGEzYjRkYjk4ZTgzODk5M2NhMTZjOTAwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBiYWNmMDJhY2M2MTQzMjE5MzFhN2RiYjA5MjljODQzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzM3NDczMjAwMDAwMDA0LC03OS40NjQ3NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mYzkyNmNiOTA4ZTQ0ZTk3ODQzOWY2YjZjNWM0MjY1NSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80ZWI2NTc2ZTYzMTg0MzY4YWNjMmYwOGRiYjU3ZGQzOCA9ICQoJzxkaXYgaWQ9Imh0bWxfNGViNjU3NmU2MzE4NDM2OGFjYzJmMDhkYmI1N2RkMzgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNGQiBUb3JvbnRvLERvd25zdmlldyBFYXN0LCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZjOTI2Y2I5MDhlNDRlOTc4NDM5ZjZiNmM1YzQyNjU1LnNldENvbnRlbnQoaHRtbF80ZWI2NTc2ZTYzMTg0MzY4YWNjMmYwOGRiYjU3ZGQzOCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wYmFjZjAyYWNjNjE0MzIxOTMxYTdkYmIwOTI5Yzg0My5iaW5kUG9wdXAocG9wdXBfZmM5MjZjYjkwOGU0NGU5Nzg0MzlmNmI2YzVjNDI2NTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWI5NzA3ZWYzNmIwNDhlNjllYmIwOGQxYmJkMDU1ODEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MzkwMTQ2LC03OS41MDY5NDM2XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2IwMzhkOTg4MDVjMzQ0NzI5ZGFmZWMwODI2MGE5YTRiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzdkYjk5NDMyOWZhOTRlY2Y5NTk2MGE2ZTQ0YmQ5OGU1ID0gJCgnPGRpdiBpZD0iaHRtbF83ZGI5OTQzMjlmYTk0ZWNmOTU5NjBhNmU0NGJkOThlNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IFdlc3QsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjAzOGQ5ODgwNWMzNDQ3MjlkYWZlYzA4MjYwYTlhNGIuc2V0Q29udGVudChodG1sXzdkYjk5NDMyOWZhOTRlY2Y5NTk2MGE2ZTQ0YmQ5OGU1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzliOTcwN2VmMzZiMDQ4ZTY5ZWJiMDhkMWJiZDA1NTgxLmJpbmRQb3B1cChwb3B1cF9iMDM4ZDk4ODA1YzM0NDcyOWRhZmVjMDgyNjBhOWE0Yik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85M2Y5NTkyZjc2Y2Q0YjEyODY1ZTIzNjc3ZDY3NGI0MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyODQ5NjQsLTc5LjQ5NTY5NzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFhM2Y0OThhNDE3NDQ0NDI4NjhmMDk0YTE3MmNjOTZkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzExZjIyNWMxNGY1MTQyMzJhN2FlNzQzZWMxYjdjZmI3ID0gJCgnPGRpdiBpZD0iaHRtbF8xMWYyMjVjMTRmNTE0MjMyYTdhZTc0M2VjMWI3Y2ZiNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IENlbnRyYWwsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMWEzZjQ5OGE0MTc0NDQ0Mjg2OGYwOTRhMTcyY2M5NmQuc2V0Q29udGVudChodG1sXzExZjIyNWMxNGY1MTQyMzJhN2FlNzQzZWMxYjdjZmI3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzkzZjk1OTJmNzZjZDRiMTI4NjVlMjM2NzdkNjc0YjQyLmJpbmRQb3B1cChwb3B1cF8xYTNmNDk4YTQxNzQ0NDQyODY4ZjA5NGExNzJjYzk2ZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iMGQ3ZmFkYzFiNDY0NWQ3YTBlNzI1Y2VmZGFiMjBmZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc2MTYzMTMsLTc5LjUyMDk5OTQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk3YmFjMDkzMmZiMDRhZjlhNjYyYTUwZGQ1MDNlZWYxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFjZDg4Nzc1NWY5NTQ1YThhOTJiZmU4ZGNkMDkyNWM2ID0gJCgnPGRpdiBpZD0iaHRtbF8xY2Q4ODc3NTVmOTU0NWE4YTkyYmZlOGRjZDA5MjVjNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IE5vcnRod2VzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85N2JhYzA5MzJmYjA0YWY5YTY2MmE1MGRkNTAzZWVmMS5zZXRDb250ZW50KGh0bWxfMWNkODg3NzU1Zjk1NDVhOGE5MmJmZThkY2QwOTI1YzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjBkN2ZhZGMxYjQ2NDVkN2EwZTcyNWNlZmRhYjIwZmQuYmluZFBvcHVwKHBvcHVwXzk3YmFjMDkzMmZiMDRhZjlhNjYyYTUwZGQ1MDNlZWYxKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M3YmZhZmIwOTAxNzRkMWFhNDM5N2E1NGRmZGQyZmVjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI1ODgyMjk5OTk5OTk1LC03OS4zMTU1NzE1OTk5OTk5OF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83Nzc0NDg5NjdhNzI0NmY5OGU1Yjc0NTUxNmJhZTljOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yNWJjYmUzMTdlNDI0MjdmYTYyMzVlMmEzZDU2YzNhZSA9ICQoJzxkaXYgaWQ9Imh0bWxfMjViY2JlMzE3ZTQyNDI3ZmE2MjM1ZTJhM2Q1NmMzYWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlZpY3RvcmlhIFZpbGxhZ2UsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzc3NDQ4OTY3YTcyNDZmOThlNWI3NDU1MTZiYWU5Yzguc2V0Q29udGVudChodG1sXzI1YmNiZTMxN2U0MjQyN2ZhNjIzNWUyYTNkNTZjM2FlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M3YmZhZmIwOTAxNzRkMWFhNDM5N2E1NGRmZGQyZmVjLmJpbmRQb3B1cChwb3B1cF83Nzc0NDg5NjdhNzI0NmY5OGU1Yjc0NTUxNmJhZTljOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82MDBhNWUzZmRkMWE0YzcyYWU2ZWI3NDg2MTE1ZDcwMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcwNjM5NzIsLTc5LjMwOTkzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84MDFkOTUyNDljMDk0MTVmYTIxMzJiNzNiN2QwYjRlOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jYWM5MTlmODY4OGU0OTRmYmNiMDYyNGYwZjgzMTlhOSA9ICQoJzxkaXYgaWQ9Imh0bWxfY2FjOTE5Zjg2ODhlNDk0ZmJjYjA2MjRmMGY4MzE5YTkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldvb2RiaW5lIEdhcmRlbnMsUGFya3ZpZXcgSGlsbCwgRWFzdFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzgwMWQ5NTI0OWMwOTQxNWZhMjEzMmI3M2I3ZDBiNGU4LnNldENvbnRlbnQoaHRtbF9jYWM5MTlmODY4OGU0OTRmYmNiMDYyNGYwZjgzMTlhOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82MDBhNWUzZmRkMWE0YzcyYWU2ZWI3NDg2MTE1ZDcwMC5iaW5kUG9wdXAocG9wdXBfODAxZDk1MjQ5YzA5NDE1ZmEyMTMyYjczYjdkMGI0ZTgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDU4NDk5NjQ0NDQzNGQ2YmI0NTk5OGQyNWE0MGFhZmMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTUzNDM5MDAwMDAwMDUsLTc5LjMxODM4ODddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfM2M3OGMyMzAwNDc3NGJkMzlhODkwNWFmNzU3Nzg5YWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjA0MDUwMTdkZjM1NDRlOGJhMDNiYWRhMjZiY2EwNTQgPSAkKCc8ZGl2IGlkPSJodG1sX2IwNDA1MDE3ZGYzNTQ0ZThiYTAzYmFkYTI2YmNhMDU0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Xb29kYmluZSBIZWlnaHRzLCBFYXN0WW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfM2M3OGMyMzAwNDc3NGJkMzlhODkwNWFmNzU3Nzg5YWMuc2V0Q29udGVudChodG1sX2IwNDA1MDE3ZGYzNTQ0ZThiYTAzYmFkYTI2YmNhMDU0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQ1ODQ5OTY0NDQ0MzRkNmJiNDU5OThkMjVhNDBhYWZjLmJpbmRQb3B1cChwb3B1cF8zYzc4YzIzMDA0Nzc0YmQzOWE4OTA1YWY3NTc3ODlhYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZTFjODEyNTUxODI0OTI5YjEyNGY2OWU1MDM4ODRhZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY3NjM1NzM5OTk5OTk5LC03OS4yOTMwMzEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI2MGM3YmVlZDQ5NjRjYTY4ZGVjMjk3ZDM5NjUwMzExID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2JjNDUwZjI5MzMxMzQyNDg4ZGFkNmQyZjViZTg5Y2NlID0gJCgnPGRpdiBpZD0iaHRtbF9iYzQ1MGYyOTMzMTM0MjQ4OGRhZDZkMmY1YmU4OWNjZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhlIEJlYWNoZXMsIEVhc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yNjBjN2JlZWQ0OTY0Y2E2OGRlYzI5N2QzOTY1MDMxMS5zZXRDb250ZW50KGh0bWxfYmM0NTBmMjkzMzEzNDI0ODhkYWQ2ZDJmNWJlODljY2UpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfN2UxYzgxMjU1MTgyNDkyOWIxMjRmNjllNTAzODg0YWUuYmluZFBvcHVwKHBvcHVwXzI2MGM3YmVlZDQ5NjRjYTY4ZGVjMjk3ZDM5NjUwMzExKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2MwNWM1OTRhYjZlMDRhNWE5NWFlZTU2NGRkYWEyYTZmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA5MDYwNCwtNzkuMzYzNDUxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85MzA2ZjJhZWQyMmY0Yjk5YjhhYzljMjliN2ZkNDJhYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jZjJmNmFhNWFhMGU0NTk1YWI0ZTRlOGE2NzdlNmJlYyA9ICQoJzxkaXYgaWQ9Imh0bWxfY2YyZjZhYTVhYTBlNDU5NWFiNGU0ZThhNjc3ZTZiZWMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxlYXNpZGUsIEVhc3RZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85MzA2ZjJhZWQyMmY0Yjk5YjhhYzljMjliN2ZkNDJhYy5zZXRDb250ZW50KGh0bWxfY2YyZjZhYTVhYTBlNDU5NWFiNGU0ZThhNjc3ZTZiZWMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzA1YzU5NGFiNmUwNGE1YTk1YWVlNTY0ZGRhYTJhNmYuYmluZFBvcHVwKHBvcHVwXzkzMDZmMmFlZDIyZjRiOTliOGFjOWMyOWI3ZmQ0MmFjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UyMDFmYjkyOWFiYjQ5MjM5YWJiN2U3MDg1NTE0MDZjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA1MzY4OSwtNzkuMzQ5MzcxOTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzgyNzBjODA5MDZlNDE1OWFhMDg4YjRlNjliMDFiNTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTVlYTVlNzkzMjQxNDI1OGE0NGNjYjI0N2M1YjBkOGEgPSAkKCc8ZGl2IGlkPSJodG1sX2U1ZWE1ZTc5MzI0MTQyNThhNDRjY2IyNDdjNWIwZDhhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaG9ybmNsaWZmZSBQYXJrLCBFYXN0WW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzgyNzBjODA5MDZlNDE1OWFhMDg4YjRlNjliMDFiNTAuc2V0Q29udGVudChodG1sX2U1ZWE1ZTc5MzI0MTQyNThhNDRjY2IyNDdjNWIwZDhhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UyMDFmYjkyOWFiYjQ5MjM5YWJiN2U3MDg1NTE0MDZjLmJpbmRQb3B1cChwb3B1cF9jODI3MGM4MDkwNmU0MTU5YWEwODhiNGU2OWIwMWI1MCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jODhiNDU2NDZlMzY0NWU5ODQyYmVmNThiMWM0OTBjNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY4NTM0NywtNzkuMzM4MTA2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lZGYxYmRjY2M1MjA0MGRlOGIyYWI4MDg2ZjhjZDk5YiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hNTk0NTVkMjAwZjI0ODU3OWJhZjk1ZTkyNmU0MTkwNyA9ICQoJzxkaXYgaWQ9Imh0bWxfYTU5NDU1ZDIwMGYyNDg1NzliYWY5NWU5MjZlNDE5MDciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgVG9yb250bywgRWFzdFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2VkZjFiZGNjYzUyMDQwZGU4YjJhYjgwODZmOGNkOTliLnNldENvbnRlbnQoaHRtbF9hNTk0NTVkMjAwZjI0ODU3OWJhZjk1ZTkyNmU0MTkwNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jODhiNDU2NDZlMzY0NWU5ODQyYmVmNThiMWM0OTBjNS5iaW5kUG9wdXAocG9wdXBfZWRmMWJkY2NjNTIwNDBkZThiMmFiODA4NmY4Y2Q5OWIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmViYTQyYTY3MjZhNDYyOGEzYWZmM2Q1ODViMzIzZDQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Nzk1NTcxLC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjdlMDU5ZWRkY2FmNDNlYWI1YTZjOTQ3ODk3YzExZjQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2U1NDU5ZDc0ZjhjNDNkNGE5NWQ0OTNkMzBlZDExN2QgPSAkKCc8ZGl2IGlkPSJodG1sXzNlNTQ1OWQ3NGY4YzQzZDRhOTVkNDkzZDMwZWQxMTdkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgRGFuZm9ydGggV2VzdCxSaXZlcmRhbGUsIEVhc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mN2UwNTllZGRjYWY0M2VhYjVhNmM5NDc4OTdjMTFmNC5zZXRDb250ZW50KGh0bWxfM2U1NDU5ZDc0ZjhjNDNkNGE5NWQ0OTNkMzBlZDExN2QpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmViYTQyYTY3MjZhNDYyOGEzYWZmM2Q1ODViMzIzZDQuYmluZFBvcHVwKHBvcHVwX2Y3ZTA1OWVkZGNhZjQzZWFiNWE2Yzk0Nzg5N2MxMWY0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFjZjRlMWVjYTFiMzQ1MmQ4NGEwY2E0NmYwY2IxMjliID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY4OTk4NSwtNzkuMzE1NTcxNTk5OTk5OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWI1Nzk3MWNiYjRlNDZkNjg2YWQzNWM4YWY0NTAwMTIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmQ5YTkwYjUxMjMwNDYyMThkMDM0N2EwNTNhYjFkYmUgPSAkKCc8ZGl2IGlkPSJodG1sX2ZkOWE5MGI1MTIzMDQ2MjE4ZDAzNDdhMDUzYWIxZGJlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgQmVhY2hlcyBXZXN0LEluZGlhIEJhemFhciwgRWFzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzViNTc5NzFjYmI0ZTQ2ZDY4NmFkMzVjOGFmNDUwMDEyLnNldENvbnRlbnQoaHRtbF9mZDlhOTBiNTEyMzA0NjIxOGQwMzQ3YTA1M2FiMWRiZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xY2Y0ZTFlY2ExYjM0NTJkODRhMGNhNDZmMGNiMTI5Yi5iaW5kUG9wdXAocG9wdXBfNWI1Nzk3MWNiYjRlNDZkNjg2YWQzNWM4YWY0NTAwMTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjg0NjlkNDQxMjk2NGZmYzllZjZiNDk0MDM0MzhjNjYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTk1MjU1LC03OS4zNDA5MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMTM1YzAwOGQyMGJhNDEzMzk1YThkM2I0MTc1Njc0Y2QgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTAyMzZhNmYxMzQ0NGNhNzk2Mjg1NTRlMmNiNmE1YmYgPSAkKCc8ZGl2IGlkPSJodG1sX2EwMjM2YTZmMTM0NDRjYTc5NjI4NTU0ZTJjYjZhNWJmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdHVkaW8gRGlzdHJpY3QsIEVhc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xMzVjMDA4ZDIwYmE0MTMzOTVhOGQzYjQxNzU2NzRjZC5zZXRDb250ZW50KGh0bWxfYTAyMzZhNmYxMzQ0NGNhNzk2Mjg1NTRlMmNiNmE1YmYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZjg0NjlkNDQxMjk2NGZmYzllZjZiNDk0MDM0MzhjNjYuYmluZFBvcHVwKHBvcHVwXzEzNWMwMDhkMjBiYTQxMzM5NWE4ZDNiNDE3NTY3NGNkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk0MjgzMjZiZTcwMjRmYjhiMTI1MmY0NzdiZGQ4ZWQyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI4MDIwNSwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iZjY3NjFiNmFiZWM0MDg4OTFmNmE5YTNjNWYyZmVjOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84ODU3NDdiYTY3OWY0MDJhOGExYzg0MWFkN2U0ZjI1YyA9ICQoJzxkaXYgaWQ9Imh0bWxfODg1NzQ3YmE2NzlmNDAyYThhMWM4NDFhZDdlNGYyNWMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIFBhcmssIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iZjY3NjFiNmFiZWM0MDg4OTFmNmE5YTNjNWYyZmVjOC5zZXRDb250ZW50KGh0bWxfODg1NzQ3YmE2NzlmNDAyYThhMWM4NDFhZDdlNGYyNWMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTQyODMyNmJlNzAyNGZiOGIxMjUyZjQ3N2JkZDhlZDIuYmluZFBvcHVwKHBvcHVwX2JmNjc2MWI2YWJlYzQwODg5MWY2YTlhM2M1ZjJmZWM4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJmMGNhMjYzOTNkZDQ5MGI4OTRiYWFhNGU4YjVlYTU5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzEyNzUxMSwtNzkuMzkwMTk3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hMjgxZWJiYjgxYzI0NmU0OTg0NWJkYzcxMDhjZjRkYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81NGZiNzkxNGFhZjk0YTBiYjc2ZTJkYzM4NDI4NTFjOSA9ICQoJzxkaXYgaWQ9Imh0bWxfNTRmYjc5MTRhYWY5NGEwYmI3NmUyZGMzODQyODUxYzkiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUgTm9ydGgsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hMjgxZWJiYjgxYzI0NmU0OTg0NWJkYzcxMDhjZjRkYy5zZXRDb250ZW50KGh0bWxfNTRmYjc5MTRhYWY5NGEwYmI3NmUyZGMzODQyODUxYzkpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmYwY2EyNjM5M2RkNDkwYjg5NGJhYWE0ZThiNWVhNTkuYmluZFBvcHVwKHBvcHVwX2EyODFlYmJiODFjMjQ2ZTQ5ODQ1YmRjNzEwOGNmNGRjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzM5YzFkZGQ5NWI4MDQ5MzA4ZjY2MjA0MjViMjEwNTgxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE1MzgzNCwtNzkuNDA1Njc4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjY0NWMzZDEzNDgzNGViM2I5NjQxNmI1NTM3YmI2NmUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2I3ZmJmMGMwZDJmNGY1ODllMzkxODc4Y2FlMTJkM2IgPSAkKCc8ZGl2IGlkPSJodG1sXzNiN2ZiZjBjMGQyZjRmNTg5ZTM5MTg3OGNhZTEyZDNiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aCBUb3JvbnRvIFdlc3QsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mNjQ1YzNkMTM0ODM0ZWIzYjk2NDE2YjU1MzdiYjY2ZS5zZXRDb250ZW50KGh0bWxfM2I3ZmJmMGMwZDJmNGY1ODllMzkxODc4Y2FlMTJkM2IpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzljMWRkZDk1YjgwNDkzMDhmNjYyMDQyNWIyMTA1ODEuYmluZFBvcHVwKHBvcHVwX2Y2NDVjM2QxMzQ4MzRlYjNiOTY0MTZiNTUzN2JiNjZlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk0NWE1ZTk2MjYyNjRiMjRiNWQyOTYxMDZmY2ZmZjM2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA0MzI0NCwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iYjM0NWNhODE0MzQ0MDY1OWRjMTJkMzViYTYyYTUyMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNGFlYjY2OTkzZDI0MDg4YmUwMmM5YjNkYzk1ODExMCA9ICQoJzxkaXYgaWQ9Imh0bWxfMTRhZWI2Njk5M2QyNDA4OGJlMDJjOWIzZGM5NTgxMTAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iYjM0NWNhODE0MzQ0MDY1OWRjMTJkMzViYTYyYTUyMi5zZXRDb250ZW50KGh0bWxfMTRhZWI2Njk5M2QyNDA4OGJlMDJjOWIzZGM5NTgxMTApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTQ1YTVlOTYyNjI2NGIyNGI1ZDI5NjEwNmZjZmZmMzYuYmluZFBvcHVwKHBvcHVwX2JiMzQ1Y2E4MTQzNDQwNjU5ZGMxMmQzNWJhNjJhNTIyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhlZjk0NjJjN2I3ODQ0YzhiODc3NjZmZDQxZDY3N2JhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg5NTc0MywtNzkuMzgzMTU5OTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzFkOGM3MmE5YTkzNDcxOTkzMGNiMjM1ODA0ZTJkZGIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWU5NGU3NTg5ZGEzNDI4MDlhYjM5Njc1MWJmM2QyYmIgPSAkKCc8ZGl2IGlkPSJodG1sXzVlOTRlNzU4OWRhMzQyODA5YWIzOTY3NTFiZjNkMmJiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb29yZSBQYXJrLFN1bW1lcmhpbGwgRWFzdCwgQ2VudHJhbFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2MxZDhjNzJhOWE5MzQ3MTk5MzBjYjIzNTgwNGUyZGRiLnNldENvbnRlbnQoaHRtbF81ZTk0ZTc1ODlkYTM0MjgwOWFiMzk2NzUxYmYzZDJiYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84ZWY5NDYyYzdiNzg0NGM4Yjg3NzY2ZmQ0MWQ2NzdiYS5iaW5kUG9wdXAocG9wdXBfYzFkOGM3MmE5YTkzNDcxOTkzMGNiMjM1ODA0ZTJkZGIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMGRhYWIzZGEwMGZmNDMxOWIwOGJjZGY4ZGM1MzUzMjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42ODY0MTIyOTk5OTk5OSwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMTFiMWY4N2E2ZTM0YzMxODNkYjdlZTdjMDZhYTk1YiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zZTUzZTc0ZDVhYTE0Zjg3YjhmZDMxNGU4MmY3MzY2MiA9ICQoJzxkaXYgaWQ9Imh0bWxfM2U1M2U3NGQ1YWExNGY4N2I4ZmQzMTRlODJmNzM2NjIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRlZXIgUGFyayxGb3Jlc3QgSGlsbCBTRSxSYXRobmVsbHksU291dGggSGlsbCxTdW1tZXJoaWxsIFdlc3QsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mMTFiMWY4N2E2ZTM0YzMxODNkYjdlZTdjMDZhYTk1Yi5zZXRDb250ZW50KGh0bWxfM2U1M2U3NGQ1YWExNGY4N2I4ZmQzMTRlODJmNzM2NjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMGRhYWIzZGEwMGZmNDMxOWIwOGJjZGY4ZGM1MzUzMjcuYmluZFBvcHVwKHBvcHVwX2YxMWIxZjg3YTZlMzRjMzE4M2RiN2VlN2MwNmFhOTViKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzhmNDgxOTRkMWU4MzQyYjg4NDIzMjQyYTc3ODFmYzhhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjc5NTYyNiwtNzkuMzc3NTI5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjk1ZDNiYzNkODJhNGVmNmE2N2M0MWFmMzdhZDU3OWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmFkMTI2MzgxMWQ0NDkyNTkzMzU4ODYyMDUzOTcwMDIgPSAkKCc8ZGl2IGlkPSJodG1sX2ZhZDEyNjM4MTFkNDQ5MjU5MzM1ODg2MjA1Mzk3MDAyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlZGFsZSwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iOTVkM2JjM2Q4MmE0ZWY2YTY3YzQxYWYzN2FkNTc5YS5zZXRDb250ZW50KGh0bWxfZmFkMTI2MzgxMWQ0NDkyNTkzMzU4ODYyMDUzOTcwMDIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOGY0ODE5NGQxZTgzNDJiODg0MjMyNDJhNzc4MWZjOGEuYmluZFBvcHVwKHBvcHVwX2I5NWQzYmMzZDgyYTRlZjZhNjdjNDFhZjM3YWQ1NzlhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNhYTRkODNlODg5NTQ0Y2VhM2JkNmU4YWQyZjBmNjNhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY3OTY3LC03OS4zNjc2NzUzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzQ5OWViMWZkYzcxYjQ4Y2I4MmFjZDkwYzg0MDgyM2VjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2QzNWJlMmE4NDBjNjQ2MjM5MjE4YWMzZjk4Y2VmOTZhID0gJCgnPGRpdiBpZD0iaHRtbF9kMzViZTJhODQwYzY0NjIzOTIxOGFjM2Y5OGNlZjk2YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FiYmFnZXRvd24sU3QuIEphbWVzIFRvd24sIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDk5ZWIxZmRjNzFiNDhjYjgyYWNkOTBjODQwODIzZWMuc2V0Q29udGVudChodG1sX2QzNWJlMmE4NDBjNjQ2MjM5MjE4YWMzZjk4Y2VmOTZhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNhYTRkODNlODg5NTQ0Y2VhM2JkNmU4YWQyZjBmNjNhLmJpbmRQb3B1cChwb3B1cF80OTllYjFmZGM3MWI0OGNiODJhY2Q5MGM4NDA4MjNlYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ZGZiN2IyMjkyMjk0YTJiYTg0ZjNhNTZhODcwYzVlYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2NTg1OTksLTc5LjM4MzE1OTkwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzcwOWYzNWNiZWJjYzQ4NmVhOTQ0NDBlYzA2Nzk5ZmUzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFhNTM5OWRlNGRiMDRiMjg5ZDA1MzA4MTI4MDMwNWNiID0gJCgnPGRpdiBpZD0iaHRtbF8xYTUzOTlkZTRkYjA0YjI4OWQwNTMwODEyODAzMDVjYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2h1cmNoIGFuZCBXZWxsZXNsZXksIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzA5ZjM1Y2JlYmNjNDg2ZWE5NDQ0MGVjMDY3OTlmZTMuc2V0Q29udGVudChodG1sXzFhNTM5OWRlNGRiMDRiMjg5ZDA1MzA4MTI4MDMwNWNiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzdkZmI3YjIyOTIyOTRhMmJhODRmM2E1NmE4NzBjNWViLmJpbmRQb3B1cChwb3B1cF83MDlmMzVjYmViY2M0ODZlYTk0NDQwZWMwNjc5OWZlMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85ZjllZDg1MzJhYjE0ZWMxOGZjZWNjOTY4MzJlNTllNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1NDI1OTksLTc5LjM2MDYzNTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjg1MTkyZDk4Mzg5NGI2NThhOTYwYzRmYTdkMTMzMGUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDIxYzQyYzJkZmEyNDM0M2JmZDExNmZhYTI1N2IwN2UgPSAkKCc8ZGl2IGlkPSJodG1sX2QyMWM0MmMyZGZhMjQzNDNiZmQxMTZmYWEyNTdiMDdlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQsUmVnZW50IFBhcmssIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjg1MTkyZDk4Mzg5NGI2NThhOTYwYzRmYTdkMTMzMGUuc2V0Q29udGVudChodG1sX2QyMWM0MmMyZGZhMjQzNDNiZmQxMTZmYWEyNTdiMDdlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzlmOWVkODUzMmFiMTRlYzE4ZmNlY2M5NjgzMmU1OWU2LmJpbmRQb3B1cChwb3B1cF82ODUxOTJkOTgzODk0YjY1OGE5NjBjNGZhN2QxMzMwZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85NTE5NDgwZWZhMzU0NDFiOTAyOTA3YjZkNjA1ZmM5ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1NzE2MTgsLTc5LjM3ODkzNzA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzEyOTJhM2Y1Nzk0NDQ2NWZhZjljNWNlMWE4YmJjN2I4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2EzZDAyYzZkMzQzMDQwM2ViNjQ5YTg2ZGI3MTcwZDQxID0gJCgnPGRpdiBpZD0iaHRtbF9hM2QwMmM2ZDM0MzA0MDNlYjY0OWE4NmRiNzE3MGQ0MSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+UnllcnNvbixHYXJkZW4gRGlzdHJpY3QsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMTI5MmEzZjU3OTQ0NDY1ZmFmOWM1Y2UxYThiYmM3Yjguc2V0Q29udGVudChodG1sX2EzZDAyYzZkMzQzMDQwM2ViNjQ5YTg2ZGI3MTcwZDQxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk1MTk0ODBlZmEzNTQ0MWI5MDI5MDdiNmQ2MDVmYzllLmJpbmRQb3B1cChwb3B1cF8xMjkyYTNmNTc5NDQ0NjVmYWY5YzVjZTFhOGJiYzdiOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80YWZlNzg4OWEzZjM0OTg0ODdjNmViODZjNGQ0ODg2YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1MTQ5MzksLTc5LjM3NTQxNzldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWYzMjY4NzdlNDZiNDUwNTllNTE5MTg0NWVmNmJiOGUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjc5Zjc1ODU1MThhNDJhZDhmMzE4MDM1YTgwYTk3MGIgPSAkKCc8ZGl2IGlkPSJodG1sXzI3OWY3NTg1NTE4YTQyYWQ4ZjMxODAzNWE4MGE5NzBiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdC4gSmFtZXMgVG93biwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hZjMyNjg3N2U0NmI0NTA1OWU1MTkxODQ1ZWY2YmI4ZS5zZXRDb250ZW50KGh0bWxfMjc5Zjc1ODU1MThhNDJhZDhmMzE4MDM1YTgwYTk3MGIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNGFmZTc4ODlhM2YzNDk4NDg3YzZlYjg2YzRkNDg4NmEuYmluZFBvcHVwKHBvcHVwX2FmMzI2ODc3ZTQ2YjQ1MDU5ZTUxOTE4NDVlZjZiYjhlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFlZmE2ZjlmMGEzYTQyMWE4YWZiNDM5ZTZkYjE5Yjg4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ0NzcwNzk5OTk5OTk2LC03OS4zNzMzMDY0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzJmY2RmN2YxZWU1YzRjM2VhMTZmNmU4NzJiZjZiZDc0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRhNjU5OGI0MjYzMDQwNTdiNmFkNjE4MDNlYjI3MDJiID0gJCgnPGRpdiBpZD0iaHRtbF80YTY1OThiNDI2MzA0MDU3YjZhZDYxODAzZWIyNzAyYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVyY3p5IFBhcmssIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmZjZGY3ZjFlZTVjNGMzZWExNmY2ZTg3MmJmNmJkNzQuc2V0Q29udGVudChodG1sXzRhNjU5OGI0MjYzMDQwNTdiNmFkNjE4MDNlYjI3MDJiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFlZmE2ZjlmMGEzYTQyMWE4YWZiNDM5ZTZkYjE5Yjg4LmJpbmRQb3B1cChwb3B1cF8yZmNkZjdmMWVlNWM0YzNlYTE2ZjZlODcyYmY2YmQ3NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xOGFkNjRiNDExZjY0ZmYxOTJhZTk5MjAzYTllMDYwNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1Nzk1MjQsLTc5LjM4NzM4MjZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGM3ZWM4MmVmY2Q3NGY0MTkwMmU3NTNkY2ZmYjNlNDUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTI3NmU0ZTQ5ODk4NDA5ZGE5YmM2MTE0Y2ZiNTUxOTAgPSAkKCc8ZGl2IGlkPSJodG1sXzUyNzZlNGU0OTg5ODQwOWRhOWJjNjExNGNmYjU1MTkwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZW50cmFsIEJheSBTdHJlZXQsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGM3ZWM4MmVmY2Q3NGY0MTkwMmU3NTNkY2ZmYjNlNDUuc2V0Q29udGVudChodG1sXzUyNzZlNGU0OTg5ODQwOWRhOWJjNjExNGNmYjU1MTkwKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzE4YWQ2NGI0MTFmNjRmZjE5MmFlOTkyMDNhOWUwNjA3LmJpbmRQb3B1cChwb3B1cF84YzdlYzgyZWZjZDc0ZjQxOTAyZTc1M2RjZmZiM2U0NSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hMTIzYjk4YWE5NTQ0Y2ZlOWZlZTI5NmJiOWNjZWVlZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1MDU3MTIwMDAwMDAxLC03OS4zODQ1Njc1XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2YzMDQ3ZTZmYTkyMzRhMmNiNGExZmQ2MGZiNTlkZWNhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ExNGQ4YjBlMzI1MDRhOGU4NWY3MTg3NzA4Y2YwYzc2ID0gJCgnPGRpdiBpZD0iaHRtbF9hMTRkOGIwZTMyNTA0YThlODVmNzE4NzcwOGNmMGM3NiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWRlbGFpZGUsS2luZyxSaWNobW9uZCwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mMzA0N2U2ZmE5MjM0YTJjYjRhMWZkNjBmYjU5ZGVjYS5zZXRDb250ZW50KGh0bWxfYTE0ZDhiMGUzMjUwNGE4ZTg1ZjcxODc3MDhjZjBjNzYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTEyM2I5OGFhOTU0NGNmZTlmZWUyOTZiYjljY2VlZWQuYmluZFBvcHVwKHBvcHVwX2YzMDQ3ZTZmYTkyMzRhMmNiNGExZmQ2MGZiNTlkZWNhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M0NDhjNWY1YTk3OTRmZmY5YTc1YTUxMjlhZjA3ZTk2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQwODE1NywtNzkuMzgxNzUyMjk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDNjYTRmN2RhZTA3NGMzNmIxMWU3ZDNjZGEwODUxMjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTdlN2MyZGQwNjc4NDE2OGI3NDhkM2UyOTdmYjdmYWQgPSAkKCc8ZGl2IGlkPSJodG1sX2E3ZTdjMmRkMDY3ODQxNjhiNzQ4ZDNlMjk3ZmI3ZmFkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQgRWFzdCxUb3JvbnRvIElzbGFuZHMsVW5pb24gU3RhdGlvbiwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wM2NhNGY3ZGFlMDc0YzM2YjExZTdkM2NkYTA4NTEyNS5zZXRDb250ZW50KGh0bWxfYTdlN2MyZGQwNjc4NDE2OGI3NDhkM2UyOTdmYjdmYWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzQ0OGM1ZjVhOTc5NGZmZjlhNzVhNTEyOWFmMDdlOTYuYmluZFBvcHVwKHBvcHVwXzAzY2E0ZjdkYWUwNzRjMzZiMTFlN2QzY2RhMDg1MTI1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y0YzAxNjk1MWE3NzQyNzdhZWQ5MzY0M2IxYTFlN2ZhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ3MTc2OCwtNzkuMzgxNTc2NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOThlMDgyMmMxYmRlNGE4ZmJhOWQ4OTdjNDNmMTU2MWQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZDUyZGNlYmY1MzQwNDFhYWI2ZjU4ZWM3Y2ExYTg5ZTUgPSAkKCc8ZGl2IGlkPSJodG1sX2Q1MmRjZWJmNTM0MDQxYWFiNmY1OGVjN2NhMWE4OWU1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5EZXNpZ24gRXhjaGFuZ2UsVG9yb250byBEb21pbmlvbiBDZW50cmUsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOThlMDgyMmMxYmRlNGE4ZmJhOWQ4OTdjNDNmMTU2MWQuc2V0Q29udGVudChodG1sX2Q1MmRjZWJmNTM0MDQxYWFiNmY1OGVjN2NhMWE4OWU1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y0YzAxNjk1MWE3NzQyNzdhZWQ5MzY0M2IxYTFlN2ZhLmJpbmRQb3B1cChwb3B1cF85OGUwODIyYzFiZGU0YThmYmE5ZDg5N2M0M2YxNTYxZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yMzE1ZjkwY2JmZWY0OTYzYTRkNGNkYjkwZmUzZjU2MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY0ODE5ODUsLTc5LjM3OTgxNjkwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg5ZDk3MWM0YzBiNzQzOGNiYzc4YzAzNGNkODBiNTg0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzMwM2ZjYjUzNzNmNDRiOWFiNzk4ZDEzMDQ5YWFhZjlkID0gJCgnPGRpdiBpZD0iaHRtbF8zMDNmY2I1MzczZjQ0YjlhYjc5OGQxMzA0OWFhYWY5ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q29tbWVyY2UgQ291cnQsVmljdG9yaWEgSG90ZWwsIERvd250b3duVG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODlkOTcxYzRjMGI3NDM4Y2JjNzhjMDM0Y2Q4MGI1ODQuc2V0Q29udGVudChodG1sXzMwM2ZjYjUzNzNmNDRiOWFiNzk4ZDEzMDQ5YWFhZjlkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzIzMTVmOTBjYmZlZjQ5NjNhNGQ0Y2RiOTBmZTNmNTYxLmJpbmRQb3B1cChwb3B1cF84OWQ5NzFjNGMwYjc0MzhjYmM3OGMwMzRjZDgwYjU4NCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81ZmMwY2FlMzIwMzM0YzUyOWE1ZGQ4MTQxOTliZGFjNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjczMzI4MjUsLTc5LjQxOTc0OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzYyMzk4YmU5NDc5NDI0NWI1YmVjZjM1MWI1MGRiYTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYmVjODQzODc4MTc5NDYwOThmOGNiMzI0NzgwM2ZjMmMgPSAkKCc8ZGl2IGlkPSJodG1sX2JlYzg0Mzg3ODE3OTQ2MDk4ZjhjYjMyNDc4MDNmYzJjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWRmb3JkIFBhcmssTGF3cmVuY2UgTWFub3IgRWFzdCwgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83NjIzOThiZTk0Nzk0MjQ1YjViZWNmMzUxYjUwZGJhOS5zZXRDb250ZW50KGh0bWxfYmVjODQzODc4MTc5NDYwOThmOGNiMzI0NzgwM2ZjMmMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNWZjMGNhZTMyMDMzNGM1MjlhNWRkODE0MTk5YmRhYzcuYmluZFBvcHVwKHBvcHVwXzc2MjM5OGJlOTQ3OTQyNDViNWJlY2YzNTFiNTBkYmE5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2MzNzlkNjBkZmNkMjQ1ZmU4ZDg5NmQ1NWFjMTc3ZmY3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzExNjk0OCwtNzkuNDE2OTM1NTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNmRiY2NlODhmM2FlNDE3YjhhZmMyZDJiMmZjMzI3ZTQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTZhNmQyZDM5NGEzNDAyNzk4OTk3MzEwNGVmOTdlNTcgPSAkKCc8ZGl2IGlkPSJodG1sX2U2YTZkMmQzOTRhMzQwMjc5ODk5NzMxMDRlZjk3ZTU3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlbGF3biwgQ2VudHJhbFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzZkYmNjZTg4ZjNhZTQxN2I4YWZjMmQyYjJmYzMyN2U0LnNldENvbnRlbnQoaHRtbF9lNmE2ZDJkMzk0YTM0MDI3OTg5OTczMTA0ZWY5N2U1Nyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jMzc5ZDYwZGZjZDI0NWZlOGQ4OTZkNTVhYzE3N2ZmNy5iaW5kUG9wdXAocG9wdXBfNmRiY2NlODhmM2FlNDE3YjhhZmMyZDJiMmZjMzI3ZTQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzgwNzljMTJmMTZjNDFkOTkwZDdlZWNhMTA0ZmI2NzMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTY5NDc2LC03OS40MTEzMDcyMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lNWQxZTA2YzUyYzk0ZTg4OTQzMGYyMzczYmMwMWE2NCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jZDQwNGE1YjAxZjU0YzJlOThjYmJiNjdjY2FjY2I2ZCA9ICQoJzxkaXYgaWQ9Imh0bWxfY2Q0MDRhNWIwMWY1NGMyZTk4Y2JiYjY3Y2NhY2NiNmQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZvcmVzdCBIaWxsIE5vcnRoLEZvcmVzdCBIaWxsIFdlc3QsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lNWQxZTA2YzUyYzk0ZTg4OTQzMGYyMzczYmMwMWE2NC5zZXRDb250ZW50KGh0bWxfY2Q0MDRhNWIwMWY1NGMyZTk4Y2JiYjY3Y2NhY2NiNmQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzgwNzljMTJmMTZjNDFkOTkwZDdlZWNhMTA0ZmI2NzMuYmluZFBvcHVwKHBvcHVwX2U1ZDFlMDZjNTJjOTRlODg5NDMwZjIzNzNiYzAxYTY0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2QxNWRjYmMyNTU3MDQyOTBiZjA5YzBlMGE0MTFlMDg4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjcyNzA5NywtNzkuNDA1Njc4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOWI4Nzk5NDFhNmVhNDI2Y2IzYTBiMzM4MTE1ZjEyNWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDkwMzhhYzMwNzJhNDJjY2EwODk0OTY1MWM3Nzg3MzggPSAkKCc8ZGl2IGlkPSJodG1sXzA5MDM4YWMzMDcyYTQyY2NhMDg5NDk2NTFjNzc4NzM4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgQW5uZXgsTm9ydGggTWlkdG93bixZb3JrdmlsbGUsIENlbnRyYWxUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85Yjg3OTk0MWE2ZWE0MjZjYjNhMGIzMzgxMTVmMTI1Yy5zZXRDb250ZW50KGh0bWxfMDkwMzhhYzMwNzJhNDJjY2EwODk0OTY1MWM3Nzg3MzgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDE1ZGNiYzI1NTcwNDI5MGJmMDljMGUwYTQxMWUwODguYmluZFBvcHVwKHBvcHVwXzliODc5OTQxYTZlYTQyNmNiM2EwYjMzODExNWYxMjVjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzAxYjY0MjZkYTllMzRmZDE4NTJhMGU3MzMxMTE1MmU2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjYyNjk1NiwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hYzM3NDIzNTIyZjA0MjYyODc0MjM4ZGM1N2Y0Nzk3ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jY2NkMmNiYWU2NmY0NWUzYmUzMWJlZjk5ZTQxYTFjMSA9ICQoJzxkaXYgaWQ9Imh0bWxfY2NjZDJjYmFlNjZmNDVlM2JlMzFiZWY5OWU0MWExYzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhhcmJvcmQsVW5pdmVyc2l0eSBvZiBUb3JvbnRvLCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FjMzc0MjM1MjJmMDQyNjI4NzQyMzhkYzU3ZjQ3OTdmLnNldENvbnRlbnQoaHRtbF9jY2NkMmNiYWU2NmY0NWUzYmUzMWJlZjk5ZTQxYTFjMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wMWI2NDI2ZGE5ZTM0ZmQxODUyYTBlNzMzMTExNTJlNi5iaW5kUG9wdXAocG9wdXBfYWMzNzQyMzUyMmYwNDI2Mjg3NDIzOGRjNTdmNDc5N2YpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzMzYmJkNWMzNzZlNDZjMDlmYzFjNWMyNDkwOGE4NmMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTMyMDU3LC03OS40MDAwNDkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2IyZTA5ZjFmYWRhNjQ5ZDQ4ZmQ0ZTdjYmYyMDA3YTM1ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzdkYTRjZDAwZTYxMDQ5MmJiMzE0ZGY4MTkxZDM3MTU4ID0gJCgnPGRpdiBpZD0iaHRtbF83ZGE0Y2QwMGU2MTA0OTJiYjMxNGRmODE5MWQzNzE1OCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2hpbmF0b3duLEdyYW5nZSBQYXJrLEtlbnNpbmd0b24gTWFya2V0LCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2IyZTA5ZjFmYWRhNjQ5ZDQ4ZmQ0ZTdjYmYyMDA3YTM1LnNldENvbnRlbnQoaHRtbF83ZGE0Y2QwMGU2MTA0OTJiYjMxNGRmODE5MWQzNzE1OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMzNiYmQ1YzM3NmU0NmMwOWZjMWM1YzI0OTA4YTg2Yy5iaW5kUG9wdXAocG9wdXBfYjJlMDlmMWZhZGE2NDlkNDhmZDRlN2NiZjIwMDdhMzUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWU4Njk5YTI4OTNjNDE1MDg5OTAwZTVjYjZkMWZmMjEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Mjg5NDY3LC03OS4zOTQ0MTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzZkNGRjZDE5OWI2MDRjMWJhYTQ2MzJkMmNjOGJmMjk0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRjYzExZmFlNjU4NjQzM2ZhNmRhOWZjMThiZDk0NTFhID0gJCgnPGRpdiBpZD0iaHRtbF80Y2MxMWZhZTY1ODY0MzNmYTZkYTlmYzE4YmQ5NDUxYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q04gVG93ZXIsQmF0aHVyc3QgUXVheSxJc2xhbmQgYWlycG9ydCxIYXJib3VyZnJvbnQgV2VzdCxLaW5nIGFuZCBTcGFkaW5hLFJhaWx3YXkgTGFuZHMsU291dGggTmlhZ2FyYSwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82ZDRkY2QxOTliNjA0YzFiYWE0NjMyZDJjYzhiZjI5NC5zZXRDb250ZW50KGh0bWxfNGNjMTFmYWU2NTg2NDMzZmE2ZGE5ZmMxOGJkOTQ1MWEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWU4Njk5YTI4OTNjNDE1MDg5OTAwZTVjYjZkMWZmMjEuYmluZFBvcHVwKHBvcHVwXzZkNGRjZDE5OWI2MDRjMWJhYTQ2MzJkMmNjOGJmMjk0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U1ZWNlODMzMWIzZjRiOGRhNTc1MGY0ZDg2NWI0YWJiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ2NDM1MiwtNzkuMzc0ODQ1OTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWEwMzk0ZTA3YzdlNDM4NDljMzY5YjczZmU0ODI0OGQgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWZjOTA1YjE0NWVjNDc2MDg2MzhjZDVlZjFkYmI0YjEgPSAkKCc8ZGl2IGlkPSJodG1sXzVmYzkwNWIxNDVlYzQ3NjA4NjM4Y2Q1ZWYxZGJiNGIxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdG4gQSBQTyBCb3hlcyAyNSBUaGUgRXNwbGFuYWRlLCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFhMDM5NGUwN2M3ZTQzODQ5YzM2OWI3M2ZlNDgyNDhkLnNldENvbnRlbnQoaHRtbF81ZmM5MDViMTQ1ZWM0NzYwODYzOGNkNWVmMWRiYjRiMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNWVjZTgzMzFiM2Y0YjhkYTU3NTBmNGQ4NjViNGFiYi5iaW5kUG9wdXAocG9wdXBfMWEwMzk0ZTA3YzdlNDM4NDljMzY5YjczZmU0ODI0OGQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzBlYmQ2Y2I2NDlmNDljZDg4NWIwNDhlOGE4MmM1YmEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDg0MjkyLC03OS4zODIyODAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2FmYzQzZWQwOTdkZTQzMDhhYjQ3MDdkZTBkNDUzZjE3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzllZjYwMzNlZTI4ZTQ1ZGI5NjcyMjJmNGY5MTY5OWNkID0gJCgnPGRpdiBpZD0iaHRtbF85ZWY2MDMzZWUyOGU0NWRiOTY3MjIyZjRmOTE2OTljZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rmlyc3QgQ2FuYWRpYW4gUGxhY2UsVW5kZXJncm91bmQgY2l0eSwgRG93bnRvd25Ub3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hZmM0M2VkMDk3ZGU0MzA4YWI0NzA3ZGUwZDQ1M2YxNy5zZXRDb250ZW50KGh0bWxfOWVmNjAzM2VlMjhlNDVkYjk2NzIyMmY0ZjkxNjk5Y2QpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzBlYmQ2Y2I2NDlmNDljZDg4NWIwNDhlOGE4MmM1YmEuYmluZFBvcHVwKHBvcHVwX2FmYzQzZWQwOTdkZTQzMDhhYjQ3MDdkZTBkNDUzZjE3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2NjOWI3ZTA3NGIzODRlZTBhMDIxNWRhMmNjYzBhOWE5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE4NTE3OTk5OTk5OTk2LC03OS40NjQ3NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82NTc5NzFkOTI1ZmE0MjhiYmJlMjE0MzI1NWU2NDI4ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yZDcyODJlNjhjYzU0MjcwYTIxMGQ5MDVmMjIwN2Q0NyA9ICQoJzxkaXYgaWQ9Imh0bWxfMmQ3MjgyZTY4Y2M1NDI3MGEyMTBkOTA1ZjIyMDdkNDciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIEhlaWdodHMsTGF3cmVuY2UgTWFub3IsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjU3OTcxZDkyNWZhNDI4YmJiZTIxNDMyNTVlNjQyOGYuc2V0Q29udGVudChodG1sXzJkNzI4MmU2OGNjNTQyNzBhMjEwZDkwNWYyMjA3ZDQ3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2NjOWI3ZTA3NGIzODRlZTBhMDIxNWRhMmNjYzBhOWE5LmJpbmRQb3B1cChwb3B1cF82NTc5NzFkOTI1ZmE0MjhiYmJlMjE0MzI1NWU2NDI4Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85OTBkMDRlZGIwNWU0ZTA1OGQwYTlkODRkYTk4ZmNmYyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcwOTU3NywtNzkuNDQ1MDcyNTk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfOGZjOWZhM2RlYjczNGZhZTk4NWY0ZjBjYzMzYTU1ZjEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMWQyZDJlYjk3MWZiNDJmYTkzM2U1ZWM1YmQ0Y2JmMjYgPSAkKCc8ZGl2IGlkPSJodG1sXzFkMmQyZWI5NzFmYjQyZmE5MzNlNWVjNWJkNGNiZjI2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HbGVuY2Fpcm4sIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGZjOWZhM2RlYjczNGZhZTk4NWY0ZjBjYzMzYTU1ZjEuc2V0Q29udGVudChodG1sXzFkMmQyZWI5NzFmYjQyZmE5MzNlNWVjNWJkNGNiZjI2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk5MGQwNGVkYjA1ZTRlMDU4ZDBhOWQ4NGRhOThmY2ZjLmJpbmRQb3B1cChwb3B1cF84ZmM5ZmEzZGViNzM0ZmFlOTg1ZjRmMGNjMzNhNTVmMSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hMDZkNjU1MzUzYzI0NzBiYmRhMzZhZjIzZDk5MmFlYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5Mzc4MTMsLTc5LjQyODE5MTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzVmNWRiM2Q5ZTViYjRhZjk5N2M0YTg4ZTEyZjM1NmYzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Y3M2VmMGMzMjRlMDQ5YmE5MTk4NDFjYzAwODY4NzM1ID0gJCgnPGRpdiBpZD0iaHRtbF9mNzNlZjBjMzI0ZTA0OWJhOTE5ODQxY2MwMDg2ODczNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtZXdvb2QtQ2VkYXJ2YWxlLCBZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81ZjVkYjNkOWU1YmI0YWY5OTdjNGE4OGUxMmYzNTZmMy5zZXRDb250ZW50KGh0bWxfZjczZWYwYzMyNGUwNDliYTkxOTg0MWNjMDA4Njg3MzUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTA2ZDY1NTM1M2MyNDcwYmJkYTM2YWYyM2Q5OTJhZWEuYmluZFBvcHVwKHBvcHVwXzVmNWRiM2Q5ZTViYjRhZjk5N2M0YTg4ZTEyZjM1NmYzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2UyYjQ2ZmVlODY4MTRlNjU5MDhjNWM0NjBkZDkyNWQ3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg5MDI1NiwtNzkuNDUzNTEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzRmODc2YjJmMDM0MjQ0NjU5NTdjZjFiZmZhMmExYzg3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzk1MTI4MGY3ZGFlNDQ2ZmE4ZDNkNWU4MTEzODhkMWU2ID0gJCgnPGRpdiBpZD0iaHRtbF85NTEyODBmN2RhZTQ0NmZhOGQzZDVlODExMzg4ZDFlNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FsZWRvbmlhLUZhaXJiYW5rcywgWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNGY4NzZiMmYwMzQyNDQ2NTk1N2NmMWJmZmEyYTFjODcuc2V0Q29udGVudChodG1sXzk1MTI4MGY3ZGFlNDQ2ZmE4ZDNkNWU4MTEzODhkMWU2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2UyYjQ2ZmVlODY4MTRlNjU5MDhjNWM0NjBkZDkyNWQ3LmJpbmRQb3B1cChwb3B1cF80Zjg3NmIyZjAzNDI0NDY1OTU3Y2YxYmZmYTJhMWM4Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wYWNhZjJjZjdjMmY0NGEwYTkxYzFjMDA1ZTlhNGJkZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2OTU0MiwtNzkuNDIyNTYzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84MTkxMTI4ZjVmYjI0N2FhODUzM2I4NjYwNWFlMmMxYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hMTM4NjQ2ODk5ZDA0ODViOTBiMDI2MzlkOTZhMGZlNSA9ICQoJzxkaXYgaWQ9Imh0bWxfYTEzODY0Njg5OWQwNDg1YjkwYjAyNjM5ZDk2YTBmZTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNocmlzdGllLCBEb3dudG93blRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzgxOTExMjhmNWZiMjQ3YWE4NTMzYjg2NjA1YWUyYzFjLnNldENvbnRlbnQoaHRtbF9hMTM4NjQ2ODk5ZDA0ODViOTBiMDI2MzlkOTZhMGZlNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wYWNhZjJjZjdjMmY0NGEwYTkxYzFjMDA1ZTlhNGJkZi5iaW5kUG9wdXAocG9wdXBfODE5MTEyOGY1ZmIyNDdhYTg1MzNiODY2MDVhZTJjMWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjM1Nzk3NTZjMmY3NGQzZTkwMDI2ZTg0ODg1MjRhYTYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjkwMDUxMDAwMDAwMSwtNzkuNDQyMjU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mODY2MDYzYzBlMzA0OGE4OGIzZDI5NmQwZDdkYmRhNSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iOGQ2MDFjYzYxZTk0OTQyODRkMGQ2ZjMxYjZmOGQ0MSA9ICQoJzxkaXYgaWQ9Imh0bWxfYjhkNjAxY2M2MWU5NDk0Mjg0ZDBkNmYzMWI2ZjhkNDEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvdmVyY291cnQgVmlsbGFnZSxEdWZmZXJpbiwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y4NjYwNjNjMGUzMDQ4YTg4YjNkMjk2ZDBkN2RiZGE1LnNldENvbnRlbnQoaHRtbF9iOGQ2MDFjYzYxZTk0OTQyODRkMGQ2ZjMxYjZmOGQ0MSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82MzU3OTc1NmMyZjc0ZDNlOTAwMjZlODQ4ODUyNGFhNi5iaW5kUG9wdXAocG9wdXBfZjg2NjA2M2MwZTMwNDhhODhiM2QyOTZkMGQ3ZGJkYTUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTEzMmQ3MDFiNGNlNGUzNmJmN2M5NzUxZWQ1NTRmYTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDc5MjY3MDAwMDAwMDYsLTc5LjQxOTc0OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYThkNjc3ZjE3MzA1NDE3ODgxZmFjMzliYTAzMTk3YzcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMWM2Njc2OGE5NjcwNGI4M2FkMjc3MGUwYzBlMTJjOWUgPSAkKCc8ZGl2IGlkPSJodG1sXzFjNjY3NjhhOTY3MDRiODNhZDI3NzBlMGMwZTEyYzllIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5MaXR0bGUgUG9ydHVnYWwsVHJpbml0eSwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2E4ZDY3N2YxNzMwNTQxNzg4MWZhYzM5YmEwMzE5N2M3LnNldENvbnRlbnQoaHRtbF8xYzY2NzY4YTk2NzA0YjgzYWQyNzcwZTBjMGUxMmM5ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xMTMyZDcwMWI0Y2U0ZTM2YmY3Yzk3NTFlZDU1NGZhMS5iaW5kUG9wdXAocG9wdXBfYThkNjc3ZjE3MzA1NDE3ODgxZmFjMzliYTAzMTk3YzcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTI0YjI5MTgzMTAzNDRkYmJkZjdmZTExNGQ4ODhkYTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MzY4NDcyLC03OS40MjgxOTE0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mNzI1NzQ4Yjc1OWI0Y2U3OTg3OTczZWQ2MjY5YjQxYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81ODYxNDI0ZTUxMDc0OGYwODMzZTYwODY5NjJjZTZhZCA9ICQoJzxkaXYgaWQ9Imh0bWxfNTg2MTQyNGU1MTA3NDhmMDgzM2U2MDg2OTYyY2U2YWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJyb2NrdG9uLEV4aGliaXRpb24gUGxhY2UsUGFya2RhbGUgVmlsbGFnZSwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Y3MjU3NDhiNzU5YjRjZTc5ODc5NzNlZDYyNjliNDFjLnNldENvbnRlbnQoaHRtbF81ODYxNDI0ZTUxMDc0OGYwODMzZTYwODY5NjJjZTZhZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81MjRiMjkxODMxMDM0NGRiYmRmN2ZlMTE0ZDg4OGRhMS5iaW5kUG9wdXAocG9wdXBfZjcyNTc0OGI3NTliNGNlNzk4Nzk3M2VkNjI2OWI0MWMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYzMzNjgyYjQwMTdhNGQyMmFmODFlYTYyMGZiZThiZTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MTM3NTYyMDAwMDAwMDYsLTc5LjQ5MDA3MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzY5ZjU4NmYwODY0NGQ2NmI3MGJjZmViNDUxZGJmMTEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTVmMDQ5YmVlZDhmNDFjNTg0MzY5MDIzZDZhODU2NjUgPSAkKCc8ZGl2IGlkPSJodG1sXzU1ZjA0OWJlZWQ4ZjQxYzU4NDM2OTAyM2Q2YTg1NjY1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb3duc3ZpZXcsTm9ydGggUGFyayxVcHdvb2QgUGFyaywgTm9ydGhZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jNjlmNTg2ZjA4NjQ0ZDY2YjcwYmNmZWI0NTFkYmYxMS5zZXRDb250ZW50KGh0bWxfNTVmMDQ5YmVlZDhmNDFjNTg0MzY5MDIzZDZhODU2NjUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzMzNjgyYjQwMTdhNGQyMmFmODFlYTYyMGZiZThiZTguYmluZFBvcHVwKHBvcHVwX2M2OWY1ODZmMDg2NDRkNjZiNzBiY2ZlYjQ1MWRiZjExKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2ZiMWY1ZGViYWVlODRkZDk4NzA2NzU0YTc2N2U1YTQ4ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjkxMTE1OCwtNzkuNDc2MDEzMjk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZjg4YzM2MjljM2ZmNGZlYWI4N2JjOTNhZGE3MzUwZTUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2IxZDgzMTY5OWZmNGNkYTgxOWYyNzFkY2NhYjQ5NzMgPSAkKCc8ZGl2IGlkPSJodG1sXzdiMWQ4MzE2OTlmZjRjZGE4MTlmMjcxZGNjYWI0OTczIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5EZWwgUmF5LEtlZWxlc2RhbGUsTW91bnQgRGVubmlzLFNpbHZlcnRob3JuLCBZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mODhjMzYyOWMzZmY0ZmVhYjg3YmM5M2FkYTczNTBlNS5zZXRDb250ZW50KGh0bWxfN2IxZDgzMTY5OWZmNGNkYTgxOWYyNzFkY2NhYjQ5NzMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZmIxZjVkZWJhZWU4NGRkOTg3MDY3NTRhNzY3ZTVhNDguYmluZFBvcHVwKHBvcHVwX2Y4OGMzNjI5YzNmZjRmZWFiODdiYzkzYWRhNzM1MGU1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk3ZDM3ZTQ1MTQ3MzRiYWRhMDQwZDEyOTk1YWYyODAxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjczMTg1Mjk5OTk5OTksLTc5LjQ4NzI2MTkwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzczMmNiYWJjZjE1NDRkMWNiZDcyZTg3MmFjMjNmYjZiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzVmMTNiZTJiNWYzODQyN2VhYTM2NGZjMjJlZDA2MDU3ID0gJCgnPGRpdiBpZD0iaHRtbF81ZjEzYmUyYjVmMzg0MjdlYWEzNjRmYzIyZWQwNjA1NyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhlIEp1bmN0aW9uIE5vcnRoLFJ1bm55bWVkZSwgWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNzMyY2JhYmNmMTU0NGQxY2JkNzJlODcyYWMyM2ZiNmIuc2V0Q29udGVudChodG1sXzVmMTNiZTJiNWYzODQyN2VhYTM2NGZjMjJlZDA2MDU3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzk3ZDM3ZTQ1MTQ3MzRiYWRhMDQwZDEyOTk1YWYyODAxLmJpbmRQb3B1cChwb3B1cF83MzJjYmFiY2YxNTQ0ZDFjYmQ3MmU4NzJhYzIzZmI2Yik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84NDJmN2NjYjllY2Q0MDgyODI1NDM4NzNkZDk0MTQwMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MTYwODMsLTc5LjQ2NDc2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NmNTdhYjE0ZjY4NDQyYTRhNjE0MzM3NjY1ZTQ0YTM3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzU1YjY4ZDk4YTcwYTQyNGU5NzZiN2QxMWU3MzZmNzE2ID0gJCgnPGRpdiBpZD0iaHRtbF81NWI2OGQ5OGE3MGE0MjRlOTc2YjdkMTFlNzM2ZjcxNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaCBQYXJrLFRoZSBKdW5jdGlvbiBTb3V0aCwgV2VzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2NmNTdhYjE0ZjY4NDQyYTRhNjE0MzM3NjY1ZTQ0YTM3LnNldENvbnRlbnQoaHRtbF81NWI2OGQ5OGE3MGE0MjRlOTc2YjdkMTFlNzM2ZjcxNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84NDJmN2NjYjllY2Q0MDgyODI1NDM4NzNkZDk0MTQwMC5iaW5kUG9wdXAocG9wdXBfY2Y1N2FiMTRmNjg0NDJhNGE2MTQzMzc2NjVlNDRhMzcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzU1N2ExY2QxYWYzNDNjNGFkYzNmNTgyODExNGUyOTggPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDg5NTk3LC03OS40NTYzMjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDU2ZTAyMDA0ZmNhNDljMmE0NTE1NDJkY2U4ZDA4ZjIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjRjZjViNWJmMTA1NDk3ZmE0NDlmMjA0NTFhMjM0MTggPSAkKCc8ZGl2IGlkPSJodG1sX2Y0Y2Y1YjViZjEwNTQ5N2ZhNDQ5ZjIwNDUxYTIzNDE4IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrZGFsZSxSb25jZXN2YWxsZXMsIFdlc3RUb3JvbnRvPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80NTZlMDIwMDRmY2E0OWMyYTQ1MTU0MmRjZThkMDhmMi5zZXRDb250ZW50KGh0bWxfZjRjZjViNWJmMTA1NDk3ZmE0NDlmMjA0NTFhMjM0MTgpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzU1N2ExY2QxYWYzNDNjNGFkYzNmNTgyODExNGUyOTguYmluZFBvcHVwKHBvcHVwXzQ1NmUwMjAwNGZjYTQ5YzJhNDUxNTQyZGNlOGQwOGYyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2FlZDgwNGUyZGFmYTQ5ODk4NDM3OTVmOGJiMTU2NzgyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUxNTcwNiwtNzkuNDg0NDQ5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wZDVkZDM2NDc4OGE0NGM0YWI1NGM1YWM4MmZmYjBhMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kMDcwZTlmNzlkMDY0ZDdlYmFlODU2MWQ0ZjU5MTk3ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfZDA3MGU5Zjc5ZDA2NGQ3ZWJhZTg1NjFkNGY1OTE5N2YiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJ1bm55bWVkZSxTd2Fuc2VhLCBXZXN0VG9yb250bzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMGQ1ZGQzNjQ3ODhhNDRjNGFiNTRjNWFjODJmZmIwYTIuc2V0Q29udGVudChodG1sX2QwNzBlOWY3OWQwNjRkN2ViYWU4NTYxZDRmNTkxOTdmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2FlZDgwNGUyZGFmYTQ5ODk4NDM3OTVmOGJiMTU2NzgyLmJpbmRQb3B1cChwb3B1cF8wZDVkZDM2NDc4OGE0NGM0YWI1NGM1YWM4MmZmYjBhMik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yN2U0YjQyNGY0Yzc0MTJmOTc1YWI0MDg1OWE2YzQ3MyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MjMwMTUsLTc5LjM4OTQ5MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfY2MzNThhNWE2NTgzNGRiZDkxNTFhMjMyZWI5MDIzMzkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTM3M2MxNDhjOTU0NDc4Mjk0MDNmNDA5ZmYzYzFhYTQgPSAkKCc8ZGl2IGlkPSJodG1sXzkzNzNjMTQ4Yzk1NDQ3ODI5NDAzZjQwOWZmM2MxYWE0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5RdWVlbiYjMzk7cyBQYXJrLCBRdWVlbiYjMzk7c1Bhcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2NjMzU4YTVhNjU4MzRkYmQ5MTUxYTIzMmViOTAyMzM5LnNldENvbnRlbnQoaHRtbF85MzczYzE0OGM5NTQ0NzgyOTQwM2Y0MDlmZjNjMWFhNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yN2U0YjQyNGY0Yzc0MTJmOTc1YWI0MDg1OWE2YzQ3My5iaW5kUG9wdXAocG9wdXBfY2MzNThhNWE2NTgzNGRiZDkxNTFhMjMyZWI5MDIzMzkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTFlNjZlMjIwOTM4NGRiZGE4ZjJlOTAzOTc4ZmE5NzMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MzY5NjU2LC03OS42MTU4MTg5OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83ODIwZGY3Mzk4NDM0NjVlYmZkNWEzOWQ1ODViYzZmNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83YjQ1ZmUzZGM1MGM0NjZmOTU2MzM4ZDBhZDdmYjBhYiA9ICQoJzxkaXYgaWQ9Imh0bWxfN2I0NWZlM2RjNTBjNDY2Zjk1NjMzOGQwYWQ3ZmIwYWIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNhbmFkYSBQb3N0IEdhdGV3YXkgUHJvY2Vzc2luZyBDZW50cmUsIE1pc3Npc3NhdWdhPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83ODIwZGY3Mzk4NDM0NjVlYmZkNWEzOWQ1ODViYzZmNy5zZXRDb250ZW50KGh0bWxfN2I0NWZlM2RjNTBjNDY2Zjk1NjMzOGQwYWQ3ZmIwYWIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTFlNjZlMjIwOTM4NGRiZGE4ZjJlOTAzOTc4ZmE5NzMuYmluZFBvcHVwKHBvcHVwXzc4MjBkZjczOTg0MzQ2NWViZmQ1YTM5ZDU4NWJjNmY3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzE2MDhiNzZkMGIyOTQ2MWViMDZkMGU1OWVlZmFkODkzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjYyNzQzOSwtNzkuMzIxNTU4XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg2ZGJlNmY5MjcyZDQzZmNhNWQ2MTM1OTY5ZGNmZjA3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzBmYjMxY2UxMDAyNjQyODA5NmJlOGQyNGRiMzg0NzA5ID0gJCgnPGRpdiBpZD0iaHRtbF8wZmIzMWNlMTAwMjY0MjgwOTZiZThkMjRkYjM4NDcwOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnVzaW5lc3MgUmVwbHkgTWFpbCBQcm9jZXNzaW5nIENlbnRyZSA5NjkgRWFzdGVybiwgRWFzdFRvcm9udG88L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg2ZGJlNmY5MjcyZDQzZmNhNWQ2MTM1OTY5ZGNmZjA3LnNldENvbnRlbnQoaHRtbF8wZmIzMWNlMTAwMjY0MjgwOTZiZThkMjRkYjM4NDcwOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xNjA4Yjc2ZDBiMjk0NjFlYjA2ZDBlNTllZWZhZDg5My5iaW5kUG9wdXAocG9wdXBfODZkYmU2ZjkyNzJkNDNmY2E1ZDYxMzU5NjlkY2ZmMDcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNzdlMTg3ZTRiN2ZmNDhlYmE0ZjA3ZGY2NDcyZTAxNzEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MDU2NDY2LC03OS41MDEzMjA3MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xOTE5MTNjYjk4OTg0NWRkYWFiODYyMzQ0NDVlNDgxMCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iODEzOGExOGY3MjI0MGQ3YWMzNmM2NGU3OWUwMDA1ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfYjgxMzhhMThmNzIyNDBkN2FjMzZjNjRlNzllMDAwNWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWJlciBCYXkgU2hvcmVzLE1pbWljbyBTb3V0aCxOZXcgVG9yb250bywgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xOTE5MTNjYjk4OTg0NWRkYWFiODYyMzQ0NDVlNDgxMC5zZXRDb250ZW50KGh0bWxfYjgxMzhhMThmNzIyNDBkN2FjMzZjNjRlNzllMDAwNWYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNzdlMTg3ZTRiN2ZmNDhlYmE0ZjA3ZGY2NDcyZTAxNzEuYmluZFBvcHVwKHBvcHVwXzE5MTkxM2NiOTg5ODQ1ZGRhYWI4NjIzNDQ0NWU0ODEwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2EzMTE5ZDA4MDAzZjRmNjc4ZGM1Y2NiMTk0ZjExYWFjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjAyNDEzNzAwMDAwMDEsLTc5LjU0MzQ4NDA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzdiZjYxMzYxZjIxMzQ4ZjJiMmViNjNjZjA0MDU2MjBkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2FiMGM3ZDRlMTc2ZjQ4YTg4MmJhZTg5NjFiZDRlMjNlID0gJCgnPGRpdiBpZD0iaHRtbF9hYjBjN2Q0ZTE3NmY0OGE4ODJiYWU4OTYxYmQ0ZTIzZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWxkZXJ3b29kLExvbmcgQnJhbmNoLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzdiZjYxMzYxZjIxMzQ4ZjJiMmViNjNjZjA0MDU2MjBkLnNldENvbnRlbnQoaHRtbF9hYjBjN2Q0ZTE3NmY0OGE4ODJiYWU4OTYxYmQ0ZTIzZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hMzExOWQwODAwM2Y0ZjY3OGRjNWNjYjE5NGYxMWFhYy5iaW5kUG9wdXAocG9wdXBfN2JmNjEzNjFmMjEzNDhmMmIyZWI2M2NmMDQwNTYyMGQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNDMzOTgxYzBjNmM3NDZkMWE5YmZhYmMyMDE0ZjQyY2QgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTM2NTM2MDAwMDAwMDUsLTc5LjUwNjk0MzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWMzZjFkMTU0OWY5NDBkMTg1YmNlNThmN2ViYzgyYzMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNDg4NmE5YTA3OTAwNDlhMWE5YmU2YzgyMzMyODdhZmUgPSAkKCc8ZGl2IGlkPSJodG1sXzQ4ODZhOWEwNzkwMDQ5YTFhOWJlNmM4MjMzMjg3YWZlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgS2luZ3N3YXksTW9udGdvbWVyeSBSb2FkLE9sZCBNaWxsIE5vcnRoLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2FjM2YxZDE1NDlmOTQwZDE4NWJjZTU4ZjdlYmM4MmMzLnNldENvbnRlbnQoaHRtbF80ODg2YTlhMDc5MDA0OWExYTliZTZjODIzMzI4N2FmZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MzM5ODFjMGM2Yzc0NmQxYTliZmFiYzIwMTRmNDJjZC5iaW5kUG9wdXAocG9wdXBfYWMzZjFkMTU0OWY5NDBkMTg1YmNlNThmN2ViYzgyYzMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZGE4ZjhlMjhhZWJkNGY5OGE4NzJmNjA1NGQ3ODI1MmIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42MzYyNTc5LC03OS40OTg1MDkwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85YjczZGQ3YzQ2YjE0YmUzYjU5YmEyYWJhNTA2YmU4MSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNGE1MDhmMTAwYzI0YWU3YjkzZDBmMmFjNzM1ZDQ3MSA9ICQoJzxkaXYgaWQ9Imh0bWxfMTRhNTA4ZjEwMGMyNGFlN2I5M2QwZjJhYzczNWQ0NzEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWJlciBCYXksS2luZyYjMzk7cyBNaWxsIFBhcmssS2luZ3N3YXkgUGFyayBTb3V0aCBFYXN0LE1pbWljbyBORSxPbGQgTWlsbCBTb3V0aCxUaGUgUXVlZW5zd2F5IEVhc3QsUm95YWwgWW9yayBTb3V0aCBFYXN0LFN1bm55bGVhLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzliNzNkZDdjNDZiMTRiZTNiNTliYTJhYmE1MDZiZTgxLnNldENvbnRlbnQoaHRtbF8xNGE1MDhmMTAwYzI0YWU3YjkzZDBmMmFjNzM1ZDQ3MSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kYThmOGUyOGFlYmQ0Zjk4YTg3MmY2MDU0ZDc4MjUyYi5iaW5kUG9wdXAocG9wdXBfOWI3M2RkN2M0NmIxNGJlM2I1OWJhMmFiYTUwNmJlODEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDI5OGUwZTljOGNhNGRlZThmYzcyZTJkNWNlZTcyNGYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Mjg4NDA4LC03OS41MjA5OTk0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84NjE5ZGMyNDlhODA0NTZhOTU2MWY2M2Q5MzBhMzRiOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF85ZDE3NjJkMzRiOGQ0ZDA5YjJjNTg5OWIxNzdmMDZiMiA9ICQoJzxkaXYgaWQ9Imh0bWxfOWQxNzYyZDM0YjhkNGQwOWIyYzU4OTliMTc3ZjA2YjIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPktpbmdzd2F5IFBhcmsgU291dGggV2VzdCxNaW1pY28gTlcsVGhlIFF1ZWVuc3dheSBXZXN0LFJveWFsIFlvcmsgU291dGggV2VzdCxTb3V0aCBvZiBCbG9vciwgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84NjE5ZGMyNDlhODA0NTZhOTU2MWY2M2Q5MzBhMzRiOC5zZXRDb250ZW50KGh0bWxfOWQxNzYyZDM0YjhkNGQwOWIyYzU4OTliMTc3ZjA2YjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMDI5OGUwZTljOGNhNGRlZThmYzcyZTJkNWNlZTcyNGYuYmluZFBvcHVwKHBvcHVwXzg2MTlkYzI0OWE4MDQ1NmE5NTYxZjYzZDkzMGEzNGI4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2U1Y2E3NDgwODI2OTQ3NThhNTliYmViZmMyNWNhNzcwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY3ODU1NiwtNzkuNTMyMjQyNDAwMDAwMDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYTNlODdkNDdmN2QwNGIxMTlkNmM2MDZiYzc1MzljZDggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODRlMDljMmVkZDQ5NGMwZjgyYTY4NGU0NDIwNDczMGEgPSAkKCc8ZGl2IGlkPSJodG1sXzg0ZTA5YzJlZGQ0OTRjMGY4MmE2ODRlNDQyMDQ3MzBhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Jc2xpbmd0b24gQXZlbnVlLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2EzZTg3ZDQ3ZjdkMDRiMTE5ZDZjNjA2YmM3NTM5Y2Q4LnNldENvbnRlbnQoaHRtbF84NGUwOWMyZWRkNDk0YzBmODJhNjg0ZTQ0MjA0NzMwYSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lNWNhNzQ4MDgyNjk0NzU4YTU5YmJlYmZjMjVjYTc3MC5iaW5kUG9wdXAocG9wdXBfYTNlODdkNDdmN2QwNGIxMTlkNmM2MDZiYzc1MzljZDgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmExYzU0Y2Y3ZGUzNGFmNTkzZTFkNDVhZDhlODY2NzkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTA5NDMyLC03OS41NTQ3MjQ0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lMjMxNmZjZTdhNzc0ZWEwYTg4NjQ0ZWUxNmI1ODA3YyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lNGQxOTJkY2E1ZDI0ZTBkOGVlNWFhM2JmM2NkMGQyYiA9ICQoJzxkaXYgaWQ9Imh0bWxfZTRkMTkyZGNhNWQyNGUwZDhlZTVhYTNiZjNjZDBkMmIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsb3ZlcmRhbGUsSXNsaW5ndG9uLE1hcnRpbiBHcm92ZSxQcmluY2VzcyBHYXJkZW5zLFdlc3QgRGVhbmUgUGFyaywgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lMjMxNmZjZTdhNzc0ZWEwYTg4NjQ0ZWUxNmI1ODA3Yy5zZXRDb250ZW50KGh0bWxfZTRkMTkyZGNhNWQyNGUwZDhlZTVhYTNiZjNjZDBkMmIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmExYzU0Y2Y3ZGUzNGFmNTkzZTFkNDVhZDhlODY2NzkuYmluZFBvcHVwKHBvcHVwX2UyMzE2ZmNlN2E3NzRlYTBhODg2NDRlZTE2YjU4MDdjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Y0ZWQ3YmI3Yzk0OTQ2MmNiNTYyNjE3YmEwNWMyOGU5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQzNTE1MiwtNzkuNTc3MjAwNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDU2ZTNjYzYyZDcyNDZmZTliM2Y5ZWUwMWQzOWNjZGUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTY0ZWIyM2QxZjZlNGE1ODg0YzFjNzExZDU4NWMwOWEgPSAkKCc8ZGl2IGlkPSJodG1sXzU2NGViMjNkMWY2ZTRhNTg4NGMxYzcxMWQ1ODVjMDlhIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CbG9vcmRhbGUgR2FyZGVucyxFcmluZ2F0ZSxNYXJrbGFuZCBXb29kLE9sZCBCdXJuaGFtdGhvcnBlLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q1NmUzY2M2MmQ3MjQ2ZmU5YjNmOWVlMDFkMzljY2RlLnNldENvbnRlbnQoaHRtbF81NjRlYjIzZDFmNmU0YTU4ODRjMWM3MTFkNTg1YzA5YSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mNGVkN2JiN2M5NDk0NjJjYjU2MjYxN2JhMDVjMjhlOS5iaW5kUG9wdXAocG9wdXBfZDU2ZTNjYzYyZDcyNDZmZTliM2Y5ZWUwMWQzOWNjZGUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmIwODNhN2NjNThiNDIyMWFlMjkzNmRhYzg5YzFkZGQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTYzMDMzLC03OS41NjU5NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lODNlOGJhNzc2ZDU0OTU5OGQwNDU0ODgzYTI3YjVmNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hYzcwN2Y3YTEyOTY0MmFiYjc0NjViOWQxYzgwNGNhZiA9ICQoJzxkaXYgaWQ9Imh0bWxfYWM3MDdmN2ExMjk2NDJhYmI3NDY1YjlkMWM4MDRjYWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWJlciBTdW1taXQsIE5vcnRoWW9yazwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTgzZThiYTc3NmQ1NDk1OThkMDQ1NDg4M2EyN2I1ZjQuc2V0Q29udGVudChodG1sX2FjNzA3ZjdhMTI5NjQyYWJiNzQ2NWI5ZDFjODA0Y2FmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2ZiMDgzYTdjYzU4YjQyMjFhZTI5MzZkYWM4OWMxZGRkLmJpbmRQb3B1cChwb3B1cF9lODNlOGJhNzc2ZDU0OTU5OGQwNDU0ODgzYTI3YjVmNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xNWJhNmNiYzNkNmE0YmFmYWRjZDdkYTAyODU3MDU2MyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNDc2NTksLTc5LjUzMjI0MjQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2EyMDhmY2IwMzg3ZjQxM2I4MmMwMTdkMmFkYzg5ZTJjID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZkMmJjZGRkODJkMTQwM2RhZDc5ZTAxZDllNDUyMGY1ID0gJCgnPGRpdiBpZD0iaHRtbF9mZDJiY2RkZDgyZDE0MDNkYWQ3OWUwMWQ5ZTQ1MjBmNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RW1lcnksSHVtYmVybGVhLCBOb3J0aFlvcms8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2EyMDhmY2IwMzg3ZjQxM2I4MmMwMTdkMmFkYzg5ZTJjLnNldENvbnRlbnQoaHRtbF9mZDJiY2RkZDgyZDE0MDNkYWQ3OWUwMWQ5ZTQ1MjBmNSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xNWJhNmNiYzNkNmE0YmFmYWRjZDdkYTAyODU3MDU2My5iaW5kUG9wdXAocG9wdXBfYTIwOGZjYjAzODdmNDEzYjgyYzAxN2QyYWRjODllMmMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzZkY2U3Y2M1OTU4NGQ0Y2I1M2M2NDY2OGRlNmU5M2MgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MDY4NzYsLTc5LjUxODE4ODQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzkyZDcxMGI1ZTJjZTQzZDA5NTU1MzQwNTg4YzkxNzViID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzMwMTQ2NjE4ZTkwZjQ1MmViZmJjODU0M2Q4OGUwMTlkID0gJCgnPGRpdiBpZD0iaHRtbF8zMDE0NjYxOGU5MGY0NTJlYmZiYzg1NDNkODhlMDE5ZCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2VzdG9uLCBZb3JrPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF85MmQ3MTBiNWUyY2U0M2QwOTU1NTM0MDU4OGM5MTc1Yi5zZXRDb250ZW50KGh0bWxfMzAxNDY2MThlOTBmNDUyZWJmYmM4NTQzZDg4ZTAxOWQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzZkY2U3Y2M1OTU4NGQ0Y2I1M2M2NDY2OGRlNmU5M2MuYmluZFBvcHVwKHBvcHVwXzkyZDcxMGI1ZTJjZTQzZDA5NTU1MzQwNTg4YzkxNzViKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q2ZmM4YmM0Zjc2NzQ4YzJhNzFmZWFkMDM2NWQ3ODZiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjk2MzE5LC03OS41MzIyNDI0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICJibHVlIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzMxODZjYyIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNCwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF83ZDBhNjI4Njc0ZDU0ZTg4YmJkNzU1MmZlMzJkZDdmNCk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83NzY4M2ViMTdmZWE0YzBlYTZmNjhmMjk5MjZiYTNhMSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xYTliODY0ZTNlZGY0YjY4ODI1OWYwYzIyMjZiYjNlMSA9ICQoJzxkaXYgaWQ9Imh0bWxfMWE5Yjg2NGUzZWRmNGI2ODgyNTlmMGMyMjI2YmIzZTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldlc3Rtb3VudCwgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF83NzY4M2ViMTdmZWE0YzBlYTZmNjhmMjk5MjZiYTNhMS5zZXRDb250ZW50KGh0bWxfMWE5Yjg2NGUzZWRmNGI2ODgyNTlmMGMyMjI2YmIzZTEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDZmYzhiYzRmNzY3NDhjMmE3MWZlYWQwMzY1ZDc4NmIuYmluZFBvcHVwKHBvcHVwXzc3NjgzZWIxN2ZlYTRjMGVhNmY2OGYyOTkyNmJhM2ExKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzk3ZTk2MzhjODA3MDQ5ZWJhMGFiNmQ4ZDg4Zjc1NmRkID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg4OTA1NCwtNzkuNTU0NzI0NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNGU5NWRjODk1ZDFhNDc0Mzg0NjMwYmU0NmJhMDc2MjIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWI4YTgzZmFjYTAxNGUyMzg1NTFhOTViZGM3NTE5MzcgPSAkKCc8ZGl2IGlkPSJodG1sX2ViOGE4M2ZhY2EwMTRlMjM4NTUxYTk1YmRjNzUxOTM3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc3ZpZXcgVmlsbGFnZSxNYXJ0aW4gR3JvdmUgR2FyZGVucyxSaWNodmlldyBHYXJkZW5zLFN0LiBQaGlsbGlwcywgRXRvYmljb2tlPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80ZTk1ZGM4OTVkMWE0NzQzODQ2MzBiZTQ2YmEwNzYyMi5zZXRDb250ZW50KGh0bWxfZWI4YTgzZmFjYTAxNGUyMzg1NTFhOTViZGM3NTE5MzcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTdlOTYzOGM4MDcwNDllYmEwYWI2ZDhkODhmNzU2ZGQuYmluZFBvcHVwKHBvcHVwXzRlOTVkYzg5NWQxYTQ3NDM4NDYzMGJlNDZiYTA3NjIyKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2JkZjA2ZTVhZTcyNjQyODQ4Nzk2NzE1MTcwZDEyMGM0ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzM5NDE2Mzk5OTk5OTk2LC03OS41ODg0MzY5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogImJsdWUiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMzE4NmNjIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA0LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzdkMGE2Mjg2NzRkNTRlODhiYmQ3NTUyZmUzMmRkN2Y0KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzI1YWRjMjg2OTIyNDRjOWVhOWRjNDhkMGY0MmM4NDFiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzFmZGJkMGI0YWFmNzRmNTBiOGIyNzZhOGQ4NThmNTg4ID0gJCgnPGRpdiBpZD0iaHRtbF8xZmRiZDBiNGFhZjc0ZjUwYjhiMjc2YThkODU4ZjU4OCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWxiaW9uIEdhcmRlbnMsQmVhdW1vbmQgSGVpZ2h0cyxIdW1iZXJnYXRlLEphbWVzdG93bixNb3VudCBPbGl2ZSxTaWx2ZXJzdG9uZSxTb3V0aCBTdGVlbGVzLFRoaXN0bGV0b3duLCBFdG9iaWNva2U8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI1YWRjMjg2OTIyNDRjOWVhOWRjNDhkMGY0MmM4NDFiLnNldENvbnRlbnQoaHRtbF8xZmRiZDBiNGFhZjc0ZjUwYjhiMjc2YThkODU4ZjU4OCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iZGYwNmU1YWU3MjY0Mjg0ODc5NjcxNTE3MGQxMjBjNC5iaW5kUG9wdXAocG9wdXBfMjVhZGMyODY5MjI0NGM5ZWE5ZGM0OGQwZjQyYzg0MWIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYmIwZjQ2NTk0YjI0NDFhN2I3MGUyNzQ5MDU2OTczZDEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MDY3NDgyOTk5OTk5OTQsLTc5LjU5NDA1NDRdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiYmx1ZSIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMzMTg2Y2MiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDQsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfN2QwYTYyODY3NGQ1NGU4OGJiZDc1NTJmZTMyZGQ3ZjQpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZWYxNGYxNWQ3ZWI2NGM2MjgzYmViM2U5Mzc2MTQ5NTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjU3NjcwYzM1ZWMwNGFkMjlmNWEzN2I1YzU3ZWIzMjcgPSAkKCc8ZGl2IGlkPSJodG1sX2Y1NzY3MGMzNWVjMDRhZDI5ZjVhMzdiNWM1N2ViMzI3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aHdlc3QsIEV0b2JpY29rZTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZWYxNGYxNWQ3ZWI2NGM2MjgzYmViM2U5Mzc2MTQ5NTAuc2V0Q29udGVudChodG1sX2Y1NzY3MGMzNWVjMDRhZDI5ZjVhMzdiNWM1N2ViMzI3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2JiMGY0NjU5NGIyNDQxYTdiNzBlMjc0OTA1Njk3M2QxLmJpbmRQb3B1cChwb3B1cF9lZjE0ZjE1ZDdlYjY0YzYyODNiZWIzZTkzNzYxNDk1MCk7CgogICAgICAgICAgICAKICAgICAgICAKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



# Using Foursquare API to explore the neighborhoods


```python
{
    "tags": [
        "remove_input",
    ]
}
CLIENT_ID = 'XMCICN4YC1PQCMXSJEA2YVR5PRAC4N22MLOUV115WCWNA1HW' 
CLIENT_SECRET = '2VYYN4JX2SG1NTZUOGDOCKY1MRM12V40FV5KYFBMQUBLWRFY' 
VERSION = '20180605' 
```


```python
{
    "tags": [
        "remove_input",
    ]
}
radius = 300
url = 'https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&ll={},{}&v={}&radius={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, radius)
```


```python
results = requests.get(url).json()
```


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
      <td>0</td>
      <td>Downtown Toronto</td>
      <td>Neighborhood</td>
      <td>43.653232</td>
      <td>-79.385296</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Cafe Plenty</td>
      <td>Café</td>
      <td>43.654571</td>
      <td>-79.389450</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Japango</td>
      <td>Sushi Restaurant</td>
      <td>43.655268</td>
      <td>-79.385165</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Sansotei Ramen 三草亭</td>
      <td>Ramen Restaurant</td>
      <td>43.655157</td>
      <td>-79.386501</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Rolltation</td>
      <td>Japanese Restaurant</td>
      <td>43.654918</td>
      <td>-79.387424</td>
    </tr>
  </tbody>
</table>
</div>



Then we explore nearby venues


```python
def getNearbyVenues(names, latitudes, longitudes, radius=500):
    
    venues_list=[]
    for name, lat, lng in zip(names, latitudes, longitudes):
        print(name)
            
        # create the API request URL
        url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}'.format(
            CLIENT_ID, 
            CLIENT_SECRET, 
            VERSION, 
            lat, 
            lng, 
            radius)
            
        # make the GET request
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

    (1334, 7)





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
      <td>0</td>
      <td>Rouge,Malvern</td>
      <td>43.806686</td>
      <td>-79.194353</td>
      <td>Wendy's</td>
      <td>43.807448</td>
      <td>-79.199056</td>
      <td>Fast Food Restaurant</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Highland Creek,Rouge Hill,Port Union</td>
      <td>43.784535</td>
      <td>-79.160497</td>
      <td>Royal Canadian Legion</td>
      <td>43.782533</td>
      <td>-79.163085</td>
      <td>Bar</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Highland Creek,Rouge Hill,Port Union</td>
      <td>43.784535</td>
      <td>-79.160497</td>
      <td>Affordable Toronto Movers</td>
      <td>43.787919</td>
      <td>-79.162977</td>
      <td>Moving Target</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Highland Creek,Rouge Hill,Port Union</td>
      <td>43.784535</td>
      <td>-79.160497</td>
      <td>Scarborough Historical Society</td>
      <td>43.788755</td>
      <td>-79.162438</td>
      <td>History Museum</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Guildwood,Morningside,West Hill</td>
      <td>43.763573</td>
      <td>-79.188711</td>
      <td>Swiss Chalet Rotisserie &amp; Grill</td>
      <td>43.767697</td>
      <td>-79.189914</td>
      <td>Pizza Place</td>
    </tr>
  </tbody>
</table>
</div>



Then we group these venues by Neighborhood


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
      <td>Adelaide,King,Richmond</td>
      <td>30</td>
      <td>30</td>
      <td>30</td>
      <td>30</td>
      <td>30</td>
      <td>30</td>
    </tr>
    <tr>
      <td>Agincourt</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <td>Agincourt North,L'Amoreaux East,Milliken,Steeles East</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Albion Gardens,Beaumond Heights,Humbergate,Jamestown,Mount Olive,Silverstone,South Steeles,Thistletown</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <td>Alderwood,Long Branch</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>Willowdale West</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <td>Woburn</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Woodbine Gardens,Parkview Hill</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Woodbine Heights</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <td>York Mills West</td>
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
      <th>Trail</th>
      <th>Train Station</th>
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
      <td>0</td>
      <td>Adelaide,King,Richmond</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.033333</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.033333</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Agincourt</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Agincourt North,L'Amoreaux East,Milliken,Steel...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Albion Gardens,Beaumond Heights,Humbergate,Jam...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Alderwood,Long Branch</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
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
      <td>...</td>
    </tr>
    <tr>
      <td>94</td>
      <td>Willowdale West</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>95</td>
      <td>Woburn</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>96</td>
      <td>Woodbine Gardens,Parkview Hill</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>97</td>
      <td>Woodbine Heights</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>98</td>
      <td>York Mills West</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
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
    1       Hotel  0.07
    2  Steakhouse  0.07
    
    
    ----Agincourt----
                venue  freq
    0  Sandwich Place  0.25
    1    Skating Rink  0.25
    2          Lounge  0.25
    
    
    ----Agincourt North,L'Amoreaux East,Milliken,Steeles East----
             venue  freq
    0   Playground   0.5
    1         Park   0.5
    2  Music Venue   0.0
    
    
    ----Albion Gardens,Beaumond Heights,Humbergate,Jamestown,Mount Olive,Silverstone,South Steeles,Thistletown----
                venue  freq
    0   Grocery Store  0.25
    1        Pharmacy  0.12
    2  Sandwich Place  0.12
    
    
    ----Alderwood,Long Branch----
             venue  freq
    0  Pizza Place  0.18
    1     Pharmacy  0.09
    2          Gym  0.09
    
    
    ----Bathurst Manor,Downsview North,Wilson Heights----
                           venue  freq
    0                Coffee Shop  0.11
    1  Middle Eastern Restaurant  0.06
    2             Sandwich Place  0.06
    
    
    ----Bayview Village----
                    venue  freq
    0                Café  0.25
    1  Chinese Restaurant  0.25
    2                Bank  0.25
    
    
    ----Bedford Park,Lawrence Manor East----
                         venue  freq
    0       Italian Restaurant  0.08
    1              Coffee Shop  0.08
    2  Comfort Food Restaurant  0.04
    
    
    ----Berczy Park----
                    venue  freq
    0  Seafood Restaurant  0.07
    1        Cocktail Bar  0.07
    2            Beer Bar  0.07
    
    
    ----Birch Cliff,Cliffside West----
                       venue  freq
    0        College Stadium  0.25
    1           Skating Rink  0.25
    2  General Entertainment  0.25
    
    
    ----Bloordale Gardens,Eringate,Markland Wood,Old Burnhamthorpe----
                   venue  freq
    0  Convenience Store  0.11
    1        Coffee Shop  0.11
    2     Shopping Plaza  0.11
    
    
    ----Brockton,Exhibition Place,Parkdale Village----
                venue  freq
    0            Café  0.11
    1     Yoga Studio  0.07
    2  Breakfast Spot  0.07
    
    
    ----Business Reply Mail Processing Centre 969 Eastern----
                    venue  freq
    0  Light Rail Station  0.11
    1         Yoga Studio  0.05
    2       Garden Center  0.05
    
    
    ----CFB Toronto,Downsview East----
             venue  freq
    0      Airport  0.33
    1  Snack Place  0.33
    2         Park  0.33
    
    
    ----CN Tower,Bathurst Quay,Island airport,Harbourfront West,King and Spadina,Railway Lands,South Niagara----
                  venue  freq
    0    Airport Lounge  0.13
    1   Airport Service  0.13
    2  Airport Terminal  0.13
    
    
    ----Cabbagetown,St. James Town----
                    venue  freq
    0                Café  0.07
    1         Coffee Shop  0.07
    2  Italian Restaurant  0.07
    
    
    ----Caledonia-Fairbanks----
               venue  freq
    0           Park   0.4
    1  Women's Store   0.2
    2         Market   0.2
    
    
    ----Canada Post Gateway Processing Centre----
                          venue  freq
    0                     Hotel   0.2
    1               Coffee Shop   0.2
    2  Mediterranean Restaurant   0.1
    
    
    ----Cedarbrae----
                      venue  freq
    0                Bakery  0.14
    1       Thai Restaurant  0.14
    2  Caribbean Restaurant  0.14
    
    
    ----Central Bay Street----
             venue  freq
    0  Coffee Shop  0.20
    1          Spa  0.07
    2         Café  0.07
    
    
    ----Chinatown,Grange Park,Kensington Market----
                      venue  freq
    0                  Café  0.13
    1    Mexican Restaurant  0.07
    2  Caribbean Restaurant  0.07
    
    
    ----Christie----
               venue  freq
    0  Grocery Store  0.19
    1           Café  0.19
    2           Park  0.12
    
    
    ----Church and Wellesley----
              venue  freq
    0       Gay Bar  0.07
    1  Burger Joint  0.07
    2    Restaurant  0.03
    
    
    ----Clairlea,Golden Mile,Oakridge----
          venue  freq
    0  Bus Line   0.2
    1    Bakery   0.2
    2      Park   0.1
    
    
    ----Clarks Corners,Sullivan,Tam O'Shanter----
              venue  freq
    0   Pizza Place  0.17
    1      Pharmacy  0.17
    2  Noodle House  0.08
    
    
    ----Cliffcrest,Cliffside,Scarborough Village West----
                     venue  freq
    0         Skating Rink  0.33
    1  American Restaurant  0.33
    2                Motel  0.33
    
    
    ----Cloverdale,Islington,Martin Grove,Princess Gardens,West Deane Park----
             venue  freq
    0   Print Shop   1.0
    1  Yoga Studio   0.0
    2  Music Venue   0.0
    
    
    ----Commerce Court,Victoria Hotel----
             venue  freq
    0         Café  0.17
    1  Coffee Shop  0.13
    2   Restaurant  0.10
    
    
    ----Davisville----
                  venue  freq
    0      Dessert Shop  0.10
    1  Sushi Restaurant  0.07
    2       Pizza Place  0.07
    
    
    ----Davisville North----
                   venue  freq
    0  Convenience Store   0.1
    1                Gym   0.1
    2        Pizza Place   0.1
    
    
    ----Deer Park,Forest Hill SE,Rathnelly,South Hill,Summerhill West----
                  venue  freq
    0               Pub  0.12
    1       Coffee Shop  0.12
    2  Sushi Restaurant  0.06
    
    
    ----Del Ray,Keelesdale,Mount Dennis,Silverthorn----
                   venue  freq
    0  Convenience Store  0.17
    1         Restaurant  0.17
    2                Bar  0.17
    
    
    ----Design Exchange,Toronto Dominion Centre----
             venue  freq
    0  Coffee Shop  0.17
    1   Restaurant  0.10
    2         Café  0.10
    
    
    ----Don Mills North----
                      venue  freq
    0   Japanese Restaurant   0.2
    1                  Café   0.2
    2  Gym / Fitness Center   0.2
    
    
    ----Dorset Park,Scarborough Town Centre,Wexford Heights----
                           venue  freq
    0          Indian Restaurant  0.29
    1                Gaming Cafe  0.14
    2  Latin American Restaurant  0.14
    
    
    ----Dovercourt Village,Dufferin----
             venue  freq
    0     Pharmacy  0.13
    1       Bakery  0.13
    2  Supermarket  0.13
    
    
    ----Downsview Central----
                venue  freq
    0    Home Service  0.25
    1      Food Truck  0.25
    2  Baseball Field  0.25
    
    
    ----Downsview Northwest----
                      venue  freq
    0         Grocery Store  0.25
    1    Athletics & Sports  0.25
    2  Gym / Fitness Center  0.25
    
    
    ----Downsview West----
               venue  freq
    0  Grocery Store  0.33
    1          Hotel  0.17
    2           Bank  0.17
    
    
    ----Downsview,North Park,Upwood Park----
                            venue  freq
    0  Construction & Landscaping  0.25
    1                        Park  0.25
    2            Basketball Court  0.25
    
    
    ----East Birchmount Park,Ionview,Kennedy Park----
                venue  freq
    0  Discount Store   0.4
    1     Coffee Shop   0.2
    2     Bus Station   0.2
    
    
    ----East Toronto----
                   venue  freq
    0  Convenience Store  0.33
    1        Coffee Shop  0.33
    2               Park  0.33
    
    
    ----Emery,Humberlea----
                               venue  freq
    0  Paper / Office Supplies Store   0.5
    1                 Baseball Field   0.5
    2                    Yoga Studio   0.0
    
    
    ----Fairview,Henry Farm,Oriole----
                venue  freq
    0  Clothing Store  0.13
    1     Coffee Shop  0.13
    2        Pharmacy  0.03
    
    
    ----First Canadian Place,Underground city----
               venue  freq
    0           Café  0.13
    1    Coffee Shop  0.10
    2  Deli / Bodega  0.07
    
    
    ----Flemingdon Park,Don Mills South----
             venue  freq
    0   Beer Store  0.09
    1  Coffee Shop  0.09
    2          Gym  0.09
    
    
    ----Forest Hill North,Forest Hill West----
                  venue  freq
    0              Park   0.2
    1          Bus Line   0.2
    2  Sushi Restaurant   0.2
    
    
    ----Glencairn----
                     venue  freq
    0           Playground  0.17
    1  Japanese Restaurant  0.17
    2   Italian Restaurant  0.17
    
    
    ----Guildwood,Morningside,West Hill----
                venue  freq
    0     Pizza Place  0.14
    1  Medical Center  0.14
    2  Breakfast Spot  0.14
    
    
    ----Harbord,University of Toronto----
            venue  freq
    0        Café  0.13
    1         Bar  0.07
    2  Restaurant  0.07
    
    
    ----Harbourfront East,Toronto Islands,Union Station----
       venue  freq
    0   Café  0.07
    1  Hotel  0.07
    2  Plaza  0.07
    
    
    ----Harbourfront,Regent Park----
             venue  freq
    0  Coffee Shop   0.2
    1       Bakery   0.1
    2         Park   0.1
    
    
    ----High Park,The Junction South----
                    venue  freq
    0  Mexican Restaurant  0.08
    1                Café  0.08
    2                 Bar  0.08
    
    
    ----Highland Creek,Rouge Hill,Port Union----
                venue  freq
    0  History Museum  0.33
    1             Bar  0.33
    2   Moving Target  0.33
    
    
    ----Hillcrest Village----
                          venue  freq
    0               Golf Course   0.2
    1  Mediterranean Restaurant   0.2
    2                      Pool   0.2
    
    
    ----Humber Bay Shores,Mimico South,New Toronto----
             venue  freq
    0  Pizza Place  0.07
    1   Restaurant  0.07
    2  Flower Shop  0.07
    
    
    ----Humber Bay,King's Mill Park,Kingsway Park South East,Mimico NE,Old Mill South,The Queensway East,Royal York South East,Sunnylea----
                venue  freq
    0            Park   0.5
    1  Baseball Field   0.5
    2     Yoga Studio   0.0
    
    
    ----Humber Summit----
             venue  freq
    0  Pizza Place   1.0
    1  Music Venue   0.0
    2  Men's Store   0.0
    
    
    ----Humewood-Cedarvale----
              venue  freq
    0  Tennis Court  0.25
    1         Trail  0.25
    2         Field  0.25
    
    
    ----Kingsview Village,Martin Grove Gardens,Richview Gardens,St. Phillips----
                   venue  freq
    0        Pizza Place  0.25
    1               Park  0.25
    2  Mobile Phone Shop  0.25
    
    
    ----Kingsway Park South West,Mimico NW,The Queensway West,Royal York South West,South of Bloor----
                      venue  freq
    0                Bakery  0.07
    1                   Gym  0.07
    2  Fast Food Restaurant  0.07
    
    
    ----L'Amoreaux West----
                      venue  freq
    0  Fast Food Restaurant  0.15
    1    Chinese Restaurant  0.15
    2              Pharmacy  0.08
    
    
    ----Lawrence Heights,Lawrence Manor----
                        venue  freq
    0  Furniture / Home Store  0.25
    1                Boutique  0.08
    2             Coffee Shop  0.08
    
    
    ----Lawrence Park----
             venue  freq
    0         Park  0.33
    1  Swim School  0.33
    2     Bus Line  0.33
    
    
    ----Leaside----
                        venue  freq
    0             Coffee Shop  0.10
    1     Sporting Goods Shop  0.10
    2  Furniture / Home Store  0.07
    
    
    ----Little Portugal,Trinity----
                       venue  freq
    0                    Bar  0.13
    1       Asian Restaurant  0.10
    2  Vietnamese Restaurant  0.07
    
    
    ----Maryvale,Wexford----
                           venue  freq
    0             Breakfast Spot  0.25
    1  Middle Eastern Restaurant  0.25
    2                 Smoke Shop  0.25
    
    
    ----Moore Park,Summerhill East----
            venue  freq
    0  Playground  0.25
    1         Gym  0.25
    2  Restaurant  0.25
    
    
    ----North Toronto West----
                     venue  freq
    0          Coffee Shop  0.11
    1  Sporting Goods Shop  0.11
    2          Yoga Studio  0.05
    
    
    ----Northwest----
                     venue  freq
    0  Rental Car Location   0.5
    1            Drugstore   0.5
    2          Yoga Studio   0.0
    
    
    ----Northwood Park,York University----
                      venue  freq
    0    Falafel Restaurant  0.17
    1  Caribbean Restaurant  0.17
    2        Massage Studio  0.17
    
    
    ----Parkdale,Roncesvalles----
                venue  freq
    0  Breakfast Spot  0.13
    1       Gift Shop  0.13
    2     Coffee Shop  0.07
    
    
    ----Parkwoods----
                   venue  freq
    0  Food & Drink Shop   0.5
    1               Park   0.5
    2        Yoga Studio   0.0
    
    
    ----Queen's Park----
             venue  freq
    0  Coffee Shop  0.17
    1          Gym  0.07
    2        Diner  0.07
    
    
    ----Rosedale----
            venue  freq
    0        Park   0.4
    1  Playground   0.2
    2    Building   0.2
    
    
    ----Roselawn----
              venue  freq
    0        Garden   0.5
    1  Home Service   0.5
    2   Yoga Studio   0.0
    
    
    ----Rouge,Malvern----
                      venue  freq
    0  Fast Food Restaurant   1.0
    1           Yoga Studio   0.0
    2           Music Venue   0.0
    
    
    ----Runnymede,Swansea----
                    venue  freq
    0                Café  0.13
    1         Pizza Place  0.07
    2  Italian Restaurant  0.07
    
    
    ----Ryerson,Garden District----
                venue  freq
    0            Café  0.10
    1  Clothing Store  0.07
    2   Burrito Place  0.03
    
    
    ----Scarborough Village----
             venue  freq
    0   Playground   1.0
    1  Music Venue   0.0
    2  Men's Store   0.0
    
    
    ----St. James Town----
                    venue  freq
    0         Coffee Shop  0.13
    1  Italian Restaurant  0.10
    2           Gastropub  0.10
    
    
    ----Stn A PO Boxes 25 The Esplanade----
                venue  freq
    0            Café  0.10
    1  Farmers Market  0.07
    2        Beer Bar  0.07
    
    
    ----Studio District----
                    venue  freq
    0                Café  0.13
    1         Coffee Shop  0.10
    2  Italian Restaurant  0.07
    
    
    ----The Annex,North Midtown,Yorkville----
                venue  freq
    0            Café  0.14
    1  Sandwich Place  0.14
    2     Coffee Shop  0.10
    
    
    ----The Beaches----
                      venue  freq
    0     Health Food Store   0.2
    1                   Pub   0.2
    2  Other Great Outdoors   0.2
    
    
    ----The Beaches West,India Bazaar----
                    venue  freq
    0         Pizza Place  0.06
    1  Italian Restaurant  0.06
    2       Burrito Place  0.06
    
    
    ----The Danforth West,Riverdale----
                    venue  freq
    0    Greek Restaurant  0.27
    1      Ice Cream Shop  0.07
    2  Italian Restaurant  0.07
    
    
    ----The Junction North,Runnymede----
                   venue  freq
    0        Pizza Place  0.25
    1  Convenience Store  0.25
    2      Grocery Store  0.25
    
    
    ----The Kingsway,Montgomery Road,Old Mill North----
       venue  freq
    0   Pool  0.33
    1   Park  0.33
    2  River  0.33
    
    
    ----Thorncliffe Park----
                   venue  freq
    0  Indian Restaurant  0.12
    1       Burger Joint  0.12
    2        Yoga Studio  0.06
    
    
    ----Victoria Village----
                       venue  freq
    0            Pizza Place  0.17
    1           Hockey Arena  0.17
    2  Portuguese Restaurant  0.17
    
    
    ----Westmount----
              venue  freq
    0   Pizza Place  0.29
    1   Coffee Shop  0.14
    2  Intersection  0.14
    
    
    ----Weston----
             venue  freq
    0         Park   1.0
    1  Yoga Studio   0.0
    2  Music Venue   0.0
    
    
    ----Willowdale South----
                  venue  freq
    0  Ramen Restaurant  0.10
    1       Coffee Shop  0.07
    2    Sandwich Place  0.07
    
    
    ----Willowdale West----
             venue  freq
    0  Pizza Place  0.17
    1  Coffee Shop  0.17
    2      Butcher  0.17
    
    
    ----Woburn----
                   venue  freq
    0        Coffee Shop  0.67
    1  Korean Restaurant  0.33
    2        Yoga Studio  0.00
    
    
    ----Woodbine Gardens,Parkview Hill----
                      venue  freq
    0           Pizza Place  0.17
    1  Fast Food Restaurant  0.17
    2  Gym / Fitness Center  0.08
    
    
    ----Woodbine Heights----
              venue  freq
    0  Skating Rink  0.25
    1      Pharmacy  0.12
    2          Park  0.12
    
    
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
      <td>0</td>
      <td>Adelaide,King,Richmond</td>
      <td>Café</td>
      <td>Asian Restaurant</td>
      <td>Steakhouse</td>
      <td>Hotel</td>
      <td>Greek Restaurant</td>
      <td>Lounge</td>
      <td>Bar</td>
      <td>Food Court</td>
      <td>Speakeasy</td>
      <td>Seafood Restaurant</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Agincourt</td>
      <td>Breakfast Spot</td>
      <td>Lounge</td>
      <td>Skating Rink</td>
      <td>Sandwich Place</td>
      <td>Women's Store</td>
      <td>Diner</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Agincourt North,L'Amoreaux East,Milliken,Steel...</td>
      <td>Playground</td>
      <td>Park</td>
      <td>Women's Store</td>
      <td>Dessert Shop</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
      <td>Eastern European Restaurant</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Albion Gardens,Beaumond Heights,Humbergate,Jam...</td>
      <td>Grocery Store</td>
      <td>Pizza Place</td>
      <td>Fried Chicken Joint</td>
      <td>Sandwich Place</td>
      <td>Fast Food Restaurant</td>
      <td>Beer Store</td>
      <td>Pharmacy</td>
      <td>Gluten-free Restaurant</td>
      <td>Deli / Bodega</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Alderwood,Long Branch</td>
      <td>Pizza Place</td>
      <td>Pharmacy</td>
      <td>Athletics &amp; Sports</td>
      <td>Dance Studio</td>
      <td>Coffee Shop</td>
      <td>Pool</td>
      <td>Pub</td>
      <td>Sandwich Place</td>
      <td>Skating Rink</td>
      <td>Gym</td>
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




    array([1, 1, 3, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 1, 0, 1, 1, 1, 2, 1, 1,
           1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 0,
           2, 1, 0, 0, 2, 1, 0, 0, 1, 1], dtype=int32)




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
      <td>0</td>
      <td>M1B</td>
      <td>Scarborough</td>
      <td>Rouge,Malvern</td>
      <td>43.806686</td>
      <td>-79.194353</td>
      <td>2.0</td>
      <td>Fast Food Restaurant</td>
      <td>Women's Store</td>
      <td>Dim Sum Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
      <td>Eastern European Restaurant</td>
      <td>Dumpling Restaurant</td>
    </tr>
    <tr>
      <td>1</td>
      <td>M1C</td>
      <td>Scarborough</td>
      <td>Highland Creek,Rouge Hill,Port Union</td>
      <td>43.784535</td>
      <td>-79.160497</td>
      <td>1.0</td>
      <td>Moving Target</td>
      <td>History Museum</td>
      <td>Bar</td>
      <td>Women's Store</td>
      <td>Fast Food Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>2</td>
      <td>M1E</td>
      <td>Scarborough</td>
      <td>Guildwood,Morningside,West Hill</td>
      <td>43.763573</td>
      <td>-79.188711</td>
      <td>1.0</td>
      <td>Intersection</td>
      <td>Pizza Place</td>
      <td>Breakfast Spot</td>
      <td>Medical Center</td>
      <td>Electronics Store</td>
      <td>Mexican Restaurant</td>
      <td>Rental Car Location</td>
      <td>Women's Store</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
    </tr>
    <tr>
      <td>3</td>
      <td>M1G</td>
      <td>Scarborough</td>
      <td>Woburn</td>
      <td>43.770992</td>
      <td>-79.216917</td>
      <td>0.0</td>
      <td>Coffee Shop</td>
      <td>Korean Restaurant</td>
      <td>Women's Store</td>
      <td>Diner</td>
      <td>Fast Food Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>4</td>
      <td>M1H</td>
      <td>Scarborough</td>
      <td>Cedarbrae</td>
      <td>43.773136</td>
      <td>-79.239476</td>
      <td>1.0</td>
      <td>Hakka Restaurant</td>
      <td>Bakery</td>
      <td>Athletics &amp; Sports</td>
      <td>Thai Restaurant</td>
      <td>Caribbean Restaurant</td>
      <td>Bank</td>
      <td>Fried Chicken Joint</td>
      <td>Discount Store</td>
      <td>Drugstore</td>
      <td>Dumpling Restaurant</td>
    </tr>
  </tbody>
</table>
</div>



We visualize the clusters in a map!


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




<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><iframe src="data:text/html;charset=utf-8;base64,PCFET0NUWVBFIGh0bWw+CjxoZWFkPiAgICAKICAgIDxtZXRhIGh0dHAtZXF1aXY9ImNvbnRlbnQtdHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PVVURi04IiAvPgogICAgPHNjcmlwdD5MX1BSRUZFUl9DQU5WQVMgPSBmYWxzZTsgTF9OT19UT1VDSCA9IGZhbHNlOyBMX0RJU0FCTEVfM0QgPSBmYWxzZTs8L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmpzIj48L3NjcmlwdD4KICAgIDxzY3JpcHQgc3JjPSJodHRwczovL2FqYXguZ29vZ2xlYXBpcy5jb20vYWpheC9saWJzL2pxdWVyeS8xLjExLjEvanF1ZXJ5Lm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvanMvYm9vdHN0cmFwLm1pbi5qcyI+PC9zY3JpcHQ+CiAgICA8c2NyaXB0IHNyYz0iaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvTGVhZmxldC5hd2Vzb21lLW1hcmtlcnMvMi4wLjIvbGVhZmxldC5hd2Vzb21lLW1hcmtlcnMuanMiPjwvc2NyaXB0PgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2Nkbi5qc2RlbGl2ci5uZXQvbnBtL2xlYWZsZXRAMS4yLjAvZGlzdC9sZWFmbGV0LmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL21heGNkbi5ib290c3RyYXBjZG4uY29tL2Jvb3RzdHJhcC8zLjIuMC9jc3MvYm9vdHN0cmFwLm1pbi5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9tYXhjZG4uYm9vdHN0cmFwY2RuLmNvbS9ib290c3RyYXAvMy4yLjAvY3NzL2Jvb3RzdHJhcC10aGVtZS5taW4uY3NzIi8+CiAgICA8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vbWF4Y2RuLmJvb3RzdHJhcGNkbi5jb20vZm9udC1hd2Vzb21lLzQuNi4zL2Nzcy9mb250LWF3ZXNvbWUubWluLmNzcyIvPgogICAgPGxpbmsgcmVsPSJzdHlsZXNoZWV0IiBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9MZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy8yLjAuMi9sZWFmbGV0LmF3ZXNvbWUtbWFya2Vycy5jc3MiLz4KICAgIDxsaW5rIHJlbD0ic3R5bGVzaGVldCIgaHJlZj0iaHR0cHM6Ly9yYXdnaXQuY29tL3B5dGhvbi12aXN1YWxpemF0aW9uL2ZvbGl1bS9tYXN0ZXIvZm9saXVtL3RlbXBsYXRlcy9sZWFmbGV0LmF3ZXNvbWUucm90YXRlLmNzcyIvPgogICAgPHN0eWxlPmh0bWwsIGJvZHkge3dpZHRoOiAxMDAlO2hlaWdodDogMTAwJTttYXJnaW46IDA7cGFkZGluZzogMDt9PC9zdHlsZT4KICAgIDxzdHlsZT4jbWFwIHtwb3NpdGlvbjphYnNvbHV0ZTt0b3A6MDtib3R0b206MDtyaWdodDowO2xlZnQ6MDt9PC9zdHlsZT4KICAgIAogICAgICAgICAgICA8c3R5bGU+ICNtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcgewogICAgICAgICAgICAgICAgcG9zaXRpb24gOiByZWxhdGl2ZTsKICAgICAgICAgICAgICAgIHdpZHRoIDogMTAwLjAlOwogICAgICAgICAgICAgICAgaGVpZ2h0OiAxMDAuMCU7CiAgICAgICAgICAgICAgICBsZWZ0OiAwLjAlOwogICAgICAgICAgICAgICAgdG9wOiAwLjAlOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICA8L3N0eWxlPgogICAgICAgIAo8L2hlYWQ+Cjxib2R5PiAgICAKICAgIAogICAgICAgICAgICA8ZGl2IGNsYXNzPSJmb2xpdW0tbWFwIiBpZD0ibWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3IiA+PC9kaXY+CiAgICAgICAgCjwvYm9keT4KPHNjcmlwdD4gICAgCiAgICAKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGJvdW5kcyA9IG51bGw7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgdmFyIG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyA9IEwubWFwKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ21hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNycsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB7Y2VudGVyOiBbNDMuNjUzOTYzLC03OS4zODcyMDddLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgem9vbTogMTEsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtYXhCb3VuZHM6IGJvdW5kcywKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxheWVyczogW10sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB3b3JsZENvcHlKdW1wOiBmYWxzZSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNyczogTC5DUlMuRVBTRzM4NTcKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7CiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciB0aWxlX2xheWVyX2QwNGNiMzc2Nzc5YTQxMTU5YTlmODk4NTRlYTY3M2YzID0gTC50aWxlTGF5ZXIoCiAgICAgICAgICAgICAgICAnaHR0cHM6Ly97c30udGlsZS5vcGVuc3RyZWV0bWFwLm9yZy97en0ve3h9L3t5fS5wbmcnLAogICAgICAgICAgICAgICAgewogICJhdHRyaWJ1dGlvbiI6IG51bGwsCiAgImRldGVjdFJldGluYSI6IGZhbHNlLAogICJtYXhab29tIjogMTgsCiAgIm1pblpvb20iOiAxLAogICJub1dyYXAiOiBmYWxzZSwKICAic3ViZG9tYWlucyI6ICJhYmMiCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82MDZkYmYzODdjY2I0ODFmYTE3MDQwOTMzNjgyMmI4MyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjgwNjY4NjI5OTk5OTk5NiwtNzkuMTk0MzUzNDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYzNkZjRkMzAzMTk2NGVkYmJiMTljNmFjNWNiMjIzYzUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMmViMTBlYTdlZTgyNDM2NmFhNzNiMWExYjBhMGIwNGMgPSAkKCc8ZGl2IGlkPSJodG1sXzJlYjEwZWE3ZWU4MjQzNjZhYTczYjFhMWIwYTBiMDRjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3VnZSxNYWx2ZXJuIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYzNkZjRkMzAzMTk2NGVkYmJiMTljNmFjNWNiMjIzYzUuc2V0Q29udGVudChodG1sXzJlYjEwZWE3ZWU4MjQzNjZhYTczYjFhMWIwYTBiMDRjKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzYwNmRiZjM4N2NjYjQ4MWZhMTcwNDA5MzM2ODIyYjgzLmJpbmRQb3B1cChwb3B1cF9jM2RmNGQzMDMxOTY0ZWRiYmIxOWM2YWM1Y2IyMjNjNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83ODhlMjk3ZjE4YmU0YzJjOWYwYjE2OWM1MjJjYzU0ZSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4NDUzNTEsLTc5LjE2MDQ5NzA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzNlMTM5MzFjYzQxNjQyM2E5MjMxYThlZDYzM2I1ZTgxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzRhMjJiOTRjOTJjNDRmNDk5NTc5MmZlYzkzNDM2OGQ2ID0gJCgnPGRpdiBpZD0iaHRtbF80YTIyYjk0YzkyYzQ0ZjQ5OTU3OTJmZWM5MzQzNjhkNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaGxhbmQgQ3JlZWssUm91Z2UgSGlsbCxQb3J0IFVuaW9uIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfM2UxMzkzMWNjNDE2NDIzYTkyMzFhOGVkNjMzYjVlODEuc2V0Q29udGVudChodG1sXzRhMjJiOTRjOTJjNDRmNDk5NTc5MmZlYzkzNDM2OGQ2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc4OGUyOTdmMThiZTRjMmM5ZjBiMTY5YzUyMmNjNTRlLmJpbmRQb3B1cChwb3B1cF8zZTEzOTMxY2M0MTY0MjNhOTIzMWE4ZWQ2MzNiNWU4MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jOWMxODIwNTdiNGQ0YzhiOWNkMDdhOTFiNzk5ZTc0YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc2MzU3MjYsLTc5LjE4ODcxMTVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzE3MTFjNzhlNGNhNGJlODg0ZTNiNGViNTAyNmUyOTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYmI4ZTI0MjkyZDlmNGFjMWI3YmZmMmEwNTg4OGRjZjkgPSAkKCc8ZGl2IGlkPSJodG1sX2JiOGUyNDI5MmQ5ZjRhYzFiN2JmZjJhMDU4ODhkY2Y5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5HdWlsZHdvb2QsTW9ybmluZ3NpZGUsV2VzdCBIaWxsIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzE3MTFjNzhlNGNhNGJlODg0ZTNiNGViNTAyNmUyOTAuc2V0Q29udGVudChodG1sX2JiOGUyNDI5MmQ5ZjRhYzFiN2JmZjJhMDU4ODhkY2Y5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2M5YzE4MjA1N2I0ZDRjOGI5Y2QwN2E5MWI3OTllNzRjLmJpbmRQb3B1cChwb3B1cF8zMTcxMWM3OGU0Y2E0YmU4ODRlM2I0ZWI1MDI2ZTI5MCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mNDQ5NjM4ODE3NWY0ZWVhYjBkNzE5Y2QzOTk5ZGIxNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MDk5MjEsLTc5LjIxNjkxNzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzY4NDg4NjRkZTBkMTQ1MmNiOGMwMDE2NmY0YzlmMTYxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzE3NzlhOTA0ZjkwYzRkYTlhODQ1YmExMDZjYWRkYTA5ID0gJCgnPGRpdiBpZD0iaHRtbF8xNzc5YTkwNGY5MGM0ZGE5YTg0NWJhMTA2Y2FkZGEwOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V29idXJuIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjg0ODg2NGRlMGQxNDUyY2I4YzAwMTY2ZjRjOWYxNjEuc2V0Q29udGVudChodG1sXzE3NzlhOTA0ZjkwYzRkYTlhODQ1YmExMDZjYWRkYTA5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y0NDk2Mzg4MTc1ZjRlZWFiMGQ3MTljZDM5OTlkYjE1LmJpbmRQb3B1cChwb3B1cF82ODQ4ODY0ZGUwZDE0NTJjYjhjMDAxNjZmNGM5ZjE2MSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lMWQ3MmVkYmE4Y2Q0ODM2YjhlMWE2NzkyMzAxNmIxNSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3MzEzNiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODZkNjk4YzUzMGVmNDUyNzgwOTc4YjlkN2Y3ZjBhNTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODc3ZmQ5MmI4MmU2NGFkMmJjYjE2MWJiMjVlMmVkMjMgPSAkKCc8ZGl2IGlkPSJodG1sXzg3N2ZkOTJiODJlNjRhZDJiY2IxNjFiYjI1ZTJlZDIzIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DZWRhcmJyYWUgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84NmQ2OThjNTMwZWY0NTI3ODA5NzhiOWQ3ZjdmMGE1OC5zZXRDb250ZW50KGh0bWxfODc3ZmQ5MmI4MmU2NGFkMmJjYjE2MWJiMjVlMmVkMjMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZTFkNzJlZGJhOGNkNDgzNmI4ZTFhNjc5MjMwMTZiMTUuYmluZFBvcHVwKHBvcHVwXzg2ZDY5OGM1MzBlZjQ1Mjc4MDk3OGI5ZDdmN2YwYTU4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzE5ZmFjZGNiYjczOTQyY2RiMmNhMGZiZGRkZjkyZTYzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ0NzM0MiwtNzkuMjM5NDc2MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwZmZiNCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MGZmYjQiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfY2U1YmZmYWE2MGIwNDJkMmI1MzNhNDRlMmE4M2YzMTMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODg0MGE2ZDgzNmViNGIzMWFhYjFmZTk5Mzk0M2Y5NzYgPSAkKCc8ZGl2IGlkPSJodG1sXzg4NDBhNmQ4MzZlYjRiMzFhYWIxZmU5OTM5NDNmOTc2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TY2FyYm9yb3VnaCBWaWxsYWdlIENsdXN0ZXIgMzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfY2U1YmZmYWE2MGIwNDJkMmI1MzNhNDRlMmE4M2YzMTMuc2V0Q29udGVudChodG1sXzg4NDBhNmQ4MzZlYjRiMzFhYWIxZmU5OTM5NDNmOTc2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzE5ZmFjZGNiYjczOTQyY2RiMmNhMGZiZGRkZjkyZTYzLmJpbmRQb3B1cChwb3B1cF9jZTViZmZhYTYwYjA0MmQyYjUzM2E0NGUyYTgzZjMxMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9jMTVmYTI1OGE2ZmM0ODIzODAxMDVkNTY0YjViOTIxNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNzkyOTIsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzBiZTBhODBhZDdiZDQ4ZDNhOGYzM2JhZWIzMWVjOWQ4ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzAxYjcwMDJmOTBmYzRlODFhOTA5NWNkNWZlYTZhMTliID0gJCgnPGRpdiBpZD0iaHRtbF8wMWI3MDAyZjkwZmM0ZTgxYTkwOTVjZDVmZWE2YTE5YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RWFzdCBCaXJjaG1vdW50IFBhcmssSW9udmlldyxLZW5uZWR5IFBhcmsgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wYmUwYTgwYWQ3YmQ0OGQzYThmMzNiYWViMzFlYzlkOC5zZXRDb250ZW50KGh0bWxfMDFiNzAwMmY5MGZjNGU4MWE5MDk1Y2Q1ZmVhNmExOWIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYzE1ZmEyNThhNmZjNDgyMzgwMTA1ZDU2NGI1YjkyMTcuYmluZFBvcHVwKHBvcHVwXzBiZTBhODBhZDdiZDQ4ZDNhOGYzM2JhZWIzMWVjOWQ4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzE4MjQ5M2FmNDQwZDQ1MmI4NmI0NjI2MzQ2YzNkNTJhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzExMTExNzAwMDAwMDA0LC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2E5NjBmMGRhM2I3YjQ3YTRiNDI5YmRmODViNmQ0OWFlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ExZTE2OGJmYTcwNjRjYzhiOGMzODYzNGNmOGE0NjI0ID0gJCgnPGRpdiBpZD0iaHRtbF9hMWUxNjhiZmE3MDY0Y2M4YjhjMzg2MzRjZjhhNDYyNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2xhaXJsZWEsR29sZGVuIE1pbGUsT2FrcmlkZ2UgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hOTYwZjBkYTNiN2I0N2E0YjQyOWJkZjg1YjZkNDlhZS5zZXRDb250ZW50KGh0bWxfYTFlMTY4YmZhNzA2NGNjOGI4YzM4NjM0Y2Y4YTQ2MjQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTgyNDkzYWY0NDBkNDUyYjg2YjQ2MjYzNDZjM2Q1MmEuYmluZFBvcHVwKHBvcHVwX2E5NjBmMGRhM2I3YjQ3YTRiNDI5YmRmODViNmQ0OWFlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZhNWMwMWM3NTQ5ZTQyOThiY2QyMzI3NzRmODcyOWM2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE2MzE2LC03OS4yMzk0NzYwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hM2ZlOWMzZjYyZDQ0MDgyYTcxZDk1NGVlOTcwZWYxOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8zZWY4YmMxYjFlMGI0ODVlODUxNzdlN2M2MGViZTlmNiA9ICQoJzxkaXYgaWQ9Imh0bWxfM2VmOGJjMWIxZTBiNDg1ZTg1MTc3ZTdjNjBlYmU5ZjYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNsaWZmY3Jlc3QsQ2xpZmZzaWRlLFNjYXJib3JvdWdoIFZpbGxhZ2UgV2VzdCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2EzZmU5YzNmNjJkNDQwODJhNzFkOTU0ZWU5NzBlZjE4LnNldENvbnRlbnQoaHRtbF8zZWY4YmMxYjFlMGI0ODVlODUxNzdlN2M2MGViZTlmNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82YTVjMDFjNzU0OWU0Mjk4YmNkMjMyNzc0Zjg3MjljNi5iaW5kUG9wdXAocG9wdXBfYTNmZTljM2Y2MmQ0NDA4MmE3MWQ5NTRlZTk3MGVmMTgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZGVjZGRkMGEzNTNkNDRiNmFmOGIzZGVjYzRlODZjNWQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTI2NTcwMDAwMDAwMDQsLTc5LjI2NDg0ODFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNTQ4Y2NlNDkzOGFjNGVkOTg1MjIxNDQ2OTNjMzVhODMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODIyYmNmMTE4MzZjNDk4NDgxZjkyNTNiOTlkZWVlYzAgPSAkKCc8ZGl2IGlkPSJodG1sXzgyMmJjZjExODM2YzQ5ODQ4MWY5MjUzYjk5ZGVlZWMwIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CaXJjaCBDbGlmZixDbGlmZnNpZGUgV2VzdCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzU0OGNjZTQ5MzhhYzRlZDk4NTIyMTQ0NjkzYzM1YTgzLnNldENvbnRlbnQoaHRtbF84MjJiY2YxMTgzNmM0OTg0ODFmOTI1M2I5OWRlZWVjMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kZWNkZGQwYTM1M2Q0NGI2YWY4YjNkZWNjNGU4NmM1ZC5iaW5kUG9wdXAocG9wdXBfNTQ4Y2NlNDkzOGFjNGVkOTg1MjIxNDQ2OTNjMzVhODMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZmRkYjE5MGExNDdmNDc3ZWI4MDcxODgxMWZhZmU5ZWYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTc0MDk2LC03OS4yNzMzMDQwMDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mYzA0NDk2MTU1Yzk0NjgyYWViMDE4MjI5MjBlYWZkOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80ZGM0MzkxOTY2N2Y0NDc4Yjc5NjYyNDlhYTg5OTU5ZSA9ICQoJzxkaXYgaWQ9Imh0bWxfNGRjNDM5MTk2NjdmNDQ3OGI3OTY2MjQ5YWE4OTk1OWUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvcnNldCBQYXJrLFNjYXJib3JvdWdoIFRvd24gQ2VudHJlLFdleGZvcmQgSGVpZ2h0cyBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZjMDQ0OTYxNTVjOTQ2ODJhZWIwMTgyMjkyMGVhZmQ4LnNldENvbnRlbnQoaHRtbF80ZGM0MzkxOTY2N2Y0NDc4Yjc5NjYyNDlhYTg5OTU5ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mZGRiMTkwYTE0N2Y0NzdlYjgwNzE4ODExZmFmZTllZi5iaW5kUG9wdXAocG9wdXBfZmMwNDQ5NjE1NWM5NDY4MmFlYjAxODIyOTIwZWFmZDgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDc5ZmY0Y2QwNWM1NDczMzkxZTVmZTYwODE0NDBkOTUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43NTAwNzE1MDAwMDAwMDQsLTc5LjI5NTg0OTFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDgyZTY5Njc0ZmJhNGVkNWFiMTc0MjMyOGQ4MTUyZTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGIwNTZhZDRhYTdiNDM1NGFmODRiYTk2ZTk0NDQ2YmQgPSAkKCc8ZGl2IGlkPSJodG1sXzRiMDU2YWQ0YWE3YjQzNTRhZjg0YmE5NmU5NDQ0NmJkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5NYXJ5dmFsZSxXZXhmb3JkIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDgyZTY5Njc0ZmJhNGVkNWFiMTc0MjMyOGQ4MTUyZTAuc2V0Q29udGVudChodG1sXzRiMDU2YWQ0YWE3YjQzNTRhZjg0YmE5NmU5NDQ0NmJkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Q3OWZmNGNkMDVjNTQ3MzM5MWU1ZmU2MDgxNDQwZDk1LmJpbmRQb3B1cChwb3B1cF80ODJlNjk2NzRmYmE0ZWQ1YWIxNzQyMzI4ZDgxNTJlMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hOGFjZjkzNWZiM2U0YWIxYTVjMGVkNzQwMjY2ZDExZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5NDIwMDMsLTc5LjI2MjAyOTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzUyMmZkZDA0NDVjODQwZTI5ZjZlNGIzYTU4ODA4M2ViID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2E5MDhhNjczN2QzYzQ2M2M4M2QyYjI2OGZlYjk3ZjFlID0gJCgnPGRpdiBpZD0iaHRtbF9hOTA4YTY3MzdkM2M0NjNjODNkMmIyNjhmZWI5N2YxZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0IENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNTIyZmRkMDQ0NWM4NDBlMjlmNmU0YjNhNTg4MDgzZWIuc2V0Q29udGVudChodG1sX2E5MDhhNjczN2QzYzQ2M2M4M2QyYjI2OGZlYjk3ZjFlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2E4YWNmOTM1ZmIzZTRhYjFhNWMwZWQ3NDAyNjZkMTFkLmJpbmRQb3B1cChwb3B1cF81MjJmZGQwNDQ1Yzg0MGUyOWY2ZTRiM2E1ODgwODNlYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84NDU0ZTU0OTEzNmI0NzZhOWJlZDQ1ZDk4NDQ5MTViYSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc4MTYzNzUsLTc5LjMwNDMwMjFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNzM2NWM3MWNjYzBmNDhlZjkxMzlhNDIyNDlkNTlhMDUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjJjYzkxZDIwZjI2NDM1ZDhlNmRjNTQ5ZjQzNmZiN2YgPSAkKCc8ZGl2IGlkPSJodG1sXzYyY2M5MWQyMGYyNjQzNWQ4ZTZkYzU0OWY0MzZmYjdmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbGFya3MgQ29ybmVycyxTdWxsaXZhbixUYW0gTyYjMzk7U2hhbnRlciBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzczNjVjNzFjY2MwZjQ4ZWY5MTM5YTQyMjQ5ZDU5YTA1LnNldENvbnRlbnQoaHRtbF82MmNjOTFkMjBmMjY0MzVkOGU2ZGM1NDlmNDM2ZmI3Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84NDU0ZTU0OTEzNmI0NzZhOWJlZDQ1ZDk4NDQ5MTViYS5iaW5kUG9wdXAocG9wdXBfNzM2NWM3MWNjYzBmNDhlZjkxMzlhNDIyNDlkNTlhMDUpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODQzOGQ1OWM1M2Q4NDMxMDk5YWZiMjM2N2RkMTk0ZWYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My44MTUyNTIyLC03OS4yODQ1NzcyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MGZmYjQiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODBmZmI0IiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzQ0NTQzOGRlNjIwYTRjMzQ5M2Q5MTUwYzY5MjcwNWI0ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2Q0OTM0NmY4N2UxZDRjYjQ5ODQyMjQyMzAwNTFmNjdiID0gJCgnPGRpdiBpZD0iaHRtbF9kNDkzNDZmODdlMWQ0Y2I0OTg0MjI0MjMwMDUxZjY3YiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QWdpbmNvdXJ0IE5vcnRoLEwmIzM5O0Ftb3JlYXV4IEVhc3QsTWlsbGlrZW4sU3RlZWxlcyBFYXN0IENsdXN0ZXIgMzwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNDQ1NDM4ZGU2MjBhNGMzNDkzZDkxNTBjNjkyNzA1YjQuc2V0Q29udGVudChodG1sX2Q0OTM0NmY4N2UxZDRjYjQ5ODQyMjQyMzAwNTFmNjdiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzg0MzhkNTljNTNkODQzMTA5OWFmYjIzNjdkZDE5NGVmLmJpbmRQb3B1cChwb3B1cF80NDU0MzhkZTYyMGE0YzM0OTNkOTE1MGM2OTI3MDViNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xOTdhMGNhMjVmNWI0NjMxODdjNGE5NjRiYTBjZmQxYiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc5OTUyNTIwMDAwMDAwNSwtNzkuMzE4Mzg4N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hYzQyODA5NWJhNjk0ZThhYTU3ZDk5NDYzYTA0ZmJhNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNzdkNjkxODg5OTc0NDc3YTcwZTJjMzZiODA2NTgxMyA9ICQoJzxkaXYgaWQ9Imh0bWxfMTc3ZDY5MTg4OTk3NDQ3N2E3MGUyYzM2YjgwNjU4MTMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkwmIzM5O0Ftb3JlYXV4IFdlc3QgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hYzQyODA5NWJhNjk0ZThhYTU3ZDk5NDYzYTA0ZmJhNy5zZXRDb250ZW50KGh0bWxfMTc3ZDY5MTg4OTk3NDQ3N2E3MGUyYzM2YjgwNjU4MTMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTk3YTBjYTI1ZjViNDYzMTg3YzRhOTY0YmEwY2ZkMWIuYmluZFBvcHVwKHBvcHVwX2FjNDI4MDk1YmE2OTRlOGFhNTdkOTk0NjNhMDRmYmE3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzU5NzMyZGUyNTI2ODQzZDNiMmUzYzRlNTkyNGU0ZGY5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuODAzNzYyMiwtNzkuMzYzNDUxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hY2ZlMjYyNzk4MjU0MzAzODkxMzQ5YTUzYzFiZjI1MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kZGFhMDIwY2NjMzk0ZDlhOTE2OWRlMjFhODFjN2EzNSA9ICQoJzxkaXYgaWQ9Imh0bWxfZGRhYTAyMGNjYzM5NGQ5YTkxNjlkZTIxYTgxYzdhMzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkhpbGxjcmVzdCBWaWxsYWdlIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYWNmZTI2Mjc5ODI1NDMwMzg5MTM0OWE1M2MxYmYyNTIuc2V0Q29udGVudChodG1sX2RkYWEwMjBjY2MzOTRkOWE5MTY5ZGUyMWE4MWM3YTM1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzU5NzMyZGUyNTI2ODQzZDNiMmUzYzRlNTkyNGU0ZGY5LmJpbmRQb3B1cChwb3B1cF9hY2ZlMjYyNzk4MjU0MzAzODkxMzQ5YTUzYzFiZjI1Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xM2FhMTA2NTcwMjU0MzQ5OGIyZTdjN2VlOGVmZDRmNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc3ODUxNzUsLTc5LjM0NjU1NTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDQxOTdkNmEwODliNDI4ZTk4NGY1N2RmZmU2NjU5OWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfODJhNTg5MzYzYjg1NGEwMzhhNGM5YmY3Y2Y1YzNmODQgPSAkKCc8ZGl2IGlkPSJodG1sXzgyYTU4OTM2M2I4NTRhMDM4YTRjOWJmN2NmNWMzZjg0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5GYWlydmlldyxIZW5yeSBGYXJtLE9yaW9sZSBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q0MTk3ZDZhMDg5YjQyOGU5ODRmNTdkZmZlNjY1OTlhLnNldENvbnRlbnQoaHRtbF84MmE1ODkzNjNiODU0YTAzOGE0YzliZjdjZjVjM2Y4NCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xM2FhMTA2NTcwMjU0MzQ5OGIyZTdjN2VlOGVmZDRmNy5iaW5kUG9wdXAocG9wdXBfZDQxOTdkNmEwODliNDI4ZTk4NGY1N2RmZmU2NjU5OWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmFjYWQ2ZjYyZDYwNGJhOThkZDBlNDdjNjNkNzA2NWMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43ODY5NDczLC03OS4zODU5NzVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNWQxM2RiMTM1OWRmNDkzODg5MjYwYTVmZjlmMGQwMDUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTI1YTgxZWY5OGQwNDE3NGFiODg0Yjc3NzA0N2Q5MmMgPSAkKCc8ZGl2IGlkPSJodG1sX2UyNWE4MWVmOThkMDQxNzRhYjg4NGI3NzcwNDdkOTJjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CYXl2aWV3IFZpbGxhZ2UgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81ZDEzZGIxMzU5ZGY0OTM4ODkyNjBhNWZmOWYwZDAwNS5zZXRDb250ZW50KGh0bWxfZTI1YTgxZWY5OGQwNDE3NGFiODg0Yjc3NzA0N2Q5MmMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmFjYWQ2ZjYyZDYwNGJhOThkZDBlNDdjNjNkNzA2NWMuYmluZFBvcHVwKHBvcHVwXzVkMTNkYjEzNTlkZjQ5Mzg4OTI2MGE1ZmY5ZjBkMDA1KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzNjZTkxNTQ4ZTRkODRhODk5MTMxMjZmMjZiYjk2ZWZjID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzcwMTE5OSwtNzkuNDA4NDkyNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNmVmMzlhYThjZjVkNGY3OWExZjhjNmU3NGFkNzhhYTAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGFhZmIwOWJlNTUwNGE1ZmE2YmM3YzgyNjhlNDdhMmIgPSAkKCc8ZGl2IGlkPSJodG1sXzhhYWZiMDliZTU1MDRhNWZhNmJjN2M4MjY4ZTQ3YTJiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XaWxsb3dkYWxlIFNvdXRoIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmVmMzlhYThjZjVkNGY3OWExZjhjNmU3NGFkNzhhYTAuc2V0Q29udGVudChodG1sXzhhYWZiMDliZTU1MDRhNWZhNmJjN2M4MjY4ZTQ3YTJiKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzNjZTkxNTQ4ZTRkODRhODk5MTMxMjZmMjZiYjk2ZWZjLmJpbmRQb3B1cChwb3B1cF82ZWYzOWFhOGNmNWQ0Zjc5YTFmOGM2ZTc0YWQ3OGFhMCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yYTUxZGY5ZjI2Zjk0OGU0YWI2OWYxYjEwZGE5YjRiNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1Mjc1ODI5OTk5OTk5NiwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82MzA5YWJkZmIzY2Y0YzIwYmIyMDA2NTVmOTE3M2ZlNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF81YTZjYzgzODFhYWQ0ZmQwYTRkZmNhOGE4MGY5YWJkMSA9ICQoJzxkaXYgaWQ9Imh0bWxfNWE2Y2M4MzgxYWFkNGZkMGE0ZGZjYThhODBmOWFiZDEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPllvcmsgTWlsbHMgV2VzdCBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzYzMDlhYmRmYjNjZjRjMjBiYjIwMDY1NWY5MTczZmU0LnNldENvbnRlbnQoaHRtbF81YTZjYzgzODFhYWQ0ZmQwYTRkZmNhOGE4MGY5YWJkMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yYTUxZGY5ZjI2Zjk0OGU0YWI2OWYxYjEwZGE5YjRiNy5iaW5kUG9wdXAocG9wdXBfNjMwOWFiZGZiM2NmNGMyMGJiMjAwNjU1ZjkxNzNmZTQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmQyYjBiOWQ1YWIxNDMzYmE4M2RkNjY4YzJiOWEyODEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43ODI3MzY0LC03OS40NDIyNTkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZjAwMDAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmYwMDAwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U5ODlkNzNjMmRmMDRjNjk5YzMzYTU1YWE4NTg2NjIzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzc2YzcwMmExZGU4NzRkMDI5NWIyODMxMDA3NzhkZDA1ID0gJCgnPGRpdiBpZD0iaHRtbF83NmM3MDJhMWRlODc0ZDAyOTViMjgzMTAwNzc4ZGQwNSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2lsbG93ZGFsZSBXZXN0IENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZTk4OWQ3M2MyZGYwNGM2OTljMzNhNTVhYTg1ODY2MjMuc2V0Q29udGVudChodG1sXzc2YzcwMmExZGU4NzRkMDI5NWIyODMxMDA3NzhkZDA1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZkMmIwYjlkNWFiMTQzM2JhODNkZDY2OGMyYjlhMjgxLmJpbmRQb3B1cChwb3B1cF9lOTg5ZDczYzJkZjA0YzY5OWMzM2E1NWFhODU4NjYyMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MzgzMTEyZGJhNzk0NDA4YTFmNmI1YzVlZTVlOTBjMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1MzI1ODYsLTc5LjMyOTY1NjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDE4ODI0MjUyZTcxNDcyZWExNjI4Mjk3MDFlODg5ZWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMGZhOGQ5ZTgzNDZmNDExOTkyMzdjMTNlMTExZGNjNDEgPSAkKCc8ZGl2IGlkPSJodG1sXzBmYThkOWU4MzQ2ZjQxMTk5MjM3YzEzZTExMWRjYzQxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrd29vZHMgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wMTg4MjQyNTJlNzE0NzJlYTE2MjgyOTcwMWU4ODllYy5zZXRDb250ZW50KGh0bWxfMGZhOGQ5ZTgzNDZmNDExOTkyMzdjMTNlMTExZGNjNDEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODM4MzExMmRiYTc5NDQwOGExZjZiNWM1ZWU1ZTkwYzEuYmluZFBvcHVwKHBvcHVwXzAxODgyNDI1MmU3MTQ3MmVhMTYyODI5NzAxZTg4OWVjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzM3MWY5NTJkZjUwODQ4ODM4MzFhNDE1NDgwYzNmZjQwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzQ1OTA1Nzk5OTk5OTk2LC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNDMwMGIwYTk5MWEwNGNhZTgxZTU1ZGRmZGM2MjdhMWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTIxNWIxODQ2Mzk4NDU3OTg1ZDJhM2ZkMjNkOWQwYzUgPSAkKCc8ZGl2IGlkPSJodG1sXzEyMTViMTg0NjM5ODQ1Nzk4NWQyYTNmZDIzZDlkMGM1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb24gTWlsbHMgTm9ydGggQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80MzAwYjBhOTkxYTA0Y2FlODFlNTVkZGZkYzYyN2ExYS5zZXRDb250ZW50KGh0bWxfMTIxNWIxODQ2Mzk4NDU3OTg1ZDJhM2ZkMjNkOWQwYzUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzcxZjk1MmRmNTA4NDg4MzgzMWE0MTU0ODBjM2ZmNDAuYmluZFBvcHVwKHBvcHVwXzQzMDBiMGE5OTFhMDRjYWU4MWU1NWRkZmRjNjI3YTFhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzJhYjEyY2FiNTA5ZDQ3Nzk4MDljZWVjMTI3ZWRhMTQyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI1ODk5NzAwMDAwMDEsLTc5LjM0MDkyM10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9iMGMxMjBmNTA2MmQ0YmJkYTU2MjM4NmI2NTMwOGQ0MyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80YjU0Y2RhOTg4YmY0MmJhODQ1OGVmNzA4NjEwODI1MyA9ICQoJzxkaXYgaWQ9Imh0bWxfNGI1NGNkYTk4OGJmNDJiYTg0NThlZjcwODYxMDgyNTMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZsZW1pbmdkb24gUGFyayxEb24gTWlsbHMgU291dGggQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iMGMxMjBmNTA2MmQ0YmJkYTU2MjM4NmI2NTMwOGQ0My5zZXRDb250ZW50KGh0bWxfNGI1NGNkYTk4OGJmNDJiYTg0NThlZjcwODYxMDgyNTMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMmFiMTJjYWI1MDlkNDc3OTgwOWNlZWMxMjdlZGExNDIuYmluZFBvcHVwKHBvcHVwX2IwYzEyMGY1MDYyZDRiYmRhNTYyMzg2YjY1MzA4ZDQzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzMzMzg4YjkwZjgyZDQ5YjhhMDFkODE2OWI2YzNmNjM2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzU0MzI4MywtNzkuNDQyMjU5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF83NjhiYzRkNTllOTU0ZjQ3YTIwMTkxOGQ5YzcxYjcyOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xYjdkMjkwMzZhNTM0ODE4YWViNTk3OTUxYzVhYTEwNyA9ICQoJzxkaXYgaWQ9Imh0bWxfMWI3ZDI5MDM2YTUzNDgxOGFlYjU5Nzk1MWM1YWExMDciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkJhdGh1cnN0IE1hbm9yLERvd25zdmlldyBOb3J0aCxXaWxzb24gSGVpZ2h0cyBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc2OGJjNGQ1OWU5NTRmNDdhMjAxOTE4ZDljNzFiNzI5LnNldENvbnRlbnQoaHRtbF8xYjdkMjkwMzZhNTM0ODE4YWViNTk3OTUxYzVhYTEwNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8zMzM4OGI5MGY4MmQ0OWI4YTAxZDgxNjliNmMzZjYzNi5iaW5kUG9wdXAocG9wdXBfNzY4YmM0ZDU5ZTk1NGY0N2EyMDE5MThkOWM3MWI3MjkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjIwZDdlODQ2ZWZmNDNhM2EyOWY1ZmMwMTJlNGM1MjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Njc5ODAzLC03OS40ODcyNjE5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zYzEyYjQwZDJkYjQ0ZWQzOTBjODdhNWQ5YmEzYTU4ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mOWRhZmVlMDZjMTE0ODMwYjhmYWRiNmIxMjk4NDRmMSA9ICQoJzxkaXYgaWQ9Imh0bWxfZjlkYWZlZTA2YzExNDgzMGI4ZmFkYjZiMTI5ODQ0ZjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPk5vcnRod29vZCBQYXJrLFlvcmsgVW5pdmVyc2l0eSBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzNjMTJiNDBkMmRiNDRlZDM5MGM4N2E1ZDliYTNhNThkLnNldENvbnRlbnQoaHRtbF9mOWRhZmVlMDZjMTE0ODMwYjhmYWRiNmIxMjk4NDRmMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iMjBkN2U4NDZlZmY0M2EzYTI5ZjVmYzAxMmU0YzUyNy5iaW5kUG9wdXAocG9wdXBfM2MxMmI0MGQyZGI0NGVkMzkwYzg3YTVkOWJhM2E1OGQpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmIyOTE3MTM4YTQ4NDE5NDhiOTk2MDU5NGE3Yzc2MmYgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Mzc0NzMyMDAwMDAwMDQsLTc5LjQ2NDc2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2NlNTRiMmRmMjQ1OTQ1ZDk4OTY0NjNmNDQ3ZDk5NGRlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2VjOWIyMzk2YTAyNjQ1YzI4YTIyNmNmM2VlZWE2ZTE3ID0gJCgnPGRpdiBpZD0iaHRtbF9lYzliMjM5NmEwMjY0NWMyOGEyMjZjZjNlZWVhNmUxNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q0ZCIFRvcm9udG8sRG93bnN2aWV3IEVhc3QgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9jZTU0YjJkZjI0NTk0NWQ5ODk2NDYzZjQ0N2Q5OTRkZS5zZXRDb250ZW50KGh0bWxfZWM5YjIzOTZhMDI2NDVjMjhhMjI2Y2YzZWVlYTZlMTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmIyOTE3MTM4YTQ4NDE5NDhiOTk2MDU5NGE3Yzc2MmYuYmluZFBvcHVwKHBvcHVwX2NlNTRiMmRmMjQ1OTQ1ZDk4OTY0NjNmNDQ3ZDk5NGRlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzlkMDI0NzdhMjQwOTQwYWVhODM3NDJmZTdhZDJkNGY3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzM5MDE0NiwtNzkuNTA2OTQzNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82MGJmNjBmOTkwZGU0YTFmYjM1ZmQ5OTE3OTJiMjM2NiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xNDNjYmMyYjk0ZWE0YmE3YjllNDNlNmQxYTcwYjA1ZCA9ICQoJzxkaXYgaWQ9Imh0bWxfMTQzY2JjMmI5NGVhNGJhN2I5ZTQzZTZkMWE3MGIwNWQiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvd25zdmlldyBXZXN0IENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjBiZjYwZjk5MGRlNGExZmIzNWZkOTkxNzkyYjIzNjYuc2V0Q29udGVudChodG1sXzE0M2NiYzJiOTRlYTRiYTdiOWU0M2U2ZDFhNzBiMDVkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzlkMDI0NzdhMjQwOTQwYWVhODM3NDJmZTdhZDJkNGY3LmJpbmRQb3B1cChwb3B1cF82MGJmNjBmOTkwZGU0YTFmYjM1ZmQ5OTE3OTJiMjM2Nik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl85NDRhMWVlZGJlYzA0MjQwYWU5MDMxNjJkOTM5Njk1YSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyODQ5NjQsLTc5LjQ5NTY5NzQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzEyNDBmZTBkYTYwOTQzZDZhZTdiYjcyZTJmMDZkYjNlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzA3YzUzYjc5M2UwOTQ3YjliYmQwMDY4NzljOWVlYmU0ID0gJCgnPGRpdiBpZD0iaHRtbF8wN2M1M2I3OTNlMDk0N2I5YmJkMDA2ODc5YzllZWJlNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG93bnN2aWV3IENlbnRyYWwgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xMjQwZmUwZGE2MDk0M2Q2YWU3YmI3MmUyZjA2ZGIzZS5zZXRDb250ZW50KGh0bWxfMDdjNTNiNzkzZTA5NDdiOWJiZDAwNjg3OWM5ZWViZTQpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTQ0YTFlZWRiZWMwNDI0MGFlOTAzMTYyZDkzOTY5NWEuYmluZFBvcHVwKHBvcHVwXzEyNDBmZTBkYTYwOTQzZDZhZTdiYjcyZTJmMDZkYjNlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzFhZmUyNzc0NjAxMjQ5YzhiOTZiZjNkMTVkYTk3OTc5ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzYxNjMxMywtNzkuNTIwOTk5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDI5OWYyYzAzOTBmNDg0ZGIzMTE0YTM1OWNkYzcwY2UgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTY1YTQwYzZiNjZlNGQyZDgxYzFmNmYwYzkyNWJjNTUgPSAkKCc8ZGl2IGlkPSJodG1sXzU2NWE0MGM2YjY2ZTRkMmQ4MWMxZjZmMGM5MjViYzU1IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Eb3duc3ZpZXcgTm9ydGh3ZXN0IENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZDI5OWYyYzAzOTBmNDg0ZGIzMTE0YTM1OWNkYzcwY2Uuc2V0Q29udGVudChodG1sXzU2NWE0MGM2YjY2ZTRkMmQ4MWMxZjZmMGM5MjViYzU1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzFhZmUyNzc0NjAxMjQ5YzhiOTZiZjNkMTVkYTk3OTc5LmJpbmRQb3B1cChwb3B1cF9kMjk5ZjJjMDM5MGY0ODRkYjMxMTRhMzU5Y2RjNzBjZSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81NzU0Yjg0ZDA1Njk0YmE4YWFmYzZiNTM1NGJiMDhlMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcyNTg4MjI5OTk5OTk5NSwtNzkuMzE1NTcxNTk5OTk5OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODU2YWQzMGRiZTBiNDJhMzhmY2U1MWU5MDM4NjU0MjYgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGYzOTExMzk3N2JiNDgyMzkyZWI4MjAyZWYxZGEzYzQgPSAkKCc8ZGl2IGlkPSJodG1sXzRmMzkxMTM5NzdiYjQ4MjM5MmViODIwMmVmMWRhM2M0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5WaWN0b3JpYSBWaWxsYWdlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODU2YWQzMGRiZTBiNDJhMzhmY2U1MWU5MDM4NjU0MjYuc2V0Q29udGVudChodG1sXzRmMzkxMTM5NzdiYjQ4MjM5MmViODIwMmVmMWRhM2M0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzU3NTRiODRkMDU2OTRiYThhYWZjNmI1MzU0YmIwOGUwLmJpbmRQb3B1cChwb3B1cF84NTZhZDMwZGJlMGI0MmEzOGZjZTUxZTkwMzg2NTQyNik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kMDlkOTM5Y2NmNGE0OWM1YjM4ODk5NDFlNzUzOTY1OCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcwNjM5NzIsLTc5LjMwOTkzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yODA0ZDdmZGFhMmI0Y2VlYTRiODU1ZWY4NTBkMDU3ZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80ZTdmNWQxMzQzZjQ0Y2MwOGQwMDliYzBmYjI3MjI0MyA9ICQoJzxkaXYgaWQ9Imh0bWxfNGU3ZjVkMTM0M2Y0NGNjMDhkMDA5YmMwZmIyNzIyNDMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPldvb2RiaW5lIEdhcmRlbnMsUGFya3ZpZXcgSGlsbCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzI4MDRkN2ZkYWEyYjRjZWVhNGI4NTVlZjg1MGQwNTdkLnNldENvbnRlbnQoaHRtbF80ZTdmNWQxMzQzZjQ0Y2MwOGQwMDliYzBmYjI3MjI0Myk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9kMDlkOTM5Y2NmNGE0OWM1YjM4ODk5NDFlNzUzOTY1OC5iaW5kUG9wdXAocG9wdXBfMjgwNGQ3ZmRhYTJiNGNlZWE0Yjg1NWVmODUwZDA1N2QpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMDExYmRhZjVlYjZhNGM3YThhYTNmNTk3MzhhZTZkZGIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTUzNDM5MDAwMDAwMDUsLTc5LjMxODM4ODddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjdiMTEyZDYyZTE1NDNkYThhY2JiNzY3MGIzMzhjNzggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYTk5ZTkwNTM4MDQ1NGMzMGEyNjE0NGM3MTVjNmNiNWIgPSAkKCc8ZGl2IGlkPSJodG1sX2E5OWU5MDUzODA0NTRjMzBhMjYxNDRjNzE1YzZjYjViIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Xb29kYmluZSBIZWlnaHRzIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMjdiMTEyZDYyZTE1NDNkYThhY2JiNzY3MGIzMzhjNzguc2V0Q29udGVudChodG1sX2E5OWU5MDUzODA0NTRjMzBhMjYxNDRjNzE1YzZjYjViKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzAxMWJkYWY1ZWI2YTRjN2E4YWEzZjU5NzM4YWU2ZGRiLmJpbmRQb3B1cChwb3B1cF8yN2IxMTJkNjJlMTU0M2RhOGFjYmI3NjcwYjMzOGM3OCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl82MDg5YzgyOWIwZDE0OGYwYmRjMTYwYmE5NTllZWZiOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY3NjM1NzM5OTk5OTk5LC03OS4yOTMwMzEyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzg0MTdlYzQzMWZiNDQ3MGNiMTE5NjNlODNmZDk3MzgwID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2ZlN2Q2OGM3ODYxZTQ1NTRiODUxOWZlZTQzMTZmNTE3ID0gJCgnPGRpdiBpZD0iaHRtbF9mZTdkNjhjNzg2MWU0NTU0Yjg1MTlmZWU0MzE2ZjUxNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+VGhlIEJlYWNoZXMgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF84NDE3ZWM0MzFmYjQ0NzBjYjExOTYzZTgzZmQ5NzM4MC5zZXRDb250ZW50KGh0bWxfZmU3ZDY4Yzc4NjFlNDU1NGI4NTE5ZmVlNDMxNmY1MTcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNjA4OWM4MjliMGQxNDhmMGJkYzE2MGJhOTU5ZWVmYjguYmluZFBvcHVwKHBvcHVwXzg0MTdlYzQzMWZiNDQ3MGNiMTE5NjNlODNmZDk3MzgwKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzlkZThiYTAyYWY4MDQ5MzliMzRkZDBlZGVlNjQxYTMyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA5MDYwNCwtNzkuMzYzNDUxN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xMzg4MGUyZmQ4MDQ0OWY0OTM1Yzg4MTBlZWU2NzdlZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9hZjBhOWE0NjBmZDc0YmQxYWExZjkwYTRiY2MxYTlkMyA9ICQoJzxkaXYgaWQ9Imh0bWxfYWYwYTlhNDYwZmQ3NGJkMWFhMWY5MGE0YmNjMWE5ZDMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxlYXNpZGUgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xMzg4MGUyZmQ4MDQ0OWY0OTM1Yzg4MTBlZWU2NzdlZC5zZXRDb250ZW50KGh0bWxfYWYwYTlhNDYwZmQ3NGJkMWFhMWY5MGE0YmNjMWE5ZDMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWRlOGJhMDJhZjgwNDkzOWIzNGRkMGVkZWU2NDFhMzIuYmluZFBvcHVwKHBvcHVwXzEzODgwZTJmZDgwNDQ5ZjQ5MzVjODgxMGVlZTY3N2VkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzllY2Y5NDRkMWZiMDQzZGRiOTRhNmYzMzc4MGUwMDFlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA1MzY4OSwtNzkuMzQ5MzcxOTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDI3MjQ5NjkwMDQwNDlhNjk4YzVjYTVmODIwMGU4MjkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZWU5MjA3OWNlOTgyNGMyNGJlNjVhN2YxMjg5NmY0YmQgPSAkKCc8ZGl2IGlkPSJodG1sX2VlOTIwNzljZTk4MjRjMjRiZTY1YTdmMTI4OTZmNGJkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaG9ybmNsaWZmZSBQYXJrIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDI3MjQ5NjkwMDQwNDlhNjk4YzVjYTVmODIwMGU4Mjkuc2V0Q29udGVudChodG1sX2VlOTIwNzljZTk4MjRjMjRiZTY1YTdmMTI4OTZmNGJkKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzllY2Y5NDRkMWZiMDQzZGRiOTRhNmYzMzc4MGUwMDFlLmJpbmRQb3B1cChwb3B1cF8wMjcyNDk2OTAwNDA0OWE2OThjNWNhNWY4MjAwZTgyOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8xMWM4ZmFkYzVhNDc0NGRmODk3MTU1OTMzN2EyODU0MSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY4NTM0NywtNzkuMzM4MTA2NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjZmYwMDAwIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiI2ZmMDAwMCIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80MTA1Njk4MjA3MTQ0MDJiOTkzOTg2MjQyNzgyOGIzMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83MTU4NGJkZWM4NjU0YTZkOTViOTM2OTkzOTVkYjQzNyA9ICQoJzxkaXYgaWQ9Imh0bWxfNzE1ODRiZGVjODY1NGE2ZDk1YjkzNjk5Mzk1ZGI0MzciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVhc3QgVG9yb250byBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzQxMDU2OTgyMDcxNDQwMmI5OTM5ODYyNDI3ODI4YjMzLnNldENvbnRlbnQoaHRtbF83MTU4NGJkZWM4NjU0YTZkOTViOTM2OTkzOTVkYjQzNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8xMWM4ZmFkYzVhNDc0NGRmODk3MTU1OTMzN2EyODU0MS5iaW5kUG9wdXAocG9wdXBfNDEwNTY5ODIwNzE0NDAyYjk5Mzk4NjI0Mjc4MjhiMzMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODUyZDdkYmUyYmI2NGYzMzgxZDM1ZDgwZjFlMTg0NjQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Nzk1NTcxLC03OS4zNTIxODhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMjYxM2M5MTEyMmVhNGUwNGI3YjM3MjBiYzMwMjExZGEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfM2IwOGE4MWYzZTU0NGMzODljMGY4NGY5MDIzNmFjMDEgPSAkKCc8ZGl2IGlkPSJodG1sXzNiMDhhODFmM2U1NDRjMzg5YzBmODRmOTAyMzZhYzAxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgRGFuZm9ydGggV2VzdCxSaXZlcmRhbGUgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yNjEzYzkxMTIyZWE0ZTA0YjdiMzcyMGJjMzAyMTFkYS5zZXRDb250ZW50KGh0bWxfM2IwOGE4MWYzZTU0NGMzODljMGY4NGY5MDIzNmFjMDEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODUyZDdkYmUyYmI2NGYzMzgxZDM1ZDgwZjFlMTg0NjQuYmluZFBvcHVwKHBvcHVwXzI2MTNjOTExMjJlYTRlMDRiN2IzNzIwYmMzMDIxMWRhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2M2NzllZWE0NzczNjQzN2ZiOTI1OTc1YmUyMWEyMzNhID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjY4OTk4NSwtNzkuMzE1NTcxNTk5OTk5OThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMGJiZmFmZjljZDY5NDRlYmE0ZDJlOTUwNDljNWZjYzAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNzc1MmEyNTRmMGNhNGMzZjk1MTgwYzZkMjZiMjMyN2UgPSAkKCc8ZGl2IGlkPSJodG1sXzc3NTJhMjU0ZjBjYTRjM2Y5NTE4MGM2ZDI2YjIzMjdlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgQmVhY2hlcyBXZXN0LEluZGlhIEJhemFhciBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzBiYmZhZmY5Y2Q2OTQ0ZWJhNGQyZTk1MDQ5YzVmY2MwLnNldENvbnRlbnQoaHRtbF83NzUyYTI1NGYwY2E0YzNmOTUxODBjNmQyNmIyMzI3ZSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9jNjc5ZWVhNDc3MzY0MzdmYjkyNTk3NWJlMjFhMjMzYS5iaW5kUG9wdXAocG9wdXBfMGJiZmFmZjljZDY5NDRlYmE0ZDJlOTUwNDljNWZjYzApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMTkzZTQzNTk5MjI2NDczOWJhOGQwOTQzY2FkNzMzYmEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTk1MjU1LC03OS4zNDA5MjNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMDc2ODE1MDZlNTc4NGNiNDkwYTliY2RkY2RkY2MwYTEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjYzNGY0ODIwNTcyNGY2N2IyYzc1MzcxODg2NTA5MGYgPSAkKCc8ZGl2IGlkPSJodG1sXzY2MzRmNDgyMDU3MjRmNjdiMmM3NTM3MTg4NjUwOTBmIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5TdHVkaW8gRGlzdHJpY3QgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8wNzY4MTUwNmU1Nzg0Y2I0OTBhOWJjZGRjZGRjYzBhMS5zZXRDb250ZW50KGh0bWxfNjYzNGY0ODIwNTcyNGY2N2IyYzc1MzcxODg2NTA5MGYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMTkzZTQzNTk5MjI2NDczOWJhOGQwOTQzY2FkNzMzYmEuYmluZFBvcHVwKHBvcHVwXzA3NjgxNTA2ZTU3ODRjYjQ5MGE5YmNkZGNkZGNjMGExKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzZiZTZkNTU0Y2NjNTQ3MDE5MGJmZjM4NWZkYzIzNzk2ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzI4MDIwNSwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjMDBiNWViIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzAwYjVlYiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81YjdmNzNiYjFlNTQ0YWZlOTA1YzljZWM4NTJmZDExNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9mOTdiMWM4Mzc2YmE0MDNhOTU2ZGY5OTUwYzAyYmY5NSA9ICQoJzxkaXYgaWQ9Imh0bWxfZjk3YjFjODM3NmJhNDAzYTk1NmRmOTk1MGMwMmJmOTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIFBhcmsgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF81YjdmNzNiYjFlNTQ0YWZlOTA1YzljZWM4NTJmZDExNy5zZXRDb250ZW50KGh0bWxfZjk3YjFjODM3NmJhNDAzYTk1NmRmOTk1MGMwMmJmOTUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmJlNmQ1NTRjY2M1NDcwMTkwYmZmMzg1ZmRjMjM3OTYuYmluZFBvcHVwKHBvcHVwXzViN2Y3M2JiMWU1NDRhZmU5MDVjOWNlYzg1MmZkMTE3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzlhOTk1Y2QxMDA0NzQ1OGI5YjZiNjMyNjM0YzQwNzYyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzEyNzUxMSwtNzkuMzkwMTk3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF80ZjQ0YWI4M2FmMTU0ZjY5ODMxODc2ZmFjM2JmMmVkNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80YzNhMDIwNTU1ZWI0MTEwOGYwYjk0NWM1YjUwMzE4YSA9ICQoJzxkaXYgaWQ9Imh0bWxfNGMzYTAyMDU1NWViNDExMDhmMGI5NDVjNWI1MDMxOGEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUgTm9ydGggQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF80ZjQ0YWI4M2FmMTU0ZjY5ODMxODc2ZmFjM2JmMmVkNC5zZXRDb250ZW50KGh0bWxfNGMzYTAyMDU1NWViNDExMDhmMGI5NDVjNWI1MDMxOGEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOWE5OTVjZDEwMDQ3NDU4YjliNmI2MzI2MzRjNDA3NjIuYmluZFBvcHVwKHBvcHVwXzRmNDRhYjgzYWYxNTRmNjk4MzE4NzZmYWMzYmYyZWQ0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzkyM2I3YmZkMTc1YjQ5OTViN2E3YzM1YjNiOGVkMDJiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE1MzgzNCwtNzkuNDA1Njc4NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNmZjYTM2NzU0NjMwNDVjNGEwM2RjN2M1MGQ3NzM1NWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZTMwM2Q2YmQ0NGI2NDdlMmIyN2UzMTcyMzZhNTcxODcgPSAkKCc8ZGl2IGlkPSJodG1sX2UzMDNkNmJkNDRiNjQ3ZTJiMjdlMzE3MjM2YTU3MTg3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Ob3J0aCBUb3JvbnRvIFdlc3QgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF82ZmNhMzY3NTQ2MzA0NWM0YTAzZGM3YzUwZDc3MzU1YS5zZXRDb250ZW50KGh0bWxfZTMwM2Q2YmQ0NGI2NDdlMmIyN2UzMTcyMzZhNTcxODcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTIzYjdiZmQxNzViNDk5NWI3YTdjMzViM2I4ZWQwMmIuYmluZFBvcHVwKHBvcHVwXzZmY2EzNjc1NDYzMDQ1YzRhMDNkYzdjNTBkNzczNTVhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2Q5MDE5ZTJkMmU1YzQzNzNiYTk2MGE2ZjUwNWNjZGVmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA0MzI0NCwtNzkuMzg4NzkwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9lZjQzZTkwNmUzZWM0ODQyODIwYzgxZDc0ZDhkNWEyZCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9lNDc2Y2I4MzRlOWE0M2RjYTMyYTZkMDg2MjAzZmY4MCA9ICQoJzxkaXYgaWQ9Imh0bWxfZTQ3NmNiODM0ZTlhNDNkY2EzMmE2ZDA4NjIwM2ZmODAiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRhdmlzdmlsbGUgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lZjQzZTkwNmUzZWM0ODQyODIwYzgxZDc0ZDhkNWEyZC5zZXRDb250ZW50KGh0bWxfZTQ3NmNiODM0ZTlhNDNkY2EzMmE2ZDA4NjIwM2ZmODApOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDkwMTllMmQyZTVjNDM3M2JhOTYwYTZmNTA1Y2NkZWYuYmluZFBvcHVwKHBvcHVwX2VmNDNlOTA2ZTNlYzQ4NDI4MjBjODFkNzRkOGQ1YTJkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc4Nzc2NTAzNzI4MzQ2NTc4NWUzZTllMDQ3Zjk5NDExID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg5NTc0MywtNzkuMzgzMTU5OTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmRmMzNlN2U4NGJmNDMyODhmNjMyZTE5YjgzM2RkZDAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZmU1ZjM2ZmQ4MzM2NDBlY2E2NTY2ZWMxOTIwYWVhMTkgPSAkKCc8ZGl2IGlkPSJodG1sX2ZlNWYzNmZkODMzNjQwZWNhNjU2NmVjMTkyMGFlYTE5IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Nb29yZSBQYXJrLFN1bW1lcmhpbGwgRWFzdCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ZkZjMzZTdlODRiZjQzMjg4ZjYzMmUxOWI4MzNkZGQwLnNldENvbnRlbnQoaHRtbF9mZTVmMzZmZDgzMzY0MGVjYTY1NjZlYzE5MjBhZWExOSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83ODc3NjUwMzcyODM0NjU3ODVlM2U5ZTA0N2Y5OTQxMS5iaW5kUG9wdXAocG9wdXBfZmRmMzNlN2U4NGJmNDMyODhmNjMyZTE5YjgzM2RkZDApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDIwZDliN2MxNmRhNDU0MGE1MWQxYjY2NjYxOTAyMWMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42ODY0MTIyOTk5OTk5OSwtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mZDIwMmZmNGRmMjM0MTBhYTE2NmY2MThhNTJmNGU2YyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82Nzg1NDJkOTNiNzg0OTVkYTNmNGU5MWZhMjc3MjA0YyA9ICQoJzxkaXYgaWQ9Imh0bWxfNjc4NTQyZDkzYjc4NDk1ZGEzZjRlOTFmYTI3NzIwNGMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRlZXIgUGFyayxGb3Jlc3QgSGlsbCBTRSxSYXRobmVsbHksU291dGggSGlsbCxTdW1tZXJoaWxsIFdlc3QgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mZDIwMmZmNGRmMjM0MTBhYTE2NmY2MThhNTJmNGU2Yy5zZXRDb250ZW50KGh0bWxfNjc4NTQyZDkzYjc4NDk1ZGEzZjRlOTFmYTI3NzIwNGMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDIwZDliN2MxNmRhNDU0MGE1MWQxYjY2NjYxOTAyMWMuYmluZFBvcHVwKHBvcHVwX2ZkMjAyZmY0ZGYyMzQxMGFhMTY2ZjYxOGE1MmY0ZTZjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzA3YmFhMDExMTEyMDQ1YzI4YTEyOTU5NjZkN2FhYzdmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjc5NTYyNiwtNzkuMzc3NTI5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWZmY2NhNGJmNjdhNDY5M2ExNzU0ZDhjY2I1Yzg1MzggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNWNkYmU5NjIxYjBmNGRkYThjOTIxMjU4M2NlYmE3ZmQgPSAkKCc8ZGl2IGlkPSJodG1sXzVjZGJlOTYyMWIwZjRkZGE4YzkyMTI1ODNjZWJhN2ZkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5Sb3NlZGFsZSBDbHVzdGVyIDI8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFmZmNjYTRiZjY3YTQ2OTNhMTc1NGQ4Y2NiNWM4NTM4LnNldENvbnRlbnQoaHRtbF81Y2RiZTk2MjFiMGY0ZGRhOGM5MjEyNTgzY2ViYTdmZCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8wN2JhYTAxMTExMjA0NWMyOGExMjk1OTY2ZDdhYWM3Zi5iaW5kUG9wdXAocG9wdXBfMWZmY2NhNGJmNjdhNDY5M2ExNzU0ZDhjY2I1Yzg1MzgpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMmFmYjY5NDAxYTZiNDEzNGIxMDVjMmQzZjgyZmJlZjcgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Njc5NjcsLTc5LjM2NzY3NTNdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWI1YzM0ZTgwMzBkNDdiNjkzY2EzYWQ3NGE1MWM0MjAgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMjVjNTdiNmU0MTM4NGFmZjk1MzRiM2FkYjBjZDViNzIgPSAkKCc8ZGl2IGlkPSJodG1sXzI1YzU3YjZlNDEzODRhZmY5NTM0YjNhZGIwY2Q1YjcyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYWJiYWdldG93bixTdC4gSmFtZXMgVG93biBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzFiNWMzNGU4MDMwZDQ3YjY5M2NhM2FkNzRhNTFjNDIwLnNldENvbnRlbnQoaHRtbF8yNWM1N2I2ZTQxMzg0YWZmOTUzNGIzYWRiMGNkNWI3Mik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yYWZiNjk0MDFhNmI0MTM0YjEwNWMyZDNmODJmYmVmNy5iaW5kUG9wdXAocG9wdXBfMWI1YzM0ZTgwMzBkNDdiNjkzY2EzYWQ3NGE1MWM0MjApOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZGEyNGFhMjM0ZTc1NDBmZTllNDM5MjMwMGU0M2Y2Y2MgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjU4NTk5LC03OS4zODMxNTk5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81ZmQ4MmQ4ZGI4Y2M0MmM1YTJiODRkNTA2OTdkOTI1NyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wYmYzZmVjZTU5ODQ0MjllYjUwZjQxOWZkNzZhZjU3ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfMGJmM2ZlY2U1OTg0NDI5ZWI1MGY0MTlmZDc2YWY1N2YiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNodXJjaCBhbmQgV2VsbGVzbGV5IENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNWZkODJkOGRiOGNjNDJjNWEyYjg0ZDUwNjk3ZDkyNTcuc2V0Q29udGVudChodG1sXzBiZjNmZWNlNTk4NDQyOWViNTBmNDE5ZmQ3NmFmNTdmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2RhMjRhYTIzNGU3NTQwZmU5ZTQzOTIzMDBlNDNmNmNjLmJpbmRQb3B1cChwb3B1cF81ZmQ4MmQ4ZGI4Y2M0MmM1YTJiODRkNTA2OTdkOTI1Nyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9iMGRhN2E5NDAyOWY0NjQ1YjhjMjJkZjE4MWY4ODAzMSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY1NDI1OTksLTc5LjM2MDYzNTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMWE1ZThhM2RhMGJkNDQzNTllZjU3ZDIzZWRlZTdjOTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMTlmOTFiZmUzZTk2NDIxMWI0MjRjMWIxOTAxYjRlZTYgPSAkKCc8ZGl2IGlkPSJodG1sXzE5ZjkxYmZlM2U5NjQyMTFiNDI0YzFiMTkwMWI0ZWU2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQsUmVnZW50IFBhcmsgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xYTVlOGEzZGEwYmQ0NDM1OWVmNTdkMjNlZGVlN2M5OC5zZXRDb250ZW50KGh0bWxfMTlmOTFiZmUzZTk2NDIxMWI0MjRjMWIxOTAxYjRlZTYpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYjBkYTdhOTQwMjlmNDY0NWI4YzIyZGYxODFmODgwMzEuYmluZFBvcHVwKHBvcHVwXzFhNWU4YTNkYTBiZDQ0MzU5ZWY1N2QyM2VkZWU3Yzk4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzI0NGEwZTBkMzdkYzRkZjI4Mjk2ZjUxNDAxOWQ3NjM3ID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjU3MTYxOCwtNzkuMzc4OTM3MDk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfODZiZDdhN2Y3ODE0NDY4Mzk1YjViZjZkNDJjNDE4MDIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOGFlNzc3NjhjN2MyNGIzMmE3YWQxMThkMmUxYjhmMjYgPSAkKCc8ZGl2IGlkPSJodG1sXzhhZTc3NzY4YzdjMjRiMzJhN2FkMTE4ZDJlMWI4ZjI2IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5SeWVyc29uLEdhcmRlbiBEaXN0cmljdCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzg2YmQ3YTdmNzgxNDQ2ODM5NWI1YmY2ZDQyYzQxODAyLnNldENvbnRlbnQoaHRtbF84YWU3Nzc2OGM3YzI0YjMyYTdhZDExOGQyZTFiOGYyNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl8yNDRhMGUwZDM3ZGM0ZGYyODI5NmY1MTQwMTlkNzYzNy5iaW5kUG9wdXAocG9wdXBfODZiZDdhN2Y3ODE0NDY4Mzk1YjViZjZkNDJjNDE4MDIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTU1ZTVmYmYyMjFkNDdlZDg2YTBkOTk0MGVjNmRkOTUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTE0OTM5LC03OS4zNzU0MTc5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U3ZTBkYzEwZTMzYTQ3YmJiMDJjN2NhYThjMGVjYzVhID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2M5YjBmZmFmZjAxMzRlNzBiZGEyZTJhMjdhY2QwMWVjID0gJCgnPGRpdiBpZD0iaHRtbF9jOWIwZmZhZmYwMTM0ZTcwYmRhMmUyYTI3YWNkMDFlYyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+U3QuIEphbWVzIFRvd24gQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lN2UwZGMxMGUzM2E0N2JiYjAyYzdjYWE4YzBlY2M1YS5zZXRDb250ZW50KGh0bWxfYzliMGZmYWZmMDEzNGU3MGJkYTJlMmEyN2FjZDAxZWMpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNTU1ZTVmYmYyMjFkNDdlZDg2YTBkOTk0MGVjNmRkOTUuYmluZFBvcHVwKHBvcHVwX2U3ZTBkYzEwZTMzYTQ3YmJiMDJjN2NhYThjMGVjYzVhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2FmNjY1NWNkY2NhYTRiMWJhMzM2OTgyNDIwYjgyMTUzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ0NzcwNzk5OTk5OTk2LC03OS4zNzMzMDY0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzNkYjVkOTVhNTI1ZTQ3NmY5NGI3ZDlhZTkyODIxZTMzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzdhNzc4ZTRjNTIwZTQ5OGNiMDg2OTY4YmM3MzljZDA3ID0gJCgnPGRpdiBpZD0iaHRtbF83YTc3OGU0YzUyMGU0OThjYjA4Njk2OGJjNzM5Y2QwNyIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QmVyY3p5IFBhcmsgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zZGI1ZDk1YTUyNWU0NzZmOTRiN2Q5YWU5MjgyMWUzMy5zZXRDb250ZW50KGh0bWxfN2E3NzhlNGM1MjBlNDk4Y2IwODY5NjhiYzczOWNkMDcpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWY2NjU1Y2RjY2FhNGIxYmEzMzY5ODI0MjBiODIxNTMuYmluZFBvcHVwKHBvcHVwXzNkYjVkOTVhNTI1ZTQ3NmY5NGI3ZDlhZTkyODIxZTMzKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzdlNGRhM2ZiOGU1YjQ2YjRiYjliMTlkZjkzYTkxMmVlID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjU3OTUyNCwtNzkuMzg3MzgyNl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8xMDdlNzc5YzZkY2I0MmI0YjFlY2UyMGRiNmIyY2UwNyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yOWMyMzY2ZjM4MTY0ZTU2OWQ5YWFhMTg5M2U1NGE5ZiA9ICQoJzxkaXYgaWQ9Imh0bWxfMjljMjM2NmYzODE2NGU1NjlkOWFhYTE4OTNlNTRhOWYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNlbnRyYWwgQmF5IFN0cmVldCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzEwN2U3NzljNmRjYjQyYjRiMWVjZTIwZGI2YjJjZTA3LnNldENvbnRlbnQoaHRtbF8yOWMyMzY2ZjM4MTY0ZTU2OWQ5YWFhMTg5M2U1NGE5Zik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83ZTRkYTNmYjhlNWI0NmI0YmI5YjE5ZGY5M2E5MTJlZS5iaW5kUG9wdXAocG9wdXBfMTA3ZTc3OWM2ZGNiNDJiNGIxZWNlMjBkYjZiMmNlMDcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYTZjYmU0YTdkYzFiNDk3YjhiOWNjODEyMjVmOTZjZDEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTA1NzEyMDAwMDAwMSwtNzkuMzg0NTY3NV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zMzBlZWI3NDU3NmI0OTI3ODY1MDUxZDc4MDgzMzZlOCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82YjQ4MTAxODgyZjg0ZDQ4YmFkYWFhNzlkZjU3NWYwMSA9ICQoJzxkaXYgaWQ9Imh0bWxfNmI0ODEwMTg4MmY4NGQ0OGJhZGFhYTc5ZGY1NzVmMDEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFkZWxhaWRlLEtpbmcsUmljaG1vbmQgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zMzBlZWI3NDU3NmI0OTI3ODY1MDUxZDc4MDgzMzZlOC5zZXRDb250ZW50KGh0bWxfNmI0ODEwMTg4MmY4NGQ0OGJhZGFhYTc5ZGY1NzVmMDEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYTZjYmU0YTdkYzFiNDk3YjhiOWNjODEyMjVmOTZjZDEuYmluZFBvcHVwKHBvcHVwXzMzMGVlYjc0NTc2YjQ5Mjc4NjUwNTFkNzgwODMzNmU4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzg5ODQyZDJmOTFiYTRmYmJhNWE0ZDAzYmEzZmJiYjBmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQwODE1NywtNzkuMzgxNzUyMjk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZThlZjk2YzU0NmQzNDVkNzlhMTFhMjM5MzI2YzQ4MGEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNGU2NzAxY2JmNWM4NDU1ZWJiNDk4NDI0MTEzMzEwOTQgPSAkKCc8ZGl2IGlkPSJodG1sXzRlNjcwMWNiZjVjODQ1NWViYjQ5ODQyNDExMzMxMDk0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5IYXJib3VyZnJvbnQgRWFzdCxUb3JvbnRvIElzbGFuZHMsVW5pb24gU3RhdGlvbiBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2U4ZWY5NmM1NDZkMzQ1ZDc5YTExYTIzOTMyNmM0ODBhLnNldENvbnRlbnQoaHRtbF80ZTY3MDFjYmY1Yzg0NTVlYmI0OTg0MjQxMTMzMTA5NCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl84OTg0MmQyZjkxYmE0ZmJiYTVhNGQwM2JhM2ZiYmIwZi5iaW5kUG9wdXAocG9wdXBfZThlZjk2YzU0NmQzNDVkNzlhMTFhMjM5MzI2YzQ4MGEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNTlmZjQ5MzI2NzM3NDAzZDg4YTkxMWNlZGFiZDk5ZWQgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDcxNzY4LC03OS4zODE1NzY0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF81YjI1N2Y0ZDMyNjA0MmYzOWRlYjJjZmM2MjRiZjQ3NyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9jMjMxZDU2MWRmNmY0ZGFjYjNjYjM0MmFkNGNlNDFiMSA9ICQoJzxkaXYgaWQ9Imh0bWxfYzIzMWQ1NjFkZjZmNGRhY2IzY2IzNDJhZDRjZTQxYjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRlc2lnbiBFeGNoYW5nZSxUb3JvbnRvIERvbWluaW9uIENlbnRyZSBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzViMjU3ZjRkMzI2MDQyZjM5ZGViMmNmYzYyNGJmNDc3LnNldENvbnRlbnQoaHRtbF9jMjMxZDU2MWRmNmY0ZGFjYjNjYjM0MmFkNGNlNDFiMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81OWZmNDkzMjY3Mzc0MDNkODhhOTExY2VkYWJkOTllZC5iaW5kUG9wdXAocG9wdXBfNWIyNTdmNGQzMjYwNDJmMzlkZWIyY2ZjNjI0YmY0NzcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfODE2NDhkYWQzNTFhNGQyYjliNzM3MDQ1OTIxOTRlN2IgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDgxOTg1LC03OS4zNzk4MTY5MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85MGRhODY1N2FhZmE0NjJiYTczNDAxODNjYTdlYmE2MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9iMDJmYmVhMzdiMDA0MTZlOTY1ZWVkNmRiZGQwYTk5YSA9ICQoJzxkaXYgaWQ9Imh0bWxfYjAyZmJlYTM3YjAwNDE2ZTk2NWVlZDZkYmRkMGE5OWEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNvbW1lcmNlIENvdXJ0LFZpY3RvcmlhIEhvdGVsIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTBkYTg2NTdhYWZhNDYyYmE3MzQwMTgzY2E3ZWJhNjIuc2V0Q29udGVudChodG1sX2IwMmZiZWEzN2IwMDQxNmU5NjVlZWQ2ZGJkZDBhOTlhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzgxNjQ4ZGFkMzUxYTRkMmI5YjczNzA0NTkyMTk0ZTdiLmJpbmRQb3B1cChwb3B1cF85MGRhODY1N2FhZmE0NjJiYTczNDAxODNjYTdlYmE2Mik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lYTk0YTRiZDVlMWU0MWM1OTMwYzllYzY1ZGI2MjUwOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjczMzI4MjUsLTc5LjQxOTc0OTddLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDE1ZWIzYTQ2ZDBlNDZjNTg5OGMwYjdjNDVhODJkMTkgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZjVlMmNlNDhkYmM1NDY3OWFhY2RkMTZiODcxMTk1MzEgPSAkKCc8ZGl2IGlkPSJodG1sX2Y1ZTJjZTQ4ZGJjNTQ2NzlhYWNkZDE2Yjg3MTE5NTMxIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CZWRmb3JkIFBhcmssTGF3cmVuY2UgTWFub3IgRWFzdCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2QxNWViM2E0NmQwZTQ2YzU4OThjMGI3YzQ1YTgyZDE5LnNldENvbnRlbnQoaHRtbF9mNWUyY2U0OGRiYzU0Njc5YWFjZGQxNmI4NzExOTUzMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9lYTk0YTRiZDVlMWU0MWM1OTMwYzllYzY1ZGI2MjUwOC5iaW5kUG9wdXAocG9wdXBfZDE1ZWIzYTQ2ZDBlNDZjNTg5OGMwYjdjNDVhODJkMTkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjVhNTM4ZWFlYmI3NGM3NDlmNDQ3OWRmYWJmNDUyNWMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MTE2OTQ4LC03OS40MTY5MzU1OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84NzUwZTBhYjcyOTY0M2IxYWQxMzlkODkzNDdhMWYwYSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80Yjk5ZmU0YWYzYmM0NDFlYTFjMThlNGNhMjUyMGViZSA9ICQoJzxkaXYgaWQ9Imh0bWxfNGI5OWZlNGFmM2JjNDQxZWExYzE4ZTRjYTI1MjBlYmUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJvc2VsYXduIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfODc1MGUwYWI3Mjk2NDNiMWFkMTM5ZDg5MzQ3YTFmMGEuc2V0Q29udGVudChodG1sXzRiOTlmZTRhZjNiYzQ0MWVhMWMxOGU0Y2EyNTIwZWJlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y1YTUzOGVhZWJiNzRjNzQ5ZjQ0NzlkZmFiZjQ1MjVjLmJpbmRQb3B1cChwb3B1cF84NzUwZTBhYjcyOTY0M2IxYWQxMzlkODkzNDdhMWYwYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl81ZDg2MjliODNhNjY0MGJhYTFiMmUxMDBkNWY4NzRjZCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5Njk0NzYsLTc5LjQxMTMwNzIwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2ViMDM2NjEyNThjZjQzMTA5OTUwOGY2ZGQ3MjRjYjcxID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzk4ZTA1MDZjMWUyNzQzNjBhYjE1ZTNiNzNjYmRiMmI2ID0gJCgnPGRpdiBpZD0iaHRtbF85OGUwNTA2YzFlMjc0MzYwYWIxNWUzYjczY2JkYjJiNiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Rm9yZXN0IEhpbGwgTm9ydGgsRm9yZXN0IEhpbGwgV2VzdCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2ViMDM2NjEyNThjZjQzMTA5OTUwOGY2ZGQ3MjRjYjcxLnNldENvbnRlbnQoaHRtbF85OGUwNTA2YzFlMjc0MzYwYWIxNWUzYjczY2JkYjJiNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl81ZDg2MjliODNhNjY0MGJhYTFiMmUxMDBkNWY4NzRjZC5iaW5kUG9wdXAocG9wdXBfZWIwMzY2MTI1OGNmNDMxMDk5NTA4ZjZkZDcyNGNiNzEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNGYxYTQ0MTI3YzBmNDdmZmI4ZjA0OTAxMmQ1MmRlOGUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NzI3MDk3LC03OS40MDU2Nzg0MDAwMDAwMV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9jOTIyZDQwNjA2ZWM0ZDQxOWE2YmIwMzgyYmE3YjNhMiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF82NDY1NzViODUwMTE0NzlmODQwYjE4NjY1OTk4ZTFjYyA9ICQoJzxkaXYgaWQ9Imh0bWxfNjQ2NTc1Yjg1MDExNDc5Zjg0MGIxODY2NTk5OGUxY2MiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlRoZSBBbm5leCxOb3J0aCBNaWR0b3duLFlvcmt2aWxsZSBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2M5MjJkNDA2MDZlYzRkNDE5YTZiYjAzODJiYTdiM2EyLnNldENvbnRlbnQoaHRtbF82NDY1NzViODUwMTE0NzlmODQwYjE4NjY1OTk4ZTFjYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80ZjFhNDQxMjdjMGY0N2ZmYjhmMDQ5MDEyZDUyZGU4ZS5iaW5kUG9wdXAocG9wdXBfYzkyMmQ0MDYwNmVjNGQ0MTlhNmJiMDM4MmJhN2IzYTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYWNkNjdlMjE4ZTFlNDExNzk5YmQ2ODczNjE5NDMxZTUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjI2OTU2LC03OS40MDAwNDkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2U5ZDk3YWE2ODZkNzRiMDg5MDBlMjJhN2NkNWVhYjJlID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzYzYmZmNDM5YzVkOTQ5NmViODZhMjhhYTZmOTM2MmUyID0gJCgnPGRpdiBpZD0iaHRtbF82M2JmZjQzOWM1ZDk0OTZlYjg2YTI4YWE2ZjkzNjJlMiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGFyYm9yZCxVbml2ZXJzaXR5IG9mIFRvcm9udG8gQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lOWQ5N2FhNjg2ZDc0YjA4OTAwZTIyYTdjZDVlYWIyZS5zZXRDb250ZW50KGh0bWxfNjNiZmY0MzljNWQ5NDk2ZWI4NmEyOGFhNmY5MzYyZTIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfYWNkNjdlMjE4ZTFlNDExNzk5YmQ2ODczNjE5NDMxZTUuYmluZFBvcHVwKHBvcHVwX2U5ZDk3YWE2ODZkNzRiMDg5MDBlMjJhN2NkNWVhYjJlKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc2N2IyYzYzMjVkYzRlMDdiODdiMWYyZjkyYjJiYzZmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUzMjA1NywtNzkuNDAwMDQ5M10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9hMzcxOTZiYjg5ZjI0MmMwYjI5YzRhNGM5MGNkNjE3YiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83ODUzNjUzZjAwMTQ0ZTQ5OWZlNTA4ZDZiNjA1Y2Q4NiA9ICQoJzxkaXYgaWQ9Imh0bWxfNzg1MzY1M2YwMDE0NGU0OTlmZTUwOGQ2YjYwNWNkODYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNoaW5hdG93bixHcmFuZ2UgUGFyayxLZW5zaW5ndG9uIE1hcmtldCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2EzNzE5NmJiODlmMjQyYzBiMjljNGE0YzkwY2Q2MTdiLnNldENvbnRlbnQoaHRtbF83ODUzNjUzZjAwMTQ0ZTQ5OWZlNTA4ZDZiNjA1Y2Q4Nik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83NjdiMmM2MzI1ZGM0ZTA3Yjg3YjFmMmY5MmIyYmM2Zi5iaW5kUG9wdXAocG9wdXBfYTM3MTk2YmI4OWYyNDJjMGIyOWM0YTRjOTBjZDYxN2IpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfN2E2YzcwZDFjOTk4NDkxOTlkNGIzNTJiNDJlYTVkYTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42Mjg5NDY3LC03OS4zOTQ0MTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzcyOTBlZDM2ZjE4OTQ4MDI4YzUwYWRhZTVjYWM3ODUyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzhhMzkxYWU4MWY4ODRjMTlhZWVmMTU2ODliODQ2ZWU0ID0gJCgnPGRpdiBpZD0iaHRtbF84YTM5MWFlODFmODg0YzE5YWVlZjE1Njg5Yjg0NmVlNCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q04gVG93ZXIsQmF0aHVyc3QgUXVheSxJc2xhbmQgYWlycG9ydCxIYXJib3VyZnJvbnQgV2VzdCxLaW5nIGFuZCBTcGFkaW5hLFJhaWx3YXkgTGFuZHMsU291dGggTmlhZ2FyYSBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzcyOTBlZDM2ZjE4OTQ4MDI4YzUwYWRhZTVjYWM3ODUyLnNldENvbnRlbnQoaHRtbF84YTM5MWFlODFmODg0YzE5YWVlZjE1Njg5Yjg0NmVlNCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83YTZjNzBkMWM5OTg0OTE5OWQ0YjM1MmI0MmVhNWRhMS5iaW5kUG9wdXAocG9wdXBfNzI5MGVkMzZmMTg5NDgwMjhjNTBhZGFlNWNhYzc4NTIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfMzA3NmZjZDFhODA0NDQwM2FmN2UyOGMxNGZlYzczNjIgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDY0MzUyLC03OS4zNzQ4NDU5OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yM2ZlYjE0ZTZmZDU0MWNiYTUxOWUzOTAxMmJiZjAyNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8wNzFjMjQxNDI0YTg0Mjk4OWI0MWY3NGM4NmZhZjJkMiA9ICQoJzxkaXYgaWQ9Imh0bWxfMDcxYzI0MTQyNGE4NDI5ODliNDFmNzRjODZmYWYyZDIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlN0biBBIFBPIEJveGVzIDI1IFRoZSBFc3BsYW5hZGUgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8yM2ZlYjE0ZTZmZDU0MWNiYTUxOWUzOTAxMmJiZjAyNC5zZXRDb250ZW50KGh0bWxfMDcxYzI0MTQyNGE4NDI5ODliNDFmNzRjODZmYWYyZDIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMzA3NmZjZDFhODA0NDQwM2FmN2UyOGMxNGZlYzczNjIuYmluZFBvcHVwKHBvcHVwXzIzZmViMTRlNmZkNTQxY2JhNTE5ZTM5MDEyYmJmMDI0KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2QzOGMyYmVlMzcwYTQ3ZmU4ZTg3YzhhMTA5ZWY0MzUzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQ4NDI5MiwtNzkuMzgyMjgwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zNTVlYzA2YzQwMWU0NzExOGM0ZTMyZDdiZTNiODM1NyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF83NGZkYTE2YzUxNWQ0ZmVmOWIyNjQ2OTFjMzkwZDhmMiA9ICQoJzxkaXYgaWQ9Imh0bWxfNzRmZGExNmM1MTVkNGZlZjliMjY0NjkxYzM5MGQ4ZjIiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkZpcnN0IENhbmFkaWFuIFBsYWNlLFVuZGVyZ3JvdW5kIGNpdHkgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8zNTVlYzA2YzQwMWU0NzExOGM0ZTMyZDdiZTNiODM1Ny5zZXRDb250ZW50KGh0bWxfNzRmZGExNmM1MTVkNGZlZjliMjY0NjkxYzM5MGQ4ZjIpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDM4YzJiZWUzNzBhNDdmZThlODdjOGExMDllZjQzNTMuYmluZFBvcHVwKHBvcHVwXzM1NWVjMDZjNDAxZTQ3MTE4YzRlMzJkN2JlM2I4MzU3KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzIwMzg4NTBlNWIwMjQ2ZWFhZGZiODllMzA4OGY4MjdiID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzE4NTE3OTk5OTk5OTk2LC03OS40NjQ3NjMyOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9mMzZmODAyZTVkYzI0ZDVhOGYxNWZjMThkOTBkOGRhOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84ODg1OTk4NjliYjg0ZTk0YjE3OWU1ZjBhYmUzNjEzNSA9ICQoJzxkaXYgaWQ9Imh0bWxfODg4NTk5ODY5YmI4NGU5NGIxNzllNWYwYWJlMzYxMzUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxhd3JlbmNlIEhlaWdodHMsTGF3cmVuY2UgTWFub3IgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9mMzZmODAyZTVkYzI0ZDVhOGYxNWZjMThkOTBkOGRhOS5zZXRDb250ZW50KGh0bWxfODg4NTk5ODY5YmI4NGU5NGIxNzllNWYwYWJlMzYxMzUpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfMjAzODg1MGU1YjAyNDZlYWFkZmI4OWUzMDg4ZjgyN2IuYmluZFBvcHVwKHBvcHVwX2YzNmY4MDJlNWRjMjRkNWE4ZjE1ZmMxOGQ5MGQ4ZGE5KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzRlMGIxMTNiNjljNTRiM2U4OTM4MDhjZGUyNWExMWIzID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA5NTc3LC03OS40NDUwNzI1OTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF82NjlkZjgxOWE1OGU0NzY1YjM4Mjg5ZTcyNzNlMmY1YSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8yNzI1NGMzODBmZWY0NjNjYWYzODQ0MjY4OTZkMDViYyA9ICQoJzxkaXYgaWQ9Imh0bWxfMjcyNTRjMzgwZmVmNDYzY2FmMzg0NDI2ODk2ZDA1YmMiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkdsZW5jYWlybiBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzY2OWRmODE5YTU4ZTQ3NjViMzgyODllNzI3M2UyZjVhLnNldENvbnRlbnQoaHRtbF8yNzI1NGMzODBmZWY0NjNjYWYzODQ0MjY4OTZkMDViYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80ZTBiMTEzYjY5YzU0YjNlODkzODA4Y2RlMjVhMTFiMy5iaW5kUG9wdXAocG9wdXBfNjY5ZGY4MTlhNThlNDc2NWIzODI4OWU3MjczZTJmNWEpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjlmZjIzNzVkNDNjNDQ0OWJmMzgzZWNjOTFhM2ZmMWEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42OTM3ODEzLC03OS40MjgxOTE0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8wMzg5MzcwYjA2ZTQ0M2E2YjcwMTY4NjZhYzIxMWRiNiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF9kNDYyM2YyYjNkNmY0ZDRmYjFjZGVhOWMxNzNlMDMxMSA9ICQoJzxkaXYgaWQ9Imh0bWxfZDQ2MjNmMmIzZDZmNGQ0ZmIxY2RlYTljMTczZTAzMTEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkh1bWV3b29kLUNlZGFydmFsZSBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzAzODkzNzBiMDZlNDQzYTZiNzAxNjg2NmFjMjExZGI2LnNldENvbnRlbnQoaHRtbF9kNDYyM2YyYjNkNmY0ZDRmYjFjZGVhOWMxNzNlMDMxMSk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mOWZmMjM3NWQ0M2M0NDQ5YmYzODNlY2M5MWEzZmYxYS5iaW5kUG9wdXAocG9wdXBfMDM4OTM3MGIwNmU0NDNhNmI3MDE2ODY2YWMyMTFkYjYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZDBhNjFlOWNjNTYxNDhhZDg3Y2EyODc4M2YwNDBhY2YgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42ODkwMjU2LC03OS40NTM1MTJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzhkYTFjYjlmZTVjNDM1ZmE1Mjc1NTRkNGNiOWE3OTUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfZGJlM2ZjNGMwYzYxNDE4MTllZDUzNzcyNTFiYzQ5NjcgPSAkKCc8ZGl2IGlkPSJodG1sX2RiZTNmYzRjMGM2MTQxODE5ZWQ1Mzc3MjUxYmM0OTY3IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DYWxlZG9uaWEtRmFpcmJhbmtzIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzhkYTFjYjlmZTVjNDM1ZmE1Mjc1NTRkNGNiOWE3OTUuc2V0Q29udGVudChodG1sX2RiZTNmYzRjMGM2MTQxODE5ZWQ1Mzc3MjUxYmM0OTY3KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2QwYTYxZTljYzU2MTQ4YWQ4N2NhMjg3ODNmMDQwYWNmLmJpbmRQb3B1cChwb3B1cF8zOGRhMWNiOWZlNWM0MzVmYTUyNzU1NGQ0Y2I5YTc5NSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9lNTZkNGZhYzFmOGQ0OWZhOTk2YmQwZDVjNzdkNGNmNCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2OTU0MiwtNzkuNDIyNTYzN10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yZjRkNjc0Y2YyOTc0MWY2ODUyODY5ZWI2MTZkYjgxNCA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80YmE0MjhhZjg0ODc0MzBlYmVhMjM2MTI4YmJhNjY4OCA9ICQoJzxkaXYgaWQ9Imh0bWxfNGJhNDI4YWY4NDg3NDMwZWJlYTIzNjEyOGJiYTY2ODgiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkNocmlzdGllIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmY0ZDY3NGNmMjk3NDFmNjg1Mjg2OWViNjE2ZGI4MTQuc2V0Q29udGVudChodG1sXzRiYTQyOGFmODQ4NzQzMGViZWEyMzYxMjhiYmE2Njg4KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2U1NmQ0ZmFjMWY4ZDQ5ZmE5OTZiZDBkNWM3N2Q0Y2Y0LmJpbmRQb3B1cChwb3B1cF8yZjRkNjc0Y2YyOTc0MWY2ODUyODY5ZWI2MTZkYjgxNCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MmNkZGQ5MzU2NDc0YzNlYWIyZDY0MTExMjdmMTVlMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2OTAwNTEwMDAwMDAxLC03OS40NDIyNTkzXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzk4MDlhMWY2ZTVhODRlYWFiYjhlY2ZmYmU4YTBiNDIzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzEyYmIwODcyOTAxNDQyNzY4M2YwMmFmNmI4YjMyNmFhID0gJCgnPGRpdiBpZD0iaHRtbF8xMmJiMDg3MjkwMTQ0Mjc2ODNmMDJhZjZiOGIzMjZhYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RG92ZXJjb3VydCBWaWxsYWdlLER1ZmZlcmluIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTgwOWExZjZlNWE4NGVhYWJiOGVjZmZiZThhMGI0MjMuc2V0Q29udGVudChodG1sXzEyYmIwODcyOTAxNDQyNzY4M2YwMmFmNmI4YjMyNmFhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzQyY2RkZDkzNTY0NzRjM2VhYjJkNjQxMTEyN2YxNWUwLmJpbmRQb3B1cChwb3B1cF85ODA5YTFmNmU1YTg0ZWFhYmI4ZWNmZmJlOGEwYjQyMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84YTNkYjMzN2E4MzU0N2UyYjhhZmEyZjYzODhlYjQ3YyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY0NzkyNjcwMDAwMDAwNiwtNzkuNDE5NzQ5N10sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF84YzVkZGQ1MTUxYWU0NDg5YTBkNjRhNDFlMTNmMTJlYyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80NjQwOGE0MzQ0MjQ0ZmQ3ODAxZDBhMjQ2OTM0YjdlNSA9ICQoJzxkaXYgaWQ9Imh0bWxfNDY0MDhhNDM0NDI0NGZkNzgwMWQwYTI0NjkzNGI3ZTUiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkxpdHRsZSBQb3J0dWdhbCxUcmluaXR5IENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOGM1ZGRkNTE1MWFlNDQ4OWEwZDY0YTQxZTEzZjEyZWMuc2V0Q29udGVudChodG1sXzQ2NDA4YTQzNDQyNDRmZDc4MDFkMGEyNDY5MzRiN2U1KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzhhM2RiMzM3YTgzNTQ3ZTJiOGFmYTJmNjM4OGViNDdjLmJpbmRQb3B1cChwb3B1cF84YzVkZGQ1MTUxYWU0NDg5YTBkNjRhNDFlMTNmMTJlYyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yNTQxMzA5ZDg5NTY0MGY2YWY1NjE0MjJiYTA3YmVjOCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYzNjg0NzIsLTc5LjQyODE5MTQwMDAwMDAyXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzlhZTMzM2VjMmY0MTQ4MTY5OGIxNWY1ZDVmODE1YWNiID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI4NGJmYWJmY2I3ZTRiZDBiYzRmNWU2NjdlYmFkYmFmID0gJCgnPGRpdiBpZD0iaHRtbF8yODRiZmFiZmNiN2U0YmQwYmM0ZjVlNjY3ZWJhZGJhZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+QnJvY2t0b24sRXhoaWJpdGlvbiBQbGFjZSxQYXJrZGFsZSBWaWxsYWdlIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOWFlMzMzZWMyZjQxNDgxNjk4YjE1ZjVkNWY4MTVhY2Iuc2V0Q29udGVudChodG1sXzI4NGJmYWJmY2I3ZTRiZDBiYzRmNWU2NjdlYmFkYmFmKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzI1NDEzMDlkODk1NjQwZjZhZjU2MTQyMmJhMDdiZWM4LmJpbmRQb3B1cChwb3B1cF85YWUzMzNlYzJmNDE0ODE2OThiMTVmNWQ1ZjgxNWFjYik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8yNTk0ZDgzNWQwZmQ0ZGIyYjI0ZWU3MDM1MTAyODhkMiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjcxMzc1NjIwMDAwMDAwNiwtNzkuNDkwMDczOF0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8zOGNhYzBiNjhiODA0YTE5YTA5Y2VhOWI1MzI2ZDcyMyA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xMTUxYzcyODkyNzQ0MjFiOThmNDU0Njg4NDc0NmFiMSA9ICQoJzxkaXYgaWQ9Imh0bWxfMTE1MWM3Mjg5Mjc0NDIxYjk4ZjQ1NDY4ODQ3NDZhYjEiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkRvd25zdmlldyxOb3J0aCBQYXJrLFVwd29vZCBQYXJrIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzhjYWMwYjY4YjgwNGExOWEwOWNlYTliNTMyNmQ3MjMuc2V0Q29udGVudChodG1sXzExNTFjNzI4OTI3NDQyMWI5OGY0NTQ2ODg0NzQ2YWIxKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzI1OTRkODM1ZDBmZDRkYjJiMjRlZTcwMzUxMDI4OGQyLmJpbmRQb3B1cChwb3B1cF8zOGNhYzBiNjhiODA0YTE5YTA5Y2VhOWI1MzI2ZDcyMyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hZWU3N2VlZjczZTg0ZWNkOTJhMWY2ZjY5ZTg2YzFhNiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5MTExNTgsLTc5LjQ3NjAxMzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzlhZWM0YzY2ZGUzODQxMWNiZDM1ZGNhN2UzZWZmNTQzID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzk0ZTg5NmYyODIxZTRmZGU4YjhiNjc4ZWUxNGQ1N2EwID0gJCgnPGRpdiBpZD0iaHRtbF85NGU4OTZmMjgyMWU0ZmRlOGI4YjY3OGVlMTRkNTdhMCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+RGVsIFJheSxLZWVsZXNkYWxlLE1vdW50IERlbm5pcyxTaWx2ZXJ0aG9ybiBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzlhZWM0YzY2ZGUzODQxMWNiZDM1ZGNhN2UzZWZmNTQzLnNldENvbnRlbnQoaHRtbF85NGU4OTZmMjgyMWU0ZmRlOGI4YjY3OGVlMTRkNTdhMCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hZWU3N2VlZjczZTg0ZWNkOTJhMWY2ZjY5ZTg2YzFhNi5iaW5kUG9wdXAocG9wdXBfOWFlYzRjNjZkZTM4NDExY2JkMzVkY2E3ZTNlZmY1NDMpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfOWJjN2MxNDI5ZjFmNGQ3MWIxNTE2M2RiNzRkYzMxODEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NzMxODUyOTk5OTk5OSwtNzkuNDg3MjYxOTAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMmYwNTFiOTUzZGRhNDRlYjg5MzMzZWU1OWRiY2I4M2QgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTFkMDdkZTk3NGI1NDVmN2I4YWFlZmRkMmI0Y2Y4MjQgPSAkKCc8ZGl2IGlkPSJodG1sXzUxZDA3ZGU5NzRiNTQ1ZjdiOGFhZWZkZDJiNGNmODI0IiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgSnVuY3Rpb24gTm9ydGgsUnVubnltZWRlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMmYwNTFiOTUzZGRhNDRlYjg5MzMzZWU1OWRiY2I4M2Quc2V0Q29udGVudChodG1sXzUxZDA3ZGU5NzRiNTQ1ZjdiOGFhZWZkZDJiNGNmODI0KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzliYzdjMTQyOWYxZjRkNzFiMTUxNjNkYjc0ZGMzMTgxLmJpbmRQb3B1cChwb3B1cF8yZjA1MWI5NTNkZGE0NGViODkzMzNlZTU5ZGJjYjgzZCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9mM2MxZDBmMTg1NTY0ZTdjYThiYmE2NDc0YTYxYWZlOSA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MTYwODMsLTc5LjQ2NDc2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2YwODZmZGNkZTVlZDRkNTNhOTdjOTg5MDk3MzRmNmQyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzNlMjBmMTdiYTBkYjQ5NzA4ZWEyMmM4MWViMjBhYzJmID0gJCgnPGRpdiBpZD0iaHRtbF8zZTIwZjE3YmEwZGI0OTcwOGVhMjJjODFlYjIwYWMyZiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SGlnaCBQYXJrLFRoZSBKdW5jdGlvbiBTb3V0aCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2YwODZmZGNkZTVlZDRkNTNhOTdjOTg5MDk3MzRmNmQyLnNldENvbnRlbnQoaHRtbF8zZTIwZjE3YmEwZGI0OTcwOGVhMjJjODFlYjIwYWMyZik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9mM2MxZDBmMTg1NTY0ZTdjYThiYmE2NDc0YTYxYWZlOS5iaW5kUG9wdXAocG9wdXBfZjA4NmZkY2RlNWVkNGQ1M2E5N2M5ODkwOTczNGY2ZDIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmM5MDk0ZGMwYTc1NDhhM2E1ZTBjMzQzOWViN2U5NGUgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NDg5NTk3LC03OS40NTYzMjVdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZGRjZmIzNTA2OTJkNDE3MjkzNjdlOTMzNjE3OTFmN2IgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYThhZGMyMTFmZDk0NDhiOWE0NWI2NjAzOTNkMTYwN2UgPSAkKCc8ZGl2IGlkPSJodG1sX2E4YWRjMjExZmQ5NDQ4YjlhNDViNjYwMzkzZDE2MDdlIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5QYXJrZGFsZSxSb25jZXN2YWxsZXMgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9kZGNmYjM1MDY5MmQ0MTcyOTM2N2U5MzM2MTc5MWY3Yi5zZXRDb250ZW50KGh0bWxfYThhZGMyMTFmZDk0NDhiOWE0NWI2NjAzOTNkMTYwN2UpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNmM5MDk0ZGMwYTc1NDhhM2E1ZTBjMzQzOWViN2U5NGUuYmluZFBvcHVwKHBvcHVwX2RkY2ZiMzUwNjkyZDQxNzI5MzY3ZTkzMzYxNzkxZjdiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzc3ZDMxYjIwZTgwZDQwNTA4YzUwOTlmOWYzYmY4NDIyID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUxNTcwNiwtNzkuNDg0NDQ5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF85MWJkNmY2YThhOTM0MzYwOWFiZjAzNzFhMWEyNjM1ZiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF80MDYyODNhY2E5YzQ0OTMzYWRjNWI2YTJjYTc0NTcyNiA9ICQoJzxkaXYgaWQ9Imh0bWxfNDA2MjgzYWNhOWM0NDkzM2FkYzViNmEyY2E3NDU3MjYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPlJ1bm55bWVkZSxTd2Fuc2VhIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfOTFiZDZmNmE4YTkzNDM2MDlhYmYwMzcxYTFhMjYzNWYuc2V0Q29udGVudChodG1sXzQwNjI4M2FjYTljNDQ5MzNhZGM1YjZhMmNhNzQ1NzI2KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzc3ZDMxYjIwZTgwZDQwNTA4YzUwOTlmOWYzYmY4NDIyLmJpbmRQb3B1cChwb3B1cF85MWJkNmY2YThhOTM0MzYwOWFiZjAzNzFhMWEyNjM1Zik7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8zOWJjZDM4NTY3OGI0NjMzOWQ0NjQ1YzRjNDNmZGQ5YiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY2MjMwMTUsLTc5LjM4OTQ5MzhdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfNjFlMzExNGNkYWIzNGZlNGI0ZDhkMDM2ZjFmZDcyZjcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfMDVjY2VkYTNkZTE0NGQ3ZDgxNTljNTRkODQyZDE0OTIgPSAkKCc8ZGl2IGlkPSJodG1sXzA1Y2NlZGEzZGUxNDRkN2Q4MTU5YzU0ZDg0MmQxNDkyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5RdWVlbiYjMzk7cyBQYXJrIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNjFlMzExNGNkYWIzNGZlNGI0ZDhkMDM2ZjFmZDcyZjcuc2V0Q29udGVudChodG1sXzA1Y2NlZGEzZGUxNDRkN2Q4MTU5YzU0ZDg0MmQxNDkyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzM5YmNkMzg1Njc4YjQ2MzM5ZDQ2NDVjNGM0M2ZkZDliLmJpbmRQb3B1cChwb3B1cF82MWUzMTE0Y2RhYjM0ZmU0YjRkOGQwMzZmMWZkNzJmNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl83YzVkNzhhYjFlOTc0OTM0OGYyYWVhMWE2YzI0MTk2MiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYzNjk2NTYsLTc5LjYxNTgxODk5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzliMTA1YTA1NjhiNDQ0ZjNhMDNhMGFjZTBhYTJmNDAyID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzMwN2IzZDkwOGRiYzQzZDM5YjYzZjBjNTRhNGU5ZTUwID0gJCgnPGRpdiBpZD0iaHRtbF8zMDdiM2Q5MDhkYmM0M2QzOWI2M2YwYzU0YTRlOWU1MCIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Q2FuYWRhIFBvc3QgR2F0ZXdheSBQcm9jZXNzaW5nIENlbnRyZSBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzliMTA1YTA1NjhiNDQ0ZjNhMDNhMGFjZTBhYTJmNDAyLnNldENvbnRlbnQoaHRtbF8zMDdiM2Q5MDhkYmM0M2QzOWI2M2YwYzU0YTRlOWU1MCk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl83YzVkNzhhYjFlOTc0OTM0OGYyYWVhMWE2YzI0MTk2Mi5iaW5kUG9wdXAocG9wdXBfOWIxMDVhMDU2OGI0NDRmM2EwM2EwYWNlMGFhMmY0MDIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfZjQxNGY0NGU0MTBlNGM2Y2I5ZmIwYTAwNzk5MDY2YzkgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NjI3NDM5LC03OS4zMjE1NThdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZmJlYTdjMjkwNDI3NGVkMWFhNDcwYTYxNjMzZTUzZjUgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfN2I3MzkzMjZlYThmNDZjM2IyMDE3NGExYTBhYWFmMTIgPSAkKCc8ZGl2IGlkPSJodG1sXzdiNzM5MzI2ZWE4ZjQ2YzNiMjAxNzRhMWEwYWFhZjEyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CdXNpbmVzcyBSZXBseSBNYWlsIFByb2Nlc3NpbmcgQ2VudHJlIDk2OSBFYXN0ZXJuIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZmJlYTdjMjkwNDI3NGVkMWFhNDcwYTYxNjMzZTUzZjUuc2V0Q29udGVudChodG1sXzdiNzM5MzI2ZWE4ZjQ2YzNiMjAxNzRhMWEwYWFhZjEyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2Y0MTRmNDRlNDEwZTRjNmNiOWZiMGEwMDc5OTA2NmM5LmJpbmRQb3B1cChwb3B1cF9mYmVhN2MyOTA0Mjc0ZWQxYWE0NzBhNjE2MzNlNTNmNSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl8wNWExMDViNTc1OGU0NTZjYjU2MzA2MmUxYTcxMjBkNyA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYwNTY0NjYsLTc5LjUwMTMyMDcwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwX2Y4ZjA0ZTAyZmE5NTQ1ODRiMWZiZDZiMDgyMWE1ZDA3ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2RlYTJmODhhZmNiODQ0Y2Q5NjA4ZTQwNGJjOTk4MDVhID0gJCgnPGRpdiBpZD0iaHRtbF9kZWEyZjg4YWZjYjg0NGNkOTYwOGU0MDRiYzk5ODA1YSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtYmVyIEJheSBTaG9yZXMsTWltaWNvIFNvdXRoLE5ldyBUb3JvbnRvIENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfZjhmMDRlMDJmYTk1NDU4NGIxZmJkNmIwODIxYTVkMDcuc2V0Q29udGVudChodG1sX2RlYTJmODhhZmNiODQ0Y2Q5NjA4ZTQwNGJjOTk4MDVhKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzA1YTEwNWI1NzU4ZTQ1NmNiNTYzMDYyZTFhNzEyMGQ3LmJpbmRQb3B1cChwb3B1cF9mOGYwNGUwMmZhOTU0NTg0YjFmYmQ2YjA4MjFhNWQwNyk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9hZDZlMWM0MmMwZTI0NmQyOWU0NjQxNTdiNTIwZjA4ZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYwMjQxMzcwMDAwMDAxLC03OS41NDM0ODQwOTk5OTk5OV0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF9kZTY1OGQwMDRhM2U0NGNlOTFkNWEwMmJkNGQwZjRkOSA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF8xZjM4NjJkZWNhYTQ0Nzc0YmFlYmUxYTg3ODYwMjMyNiA9ICQoJzxkaXYgaWQ9Imh0bWxfMWYzODYyZGVjYWE0NDc3NGJhZWJlMWE4Nzg2MDIzMjYiIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkFsZGVyd29vZCxMb25nIEJyYW5jaCBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2RlNjU4ZDAwNGEzZTQ0Y2U5MWQ1YTAyYmQ0ZDBmNGQ5LnNldENvbnRlbnQoaHRtbF8xZjM4NjJkZWNhYTQ0Nzc0YmFlYmUxYTg3ODYwMjMyNik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9hZDZlMWM0MmMwZTI0NmQyOWU0NjQxNTdiNTIwZjA4Zi5iaW5kUG9wdXAocG9wdXBfZGU2NThkMDA0YTNlNDRjZTkxZDVhMDJiZDRkMGY0ZDkpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNmJiMjc3NjY2MzlkNDBmYzhjMWQ1ZDUwMmQ2ZTk1MzMgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My42NTM2NTM2MDAwMDAwMDUsLTc5LjUwNjk0MzZdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzAwYjVlYiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiMwMGI1ZWIiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfMzFmMjU0NDMwNjFlNDY4OTkzZjJlMjlkNGQ2NTMyMTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYjI2YzE2NGRhY2RhNDBmMGFhMGEyMGVlM2RjYWQ5NzIgPSAkKCc8ZGl2IGlkPSJodG1sX2IyNmMxNjRkYWNkYTQwZjBhYTBhMjBlZTNkY2FkOTcyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5UaGUgS2luZ3N3YXksTW9udGdvbWVyeSBSb2FkLE9sZCBNaWxsIE5vcnRoIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMzFmMjU0NDMwNjFlNDY4OTkzZjJlMjlkNGQ2NTMyMTguc2V0Q29udGVudChodG1sX2IyNmMxNjRkYWNkYTQwZjBhYTBhMjBlZTNkY2FkOTcyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzZiYjI3NzY2NjM5ZDQwZmM4YzFkNWQ1MDJkNmU5NTMzLmJpbmRQb3B1cChwb3B1cF8zMWYyNTQ0MzA2MWU0Njg5OTNmMmUyOWQ0ZDY1MzIxOCk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl9kMjZlYzQ3ZTBkNDI0YTBiODY0MzdmM2Y1ZTZkNmU5NCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjYzNjI1NzksLTc5LjQ5ODUwOTA5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzFjZmM3NTE5NTAzNTQ4YzI5ZTUyMjA0YTljMzc5NzVkID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzY0ZjVjMWM1NzY1OTRlZDU5MjVmYjEwNDg0MTZmM2JhID0gJCgnPGRpdiBpZD0iaHRtbF82NGY1YzFjNTc2NTk0ZWQ1OTI1ZmIxMDQ4NDE2ZjNiYSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtYmVyIEJheSxLaW5nJiMzOTtzIE1pbGwgUGFyayxLaW5nc3dheSBQYXJrIFNvdXRoIEVhc3QsTWltaWNvIE5FLE9sZCBNaWxsIFNvdXRoLFRoZSBRdWVlbnN3YXkgRWFzdCxSb3lhbCBZb3JrIFNvdXRoIEVhc3QsU3VubnlsZWEgQ2x1c3RlciAyPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF8xY2ZjNzUxOTUwMzU0OGMyOWU1MjIwNGE5YzM3OTc1ZC5zZXRDb250ZW50KGh0bWxfNjRmNWMxYzU3NjU5NGVkNTkyNWZiMTA0ODQxNmYzYmEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfZDI2ZWM0N2UwZDQyNGEwYjg2NDM3ZjNmNWU2ZDZlOTQuYmluZFBvcHVwKHBvcHVwXzFjZmM3NTE5NTAzNTQ4YzI5ZTUyMjA0YTljMzc5NzVkKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzkzYWVlZjU4ZDIzNjQ3ZGZhZmQ0YWZlMWRmNjBjZDNmID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjI4ODQwOCwtNzkuNTIwOTk5NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWM3MDQzYzVhOTM1NDU3Y2IyMzg5YWI4YmY4YzJiNTggPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTMyYWFjNDU1NzY2NDcwNmExZjkyMTdmZmM0Y2MxYTEgPSAkKCc8ZGl2IGlkPSJodG1sXzkzMmFhYzQ1NTc2NjQ3MDZhMWY5MjE3ZmZjNGNjMWExIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc3dheSBQYXJrIFNvdXRoIFdlc3QsTWltaWNvIE5XLFRoZSBRdWVlbnN3YXkgV2VzdCxSb3lhbCBZb3JrIFNvdXRoIFdlc3QsU291dGggb2YgQmxvb3IgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hYzcwNDNjNWE5MzU0NTdjYjIzODlhYjhiZjhjMmI1OC5zZXRDb250ZW50KGh0bWxfOTMyYWFjNDU1NzY2NDcwNmExZjkyMTdmZmM0Y2MxYTEpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfOTNhZWVmNThkMjM2NDdkZmFmZDRhZmUxZGY2MGNkM2YuYmluZFBvcHVwKHBvcHVwX2FjNzA0M2M1YTkzNTQ1N2NiMjM4OWFiOGJmOGMyYjU4KTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzVhNThkMDJiOTY0YTQxYTVhYjMwMWYxZTk5NGI2MjYxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjUwOTQzMiwtNzkuNTU0NzI0NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiIzgwMDBmZiIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiM4MDAwZmYiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjkzOGRhYTFjMTEwNGU3YzgwNWUyYWI1NzMyYzY5MGIgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfYzQ1MzRkNzhkMzM1NDUyN2EwZjNmNjQzZGQwOGEwY2IgPSAkKCc8ZGl2IGlkPSJodG1sX2M0NTM0ZDc4ZDMzNTQ1MjdhMGYzZjY0M2RkMDhhMGNiIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5DbG92ZXJkYWxlLElzbGluZ3RvbixNYXJ0aW4gR3JvdmUsUHJpbmNlc3MgR2FyZGVucyxXZXN0IERlYW5lIFBhcmsgQ2x1c3RlciAxPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9iOTM4ZGFhMWMxMTA0ZTdjODA1ZTJhYjU3MzJjNjkwYi5zZXRDb250ZW50KGh0bWxfYzQ1MzRkNzhkMzM1NDUyN2EwZjNmNjQzZGQwOGEwY2IpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNWE1OGQwMmI5NjRhNDFhNWFiMzAxZjFlOTk0YjYyNjEuYmluZFBvcHVwKHBvcHVwX2I5MzhkYWExYzExMDRlN2M4MDVlMmFiNTczMmM2OTBiKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IxZTNjMjM4Zjc5MTQwZjliNDE0OTU2NGViNDk5NzgwID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjQzNTE1MiwtNzkuNTc3MjAwNzk5OTk5OTldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYjlhNDBkMmU1YTBlNDE1MzhjMTcwZWU1MWY2MDk1ZWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNjZmNTVhZGQ4YWZiNGM3NGEzNGFiNTUwMzU0YmIwNjIgPSAkKCc8ZGl2IGlkPSJodG1sXzY2ZjU1YWRkOGFmYjRjNzRhMzRhYjU1MDM1NGJiMDYyIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5CbG9vcmRhbGUgR2FyZGVucyxFcmluZ2F0ZSxNYXJrbGFuZCBXb29kLE9sZCBCdXJuaGFtdGhvcnBlIENsdXN0ZXIgMDwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfYjlhNDBkMmU1YTBlNDE1MzhjMTcwZWU1MWY2MDk1ZWEuc2V0Q29udGVudChodG1sXzY2ZjU1YWRkOGFmYjRjNzRhMzRhYjU1MDM1NGJiMDYyKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2IxZTNjMjM4Zjc5MTQwZjliNDE0OTU2NGViNDk5NzgwLmJpbmRQb3B1cChwb3B1cF9iOWE0MGQyZTVhMGU0MTUzOGMxNzBlZTUxZjYwOTVlYSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl80MjZiZDc4NmY2Yjc0YTJmYTk3NThiZmJiMzk5YzcyMCA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjc1NjMwMzMsLTc5LjU2NTk2MzI5OTk5OTk5XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiNmZmIzNjAiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjZmZiMzYwIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzc1MTc0MDQ5MzU0NzQ3ZjY5NDA5N2NjY2IxMjY1ODJmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzI4NjkyMzBhMDIwNTQ0MTZhYjA1Mjg1YjNiOWUxN2NiID0gJCgnPGRpdiBpZD0iaHRtbF8yODY5MjMwYTAyMDU0NDE2YWIwNTI4NWIzYjllMTdjYiIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+SHVtYmVyIFN1bW1pdCBDbHVzdGVyIDQ8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzc1MTc0MDQ5MzU0NzQ3ZjY5NDA5N2NjY2IxMjY1ODJmLnNldENvbnRlbnQoaHRtbF8yODY5MjMwYTAyMDU0NDE2YWIwNTI4NWIzYjllMTdjYik7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl80MjZiZDc4NmY2Yjc0YTJmYTk3NThiZmJiMzk5YzcyMC5iaW5kUG9wdXAocG9wdXBfNzUxNzQwNDkzNTQ3NDdmNjk0MDk3Y2NjYjEyNjU4MmYpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNjJjZTdjZDEzMzNlNDY4ZWE2NzI1YWRkYzFlMWRkOTEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MjQ3NjU5LC03OS41MzIyNDI0MDAwMDAwMl0sCiAgICAgICAgICAgICAgICB7CiAgImJ1YmJsaW5nTW91c2VFdmVudHMiOiB0cnVlLAogICJjb2xvciI6ICIjODAwMGZmIiwKICAiZGFzaEFycmF5IjogbnVsbCwKICAiZGFzaE9mZnNldCI6IG51bGwsCiAgImZpbGwiOiB0cnVlLAogICJmaWxsQ29sb3IiOiAiIzgwMDBmZiIsCiAgImZpbGxPcGFjaXR5IjogMC43LAogICJmaWxsUnVsZSI6ICJldmVub2RkIiwKICAibGluZUNhcCI6ICJyb3VuZCIsCiAgImxpbmVKb2luIjogInJvdW5kIiwKICAib3BhY2l0eSI6IDEuMCwKICAicmFkaXVzIjogNSwKICAic3Ryb2tlIjogdHJ1ZSwKICAid2VpZ2h0IjogMwp9CiAgICAgICAgICAgICAgICApLmFkZFRvKG1hcF85NWY3NjA3NTRlYmE0NjI5YTJmZGU3YTY3OGZmNDgxNyk7CiAgICAgICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBwb3B1cF8yYTIwNWQ0Njk1OTk0OGJiOGQxZjA0MTAwZTE2Mjk0MiA9IEwucG9wdXAoe21heFdpZHRoOiAnMzAwJ30pOwoKICAgICAgICAgICAgCiAgICAgICAgICAgICAgICB2YXIgaHRtbF84N2NkYzhjZjhjMzc0MzU2YjUwZmQzMzM4OGUxM2MwNyA9ICQoJzxkaXYgaWQ9Imh0bWxfODdjZGM4Y2Y4YzM3NDM1NmI1MGZkMzMzODhlMTNjMDciIHN0eWxlPSJ3aWR0aDogMTAwLjAlOyBoZWlnaHQ6IDEwMC4wJTsiPkVtZXJ5LEh1bWJlcmxlYSBDbHVzdGVyIDE8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwXzJhMjA1ZDQ2OTU5OTQ4YmI4ZDFmMDQxMDBlMTYyOTQyLnNldENvbnRlbnQoaHRtbF84N2NkYzhjZjhjMzc0MzU2YjUwZmQzMzM4OGUxM2MwNyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl82MmNlN2NkMTMzM2U0NjhlYTY3MjVhZGRjMWUxZGQ5MS5iaW5kUG9wdXAocG9wdXBfMmEyMDVkNDY5NTk5NDhiYjhkMWYwNDEwMGUxNjI5NDIpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfYjI1OWExNmQyNmU2NDg1ZmFlZDY1OTc4NmEyOTAzNGEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43MDY4NzYsLTc5LjUxODE4ODQwMDAwMDAxXSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiMwMGI1ZWIiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjMDBiNWViIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzA4YmZlOTBmNmVhYzRiYmI5MzUzMmY4Nzk0NmExMzA5ID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sXzgxOTczM2NjNzNiNzQzMWM5Y2U3NjM1NzJmMjI2NGFlID0gJCgnPGRpdiBpZD0iaHRtbF84MTk3MzNjYzczYjc0MzFjOWNlNzYzNTcyZjIyNjRhZSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+V2VzdG9uIENsdXN0ZXIgMjwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfMDhiZmU5MGY2ZWFjNGJiYjkzNTMyZjg3OTQ2YTEzMDkuc2V0Q29udGVudChodG1sXzgxOTczM2NjNzNiNzQzMWM5Y2U3NjM1NzJmMjI2NGFlKTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyX2IyNTlhMTZkMjZlNjQ4NWZhZWQ2NTk3ODZhMjkwMzRhLmJpbmRQb3B1cChwb3B1cF8wOGJmZTkwZjZlYWM0YmJiOTM1MzJmODc5NDZhMTMwOSk7CgogICAgICAgICAgICAKICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgY2lyY2xlX21hcmtlcl84MGIzZGZjNGUwODc0YzRiOTZhY2FkNGJkNzA1MjkxZiA9IEwuY2lyY2xlTWFya2VyKAogICAgICAgICAgICAgICAgWzQzLjY5NjMxOSwtNzkuNTMyMjQyNDAwMDAwMDJdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZTFjZmRkMjU4NzZiNDQ1YjlhNDE2MzExYmYwZjYyNWMgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTE0MDcwOGU2YzdiNDY5ZWJjZGJhMTUxNDQ1NDlhN2QgPSAkKCc8ZGl2IGlkPSJodG1sXzkxNDA3MDhlNmM3YjQ2OWViY2RiYTE1MTQ0NTQ5YTdkIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5XZXN0bW91bnQgQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9lMWNmZGQyNTg3NmI0NDViOWE0MTYzMTFiZjBmNjI1Yy5zZXRDb250ZW50KGh0bWxfOTE0MDcwOGU2YzdiNDY5ZWJjZGJhMTUxNDQ1NDlhN2QpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfODBiM2RmYzRlMDg3NGM0Yjk2YWNhZDRiZDcwNTI5MWYuYmluZFBvcHVwKHBvcHVwX2UxY2ZkZDI1ODc2YjQ0NWI5YTQxNjMxMWJmMGY2MjVjKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyX2IyNWM4YjM3MzUwOTQ0ZjI4NjA0ZDdiZTQyZjY0NTczID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNjg4OTA1NCwtNzkuNTU0NzI0NDAwMDAwMDFdLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfZDhiZDVlODA4NDVlNDAyZTlkMGUxOTg4NDE0ZDYwYTcgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfOTM0ZTUzYmNjZjMyNGM2MTg0M2JkMTY2NGIwMjBiY2MgPSAkKCc8ZGl2IGlkPSJodG1sXzkzNGU1M2JjY2YzMjRjNjE4NDNiZDE2NjRiMDIwYmNjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5LaW5nc3ZpZXcgVmlsbGFnZSxNYXJ0aW4gR3JvdmUgR2FyZGVucyxSaWNodmlldyBHYXJkZW5zLFN0LiBQaGlsbGlwcyBDbHVzdGVyIDA8L2Rpdj4nKVswXTsKICAgICAgICAgICAgICAgIHBvcHVwX2Q4YmQ1ZTgwODQ1ZTQwMmU5ZDBlMTk4ODQxNGQ2MGE3LnNldENvbnRlbnQoaHRtbF85MzRlNTNiY2NmMzI0YzYxODQzYmQxNjY0YjAyMGJjYyk7CiAgICAgICAgICAgIAoKICAgICAgICAgICAgY2lyY2xlX21hcmtlcl9iMjVjOGIzNzM1MDk0NGYyODYwNGQ3YmU0MmY2NDU3My5iaW5kUG9wdXAocG9wdXBfZDhiZDVlODA4NDVlNDAyZTlkMGUxOTg4NDE0ZDYwYTcpOwoKICAgICAgICAgICAgCiAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIGNpcmNsZV9tYXJrZXJfNWRhYmM1MDZhMmQ5NDZkMzhhNmI5YmM4M2ZlNGZjYzEgPSBMLmNpcmNsZU1hcmtlcigKICAgICAgICAgICAgICAgIFs0My43Mzk0MTYzOTk5OTk5OTYsLTc5LjU4ODQzNjldLAogICAgICAgICAgICAgICAgewogICJidWJibGluZ01vdXNlRXZlbnRzIjogdHJ1ZSwKICAiY29sb3IiOiAiI2ZmMDAwMCIsCiAgImRhc2hBcnJheSI6IG51bGwsCiAgImRhc2hPZmZzZXQiOiBudWxsLAogICJmaWxsIjogdHJ1ZSwKICAiZmlsbENvbG9yIjogIiNmZjAwMDAiLAogICJmaWxsT3BhY2l0eSI6IDAuNywKICAiZmlsbFJ1bGUiOiAiZXZlbm9kZCIsCiAgImxpbmVDYXAiOiAicm91bmQiLAogICJsaW5lSm9pbiI6ICJyb3VuZCIsCiAgIm9wYWNpdHkiOiAxLjAsCiAgInJhZGl1cyI6IDUsCiAgInN0cm9rZSI6IHRydWUsCiAgIndlaWdodCI6IDMKfQogICAgICAgICAgICAgICAgKS5hZGRUbyhtYXBfOTVmNzYwNzU0ZWJhNDYyOWEyZmRlN2E2NzhmZjQ4MTcpOwogICAgICAgICAgICAKICAgIAogICAgICAgICAgICB2YXIgcG9wdXBfYWE3ZTY0YTY0MDQxNGVlOWIwN2YzMzJkYjcyZTk1MWEgPSBMLnBvcHVwKHttYXhXaWR0aDogJzMwMCd9KTsKCiAgICAgICAgICAgIAogICAgICAgICAgICAgICAgdmFyIGh0bWxfNTBjNjg0ZjM1MDgyNDViYTk3MWE0ZTZjOTczZmMxN2MgPSAkKCc8ZGl2IGlkPSJodG1sXzUwYzY4NGYzNTA4MjQ1YmE5NzFhNGU2Yzk3M2ZjMTdjIiBzdHlsZT0id2lkdGg6IDEwMC4wJTsgaGVpZ2h0OiAxMDAuMCU7Ij5BbGJpb24gR2FyZGVucyxCZWF1bW9uZCBIZWlnaHRzLEh1bWJlcmdhdGUsSmFtZXN0b3duLE1vdW50IE9saXZlLFNpbHZlcnN0b25lLFNvdXRoIFN0ZWVsZXMsVGhpc3RsZXRvd24gQ2x1c3RlciAwPC9kaXY+JylbMF07CiAgICAgICAgICAgICAgICBwb3B1cF9hYTdlNjRhNjQwNDE0ZWU5YjA3ZjMzMmRiNzJlOTUxYS5zZXRDb250ZW50KGh0bWxfNTBjNjg0ZjM1MDgyNDViYTk3MWE0ZTZjOTczZmMxN2MpOwogICAgICAgICAgICAKCiAgICAgICAgICAgIGNpcmNsZV9tYXJrZXJfNWRhYmM1MDZhMmQ5NDZkMzhhNmI5YmM4M2ZlNGZjYzEuYmluZFBvcHVwKHBvcHVwX2FhN2U2NGE2NDA0MTRlZTliMDdmMzMyZGI3MmU5NTFhKTsKCiAgICAgICAgICAgIAogICAgICAgIAogICAgCiAgICAgICAgICAgIHZhciBjaXJjbGVfbWFya2VyXzBjNzY4ODdjMzg3MTQ0OTFiNzZhY2UyOWFkNTdlZDMxID0gTC5jaXJjbGVNYXJrZXIoCiAgICAgICAgICAgICAgICBbNDMuNzA2NzQ4Mjk5OTk5OTk0LC03OS41OTQwNTQ0XSwKICAgICAgICAgICAgICAgIHsKICAiYnViYmxpbmdNb3VzZUV2ZW50cyI6IHRydWUsCiAgImNvbG9yIjogIiM4MDAwZmYiLAogICJkYXNoQXJyYXkiOiBudWxsLAogICJkYXNoT2Zmc2V0IjogbnVsbCwKICAiZmlsbCI6IHRydWUsCiAgImZpbGxDb2xvciI6ICIjODAwMGZmIiwKICAiZmlsbE9wYWNpdHkiOiAwLjcsCiAgImZpbGxSdWxlIjogImV2ZW5vZGQiLAogICJsaW5lQ2FwIjogInJvdW5kIiwKICAibGluZUpvaW4iOiAicm91bmQiLAogICJvcGFjaXR5IjogMS4wLAogICJyYWRpdXMiOiA1LAogICJzdHJva2UiOiB0cnVlLAogICJ3ZWlnaHQiOiAzCn0KICAgICAgICAgICAgICAgICkuYWRkVG8obWFwXzk1Zjc2MDc1NGViYTQ2MjlhMmZkZTdhNjc4ZmY0ODE3KTsKICAgICAgICAgICAgCiAgICAKICAgICAgICAgICAgdmFyIHBvcHVwXzZiNzc3YTlhMmRlNTQxMTE4MWQ1ZWZjOTFmMDk0MzNmID0gTC5wb3B1cCh7bWF4V2lkdGg6ICczMDAnfSk7CgogICAgICAgICAgICAKICAgICAgICAgICAgICAgIHZhciBodG1sX2VlYzcwMmFmODRjZjRlY2M5OWEwZGRlYmE1MDZmODE5ID0gJCgnPGRpdiBpZD0iaHRtbF9lZWM3MDJhZjg0Y2Y0ZWNjOTlhMGRkZWJhNTA2ZjgxOSIgc3R5bGU9IndpZHRoOiAxMDAuMCU7IGhlaWdodDogMTAwLjAlOyI+Tm9ydGh3ZXN0IENsdXN0ZXIgMTwvZGl2PicpWzBdOwogICAgICAgICAgICAgICAgcG9wdXBfNmI3NzdhOWEyZGU1NDExMTgxZDVlZmM5MWYwOTQzM2Yuc2V0Q29udGVudChodG1sX2VlYzcwMmFmODRjZjRlY2M5OWEwZGRlYmE1MDZmODE5KTsKICAgICAgICAgICAgCgogICAgICAgICAgICBjaXJjbGVfbWFya2VyXzBjNzY4ODdjMzg3MTQ0OTFiNzZhY2UyOWFkNTdlZDMxLmJpbmRQb3B1cChwb3B1cF82Yjc3N2E5YTJkZTU0MTExODFkNWVmYzkxZjA5NDMzZik7CgogICAgICAgICAgICAKICAgICAgICAKPC9zY3JpcHQ+" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>



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
      <td>3</td>
      <td>Scarborough</td>
      <td>0.0</td>
      <td>Coffee Shop</td>
      <td>Korean Restaurant</td>
      <td>Women's Store</td>
      <td>Diner</td>
      <td>Fast Food Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>21</td>
      <td>NorthYork</td>
      <td>0.0</td>
      <td>Pizza Place</td>
      <td>Discount Store</td>
      <td>Coffee Shop</td>
      <td>Butcher</td>
      <td>Pharmacy</td>
      <td>Grocery Store</td>
      <td>Greek Restaurant</td>
      <td>Gourmet Shop</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>31</td>
      <td>NorthYork</td>
      <td>0.0</td>
      <td>Intersection</td>
      <td>Pizza Place</td>
      <td>Coffee Shop</td>
      <td>French Restaurant</td>
      <td>Portuguese Restaurant</td>
      <td>Hockey Arena</td>
      <td>Dumpling Restaurant</td>
      <td>Diner</td>
      <td>Discount Store</td>
      <td>Dog Run</td>
    </tr>
    <tr>
      <td>37</td>
      <td>EastYork</td>
      <td>0.0</td>
      <td>Coffee Shop</td>
      <td>Park</td>
      <td>Convenience Store</td>
      <td>Women's Store</td>
      <td>Dim Sum Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>78</td>
      <td>York</td>
      <td>0.0</td>
      <td>Pizza Place</td>
      <td>Grocery Store</td>
      <td>Convenience Store</td>
      <td>Bus Line</td>
      <td>Dim Sum Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>91</td>
      <td>Etobicoke</td>
      <td>0.0</td>
      <td>Pharmacy</td>
      <td>Pet Store</td>
      <td>Pizza Place</td>
      <td>Liquor Store</td>
      <td>Coffee Shop</td>
      <td>Convenience Store</td>
      <td>Café</td>
      <td>Beer Store</td>
      <td>Shopping Plaza</td>
      <td>Drugstore</td>
    </tr>
    <tr>
      <td>95</td>
      <td>Etobicoke</td>
      <td>0.0</td>
      <td>Pizza Place</td>
      <td>Middle Eastern Restaurant</td>
      <td>Sandwich Place</td>
      <td>Coffee Shop</td>
      <td>Intersection</td>
      <td>Chinese Restaurant</td>
      <td>Drugstore</td>
      <td>Diner</td>
      <td>Discount Store</td>
      <td>Dog Run</td>
    </tr>
    <tr>
      <td>96</td>
      <td>Etobicoke</td>
      <td>0.0</td>
      <td>Pizza Place</td>
      <td>Park</td>
      <td>Mobile Phone Shop</td>
      <td>Bus Line</td>
      <td>Dim Sum Restaurant</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
      <td>Eastern European Restaurant</td>
    </tr>
    <tr>
      <td>97</td>
      <td>Etobicoke</td>
      <td>0.0</td>
      <td>Grocery Store</td>
      <td>Pizza Place</td>
      <td>Fried Chicken Joint</td>
      <td>Sandwich Place</td>
      <td>Fast Food Restaurant</td>
      <td>Beer Store</td>
      <td>Pharmacy</td>
      <td>Gluten-free Restaurant</td>
      <td>Deli / Bodega</td>
      <td>Electronics Store</td>
    </tr>
  </tbody>
</table>
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
      <td>1</td>
      <td>Scarborough</td>
      <td>1.0</td>
      <td>Moving Target</td>
      <td>History Museum</td>
      <td>Bar</td>
      <td>Women's Store</td>
      <td>Fast Food Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Scarborough</td>
      <td>1.0</td>
      <td>Intersection</td>
      <td>Pizza Place</td>
      <td>Breakfast Spot</td>
      <td>Medical Center</td>
      <td>Electronics Store</td>
      <td>Mexican Restaurant</td>
      <td>Rental Car Location</td>
      <td>Women's Store</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Scarborough</td>
      <td>1.0</td>
      <td>Hakka Restaurant</td>
      <td>Bakery</td>
      <td>Athletics &amp; Sports</td>
      <td>Thai Restaurant</td>
      <td>Caribbean Restaurant</td>
      <td>Bank</td>
      <td>Fried Chicken Joint</td>
      <td>Discount Store</td>
      <td>Drugstore</td>
      <td>Dumpling Restaurant</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Scarborough</td>
      <td>1.0</td>
      <td>Discount Store</td>
      <td>Coffee Shop</td>
      <td>Bus Station</td>
      <td>Department Store</td>
      <td>Women's Store</td>
      <td>Diner</td>
      <td>Fast Food Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Scarborough</td>
      <td>1.0</td>
      <td>Bakery</td>
      <td>Bus Line</td>
      <td>Fast Food Restaurant</td>
      <td>Metro Station</td>
      <td>Bus Station</td>
      <td>Intersection</td>
      <td>Soccer Field</td>
      <td>Park</td>
      <td>Ethiopian Restaurant</td>
      <td>Event Space</td>
    </tr>
    <tr>
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
      <td>86</td>
      <td>Etobicoke</td>
      <td>1.0</td>
      <td>Pizza Place</td>
      <td>Pharmacy</td>
      <td>Athletics &amp; Sports</td>
      <td>Dance Studio</td>
      <td>Coffee Shop</td>
      <td>Pool</td>
      <td>Pub</td>
      <td>Sandwich Place</td>
      <td>Skating Rink</td>
      <td>Gym</td>
    </tr>
    <tr>
      <td>89</td>
      <td>Etobicoke</td>
      <td>1.0</td>
      <td>Hardware Store</td>
      <td>Tanning Salon</td>
      <td>Wings Joint</td>
      <td>Grocery Store</td>
      <td>Fast Food Restaurant</td>
      <td>Discount Store</td>
      <td>Convenience Store</td>
      <td>Sandwich Place</td>
      <td>Burrito Place</td>
      <td>Burger Joint</td>
    </tr>
    <tr>
      <td>90</td>
      <td>Etobicoke</td>
      <td>1.0</td>
      <td>Print Shop</td>
      <td>Women's Store</td>
      <td>Dessert Shop</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
      <td>Eastern European Restaurant</td>
      <td>Dumpling Restaurant</td>
    </tr>
    <tr>
      <td>93</td>
      <td>NorthYork</td>
      <td>1.0</td>
      <td>Paper / Office Supplies Store</td>
      <td>Baseball Field</td>
      <td>Women's Store</td>
      <td>Diner</td>
      <td>Fast Food Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>98</td>
      <td>Etobicoke</td>
      <td>1.0</td>
      <td>Drugstore</td>
      <td>Rental Car Location</td>
      <td>Women's Store</td>
      <td>Dessert Shop</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
      <td>Eastern European Restaurant</td>
    </tr>
  </tbody>
</table>
<p>77 rows × 12 columns</p>
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
      <td>0</td>
      <td>Scarborough</td>
      <td>2.0</td>
      <td>Fast Food Restaurant</td>
      <td>Women's Store</td>
      <td>Dim Sum Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
      <td>Eastern European Restaurant</td>
      <td>Dumpling Restaurant</td>
    </tr>
    <tr>
      <td>20</td>
      <td>NorthYork</td>
      <td>2.0</td>
      <td>Park</td>
      <td>Convenience Store</td>
      <td>Bank</td>
      <td>Women's Store</td>
      <td>Diner</td>
      <td>Fast Food Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
    </tr>
    <tr>
      <td>22</td>
      <td>NorthYork</td>
      <td>2.0</td>
      <td>Park</td>
      <td>Food &amp; Drink Shop</td>
      <td>Women's Store</td>
      <td>Dim Sum Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
      <td>Eastern European Restaurant</td>
    </tr>
    <tr>
      <td>27</td>
      <td>NorthYork</td>
      <td>2.0</td>
      <td>Snack Place</td>
      <td>Airport</td>
      <td>Park</td>
      <td>Women's Store</td>
      <td>Dim Sum Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>41</td>
      <td>CentralToronto</td>
      <td>2.0</td>
      <td>Park</td>
      <td>Swim School</td>
      <td>Bus Line</td>
      <td>Women's Store</td>
      <td>Diner</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>47</td>
      <td>DowntownToronto</td>
      <td>2.0</td>
      <td>Park</td>
      <td>Building</td>
      <td>Playground</td>
      <td>Trail</td>
      <td>Women's Store</td>
      <td>Diner</td>
      <td>Discount Store</td>
      <td>Dog Run</td>
      <td>Drugstore</td>
      <td>Dumpling Restaurant</td>
    </tr>
    <tr>
      <td>71</td>
      <td>York</td>
      <td>2.0</td>
      <td>Park</td>
      <td>Women's Store</td>
      <td>Fast Food Restaurant</td>
      <td>Market</td>
      <td>Diner</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>87</td>
      <td>Etobicoke</td>
      <td>2.0</td>
      <td>Park</td>
      <td>Pool</td>
      <td>River</td>
      <td>Women's Store</td>
      <td>Dessert Shop</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
      <td>Eastern European Restaurant</td>
    </tr>
    <tr>
      <td>88</td>
      <td>Etobicoke</td>
      <td>2.0</td>
      <td>Park</td>
      <td>Baseball Field</td>
      <td>Women's Store</td>
      <td>Diner</td>
      <td>Fast Food Restaurant</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
    </tr>
    <tr>
      <td>94</td>
      <td>York</td>
      <td>2.0</td>
      <td>Park</td>
      <td>Women's Store</td>
      <td>Dessert Shop</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
      <td>Eastern European Restaurant</td>
      <td>Dumpling Restaurant</td>
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
      <td>5</td>
      <td>Scarborough</td>
      <td>3.0</td>
      <td>Playground</td>
      <td>Dessert Shop</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
      <td>Eastern European Restaurant</td>
      <td>Dumpling Restaurant</td>
      <td>Drugstore</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Scarborough</td>
      <td>3.0</td>
      <td>Playground</td>
      <td>Park</td>
      <td>Women's Store</td>
      <td>Dessert Shop</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
      <td>Eastern European Restaurant</td>
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
      <td>92</td>
      <td>NorthYork</td>
      <td>4.0</td>
      <td>Pizza Place</td>
      <td>Dessert Shop</td>
      <td>Farmers Market</td>
      <td>Falafel Restaurant</td>
      <td>Event Space</td>
      <td>Ethiopian Restaurant</td>
      <td>Electronics Store</td>
      <td>Eastern European Restaurant</td>
      <td>Dumpling Restaurant</td>
      <td>Drugstore</td>
    </tr>
  </tbody>
</table>
</div>



This concludes the clustering and segmentation!


```python

```
