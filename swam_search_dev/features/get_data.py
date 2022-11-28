#!pip3 install psycopg2-binary
#!pip3 install nltk

import data.queries as queries
import logic.globals as globals
import psycopg2
import nltk

#query the database and return a dictionary of key, value pairs
def get_products(conn):
    cursor = conn.cursor()
    query = queries.get_products_table()
    cursor.execute(query)
    rows = cursor.fetchall()
    products_dict = {}
    for r in rows:
        key = r[0]
        value = r[1]
        kv_pair = {key: value}
        products_dict.update(kv_pair)
    cursor.close()
    return(products_dict)

#query the database and print a list of vendors
def get_vendors_report(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for r in rows:
        print (r)
    cursor.close()
    return

#query the database and return a list of unique products and a list of unique customers
def get_products_customers_lists(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    products_dict = globals.return_dict(rows, 2, 3)
    customers_dict = globals.return_dict(rows, 4, 5)
    cursor.close()
    return(products_dict, customers_dict)