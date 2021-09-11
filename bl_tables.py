# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:08:51 2021

@author: antoine.mack
"""
import pandas as pd
from itertools import combinations

bl_vault = {'six':[],'five':[],'four':[],'three':[],'two':[]}

def add_one(number):
    return number + 1

def QBO_table_maker(qb_obj):
    headers = ["Category", "Sub Category", "Class", "Group", "Type",'Amount']
    values = []
    items = list(qb_obj.values())[2]['Row']
    combo6 = combinations([0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10],6)
    for seq in set(combo6):
        (i,j,k,L,m,n) = seq
        #Header values
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            group_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value']
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Header']['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Header']['ColData'][1]['value']
            if value != '':
                values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
                bl_vault['six'].append(seq)
        except:
            #print(seq," FAIL")
            pass
        
        #Category,Subcategory, Class, Group, Type
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            group_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value']
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['ColData'][1]['value']
            values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
            #print(seq," *****Success*****")
            bl_vault['six'].append(seq)
        except:
            #print(seq," FAIL")
            pass
    combo5 = combinations([0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10],5)
    for seq in set(combo5):
        (i,j,k,L,m) = seq
        #Header values
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            group_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value']
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][1]['value']
            if value != '':
                values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
                #print(seq," *****Success*****")
                bl_vault['five'].append(seq)
        except:
            #print(seq," FAIL")
            pass
        
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
            bl_vault['five'].append(seq)
        except:
            #print(seq," FAIL")
            pass
        
    combo4 = combinations([0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10,
                           0,1,2,3,4,5,6,7,8,9,10],4)
    for seq in set(combo4):
        (i,j,k,L) = seq
        #Header values 
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            group_name = ''
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][1]['value']
            if value != '':
                values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
                #print(seq," *****Success*****")
                bl_vault['four'].append(seq)
        except:
            #print(seq," FAIL")
            pass
        
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
            bl_vault['four'].append(seq)
        except:
            #print(seq," FAIL")
            pass
    combo3 = combinations([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                           0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                           0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],3)
    for seq in set(combo3):
        (i,j,k) = seq
        #Header values
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = ''
            group_name = ''
            type_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Header']['ColData'][1]['value']
            if value != '':
                values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
                #print(seq," *****Success*****")
                bl_vault['three'].append(seq)
        except:
            #print(seq," FAIL")
            pass
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
            bl_vault['three'].append(seq)
        except:
            #print(seq," FAIL")
            pass
    combo2 = combinations([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                           0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],2)
    for seq in set(combo2):
        (i,j) = seq
        #Header values
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = ''
            class_name = ''
            group_name = ''
            type_name = items[i]['Header']['ColData'][0]['value']
            value = items[i]['Header']['ColData'][1]['value']
            if value != '':
                values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
                #print(seq," *****Success*****")
                bl_vault['two'].append(seq)
        except:
            pass        
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
            bl_vault['two'].append(seq)
        except:
            #print(seq," FAIL")
            pass  
    df = pd.DataFrame(values, columns = headers)
    return df

#use with stored coordinates
def QBO_table_maker2(qb_obj,combo6, combo5,combo4,combo3,combo2):
    headers = ["Category", "Sub Category", "Class", "Group", "Type",'Amount']
    values = []
    items = list(qb_obj.values())[2]['Row']
    
    for seq in set(combo6):
        (i,j,k,L,m,n) = seq
        #Header values
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            group_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value']
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Header']['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Header']['ColData'][1]['value']
            if value != '':
                values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
                #print(seq," *****Success*****")
        except:
            #print(seq," FAIL")
            pass
        
        #Category,Subcategory, Class, Group, Type
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            group_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value']
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Rows']['Row'][m]['Rows']['Row'][n]['ColData'][1]['value']
            values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
            #print(seq," *****Success*****")
        except:
            #print(seq," FAIL")
            pass
    
    for seq in set(combo5):
        (i,j,k,L,m) = seq
        #Header values
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            group_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value']
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Rows']['Row'][L]['Header']['ColData'][1]['value']
            if value != '':
                values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
                #print(seq," *****Success*****")
        except:
            #print(seq," FAIL")
            pass
        
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
        
    for seq in set(combo4):
        (i,j,k,L) = seq
        #Header values 
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            group_name = ''
            type_name = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Rows']['Row'][k]['Header']['ColData'][1]['value']
            if value != '':
                values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
                #print(seq," *****Success*****"
        except:
            #print(seq," FAIL")
            pass
        
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
    
    for seq in set(combo3):
        (i,j,k) = seq
        #Header values
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            class_name = ''
            group_name = ''
            type_name = items[i]['Rows']['Row'][j]['Header']['ColData'][0]['value']
            value = items[i]['Rows']['Row'][j]['Header']['ColData'][1]['value']
            if value != '':
                values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
                #print(seq," *****Success*****")
        except:
            #print(seq," FAIL")
            pass
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
    
    for seq in set(combo2):
        (i,j) = seq
        #Header values
        try:
            category_name = items[i]['Header']['ColData'][0]['value']
            subcategory_name = ''
            class_name = ''
            group_name = ''
            type_name = items[i]['Header']['ColData'][0]['value']
            value = items[i]['Header']['ColData'][1]['value']
            if value != '':
                values.append([category_name, subcategory_name, class_name, group_name, type_name, value])
                #print(seq," *****Success*****")
        except:
            pass        
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
            bl_vault['two'].append(seq)
        except:
            #print(seq," FAIL")
            pass
    df = pd.DataFrame(values, columns = headers)
    return df

if __name__ == "__main__":
   print("Executed as main")
else:
    print ("Balance Sheet imported")