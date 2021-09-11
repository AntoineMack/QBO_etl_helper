# -*- coding: utf-8 -*-
"""
Created on Wed May 26 12:03:21 2021

@author: antoine.mack
"""

import pandas as pd

def add_one(number):
    return number + 1

def QBO_table_TRANS(qb_obj):
    trans_items = list(qb_obj.values())[2]['Row']
    values = []
    for i in range(len(trans_items)):
        date = trans_items[i]['ColData'][0]['value']
        trans_type = trans_items[i]['ColData'][1]['value']
        num = trans_items[i]['ColData'][2]['value']
        posting = trans_items[i]['ColData'][3]['value']
        name = trans_items[i]['ColData'][4]['value']
        desc = trans_items[i]['ColData'][6]['value']
        account = trans_items[i]['ColData'][7]['value']
        split = trans_items[i]['ColData'][8]['value']
        amount = trans_items[i]['ColData'][9]['value']
        values.append([date, trans_type, num,posting, name, desc,account, split, amount])
        #print(i)
    headers = ["date", "trans_type", "num", "posting", "name", "desc","account", "split", "amount"]
    df = pd.DataFrame(values, columns = headers)
    QBO_table_TRANS.df = df
    return df
    
if __name__ == "__main__":
   print("Executed as main")
else:
    print ("Transaction List imported")