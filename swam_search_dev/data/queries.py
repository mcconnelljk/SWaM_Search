def get_vendor_products_and_customers(vendor_key):
    query = '''    
        SELECT DISTINCT
            orders.vendor_key
            ,vendors.vendor_name
            ,products.nigp_code
            ,products.nigp_desc
            ,orders.agency_key
            ,agencies.entity_description
        FROM raw_orders AS orders
        INNER JOIN raw_vendors AS vendors ON orders.vendor_key = vendors.vendor_key
        INNER JOIN raw_products AS products ON orders.nigp_key = products.nigp_key
        INNER JOIN raw_agencies AS agencies ON orders.agency_key = agencies.agency_key
        WHERE orders.vendor_key = '{}'
        ORDER BY vendor_name asc
        ;'''.format(vendor_key)
    return (query)


def get_products_table():
    query = "SELECT nigp_code, nigp_desc FROM raw_products;"
    return(query)


def vendors_are_local(product_code, state_abbr):
    query = '''    
        SELECT
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
        INNER JOIN raw_products AS products ON orders.nigp_key = products.nigp_key
        WHERE products.nigp_code = '{}'
        AND address.vendor_state = '{}'
        group by orders.vendor_key, vendors.vendor_name, address.vendor_city, address.vendor_state
        ORDER BY vendor_name asc
        ;'''.format(product_code, state_abbr)
    return (query)


def vendors_have_set_asides(product_code):
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
        INNER JOIN raw_products AS products ON orders.nigp_key = products.nigp_key
        WHERE products.nigp_code = '{}'
        group by orders.vendor_key, vendors.vendor_name, address.vendor_city, address.vendor_state
        ORDER BY vendor_name asc
        ;'''.format(product_code)
    return (query)


def vendors_local_and_set_aside(product_code, state_abbr):
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
        INNER JOIN raw_products AS products ON orders.nigp_key = products.nigp_key
        WHERE products.nigp_code = '{}'
        AND address.vendor_state = '{}'
        group by orders.vendor_key, vendors.vendor_name, address.vendor_city, address.vendor_state
        ORDER BY vendor_name asc
        ;'''.format(product_code, state_abbr)
    return (query)


def all_vendors(product_code):
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
        INNER JOIN raw_products AS products ON orders.nigp_key = products.nigp_key
        WHERE products.nigp_code = '{}'
        group by orders.vendor_key, vendors.vendor_name, address.vendor_city, address.vendor_state
        ORDER BY vendor_name asc
        ;'''.format(product_code)
    return (query)