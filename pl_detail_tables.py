# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:04:20 2021

@author: antoine.mack
"""

import pandas as pd
from itertools import combinations

def add_one(number):
    return number + 1

def QBO_table_maker(qb_obj):
    pld_items = list(qb_obj.values())[2]['Row']
    values = []
    schema_coor = []
    #check length of items
    combo2 = combinations([0,0]+list(range(15))+
                          [0,0]+list(range(15)),2)
    for seq in set(combo2):
        (i,j) = seq
        try:
            category_name = pld_items[i]['Header']['ColData'][0]['value'] #1st header
            subcategory_name = pld_items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value'] #2nd level
            #print(seq,", ", category_name,subcategory_name)
            schema_coor.append(seq)
            for ITEMS in range(len(pld_items[i]['Rows']['Row'][j]['Rows']['Row'])):
                date = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][ITEMS]['ColData'][0]['value']
                trans_type = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][ITEMS]['ColData'][1]['value']
                num = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][ITEMS]['ColData'][2]['value']
                name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][ITEMS]['ColData'][3]['value']
                #location = items[i]['Rows']['Row'][j]['Rows']['Row'][ITEMS]['ColData'][4]['value']
                CLASS = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][ITEMS]['ColData'][5]['value']
                desc = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][ITEMS]['ColData'][6]['value']
                split = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][ITEMS]['ColData'][7]['value']
                amount = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][ITEMS]['ColData'][8]['value']
                type_name = " "
                group_name = " "
                div_name = " "
                level6= " "
                values.append([category_name, subcategory_name, type_name, group_name, div_name,level6,
                               date, trans_type, num, name, CLASS, desc, split, amount])
        except:
            pass
    combo3 = combinations([0,0]+list(range(15))+
                          [0,0]+list(range(15))+
                          [0,0]+list(range(15)),3)
    for seq in set(combo3):
        (i,j,k) = seq
        try:
            category_name = pld_items[i]['Header']['ColData'][0]['value'] #1st header
            subcategory_name = pld_items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value'] #2nd level
            type_name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value'] # 3rd level
            #print(seq,", ", category_name,subcategory_name,type_name)
            schema_coor.append(seq)
            for ITEMS in range(len(pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'])):
                date = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][ITEMS]['ColData'][0]['value']
                trans_type = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][ITEMS]['ColData'][1]['value']
                num = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][ITEMS]['ColData'][2]['value']
                name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][ITEMS]['ColData'][3]['value']
                #location = items[i]['Rows']['Row'][j]['ColData'][4]['value']
                CLASS = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][ITEMS]['ColData'][5]['value']
                desc = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][ITEMS]['ColData'][6]['value']
                split = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][ITEMS]['ColData'][7]['value']
                amount = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][ITEMS]['ColData'][8]['value']
                group_name = " "
                div_name = " "
                level6 = " "
                values.append([category_name, subcategory_name, type_name, group_name, div_name,level6,
                               date, trans_type, num, name, CLASS, desc, split, amount])
        except:
            pass
    combo4 = combinations([0,0]+list(range(15))+
                          [0,0]+list(range(15))+
                          [0,0]+list(range(15))+
                          [0,0]+list(range(15)),4)
    for seq in set(combo4):
        (i,j,k,L) = seq
        try:
            category_name = pld_items[i]['Header']['ColData'][0]['value'] #1st header
            subcategory_name = pld_items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value'] #2nd level
            type_name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value'] # 3rd level
            group_name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value'] # 4th level
            #print(seq,", ", category_name,subcategory_name,type_name,group_name )
            schema_coor.append(seq)
            for ITEMS in range(len(pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'])):
                date = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][ITEMS]['ColData'][0]['value']
                trans_type = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][ITEMS]['ColData'][1]['value']
                num = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][ITEMS]['ColData'][2]['value']
                name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][ITEMS]['ColData'][3]['value']
                #location = items[i]['Rows']['Row'][j]['ColData'][4]['value']
                CLASS = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][ITEMS]['ColData'][5]['value']
                desc = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][ITEMS]['ColData'][6]['value']
                split = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][ITEMS]['ColData'][7]['value']
                amount = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][ITEMS]['ColData'][8]['value']
                div_name = " "
                level6 = " "
                values.append([category_name, subcategory_name, type_name, group_name, div_name,level6,
                               date, trans_type, num, name, CLASS, desc, split, amount])
        except:
            pass
    combo5 = combinations([0,0]+list(range(15))+
                          [0,0]+list(range(15))+
                          [0,0]+list(range(15))+
                          [0,0]+list(range(15))+
                          [0,0]+list(range(15)),5)
    for seq in set(combo5):
        (i,j,k,L,m) = seq
        try:
            category_name = pld_items[i]['Header']['ColData'][0]['value'] #1st header
            subcategory_name = pld_items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value'] #2nd level
            type_name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value'] # 3rd level
            group_name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value'] # 4th level
            div_name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Header']['ColData'][0]['value'] # 4th level
            #print(seq,", ", category_name,subcategory_name,type_name,group_name,div_name, "***5 Row" )
            schema_coor.append(seq)
            for ITEMS in range(len(pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'])):
                date = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][ITEMS]['ColData'][0]['value']
                trans_type = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][ITEMS]['ColData'][1]['value']
                num = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][ITEMS]['ColData'][2]['value']
                name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][ITEMS]['ColData'][3]['value']
                #location
                CLASS = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][ITEMS]['ColData'][5]['value']
                desc = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][ITEMS]['ColData'][6]['value']
                split = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][ITEMS]['ColData'][7]['value']
                amount = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][ITEMS]['ColData'][8]['value']
                level6 = " "
                values.append([category_name, subcategory_name, type_name, group_name, div_name, level6,
                               date, trans_type, num, name, CLASS, desc, split, amount])
        except:
            pass
    combo6 = combinations([0,0]+list(range(8))+
                          [0,0]+list(range(8))+
                          [0,0]+list(range(8))+
                          [0,0]+list(range(8))+
                          [0,0]+list(range(8))+
                          [0,0]+list(range(8)),6)
    for seq in set(combo6):
        (i,j,k,L,m,n) = seq
        try:
            category_name = pld_items[i]['Header']['ColData'][0]['value'] #1st header
            subcategory_name = pld_items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value'] #2nd level
            type_name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value'] # 3rd level
            group_name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value'] # 4th level
            div_name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Header']['ColData'][0]['value'] # 4th level
            level6 = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['Header']['ColData'][0]['value'] # 5th level
            #print(seq,", ", category_name,subcategory_name,type_name,group_name,div_name,level6 )
            schema_coor.append(seq)
            for ITEMS in range(len(pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['Rows']['Row'])):
                date = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['Rows']['Row'][ITEMS]['ColData'][0]['value']
                trans_type = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['Rows']['Row'][ITEMS]['ColData'][1]['value']
                num = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['Rows']['Row'][ITEMS]['ColData'][2]['value']
                name = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['Rows']['Row'][ITEMS]['ColData'][3]['value']
                #location
                CLASS = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['Rows']['Row'][ITEMS]['ColData'][5]['value']
                desc = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['Rows']['Row'][ITEMS]['ColData'][6]['value']
                split = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['Rows']['Row'][ITEMS]['ColData'][7]['value']
                amount = pld_items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['Rows']['Row'][ITEMS]['ColData'][8]['value']
                values.append([category_name, subcategory_name, type_name, group_name, div_name,level6,
                               date, trans_type, num, name, CLASS, desc, split, amount])
        except:
            pass
    headers = ["category_name", "subcategory_name", "type_name", "group_name", "div_name","level6",
                           "date", "trans_type", "num", "name", "CLASS", "desc", "split", "amount"]
    
    df = pd.DataFrame(values, columns = headers)
    return df

if __name__ == "__main__":
   print("Executed as main")
else:
    print ("P&L Details imported")