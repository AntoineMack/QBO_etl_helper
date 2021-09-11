# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 08:54:53 2021

@author: antoine.mack
"""

import pandas as pd, numpy as np
#bud is 2021_Budget_transform

def add_one(number):
    return number + 1

def QBO_table_maker(bud, pnl):
    pnl.amount = [float(i) for i in pnl.amount]
    #drop unwanted columns from pnl
    pnl.drop(columns= [ 'num', 'name','desc', 'split','trans_type'], inplace=True)
    #restructure pnl dates to match budget
    for i in range(len(pnl.date)):
        new_date = pnl.iloc[i,6][5:7]+"/"+ '1'+"/"+ pnl.iloc[i,6][:4]
        if new_date[0]=='0':
            pnl.iloc[i,6] = new_date[1:]
        
    pnl.replace(' ',np.nan,inplace= True)
    val_list = []
    for i in range(len(bud)):
        sub1 = bud[i:i+1].subcategory_name[i]
        type1 = bud[i:i+1].type_name[i]
        group1 = bud[i:i+1].group_name[i]
        div1 = bud[i:i+1].div_name[i]
        lev1 = bud[i:i+1].level6[i]
        date1 = bud[i:i+1].date[i]
        if type(group1) != str and type(div1) != str and type(lev1) != str:
            new_amount = pnl[(pnl.type_name==type1)&(pnl.date==date1)].amount.sum()
            val_list.append([sub1,type1,group1,div1,lev1,date1,new_amount])
            pass
        elif type(div1) != str and type(lev1) != str:
            new_amount = pnl[(pnl.type_name==type1)&(pnl.group_name==group1)&(pnl.date==date1)].amount.sum()
            val_list.append([sub1,type1,group1,div1,lev1,date1,new_amount])
            pass
        elif type(lev1) != str:
            new_amount = pnl[(pnl.type_name==type1)&(pnl.group_name==group1)&
                             (pnl.div_name==div1)&(pnl.date==date1)].amount.sum()
            val_list.append([sub1,type1,group1,div1,lev1,date1,new_amount])
            pass
        else:
            new_amount = pnl[(pnl.type_name==type1)&(pnl.group_name==group1)&
                             (pnl.div_name==div1)&(pnl.level6==lev1)&(pnl.date==date1)].amount.sum()
            val_list.append([sub1,type1,group1,div1,lev1,date1,new_amount])
            pass
    df = pd.DataFrame(val_list, columns  =['subcategory_name', 'type_name',
                                               'group_name','div_name','level6','date','pnl_amount'])                                  
    #add budget amounts to new df
    df['budget_amount'] = bud.bud_amount
    
    missing_cons = pnl[(pnl.group_name !='4001.9 Client Resource Center') & (pnl.group_name !='4011 Vendor') &
        (pnl.group_name !='4001 Consulting') & (pnl.group_name !='4009 Coding Plus') &
        (pnl.group_name !='4008 eConsulting') &(pnl.type_name.isin(['4000 CONSULTING REVENUE']))]

    missing_cons.drop(columns=['CLASS','category_name'],inplace = True)
    missing_cons.rename(columns= {'amount':'pnl_amount'}, inplace=True)
    missing_cons.insert(7,"budget_amount",0,True)
    
    #Missing consulting DF
    values = []
    for i in missing_cons.group_name.unique():
        for j in missing_cons.date.unique():
            sub1 = "Income"
            type1 = '4000 CONSULTING REVENUE'
            group1 = i
            div1 = np.nan
            lev1 = np.nan
            date1 = j
            pnl1 = missing_cons[(missing_cons.group_name==i) &(missing_cons.date == j)].pnl_amount.sum()
            bud1 = 0
            values.append([sub1,type1,group1,div1,lev1,date1,pnl1,bud1])
    missing_con_df = pd.DataFrame(values,columns=missing_cons.columns)
    
    # Missing Shipping values
    missing_ship = pnl[pnl.type_name.isin(['4500 Postage, Shipping, & Handling'])]
    missing_ship.drop(columns=['CLASS','category_name'],inplace = True)
    missing_ship.rename(columns= {'amount':'pnl_amount'}, inplace=True)
    missing_ship.insert(7,"budget_amount",0,True)
    
    #missing Shipping DF
    values2 = []
    for j in missing_ship.date.unique():
        sub1 = "Income"
        type1 = '4500 Postage, Shipping, & Handling'
        group1 = np.nan
        div1 = np.nan
        lev1 = np.nan
        date1 = j
        pnl1 = missing_ship[missing_ship.date == j].pnl_amount.sum()
        bud1 = 0
        values2.append([sub1,type1,group1,div1,lev1,date1,pnl1,bud1])
    missing_ship_df = pd.DataFrame(values2,columns=missing_ship.columns)
    
    #append new dfs
    df = df.append(missing_con_df, ignore_index =True)
    df = df.append(missing_ship_df, ignore_index =True)    
    return df

if __name__ == "__main__":
   print("Executed as main")
else:
    print ("Budget Vs Actuals imported")