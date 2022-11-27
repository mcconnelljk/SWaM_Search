#!pip3 install psycopg2-binary
#!pip3 install nltk

import psycopg2
import nltk

#query the database and return a dictionary of key, value pairs
def get_products(conn):
    cursor = conn.cursor()
    my_query = "SELECT nigp_code, nigp_desc FROM raw_products"
    cursor.execute(my_query)
    rows = cursor.fetchall()
    products_dict = {}
    for r in rows:
        key = r[0]
        value = r[1]
        kv_pair = {key: value}
        products_dict.update(kv_pair)
    cursor.close()
    return(products_dict)

#products_dict = get_products(conn)