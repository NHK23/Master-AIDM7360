import sqlite3
from sqlite3 import Error
import numpy as np
sqlite3.register_adapter(np.int64, lambda val: int(val))
sqlite3.register_adapter(np.int32, lambda val: int(val))


# update data into table
def update_operation(dbConnection):
    while True:
        update_data = set()
        table_name = input('Which table do you want to update?\nExit please input 3\n')
        if table_name == 'Template':
            while True:
                column = input('Which column do you want to update?\n')
                if column != 'position':
                    position = input('And its position:\n')
                    content= input('Input your update content.\n')
                    update_data = (content, position)
                    update_sql = 'UPDATE ' + table_name + ' SET ' + column + ' = ? WHERE position = ?'
                else:
                    print('Primary key cannot update, please input another column.')
        elif table_name == 'Host_Info':
            while True:
                column = input('Which column do you want to update?\n')
                if column != 'Host_id':
                    host_id = input('And its host id:\n')
                    content= input('Input your update content.\n')
                    update_data = (content, host_id)
                    update_sql = 'UPDATE ' + table_name + ' SET ' + column + ' = ? WHERE Host_id = ?'
                    break
                else:
                    print('Primary key cannot update, please input another column.')
        elif table_name == '3':
            break
        elif table_name == 'House_info' or table_name == 'Host_Location' or table_name == 'Platform' or table_name == 'Fee' or table_name == 'User' or table_name == 'Connect':
            while True:   
                column = input('Which column do you want to update?\n')
                if column != 'ID':
                    id = input('And its ID:\n')
                    content= input('Input your update content.\n')
                    update_data = (content, id)
                    update_sql = 'UPDATE ' + table_name + ' SET ' + column + ' = ? WHERE ID = ?'
                    break
                else:
                    print('Primary key cannot update, please input another column.')
        else:
            print('Please input right table')
            continue

        try:
            cur = dbConnection.cursor()
            cur.execute(update_sql, update_data)
            dbConnection.commit()
            print('update successfully.')
        except Error as e:
            print(e)