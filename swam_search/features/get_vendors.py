vendor_key = 'abc123'

def get_vendor_orders(conn, vendor_key):
    cursor = conn.cursor()
    my_query = "SELECT nigp_key, nigp_desc FROM raw_orders"
    cursor.execute(my_query)
    rows = cursor.fetchall()
    for r in rows:
        print (r)
    cursor.close()
    return(products_dict)



'''

#create client-side cursor
cursor = conn.cursor()

#query - get all products from raw_prodcuts table
my_query = "SELECT nigp_key, nigp_desc FROM raw_products LIMIT 10"

#execute the cursor
cursor.execute(my_query)

#fetch the query
rows = cursor.fetchall()
products_dict = {}
for r in rows:
    key = r[0]
    value = r[1]
    kv_pair = {key: value}
    products_dict.update(kv_pair)

products_list = list(products_dict.values())

#close the cursor
cursor.close()
'''