# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:08:51 2021

@author: antoine.mack
"""
import pandas as pd
from itertools import combinations

def add_one(number):
    return number + 1

pl_vault = {'five':[],'four':[],'three':[],'two':[]}

def QBO_table_maker(qb_obj):
    headers = ["Category", "Sub Category", "Class", "Group", "Type",'Amount']
    values = []
    items = list(qb_obj.values())[2]['Row']
    
    combo5 = combinations([0,1,2,3,4,5,6,7,8,
                           0,1,2,3,4,5,6,7,8,
                           0,1,2,3,4,5,6,7,8,
                           0,1,2,3,4,5,6,7,8,
                           0,1,2,3,4,5,6,7,8],5)
    for seq in list(combo5):
        (i,j,k,L,m) = seq
        #Category,Subcategory, Class, Group, Type
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            group_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value']
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['ColData'][1]['value']
            values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
            #print(seq," *****Success*****")
            pl_vault['five'].append(seq)
        except:
            #print(seq," FAIL")
            pass
    combo4 = combinations([0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10],4)
    for seq in list(combo4):
        (i,j,k,L) = seq
        #Category, Subcategory, Class, Type
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            group_name = ''
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['ColData'][1]['value']
            values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
            #print(seq," *****Success*****")
            pl_vault['four'].append(seq)
        except:
            #print(seq," FAIL")
            pass
    combo3 = combinations([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                           0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                           0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],3)
    for seq in list(combo3):
        (i,j,k) = seq
        #Category, Subcategory, Type
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            
            class_name = ''
            
            group_name = ''
            
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['ColData'][1]['value']
            values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
            #print(seq," *****Success*****")
            pl_vault['three'].append(seq)
        except:
            #print(seq," FAIL")
            pass
    combo2 = combinations([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                           0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],2)
    for seq in list(combo2):
        (i,j) = seq
        #Category, Type
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            
            subcategory_name = ''
            
            class_name = ''
            
            group_name = ''
            
            type_name = items[i]['Rows']['Row'][j]['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['ColData'][1]['value']
            values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
            #print(seq," *****Success*****")
            pl_vault['two'].append(seq)
        except:
            #print(seq," FAIL")
            pass  
    df = pd.DataFrame(values, columns = headers)
    return df

#use with stored coordinates
def QBO_table_maker2(qb_obj, combo5,combo4,combo3,combo2):
    headers = ["Category", "Sub Category", "Class", "Group", "Type",'Amount']
    values = []
    items = list(qb_obj.values())[2]['Row']
    
    for seq in list(combo5):
        (i,j,k,L,m) = seq
        #Category,Subcategory, Class, Group, Type
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            group_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value']
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['ColData'][1]['value']
            values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
            #print(seq," *****Success*****")
    
        except:
            #print(seq," FAIL")
            pass
    
    for seq in list(combo4):
        (i,j,k,L) = seq
        #Category, Subcategory, Class, Type
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            group_name = ''
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['ColData'][1]['value']
            values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
            #print(seq," *****Success*****")
        except:
            #print(seq," FAIL")
            pass
    
    for seq in list(combo3):
        (i,j,k) = seq
        #Category, Subcategory, Type
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            
            class_name = ''
            
            group_name = ''
            
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['ColData'][1]['value']
            values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
            #print(seq," *****Success*****")
        except:
            #print(seq," FAIL")
            pass
    
    for seq in list(combo2):
        (i,j) = seq
        #Category, Type
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            
            subcategory_name = ''
            
            class_name = ''
            
            group_name = ''
            
            type_name = items[i]['Rows']['Row'][j]['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['ColData'][1]['value']
            values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
            #print(seq," *****Success*****")
        except:
            #print(seq," FAIL")
            pass  
    df = pd.DataFrame(values, columns = headers)
    return df

if __name__ == "__main__":
   print("Executed as main")
else:
    print ("Profit Loss imported")
