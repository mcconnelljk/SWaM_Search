def get_products_table():
    query = "SELECT nigp_key, nigp_code, nigp_desc FROM raw_products;"
    return(query)


def get_vendors_table():
    query = "SELECT vendor_key FROM raw_vendors;"
    return(query)


def get_associations_per_order(nigp_key):
    nigp_key = '[' + str(nigp_key) + ']'
    query = '''
        SELECT antecedents, consequents, confidence, lift
        FROM apriori_products_per_order AS apriori
        WHERE apriori.antecedents LIKE '{}'
        AND confidence >= 0.75
        ORDER BY confidence DESC, lift DESC
        LIMIT 15
        ;'''.format(nigp_key)
    return(query)


def get_associations_per_agency(nigp_key):
    nigp_key = '[' + str(nigp_key) + ']'
    query = '''
        SELECT antecedents, consequents, confidence, lift
        FROM apriori_products_per_agency AS apriori
        WHERE apriori.antecedents LIKE '{}'
        AND confidence >= 0.75
        ORDER BY confidence DESC, lift DESC
        LIMIT 15
        ;'''.format(nigp_key)
    return(query)


def get_vendor_products(vendor_key):
    query = '''    
        SELECT DISTINCT
            orders.vendor_key
            ,vendors.vendor_name
            ,products.nigp_key
            ,products.nigp_desc
        FROM raw_orders AS orders
        INNER JOIN raw_vendors AS vendors ON orders.vendor_key = vendors.vendor_key
        INNER JOIN raw_products AS products ON orders.nigp_key = products.nigp_key
        WHERE orders.vendor_key = '{}'
        ORDER BY vendor_name asc
        ;'''.format(vendor_key)
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


def vendors_no_filter(product_code):
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