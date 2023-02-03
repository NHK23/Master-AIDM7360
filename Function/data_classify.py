import pandas as pd


def divide_data(raw_data):
    House_info = pd.DataFrame(raw_data, columns = ['id', 'NAME', 'room type', 'Construction year'])
    Host_info = pd.DataFrame(raw_data, columns = ['host id', 'host_identity_verified', 'host name', 'calculated host listings count', 'license'])
    House_Location = pd.DataFrame(raw_data, columns = ['id', 'neighbourhood group', 'neighbourhood', 'lat', 'long', 'country', 'country code'])
    Platform = pd.DataFrame(raw_data, columns = ['id', 'instant_bookable', 'cancellation_policy', 'minimum nights', 'availability 365', 'house_rules'])
    Price = pd.DataFrame(raw_data, columns = ['id', 'price', 'service fee'])
    User = pd.DataFrame(raw_data, columns = ['id', 'number of reviews', 'last review', 'reviews per month', 'review rate number'])
    Connect = pd.DataFrame(raw_data, columns = ['id', 'host id'])
    
    return House_info, Host_info, House_Location, Platform, Price, User, Connect