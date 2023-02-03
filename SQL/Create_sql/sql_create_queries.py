# create Host List table
sql_create__House_info_table = """ CREATE TABLE IF NOT EXISTS House_info (
                                ID integer PRIMARY KEY,
                                Name TEXT,
                                Room_type TEXT,
                                Construction_year YEAR,
                                FOREIGN KEY (ID) REFERENCES Connect (ID)
                                ); """


# create Host information table
sql_create__Host_info_table = """ CREATE TABLE IF NOT EXISTS Host_Info (
                                Host_id integer PRIMARY KEY,
                                Host_identity_verified BOOLEAN,
                                Host_name TEXT,
                                Calculated_host_listings_count integer,
                                License TEXT,
                                FOREIGN KEY (Host_id) REFERENCES Connect (Host_id)
                                ); """


# create Host Location table
sql_create__House_Location_table = """ CREATE TABLE IF NOT EXISTS Host_Location (
                                ID integer PRIMARY KEY,
                                Neighbourhood_group TEXT,
                                Neighbourhood TEXT,
                                Latitude NUMERIC,
                                Longitude NUMERIC,
                                Country TEXT,
                                Country_code TEXT,
                                FOREIGN KEY (ID) REFERENCES Connect (ID)
                                ); """


# create Platform table
sql_create__Platform_table = """ CREATE TABLE IF NOT EXISTS Platform (
                                ID integer PRIMARY KEY,
                                Instant_bookable BOOLEAN,
                                Cancellation_policy TEXT,
                                Minimum_nights integer,
                                Availabilitty_365 FLOAT,
                                House_rules TEXT,
                                FOREIGN KEY (ID) REFERENCES Connect (ID)
                                ); """                     


#create Price table
sql_create__Fee_table = """ CREATE TABLE IF NOT EXISTS Fee (
                                ID integer PRIMARY KEY,
                                Price NUMERIC,
                                Service_fee NUMERIC,
                                FOREIGN KEY (ID) REFERENCES Connect (ID)
                                ); """      


# create User table
sql_create__User_table = """ CREATE TABLE IF NOT EXISTS User (
                                ID integer PRIMARY KEY,
                                Number_of_reviews integer,
                                Last_review DATE,
                                Review_per_month NUMERIC,
                                Review_rate_number integer,
                                FOREIGN KEY (ID) REFERENCES Connect (ID)
                                ); """ 


# create Connect table
sql_create__Connect_table = """ CREATE TABLE IF NOT EXISTS Connect (
                                ID integer PRIMARY KEY,
                                Host_id integer
                                ); """ 


# create Template table
sql_create__Template_table = """ CREATE TABLE IF NOT EXISTS Template(
                                position integer PRIMARY KEY,
                                template1 TEXT,
                                template2 TEXT,
                                template3 TEXT,
                                template4 TEXT,
                                template5 TEXT,
                                template6 TEXT,
                                template7 TEXT,
                                template8 TEXT,
                                template9 TEXT
                                ); """


sql_create__Queries_table = """ CREATE TABLE IF NOT EXISTS Queries (
                                position integer PRIMARY KEY,
                                Query TEXT
                                ); """