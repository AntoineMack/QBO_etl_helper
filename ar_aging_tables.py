# -*- coding: utf-8 -*-
"""
Created on Mon May  3 11:35:45 2021

@author: antoine.mack
"""
import pandas as pd

def add_one(number):
    return number + 1

def QBO_table_maker(qb_obj):
    ar_headers = ['Customer','Current','1-30 days','31-60 days','61 - 90 days','91 and over']
    items = list(qb_obj.values())[2]
    ar_list = []
    for i in range(len(items['Row'])-1):
        #print(i)
        try:
            cust = items['Row'][i]['ColData'][0]['value']
            current = items['Row'][i]['ColData'][1]['value']
            day30 = items['Row'][i]['ColData'][2]['value']
            day60 = items['Row'][i]['ColData'][3]['value']
            day90 = items['Row'][i]['ColData'][4]['value']
            more91 = items['Row'][i]['ColData'][5]['value']
            new_row = [cust,current,day30,day60,day90,more91]
            ar_list.append(new_row)
        except:
            cust = items['Row'][i]['Rows']['Row'][0]['ColData'][0]['value']
            current = items['Row'][i]['Rows']['Row'][0]['ColData'][1]['value']
            day30 = items['Row'][i]['Rows']['Row'][0]['ColData'][2]['value']
            day60 = items['Row'][i]['Rows']['Row'][0]['ColData'][3]['value']
            day90 = items['Row'][i]['Rows']['Row'][0]['ColData'][4]['value']
            more91 = items['Row'][i]['Rows']['Row'][0]['ColData'][5]['value']
            new_row = [cust,current,day30,day60,day90,more91]
            ar_list.append(new_row)
    
    df = pd.DataFrame(ar_list, columns=ar_headers)
    return df

if __name__ == "__main__":
   print("Executed as main")
else:
    print ("AR Aging imported")

