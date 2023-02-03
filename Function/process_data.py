import numpy as np

def clean_data(raw_data):
    raw_data.drop_duplicates(inplace = True)
    raw_data.drop_duplicates('id', inplace = True)
    raw_data.drop_duplicates('host id', inplace = True)
    # convert neighbourhood uniform
    raw_data['neighbourhood group'] = raw_data['neighbourhood group'].str.replace('brookln', 'Brooklyn', regex = True)
    raw_data['neighbourhood group'] = raw_data['neighbourhood group'].str.replace('manhatan', 'Manhattan', regex = True)


    # drop all symbol in fee table
    raw_data['price'] = raw_data['price'].str.replace('$', '', regex = True)
    raw_data['price'] = raw_data['price'].str.replace(',', '', regex = True)
    raw_data['price'] = raw_data['price'].str.replace('US', '', regex = True)
    raw_data['price'] = raw_data['price'].astype(float)
    raw_data['service fee'] = raw_data['service fee'].str.replace('$', '', regex = True)
    raw_data['service fee'] = raw_data['service fee'].str.replace(',', '', regex = True)
    raw_data['service fee'] = raw_data['service fee'].str.replace('US', '', regex = True)
    raw_data['service fee'] = raw_data['service fee'].astype(float)
    raw_data['room type'] = raw_data['room type'].str.replace('room', '', regex = True)


    # set all 'availability 365' < 0 columns produce -1 to make it positive
    raw_data['availability 365'] = np.where(raw_data['availability 365'] < 0, raw_data['availability 365'] * (-1), raw_data['availability 365'])
    # set all 'availability 365' > 365 0 columns equal to 365
    raw_data['availability 365'] = np.where(raw_data['availability 365'] > 365, 365, raw_data['availability 365'])
    
    # set all 'minimum nights' < 0 columns produce -1 to make it positive
    raw_data['minimum nights'] = np.where(raw_data['minimum nights'] < 0, raw_data['minimum nights'] * (-1), raw_data['minimum nights'])
    return raw_data