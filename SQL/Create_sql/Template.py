import pandas as pd


def get_template():
    template = {'position':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                'T1':['\'s room locations are mainly concentrated in ', 'area.', None, None, None, None, None, None, None, None, None],
                'T2':[' area has the highest average rental price which is ', ' dollars, and ', ' area has the average rental lowest price which is ', ' dollars.', None, None, None, None, None, None, None],
                'T3':['The most common word in house rule is ', ' by ', ' times.', None, None, None, None, None, None, None, None],
                'T4':['The most common cancellation policy in ', ' is ', '.', None, None, None, None, None, None, None, None],
                'T5':['The most common availability of a property is ', ' days which total number of house is ', ' And the second common is ', ' days with total number of house is ', None, None, None,  None, None, None, None],
                'T6':[' room type has the ', 'highest', 'lowest' , ' average price which is ', None, None, None, None, None, None, None],
                'T7':['Among ', ' users in ', ' area, they prefer ', ' room type.', None, None, None, None, None, None, None],
                'T8':['The room price ', 'higher', 'lower', ', the service price will ', 'higher', 'lower', '.', ' It has a ', 'negative', 'positive', ' relationship.'],
                'T9':['% of the hosts in ', ' has been verified. ', ' host has better average of review rate in ', ', and ', ' area has the highest average of review rate in ', '.', None, None, None, None, None],
    }

    template_df = pd.DataFrame(template)
    return template_df