#!pip3 install psycopg2-binary
#!pip3 install nltk

import data.queries as queries
import logic.globals as globals
import pandas as pd
import psycopg2
import nltk

#query the database and return a dataframe of key, value pairs
def get_products_df(conn):
    print('\n Loading data...\n')
    query = queries.get_products_table()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    my_df = pd.DataFrame(columns = ['NIGP_KEY', 'NIGP_CODE', 'NIGP_DESC'])
    for r in rows:      
        nigp_key = r[0]
        nigp_code = r[1]
        nigp_desc = r[2]
        temp_list = [nigp_key, nigp_code, nigp_desc]
        my_df.loc[len(my_df)] = temp_list
    print('\n ...Data loaded!\n\n')
    cursor.close()
    return(my_df)

#query the database and print results to console
def get_vendors_report(conn, query):
    print('\n Query running...\n\n')
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    rows_list = []
    for r in rows:
        rows_list.append(r[0])
    cursor.close()
    return (rows_list)

#query the database and return a list of unique products and a list of unique customers
def get_products_customers_lists(conn, vendor_key):
    query = queries.get_vendor_products_and_customers(vendor_key)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    products_dict = globals.return_dict(rows, 2, 3)
    customers_dict = globals.return_dict(rows, 4, 5)
    cursor.close()
    return(products_dict, customers_dict)

def get_vendors_list(conn):
    query = queries.get_vendors_table()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    vendors_list = []
    for r in rows:
        vendors_list.append(r[0])
    cursor.close()
    return(vendors_list)