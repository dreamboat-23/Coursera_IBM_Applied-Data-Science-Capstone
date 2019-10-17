#!/usr/bin/env python
# coding: utf-8

# # Data Wrangling
# The data was downloaded onto an excel table. I imported the excel table to IBM Watson and I downloaded the required libraries to start cleaning up the data.

# In[53]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[63]:



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


# Let us examine the missing data

# In[6]:


missing_data = df.isnull()
missing_data.head(3)


# In[7]:


for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")


# As we can see, there are 77 true values, indicating missing data, and per prompt requirement, these will be dropped from the Borough column

# In[8]:


df.dropna(subset=["Borough"], axis=0, inplace=True)

#reset the index

df.reset_index(drop=True, inplace=True)

df.head(12)


# We then assign missing neighborhoods to name of corresponding borough

# In[9]:


df['Neighbourhood'].replace(np.nan, df['Borough'], inplace=True)
df.head(12)


# Then concatenate by Postcode

# In[10]:


df_1= df.groupby('Postcode').agg(lambda x: ','.join(x))


# In[11]:


df_2=df_1.reset_index()


# Within each Borough, there are multiple Postcodes and so we clean up the data frame to remove any repeats, so that each line has only one Postcode, one Borough, and all the Neighborhoods in that Borough and Postcode.

# In[12]:


df_2['Borough']= df_2['Borough'].str.replace('[{}\s]','').str.split(',').apply(set).str.join(',').str.strip(',').str.replace(",{2,}",",")


# In[14]:


df_2.head(12)


# In[13]:


df_2.shape


# The data frame has 3 rows and 103 columns

# # Geocoding
# Using the CSV data to merge it to the cleaned table from the previous section. First examine what the data frame looks like

# In[14]:


filepath = "https://cocl.us/Geospatial_data"
df_3 = pd.read_csv('https://cocl.us/Geospatial_data')
df_3.head()


# Rename the field "Postal Code" to Postcode to match the previous section, and merge the two data sets to get the required data frame.

# In[15]:


df_3.rename(columns={'Postal Code': 'Postcode'}, inplace=True)
df_4 = pd.merge(df_3, df_2, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)

df_4.head()


# Then we fix the column order to have Latitude and Longitude as the last two columns, then assign them to the data frame.

# In[16]:


column_order = ['Postcode',
 'Borough',
 'Neighbourhood',
 'Latitude',
 'Longitude']
df_5=df_4[column_order]
df_5.head()


# # Visualization and Clustering
# First we import some required libraries

# In[1]:


get_ipython().system('conda install -c conda-forge geopy --yes')
from geopy.geocoders import Nominatim
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors
from sklearn.cluster import KMeans
get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes')
import folium
print('Libraries imported.')


# Then we look for the coordinates of Toronto

# In[2]:


address = 'Toronto, Ontario'

geolocator = Nominatim(user_agent="TO_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Toronto, Ontario are {}, {}.'.format(latitude, longitude))


# Now we show the map of Toronto with the neighborhoods as markers

# In[64]:


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


# # Using Foursquare API to explore the neighborhoods

# In[52]:


# @hidden_cell
CLIENT_ID = 'XMCICN4YC1PQCMXSJEA2YVR5PRAC4N22MLOUV115WCWNA1HW' 
CLIENT_SECRET = '2VYYN4JX2SG1NTZUOGDOCKY1MRM12V40FV5KYFBMQUBLWRFY'
VERSION = '20180605'
radius=500
url = 'https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&ll={},{}&v={}&radius={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, radius)
results = requests.get(url).json()


# Define a function to get the category

# In[26]:


def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']


# Using the get_category_type function, we clean up the json and turn it into a pandas DF. Before we start we need to import certain libraries.

# In[27]:


import json
from pandas.io.json import json_normalize 


# In[28]:


venues = results['response']['groups'][0]['items']
   
nearby_venues = json_normalize(venues) # flatten JSON

filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
nearby_venues =nearby_venues.loc[:, filtered_columns]

nearby_venues['venue.categories'] = nearby_venues.apply(get_category_type, axis=1)

nearby_venues.columns = [col.split(".")[-1] for col in nearby_venues.columns]

nearby_venues.head()


# Now we explore the nearby venues!

# In[29]:


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


# In[31]:


toronto_venues = getNearbyVenues(names=df_5['Neighbourhood'],
                                   latitudes=df_5['Latitude'],
                                   longitudes=df_5['Longitude']
                                  )


# In[32]:


print(toronto_venues.shape)
toronto_venues.head()


# Then group the venues by "Neighborhood"

# In[33]:


toronto_venues.groupby('Neighborhood').count()


# We then check to see how many unique categories of venues there are in the Toronto

# In[34]:


print('There are {} uniques categories.'.format(len(toronto_venues['Venue Category'].unique())))


# We check to see which places are most visited by neighborhood

# In[36]:


toronto_onehot = pd.get_dummies(toronto_venues[['Venue Category']], prefix="", prefix_sep="")

toronto_onehot['Neighborhood'] = toronto_venues['Neighborhood'] 

fixed_columns = [toronto_onehot.columns[-1]] + list(toronto_onehot.columns[:-1])
toronto_onehot = toronto_onehot[fixed_columns]


# In[37]:


toronto_grouped = toronto_onehot.groupby('Neighborhood').mean().reset_index()
toronto_grouped


# We see the top 3 most visited venues in each neigborhood

# In[38]:


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


# Even better, we can see in a Pandas data frame the top ten common venues in each neighborhood

# In[39]:


def _most_common_venues(row, num_top_venues):
    row_categories = row.iloc[1:]
    row_categories_sorted = row_categories.sort_values(ascending=False)
    
    return row_categories_sorted.index.values[0:num_top_venues]


# In[40]:


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


# # Clustering

# In[41]:


kclusters = 5

toronto_grouped_clustering = toronto_grouped.drop('Neighborhood', 1)

kmeans = KMeans(n_clusters=kclusters, random_state=0).fit(toronto_grouped_clustering)

kmeans.labels_[0:98]


# In[42]:


#sorted_neighborhoods_venues.drop(['Cluster Labels'],axis=1,inplace=True)
sorted_neighborhoods_venues.insert(0, 'Cluster Labels', kmeans.labels_)
toronto_merged = df_5
# merge toronto_grouped with toronto_data to add latitude/longitude for each neighborhood
toronto_merged = toronto_merged.join(sorted_neighborhoods_venues.set_index('Neighborhood'), on='Neighbourhood')
toronto_merged.dropna(subset=["Cluster Labels"], axis=0, inplace=True)
toronto_merged.reset_index(drop=True, inplace=True)
toronto_merged['Cluster Labels'].astype(int)
toronto_merged.head()


# We visualize the clusters in a map

# In[65]:


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


# Now we examine the clusters to see the distinguishing venues

# In[44]:


toronto_merged.loc[toronto_merged['Cluster Labels'] == 0, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]


# In[45]:


toronto_merged.loc[toronto_merged['Cluster Labels'] == 1, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]


# In[46]:


toronto_merged.loc[toronto_merged['Cluster Labels'] == 2, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]


# In[47]:


toronto_merged.loc[toronto_merged['Cluster Labels'] == 3, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]


# In[48]:


toronto_merged.loc[toronto_merged['Cluster Labels'] == 4, toronto_merged.columns[[1] + list(range(5, toronto_merged.shape[1]))]]


# The segmentation and clustering is achieved
