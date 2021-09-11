# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:04:51 2021

@author: antoine.mack
"""

import pandas as pd

def add_one(number):
    return number + 1

def Customer_df_maker(cust1,cust2,cust3,cust4,cust5):
    cust_list = []
    fail_list = []
    pages = [cust1,cust2,cust3,cust4,cust5]
    for n in pages:
        cust_info = n['QueryResponse']['Customer']
        for i in range(len(cust_info)):
            try:
                #print(cust_info[i]['DisplayName'],cust_info[i]['BillAddr']['City'],cust_info[i]['BillAddr']['CountrySubDivisionCode'],cust_info[i]['BillAddr']['PostalCode'])
                info = [cust_info[i]['DisplayName'],cust_info[i]['BillAddr']['City'],cust_info[i]['BillAddr']['CountrySubDivisionCode'],cust_info[i]['BillAddr']['PostalCode']]
                cust_list.append(info)
            except:
                try:
                    #print(cust_info[i]['CompanyName'],cust_info[i]['BillAddr']['City'],cust_info[i]['BillAddr']['CountrySubDivisionCode'],cust_info[i]['BillAddr']['PostalCode'])
                    info = [cust_info[i]['CompanyName'],cust_info[i]['BillAddr']['City'],cust_info[i]['BillAddr']['CountrySubDivisionCode'],cust_info[i]['BillAddr']['PostalCode']]
                    cust_list.append(info)
                except:
                    try:
                        #print(cust_info[i]['DisplayName'],cust_info[i]['BillAddr']['CountrySubDivisionCode'],cust_info[i]['BillAddr']['PostalCode'])
                        info = [cust_info[i]['DisplayName'],"",cust_info[i]['BillAddr']['CountrySubDivisionCode'],cust_info[i]['BillAddr']['PostalCode']]
                        cust_list.append(info)
                    except:
                        #print(i,"*************Failed",cust_info[i]['DisplayName'],"","","")
                        info= [cust_info[i]['DisplayName'],"","",""]
                        cust_list.append(info)
                        fail_list.append(i)
                        pass
    df_cust = pd.DataFrame(cust_list,columns=["Name","City","State","Zipcode"])
    df_cust.Name= [i.replace('.','') for i in df_cust.Name]
    return df_cust

def Sales_Detail_df_maker(sales_det):
    sale_items = list(sales_det.values())[2]['Row']
    value_list = []
    
    for i in range(len(sale_items)-1):
        comp_name = sale_items[i]["Header"]["ColData"][0]['value']
        account = sale_items[i]['Rows']['Row']
        #print(i, comp_name)
        try:
            for j in range(len(account)):
                date = sale_items[i]['Rows']['Row'][j]['ColData'][0]['value']
                trans_type = sale_items[i]['Rows']['Row'][j]['ColData'][1]['value']
                num = sale_items[i]['Rows']['Row'][j]['ColData'][2]['value']
                prod_serv = sale_items[i]['Rows']['Row'][j]['ColData'][3]['value']
                desc = sale_items[i]['Rows']['Row'][j]['ColData'][4]['value']
                qty = sale_items[i]['Rows']['Row'][j]['ColData'][5]['value']
                price = sale_items[i]['Rows']['Row'][j]['ColData'][6]['value']
                amount = sale_items[i]['Rows']['Row'][j]['ColData'][7]['value']
                value_list.append([comp_name,'',date,trans_type,num,prod_serv,desc,qty,price,amount])
        except:
            #print(i,comp_name,'******Failed')
            try:
                for j in range(len(account)):
                    buy_name = sale_items[i]['Rows']['Row'][j]["Header"]["ColData"][0]['value']
                    buy_items = sale_items[i]['Rows']['Row'][j]['Rows']['Row']
                    #print('got account')
                    for k in range(len(buy_items)):
                        date = buy_items[k]['ColData'][0]['value']
                        trans_type = buy_items[k]['ColData'][1]['value']
                        num = buy_items[k]['ColData'][2]['value']
                        prod_serv = buy_items[k]['ColData'][3]['value']
                        desc = buy_items[k]['ColData'][4]['value']
                        qty = buy_items[k]['ColData'][5]['value']
                        price = buy_items[k]['ColData'][6]['value']
                        amount = buy_items[k]['ColData'][7]['value']
                        value_list.append([comp_name,buy_name,date,trans_type,num,prod_serv,desc,qty,price,amount])
            except:
                #print(comp_name, '******Failed AGAIN')
                pass
            pass
    
    
    sale_df = pd.DataFrame(value_list, columns=['Company_Name','Buyer_Name','Date','Trans_Type','Num','Prod/Service','Desc','Qty','Price','Amount'])
    sale_df.Company_Name = [i.replace('.','') for i in sale_df.Company_Name]
    comp_list_names = list(set(list(sale_df.Company_Name)))
    return sale_df, comp_list_names

def Merge_tables(df_cust,sale_df, comp_list_names,):
    df_cust_filtered = df_cust[df_cust['Name'].isin(comp_list_names)]
    final_map_df = sale_df.merge(df_cust_filtered, left_on = 'Company_Name', right_on='Name')
    return final_map_df

if __name__ == "__main__":
   print("Executed as main")
else:
    print ("Sales Tracker imported")