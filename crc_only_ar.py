# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:38:03 2021

@author: antoine.mack
"""

import pandas as pd

def add_one(number):
    return number + 1

def QBO_table_maker(inv,prod_serv):
    col_list = []
    for i in range(len(inv['Columns']['Column'])):
        col_list.append(inv['Columns']['Column'][i]['MetaData'][0]['Value'])
    
    df_list = []
    items = inv['Rows']['Row']
    for i in range(len(items)):
        tx_date = items[i]['ColData'][0]['value']
        txn_type = items[i]['ColData'][1]['value']
        doc_num = items[i]['ColData'][2]['value']
        name = items[i]['ColData'][3]['value']
        dept_name = items[i]['ColData'][4]['value']
        memo = items[i]['ColData'][5]['value']
        due_date = items[i]['ColData'][6]['value']
        subt_amount = items[i]['ColData'][7]['value']
        open_bal = items[i]['ColData'][8]['value']
        new_row = [tx_date,txn_type,doc_num, name, dept_name, memo, due_date, subt_amount, open_bal]
        df_list.append(new_row)
    inv_df = pd.DataFrame(df_list, columns=col_list)
    inv_df = inv_df.rename(columns={'tx_date':'Invoice_Date','subt_amount':'Invoice_Amount','open_bal':'Balance','name':'Customer_Name'})

    def Paid_col(invoice_amt, bal_amt):
        if invoice_amt != bal_amt:
            paid_status = 'Paid'
        else:
            paid_status = 'Unpaid'
        return paid_status
    inv_df.insert(8, 'Paid_Status', list(map(Paid_col,inv_df.Invoice_Amount,inv_df.Balance)))
    crc_filter = prod_serv['Prod/Service'].isin(['CRC ONC','CRC - Revenue - UE'])
    prod_serv = prod_serv[crc_filter]
    crc_df = prod_serv.merge(inv_df, left_on='Num',right_on='doc_num',)
    crc_df = crc_df[['Company_Name','Prod/Service','Invoice_Date','Invoice_Amount','Paid_Status','Balance','due_date']]
    return crc_df

if __name__ == "__main__":
   print("Executed as main")
else:
    print ("CRC ONLY AR imported")
    