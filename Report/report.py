app_name = 'Airbnb'


# write Template1 into report
def write_report_T1(report_path, template1_data, template1):
    try: 
        # open file
        file = open(report_path, 'a+') 

        T1 = (app_name + template1['template1'].values[0] + template1_data['neighbourhood'].values[0] + ', '
        + template1_data['neighbourhood'].values[1] + ', ' + template1_data['neighbourhood'].values[2] 
        + ' ' +  template1['template1'].values[1] + '\n')

        file.write(T1)
    except:
        print('Error1!')
        pass
    finally: # Always executed
        file.close()
    return T1


# write Template2 into report
def write_report_T2(report_path, template2_data, template2):
    try: 
        # open file
        file = open(report_path, 'a+') 

        T2 = (template2_data['neighbourhood_group'].values[0] + template2['template2'].values[0] 
        + str(round(template2_data['avg price'].values[0])) + template2['template2'].values[1] 
        + template2_data['neighbourhood_group'].values[len(template2_data) - 1] + template2['template2'].values[2] 
        + str(round(template2_data['avg price'].values[len(template2_data) - 1])) + template2['template2'].values[3] + '\n')

        # get data from dataframe and write into report
        file.write(T2)
    except:
        print('Error2!')
        pass
    finally: # Always executed
        file.close()
    return T2


# write Template4 into report
def write_report_T4(report_path, template4_data, template4):
    try: 
        # open file
        file = open(report_path, 'a+') 

        T4 = (template4['template4'].values[0] + template4_data['Country'].values[0] 
        + template4['template4'].values[1] + template4_data['Cancellation_policy'].values[0] +'.\n')

        # get data from dataframe and write into report
        file.write(T4)
    except:
        print('Error4!')
        pass
    finally: # Always executed
        file.close()
    return T4


# write Template5 into report
def write_report_T5(report_path, template5_data, template5):
    try: 
        # open file
        file = open(report_path, 'a+') 

        T5 = (template5['template5'].values[0] + str(int(template5_data['availabilitty_365'].values[0])) 
        + template5['template5'].values[1] + str(int(template5_data['count'].values[0])) + '.' 
        + template5['template5'].values[2] + str(int(template5_data['availabilitty_365'].values[1])) 
        + template5['template5'].values[3] + str(int(template5_data['count'].values[1])) + '.' + '\n')

        # get data from dataframe and write into report
        file.write(T5)
    except:
        print('Error5!')
        pass
    finally: # Always executed
        file.close()
    return T5


# write Template6 into report
def write_report_T6(report_path, template6_data, template6):
    try: 
        # open file
        file = open(report_path, 'a+') 

        T6 = (template6_data['room type'].values[len(template6_data) - 1] + template6['template6'].values[0] 
        + template6['template6'].values[2] + template6['template6'].values[3] + str(round(template6_data['avg price'].values[0],2)) + '.\n')

        # get data from dataframe and write into report
        file.write(T6)
    except:
        print('Error6!')
        pass
    finally: # Always executed
        file.close()
    return T6


# write Template7 into report
def write_report_T7(report_path, template7_data, template7):
    try: 
        # open file
        file = open(report_path, 'a+') 

        T7 = (template7['template7'].values[0]  + app_name + template7['template7'].values[1] 
        + template7_data['country'].values[0] + ', ' + template7_data['neighbourhood'].values[0] + ', ' 
        + template7_data['neighbourhood_group'].values[0] + template7['template7'].values[2] 
        + template7_data['room type'].values[0] + template7['template7'].values[3] + '\n')

        # get data from dataframe and write into report
        file.write(T7)
    except:
        print('Error7!')
        pass
    finally: # Always executed
        file.close()
    return T7


# write Template9 into report
def write_report_T9(report_path, template9_data1, template9_data2, template9_data3, template9):
    try: 
        # open file
        file = open(report_path, 'a+') 

        T9 = (str(round(template9_data1['percentage'].values[0], 1)) + template9['template9'].values[0] 
        + app_name + template9['template9'].values[1] + template9_data2['host identity verified'].values[0] 
        + template9['template9'].values[2] + str(round(template9_data2['rate'].values[0], 1)) + template9['template9'].values[3] 
        + template9_data3['neighbourhood group'].values[0] + template9['template9'].values[4] + str(round(template9_data3['rate'].values[0], 1)) + '.\n')

        # get data from dataframe and write into report
        file.write(T9)
    except:
        print('Error9!')
        pass
    finally: # Always executed
        file.close()
    return T9