# get data sql
data1_Query = '''
    SELECT *
    FROM
        (SELECT dense_rank()
        OVER(ORDER by frequency DESC) as den_rank, 
        * FROM(
            SELECT Neighbourhood_group, count(Neighbourhood_group) as frequency
            FROM Host_Location
            GROUP BY Neighbourhood_group
            ORDER BY frequency DESC
            )
        )
    WHERE den_rank <= 3
'''
data2_Query = '''
    select Neighbourhood_group,result
    FROM
        (SELECT Host_Location.ID,Neighbourhood_group,sum(price) /count(neighbourhood_group) as result
        FROM Host_Location,Fee
        WHERE Host_Location.ID = Fee.ID and price NOTNULL and Neighbourhood_group NOTNULL
        GROUP by Neighbourhood_group
        order by result DESC
        )
'''
data4_Query = '''
        SELECT Cancellation_policy, max(policy), Country
        FROM(
            SELECT Cancellation_policy, count(Cancellation_policy) as policy, Country
            FROM Platform, Host_Location
            WHERE Platform.ID = Host_Location.ID
            GROUP BY Cancellation_policy
            ORDER BY policy DESC
            )
'''
data5_Query = '''
        SELECT Availabilitty_365, count(*) AS count
        FROM Platform
        GROUP BY Availabilitty_365
        ORDER BY count DESC
        LIMIT 2
'''
data6_Query = '''
        SELECT Room_type, avg_price
        FROM(
        SELECT Room_type, avg(Price) as avg_price,
            rank()OVER (ORDER BY avg(Price) DESC)
            FROM House_info, Fee
            WHERE House_info.ID = Fee.ID
            GROUP BY Room_type
            )
'''
data7_Query = '''
        SELECT Country, Neighbourhood, Neighbourhood_group, Room_type, count(Room_type) AS count
        FROM House_info,Host_Location
        WHERE Host_Location.ID = House_info.ID AND Room_type NOTNULL
        GROUP BY Room_type
        ORDER BY count DESC
        LIMIT 1
'''
data9_Query1 = '''
        SELECT Host_identity_verified, pc
        FROM(
            SELECT Host_identity_verified, (100.*count(*) / sum(count(*)) over()) AS pc
            FROM Host_Info
            GROUP BY Host_identity_verified
        )
        WHERE Host_identity_verified = 'verified' or Host_identity_verified = 't' 
        or Host_identity_verified = 'TRUE' or Host_identity_verified = 'True' or Host_identity_verified = 'true'
'''
data9_Query2 = '''
        SELECT Host_identity_verified, avg(Review_rate_number) AS rm
        FROM User LEFT JOIN (Host_Info LEFT JOIN Connect ON Host_Info.Host_id = Connect.Host_id ) ON User.ID = Connect.ID
        WHERE Review_rate_number > 0.0 AND Host_identity_verified NOTNULL
        GROUP BY Host_identity_verified
        ORDER BY rm DESC
        LIMIT 1
'''
data9_Query3 = '''
        SELECT Neighbourhood_group, avg(Review_rate_number) AS hr
        FROM Host_Location as HL, User as U
        WHERE HL.ID = U.ID and Neighbourhood_group NOTNULL
        GROUP by Neighbourhood_group
        ORDER by hr DESC
'''


# get template sql
template1_Query = '''
    SELECT position, template1
    FROM Template
    WHERE template1 IS NOT NULL
'''
template2_Query = '''
        SELECT position, template2
        FROM Template
        WHERE template2 IS NOT NULL
'''
template4_Query = '''
    SELECT position, template4
    FROM Template
    WHERE template4 IS NOT NULL
'''
template5_Query = '''
    SELECT position, template5
    FROM Template
    WHERE template5 IS NOT NULL
'''
template6_Query = '''
    SELECT position, template6
    FROM Template
    WHERE template6 IS NOT NULL
'''
template7_Query = '''
    SELECT position, template7
    FROM Template
    WHERE template7 IS NOT NULL
'''
template9_Query = '''
    SELECT position, template9
    FROM Template
    WHERE template9 IS NOT NULL
'''


# get data for visualization
neighbourhood_review = '''
    SELECT C.ID, HL.Neighbourhood_group, U.Number_of_reviews
    FROM User U, Connect C, Host_Location HL
    WHERE U.ID = C.ID AND C.ID = HL.ID
'''
neighbourhood = '''
    SELECT Neighbourhood
    FROM Host_Location
'''
fee_House_info = '''
    SELECT F.ID, F.Price, Hi.Room_type
    FROM Fee F, House_info Hi, Connect C
    WHERE F.ID = C.ID AND C.ID = Hi.ID
'''


Query_list = [data1_Query, data2_Query, data4_Query, data5_Query, data6_Query, 
              data7_Query, data9_Query1, data9_Query2, data9_Query3, template1_Query, template2_Query, 
              template4_Query, template5_Query, template6_Query, template7_Query, template9_Query,
              neighbourhood_review, neighbourhood, fee_House_info]