import sqlite3
from sqlite3 import Error
import numpy as np
sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))


# delete data
def delete_operation(dbConnection):
    while True:
        operation = input('Which one do you want to delete?\n1. data\n2. Exit\n')    
        if operation == '1' or operation == 'Data' or operation == 'DATA' or operation == 'data':
            table_name = input('Which table do the data belong to?\n')
            if table_name == 'House_info' or table_name == 'Host_Location' or table_name == 'Platform' or table_name == 'Fee' or table_name == 'User' or table_name == 'Connect':
                try:
                    delete_data = input('which id?\n')
                    sql = 'DELETE FROM ' + table_name + ' WHERE ID=?'
                    cur = dbConnection.cursor()
                    cur.execute(sql, (delete_data,))
                    dbConnection.commit()
                    print('Delete successfully.')
                except Error as e:
                    print(e)
                    continue
            elif table_name == 'Host_Info':
                try:
                    delete_data = input('which Host_id?\n')
                    sql = 'DELETE FROM ' + table_name + ' WHERE Host_id=?'
                    cur = dbConnection.cursor()
                    cur.execute(sql, (delete_data,))
                    dbConnection.commit()
                    print('Delete successfully.')
                except Error as e:
                    print(e)
                    continue
            elif table_name == 'Template':
                try:
                    delete_data = input('which position?\n')
                    sql = 'DELETE FROM ' + table_name + ' WHERE position=?'
                    cur = dbConnection.cursor()
                    cur.execute(sql, (delete_data,))
                    dbConnection.commit()
                    print('Delete successfully.')
                except Error as e:
                    print(e)
                    continue
        elif operation == '2' or operation == 'Exit' or operation == 'exit' or operation == 'EXIT':
            break
        else:
            print('Please input right operation.')
            continue