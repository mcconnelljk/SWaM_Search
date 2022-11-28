product_key = 'abc123'

def has_set_aside(product_key):
    query = '''    
        SELECT DISTINCT 
            orders.vendor_key
            ,vendors.vendor_name AS vendor_name
            ,concat(address.vendor_city, ', ', address.vendor_state) AS location
            ,(
                SELECT COUNT(set_aside.swam_cert) as cert_count
                FROM raw_vendor_has_certs AS set_aside 
                WHERE set_aside.vendor_key = orders.vendor_key
                group by set_aside.vendor_key
                ) 
                AS count_certs
        FROM raw_orders AS orders 
        INNER JOIN raw_vendors AS vendors ON orders.vendor_key = vendors.vendor_key
        INNER JOIN raw_vendor_has_address AS address ON orders.vendor_key = address.vendor_key
        INNER JOIN raw_vendor_has_certs AS set_aside ON orders.vendor_key = set_aside.vendor_key
        WHERE nigp_key = '1'
        group by orders.vendor_key, vendors.vendor_name, address.vendor_city, address.vendor_state
        ORDER BY vendor_name asc
        ;'''.format(str(product_key))
    return (query)


def if_is_local(product_key, state_abbr):
    query = '''    
        SELECT DISTINCT 
            orders.vendor_key
            ,vendors.vendor_name AS vendor_name
            ,concat(address.vendor_city, ', ', address.vendor_state) AS location
            ,(
                SELECT COUNT(set_aside.swam_cert) as cert_count
                FROM raw_vendor_has_certs AS set_aside 
                WHERE set_aside.vendor_key = orders.vendor_key
                group by set_aside.vendor_key
                ) 
                AS count_certs
        FROM raw_orders AS orders 
        INNER JOIN raw_vendors AS vendors ON orders.vendor_key = vendors.vendor_key
        INNER JOIN raw_vendor_has_address AS address ON orders.vendor_key = address.vendor_key
        INNER JOIN raw_vendor_has_certs AS set_aside ON orders.vendor_key = set_aside.vendor_key
        WHERE nigp_key = {}
        AND WHERE address.vendor_state = {}
        group by orders.vendor_key, vendors.vendor_name, address.vendor_city, address.vendor_state
        ORDER BY vendor_name asc
        ;'''.format(str(product_key), state_abbr)
    return (query)


def if_no_filter(product_key):
    query = '''    
        SELECT DISTINCT 
        orders.vendor_key
        ,vendors.vendor_name AS vendor_name
        ,concat(address.vendor_city, ', ', address.vendor_state) AS location
        ,(
            SELECT COUNT(set_aside.swam_cert) as cert_count
            FROM raw_vendor_has_certs AS set_aside 
            WHERE set_aside.vendor_key = orders.vendor_key
            group by set_aside.vendor_key
            ) 
            AS count_certs
        FROM raw_orders AS orders 
        INNER JOIN raw_vendors AS vendors ON orders.vendor_key = vendors.vendor_key
        INNER JOIN raw_vendor_has_address AS address ON orders.vendor_key = address.vendor_key
        LEFT JOIN raw_vendor_has_certs AS set_aside ON orders.vendor_key = set_aside.vendor_key
        WHERE nigp_key = {}
        group by orders.vendor_key, vendors.vendor_name, address.vendor_city, address.vendor_state
        ORDER BY vendor_name asc
        ;'''.format(str(product_key))
    return (query)

def get_vendors_report(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for r in rows:
        print (r)
    cursor.close()
    return(products_dict)