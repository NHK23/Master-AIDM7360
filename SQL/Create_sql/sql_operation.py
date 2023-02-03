import sqlite3
from sqlite3 import Error
import numpy as np
sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))

# create data into table
# create House information data
def create_House_info_data(dbConnection, House_info):
    try:
        for i in House_info.index:
            id = House_info.loc[i].values[0]
            name = House_info.loc[i].values[1]
            room_type = House_info.loc[i].values[2]
            construction_year = House_info.loc[i].values[3]
            sql = ''' INSERT INTO House_info(ID, NAME, Room_type, Construction_year)
                        VALUES(?,?,?,?) '''
            cur = dbConnection.cursor()

            cur.execute(sql, (id, name, room_type, construction_year))
            dbConnection.commit()
        print('House info done')
    except Error as e:
        print(e)


# create Host information data
def create_Host_info_data(dbConnection, Host_info):
    try:
        for i in Host_info.index:
            host_id = Host_info.loc[i].values[0]
            Host_identity_verified = Host_info.loc[i].values[1]
            Host_name = Host_info.loc[i].values[2]
            Calculated_host_listings_count = Host_info.loc[i].values[3]
            License = Host_info.loc[i].values[4]
            sql = ''' INSERT INTO Host_info(Host_id, Host_identity_verified, Host_name, Calculated_host_listings_count, License)
                        VALUES(?,?,?,?,?) '''
            cur = dbConnection.cursor()

            cur.execute(sql, (host_id, Host_identity_verified, Host_name, Calculated_host_listings_count, License))
            dbConnection.commit()
        print('Host info done')
    except Error as e:
        print(e)


# create Host Location data
def create_Host_Location_data(dbConnection, Host_Location):
    try:
        for i in Host_Location.index:
            id = Host_Location.loc[i].values[0]
            neighbourhood_group = Host_Location.loc[i].values[1]
            neighbourhood = Host_Location.loc[i].values[2]
            lat = Host_Location.loc[i].values[3]
            long = Host_Location.loc[i].values[4]
            country = Host_Location.loc[i].values[5]
            country_code = Host_Location.loc[i].values[6]
            sql = ''' INSERT INTO Host_Location(ID, Neighbourhood_group, Neighbourhood, Latitude, Longitude, Country, Country_code)
                        VALUES(?,?,?,?,?,?,?) '''
            cur = dbConnection.cursor()

            cur.execute(sql, (id, neighbourhood_group, neighbourhood, lat, long, country, country_code))
            dbConnection.commit()
        print('Host Location done')
    except Error as e:
        print(e)


# create Platform data
def create_Platform_data(dbConnection, Platform):
    try:
        for i in Platform.index:
            id = Platform.loc[i].values[0]
            instant_bookable = Platform.loc[i].values[1]
            cancellation_policy = Platform.loc[i].values[2]
            minimum_nights = Platform.loc[i].values[3]
            availabilitty_365 = Platform.loc[i].values[4]
            house_rules = Platform.loc[i].values[5]
            sql = ''' INSERT INTO Platform(ID, Instant_bookable, Cancellation_policy, Minimum_nights, Availabilitty_365, House_rules)
                        VALUES(?,?,?,?,?,?) '''
            cur = dbConnection.cursor()

            cur.execute(sql, (id, instant_bookable, cancellation_policy, minimum_nights, availabilitty_365, house_rules))
            dbConnection.commit()
        print('Platform done')
    except Error as e:
        print(e)


# create Fee data
def create_Fee_data(dbConnection, Price):
    try:
        for i in Price.index:
            id = Price.loc[i].values[0]
            price = Price.loc[i].values[1]
            service_fee = Price.loc[i].values[2]
            sql = ''' INSERT INTO Fee(ID, Price, Service_fee)
                        VALUES(?,?,?) '''
            cur = dbConnection.cursor()

            cur.execute(sql, (id, price, service_fee))
            dbConnection.commit()
        print('Fee done')
    except Error as e:
        print(e)


# create User data
def create_User_data(dbConnection, User):
    try:
        for i in User.index:
            id = User.loc[i].values[0]
            number_reviews = User.loc[i].values[1]
            last_review = User.loc[i].values[2]
            review_per_month = User.loc[i].values[3]
            review_rate_number = User.loc[i].values[4]
            sql = ''' INSERT INTO User(ID, Number_of_reviews, Last_review, Review_per_month, Review_rate_number)
                        VALUES(?,?,?,?,?) '''
            cur = dbConnection.cursor()

            cur.execute(sql, (id, number_reviews, last_review, review_per_month, review_rate_number))
            dbConnection.commit()
        print('User done')
    except Error as e:
        print(e)


# create Connect data
def create_Connect_data(dbConnection, Connect):
    try:
        for i in Connect.index:
            id = Connect.loc[i].values[0]
            host_id = Connect.loc[i].values[1]
            sql = ''' INSERT INTO Connect(ID, Host_id)
                        VALUES(?,?) '''
            cur = dbConnection.cursor()

            cur.execute(sql, (id, host_id))
            dbConnection.commit()
        print('Connect done')
    except Error as e:
        print(e)


# create Template data
def create_Template_data(dbConnection, Template):
    try:
        for i in Template.index:
            Template0 = Template.loc[i].values[0]
            Template1 = Template.loc[i].values[1]
            Template2 = Template.loc[i].values[2]
            Template3 = Template.loc[i].values[3]
            Template4 = Template.loc[i].values[4]
            Template5 = Template.loc[i].values[5]
            Template6 = Template.loc[i].values[6]
            Template7 = Template.loc[i].values[7]
            Template8 = Template.loc[i].values[8]
            Template9 = Template.loc[i].values[9]
            sql = ''' INSERT INTO Template(position, Template1, Template2, Template3, Template4, Template5, Template6, Template7, Template8, Template9)
                        VALUES(?,?,?,?,?,?,?,?,?,?) '''
            cur = dbConnection.cursor()

            cur.execute(sql, (Template0, Template1, Template2, Template3, Template4, 
            Template5, Template6, Template7, Template8, Template9))
            dbConnection.commit()
        print('Template done')
    except Error as e:
        print(e)


# create Queries data
def create_Queries_data(dbConnection, Queries):
    index = 0
    try:
        for i in Queries:
            cur = dbConnection.cursor()
            sql = '''INSERT INTO Queries(position, Query)
                                        VALUES(?,?) '''
            cur.execute(sql, (index, i))
            dbConnection.commit()
            index += 1
        print('Queries done')
    except Error as e:
        print(e)