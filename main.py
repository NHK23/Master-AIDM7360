import Path.open_file as of
import SQL.sql_connection as sc
import SQL.sql_folder_close as sfc
import SQL.Create_sql.create_sql_table as cst
import SQL.Create_sql.sql_operation as so
import SQL.Delete_sql.Delete_sql as ds
import SQL.Update_sql.Update_sql as us
import SQL.Query_sql.Query_sql as qs
import SQL.Create_sql.Template as Template
import SQL.Insert_sql.Insert_sql as Isql
import Function.data_classify as dc
import Function.process_data as process
import Report.report as report
import Visualization.visualization as vs
import UI.UI as UI
# import create sql
from SQL.Create_sql.sql_create_queries import sql_create__House_info_table
from SQL.Create_sql.sql_create_queries import sql_create__Host_info_table
from SQL.Create_sql.sql_create_queries import sql_create__House_Location_table
from SQL.Create_sql.sql_create_queries import sql_create__Platform_table
from SQL.Create_sql.sql_create_queries import sql_create__Fee_table
from SQL.Create_sql.sql_create_queries import sql_create__User_table
from SQL.Create_sql.sql_create_queries import sql_create__Connect_table
from SQL.Create_sql.sql_create_queries import sql_create__Template_table
from SQL.Create_sql.sql_create_queries import sql_create__Queries_table
# import query sql
from SQL.Query_sql.sql_query_template import Query_list



while True:
    file_UI = UI.UI([0], [0], [0], [0], [0], [0], [0])                  # initial UI
    csv_name, fileName = file_UI.file()        # get csv file and database name
    csv_name = csv_name[:-1] + '.csv'
    raw_data = of.csv_read(csv_name)           # get csv data to dataframme type

    # create and connect database
    fileName = fileName[:-1] + '.db'
    sql_full_path = of.sql_path(fileName)
    dbConnection = sc.create_connection(sql_full_path)


    # clean and classify data
    clean_data = process.clean_data(raw_data)
    House_info, Host_info, House_Location, Platform, Fee, User, Connect= dc.divide_data(clean_data)


    # create table
    cst.check_sql_connection(dbConnection, sql_create__House_info_table)
    cst.check_sql_connection(dbConnection, sql_create__Host_info_table)
    cst.check_sql_connection(dbConnection, sql_create__House_Location_table)
    cst.check_sql_connection(dbConnection, sql_create__Platform_table)
    cst.check_sql_connection(dbConnection, sql_create__Fee_table)
    cst.check_sql_connection(dbConnection, sql_create__User_table)
    cst.check_sql_connection(dbConnection, sql_create__Connect_table)
    cst.check_sql_connection(dbConnection, sql_create__Template_table)
    cst.check_sql_connection(dbConnection, sql_create__Queries_table)

    
    # create data
    so.create_House_info_data(dbConnection, House_info)
    so.create_Host_info_data(dbConnection, Host_info)
    so.create_Host_Location_data(dbConnection, House_Location)
    so.create_Platform_data(dbConnection, Platform)
    so.create_Fee_data(dbConnection, Fee)
    so.create_User_data(dbConnection, User)
    so.create_Connect_data(dbConnection, Connect)
    template = Template.get_template()
    so.create_Template_data(dbConnection, template)
    so.create_Queries_data(dbConnection, Query_list)



    # operation
    UI_list = []      # save report into list for UI 
    while True:
        operation_UI = UI.UI([0], [0], [0], [0], [0], [0], [0])
        operation = operation_UI.operation_sign()

        if operation == 0:
            # update data
            us.update_operation(dbConnection)
        elif operation == 1:
            # delete data
            ds.delete_operation(dbConnection)
        elif operation == 2:
            # insert data
            Isql.insert_sql(dbConnection)
        elif operation == 3:
            # get query sql
            Query = qs.get_Query(dbConnection)

            # get template data from database2
            template1_data = qs.get_template1_data(dbConnection, Query['Query'][0])
            template2_data = qs.get_template2_data(dbConnection, Query['Query'][1])
            template4_data = qs.get_template4_data(dbConnection, Query['Query'][2])
            template5_data = qs.get_template5_data(dbConnection, Query['Query'][3])
            template6_data = qs.get_template6_data(dbConnection, Query['Query'][4])
            template7_data = qs.get_template7_data(dbConnection, Query['Query'][5])
            template9_data1 = qs.get_template9_1_data(dbConnection, Query['Query'][6])
            template9_data2 = qs.get_template9_2_data(dbConnection, Query['Query'][7])
            template9_data3 = qs.get_template9_3_data(dbConnection, Query['Query'][8])

            # get template from database
            template1 = qs.get_template1(dbConnection, Query['Query'][9])
            template2 = qs.get_template2(dbConnection, Query['Query'][10])
            template4 = qs.get_template4(dbConnection, Query['Query'][11])
            template5 = qs.get_template5(dbConnection, Query['Query'][12])
            template6 = qs.get_template6(dbConnection, Query['Query'][13])
            template7 = qs.get_template7(dbConnection, Query['Query'][14])
            template9 = qs.get_template9(dbConnection, Query['Query'][15])

            # create and write report
            report_name = 'Airbnb_report.txt'
            report_path = of.report_path(report_name)
            T1 = report.write_report_T1(report_path, template1_data, template1)
            T2 = report.write_report_T2(report_path, template2_data, template2)
            T4 = report.write_report_T4(report_path, template4_data, template4)
            T5 = report.write_report_T5(report_path, template5_data, template5)
            T6 = report.write_report_T6(report_path, template6_data, template6)
            T7 = report.write_report_T7(report_path, template7_data, template7)
            T9 = report.write_report_T9(report_path, template9_data1, template9_data2, template9_data3, template9)
            UI_list = [T1,T2,T4,T5,T6,T7,T9]
            break




    # Visualization
    vs.map_visualization(House_Location)
    map_visual_data = qs.map_visualization_data(dbConnection, Query['Query'][16])     # get review data
    vs.review(map_visual_data)         
    vs.availability_365(Platform)
    vs.cancellation_policy(Platform)


    sfc.close(dbConnection)

    # report and visualization UI
    report_UI = UI.UI(UI_list, House_info, Host_info, House_Location, Platform, Fee, User)
    report_UI.UI_report()


    ui = UI.UI([0], [0], [0], [0], [0], [0], [0])
    break_or_continue = ui.Exit_or_continue()
    if break_or_continue == 1:
        break