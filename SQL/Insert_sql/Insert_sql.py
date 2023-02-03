import sqlite3
from sqlite3 import Error
import numpy as np
sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))


# insert data
def insert_sql(dbConnection):
    while True:
        table_name = input('Which table?\nOr input 2 to exit this module.\n')
        if table_name == 'House_info':
            try:
                Name = input('Name:\n')
                Room_type = input('Room type:\n')
                year = input('Construction year:\n')
                data = (Name, Room_type, year)
                sql = 'INSERT INTO ' + table_name + ' (Name, Room_type, Construction_year)' + ' VALUES(?,?,?)'
                cur = dbConnection.cursor()
                cur.execute(sql, data)
                dbConnection.commit()
                print('Insert successfully.')
            except Error as e:
                print(e)
        elif table_name == 'Host_Info':
            try:
                Host_identity_verified = input('Host identity verified:\n')
                Host_name = input('Host name:\n')
                Calculated_host_listing_count = input('Calculated host listing count:\n')
                License = input('License:\n')
                data = (Host_identity_verified, Host_name, Calculated_host_listing_count, License)
                sql = 'INSERT INTO ' + table_name + ' (Host_id, Host_identity_verified, Host_name, Calculated_host_listings_count, License)' + ' VALUES(?,?,?,?)'
                cur = dbConnection.cursor()
                cur.execute(sql, data)
                dbConnection.commit()
                print('Insert successfully.')
            except Error as e:
                print(e)
        elif table_name == 'Host_Location':
            try:
                Neighbourhood_group = input('Neighbourhoo group:\n')
                Neighbourhood = input('Neighbourhood:\n')
                Latitued = input('Latitued:\n')
                Longitude = input('Longitude:\n')
                Country = input('Country:\n')
                Country_code = input('Country code:\n')
                data = (Neighbourhood_group, Neighbourhood, Latitued, Longitude, Country, Country_code)
                sql = 'INSERT INTO ' + table_name + ' (Neighbourhood_group, Neighbourhood, Latitued, Longitude, Country, Country_code)' + ' VALUES(?,?,?,?,?,?)'
                cur = dbConnection.cursor()
                cur.execute(sql, data)
                dbConnection.commit()
                print('Insert successfully.')
            except Error as e:
                print(e)
        elif table_name == 'Platform':
            try:
                Instant_bookable = input('Instant bookable:\n')
                Cancellation_poicy = input('Cancellation poicy:\n')
                Minimum_nights = input('Minimum nights:\n')
                Availabilitty_365 = input('Availabilitty 365:\n')
                House_rules = input('House rules:\n')
                data = (Instant_bookable, Cancellation_poicy, Minimum_nights, Availabilitty_365, House_rules)
                sql = 'INSERT INTO ' + table_name + ' (Instant_bookable, Cancellation_poicy, Minimum_nights, Availabilitty_365, House_rules)' + ' VALUES(?,?,?,?,?)'
                cur = dbConnection.cursor()
                cur.execute(sql, data)
                dbConnection.commit()
                print('Insert successfully.')
            except Error as e:
                print(e)
        elif table_name == 'Fee':
            try:
                Price = input('Price:\n')
                Service_fee = input('Service fee:\n')
                data = (Price, Service_fee)
                sql = 'INSERT INTO ' + table_name + ' (Price, Service_fee)' + ' VALUES(?,?)'
                cur = dbConnection.cursor()
                cur.execute(sql, data)
                dbConnection.commit()
                print('Insert successfully.')
            except Error as e:
                print(e)
        elif table_name == 'User':
            try:
                Number_of_reviews = input('Number of reviews:\n')
                Last_review = input('Last review:\n')
                Review_per_month = input('Review per month:\n')
                Review_rate_number = input('Review rate number:\n')
                data = (Number_of_reviews, Last_review, Review_per_month, Review_rate_number)
                sql = 'INSERT INTO ' + table_name + ' (Number_of_reviews, Last_review, Review_per_month, Review_rate_number)' + ' VALUES(?,?,?,?)'
                cur = dbConnection.cursor()
                cur.execute(sql, data)
                dbConnection.commit()
                print('Insert successfully.')
            except Error as e:
                print(e)
        elif table_name == 'Connect':
            try:
                data = input('Host_id:\n')
                sql = 'INSERT INTO ' + table_name + ' (Host_id)' + ' VALUES(?)'
                cur = dbConnection.cursor()
                cur.execute(sql, data)
                dbConnection.commit()
                print('Insert successfully.')
            except Error as e:
                print(e)
        elif table_name == '2' or table_name == 'Exit' or table_name == 'exit' or table_name == 'EXIT':
            break
        else:
            print('Please input right operation.')
            continue