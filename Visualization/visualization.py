import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import folium
import webbrowser
import time
import os
import sys


path = os.getcwd()

def map_visualization(House_Location):
    lat_avg = House_Location['lat'].mean()            # calculate average of latitude
    long_avg = House_Location['long'].mean()          # calculate average of longitude
    area_lat = House_Location['lat'].groupby(House_Location['neighbourhood group']).mean()              # group by 'neighbourhood group' and calculate average of latitude
    area_long = House_Location['long'].groupby(House_Location['neighbourhood group']).mean()            # group by 'neighbourhood group' and calculate average of longitude
    area_lat_long = pd.concat([area_lat, area_long], axis = 1)
    area_lat_long = area_lat_long.values.tolist()           

    map = folium.Map(location = [lat_avg, long_avg], zoom_start = 12)

    for location_point in range(0, len(area_lat_long)):
        folium.Marker(area_lat_long[location_point], popup = area_lat_long[location_point]).add_to(map)
    
    map.save('map.html')       # save as local html
    filename = os.getcwd() + '/' + 'map.html'

    # check system type: OS/WINDOWS/LINUX
    if sys.platform == 'win32':  
        webbrowser.open(filename)     # open local map html in chrome
    elif sys.platform == 'darwin':
        webbrowser.get('open -a /Applications/Google\ Chrome.app %s').open(filename)
        
    time.sleep(3)


def review(map_visual_data):
    plt.figure(figsize = (8, 6))
    plt.xlabel('Neighbourhood_group')
    sns.barplot(x = map_visual_data['Neighbourhood_group'].value_counts(), 
                y = map_visual_data['Neighbourhood_group'].value_counts().index, palette = "GnBu")
    plt.savefig(path + '/' + 'Data' + '/images/' + 'Neighbourhood_group.png')
    plt.close()


def availability_365(Platform):
    plt.figure(figsize = (8, 6))
    sns.histplot(data = Platform, x = 'availability 365', kde = True)
    plt.savefig(path + '/' + 'Data' + '/images/' + 'availability_365.png')
    plt.close()


def cancellation_policy(Platform):
    plt.figure(figsize = (8, 6))
    sns.countplot(data = Platform, x = 'cancellation_policy', color = '#FEBE8C')
    plt.savefig(path + '/' + 'Data' + '/images/' + 'cancellation_policy.png')
    plt.close()
