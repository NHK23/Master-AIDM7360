import sqlite3
import numpy as np
import pandas as pd
sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))


# get Template data
def get_template1_data(dbConnection, sql):
    cur = dbConnection.cursor()
    t1_data = cur.execute(sql)
    t1_data_df = pd.DataFrame(data = t1_data, columns = ['rank', 'neighbourhood', 'count'])
    return t1_data_df

def get_template2_data(dbConnection, sql):
    cur = dbConnection.cursor()
    t2_data = cur.execute(sql)
    t2_data_df = pd.DataFrame(data = t2_data, columns = ['neighbourhood_group', 'avg price'])
    return t2_data_df

def get_template4_data(dbConnection, sql):
    cur = dbConnection.cursor()
    t4_data = cur.execute(sql)
    t4_data_df = pd.DataFrame(data = t4_data, columns = ['Cancellation_policy', 'count', 'Country'])
    return t4_data_df

def get_template5_data(dbConnection, sql):
    cur = dbConnection.cursor()
    t5_data = cur.execute(sql)
    t5_data_df = pd.DataFrame(data = t5_data, columns = ['availabilitty_365', 'count'])
    return t5_data_df

def get_template6_data(dbConnection, sql):
    cur = dbConnection.cursor()
    t6_data = cur.execute(sql)
    t6_data_df = pd.DataFrame(data = t6_data, columns = ['room type', 'avg price'])
    return t6_data_df

def get_template7_data(dbConnection, sql):
    cur = dbConnection.cursor()
    t7_data = cur.execute(sql)
    t7_data_df = pd.DataFrame(data = t7_data, columns = ['country', 'neighbourhood', 'neighbourhood_group', 'room type', 'count'])
    return t7_data_df

def get_template9_1_data(dbConnection, sql1):
    cur = dbConnection.cursor()
    t9_data1 = cur.execute(sql1)
    t9_data1_df = pd.DataFrame(data = t9_data1, columns = ['host identity verified', 'percentage'])
    return t9_data1_df

def get_template9_2_data(dbConnection, sql2):
    cur = dbConnection.cursor()
    t9_data2 = cur.execute(sql2)
    t9_data2_df = pd.DataFrame(data = t9_data2, columns = ['host identity verified', 'rate'])
    return t9_data2_df

def get_template9_3_data(dbConnection, sql3):
    cur = dbConnection.cursor()
    t9_data3 = cur.execute(sql3)
    t9_data3_df = pd.DataFrame(data = t9_data3, columns = ['neighbourhood group', 'rate'])
    return t9_data3_df

# get Template
def get_template1(dbConnection, sql):
    cur = dbConnection.cursor()
    t1 = cur.execute(sql)
    t1_df = pd.DataFrame(data = t1, columns = ['position', 'template1'])
    return t1_df

def get_template2(dbConnection, sql):
    cur = dbConnection.cursor()
    t2 = cur.execute(sql)
    t2_df = pd.DataFrame(data = t2, columns = ['position', 'template2'])
    return t2_df

def get_template4(dbConnection, sql):
    cur = dbConnection.cursor()
    t4 = cur.execute(sql)
    t4_df = pd.DataFrame(data = t4, columns = ['position', 'template4'])
    return t4_df

def get_template5(dbConnection, sql):
    cur = dbConnection.cursor()
    t5 = cur.execute(sql)
    t5_df = pd.DataFrame(data = t5, columns = ['position', 'template5'])
    return t5_df

def get_template6(dbConnection, sql):
    cur = dbConnection.cursor()
    t6 = cur.execute(sql)
    t6_df = pd.DataFrame(data = t6, columns = ['position', 'template6'])
    return t6_df

def get_template7(dbConnection, sql):
    cur = dbConnection.cursor()
    t7 = cur.execute(sql)
    t7_df = pd.DataFrame(data = t7, columns = ['position', 'template7'])
    return t7_df

def get_template9(dbConnection, sql):
    cur = dbConnection.cursor()
    t9_data = cur.execute(sql)
    t9_df = pd.DataFrame(data = t9_data, columns = ['position', 'template9'])
    return t9_df

# get visualization data
def map_visualization_data(dbConnection, sql):
    cur = dbConnection.cursor()
    map_visual_data = cur.execute(sql)
    map_visual_data_df = pd.DataFrame(data = map_visual_data, columns = ['ID', 'Neighbourhood_group', 'Number_of_reviews'])
    return map_visual_data_df

def Fee_House_info(dbConnection, sql):
    cur = dbConnection.cursor()
    Fee_House_info_data = cur.execute(sql)
    Fee_House_info_df = pd.DataFrame(data = Fee_House_info_data, columns = ['ID', 'Price', 'Room_type'])
    return Fee_House_info_df

# get Query
def get_Query(dbConnection):
    cur = dbConnection.cursor()
    sql = '''
        SELECT position, Query
        FROM Queries
    '''
    Query = cur.execute(sql)
    Query_df = pd.DataFrame(data = Query, columns = ['position', 'Query'])
    return Query_df