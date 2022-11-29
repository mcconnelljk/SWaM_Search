from ui import main_menu
import data.queries as queries
import logic
import features

def welcome():
    logic.globals.clear_console()
    heading = '\n Vendor Product Recommendations\n'
    instructions = '\n With this tool, *active* vendors can see recommendations of additional products to offer.\n'
    print(logic.globals.pixify(heading) + instructions)
    return

#option to return recommendations based on existing products or existing customers
def print_option_menu():
    instructions = '\n Please select: \n'
    options = '\n [A] - Get product recommendations based on existing products\n [B] - Get product recommendations based on existing customers\n\n [C] - Back\n'
    print(logic.globals.pixify(instructions) + options)
    selection = input('\n Selection: ')
    #given selected option, run queries and print formatted results
    return selection

def report_option_menu(conn, products_df, vendor_key, products_dict, customers_dict):
    selection = print_option_menu().upper()    
    results = []
    if selection == 'A' or selection == 'B':
        products_list = list(products_dict.keys())
        for nigp_key in products_list:
            print(nigp_key)
            if selection == 'A':
                query = queries.get_associations_per_order(nigp_key)
                print(query)
                report_list = features.get_data.get_vendors_report(conn, query)
            elif selection == 'B':
                query = queries.get_associations_per_agency(nigp_key)
                report_list = features.get_data.get_vendors_report(conn, query)
            for row in report_list:
                results.append(row)
        del(report_list)    
        if len(results) > 0:
            results_sorted = sorted(results, key=lambda lift: lift[3])
            print(results[0:10])
            report_option_menu(conn, products_df, vendor_key, products_dict, customers_dict)    
        else:
            print('\n No recommendations found at this time :(')
            report_option_menu(conn, products_df, vendor_key, products_dict, customers_dict)
    elif selection == 'C':
        del(products_dict, customers_dict,vendor_key)
        main_menu.print_main_menu(conn, products_df)
    else:
        logic.errors.invalid_entry()
        report_option_menu(conn, products_df, vendor_key, products_dict, customers_dict)
    return

#query database to return lists of vendor's products and vendor's customers
def get_vendor_orders(conn, products_df, vendor_key):
    products_dict, customers_dict = features.get_data.get_products_customers_lists(conn, vendor_key)
    if len(products_dict) == 0:
        #if vendor has no orders, print, 'no orders'
        msg= '\n No transactions found. Unable to recommend associated products...\n'
        print(msg)
        main_menu.print_main_menu(conn, products_df)
    else:
        report_option_menu(conn, products_df, vendor_key, products_dict, customers_dict)
    return

def validate_vendor_key(conn, products_df, vendor_key):
    vendors_list = features.get_data.get_vendors_list(conn)
    is_valid = vendor_key in vendors_list
    del(vendors_list)
    if len(vendor_key) > 0:
        if is_valid == True:
            if vendor_key.isdigit() == False:
                logic.errors.invaid_entry()
                if_vendor(conn, products_df)
            else:
                return (vendor_key)
        else:
            logic.errors.invalid_entry()
            input_vendor_key(conn, products_df)
    else:
        main_menu.print_main_menu(conn, products_df)


def input_vendor_key(conn, products_df):
    instructions = '\n Please input your unique, all-numeric vendor key, or press <<Return>> to go back...\n'
    print(instructions)
    selection = input('\n Vendor Key: ')
    vendor_key = validate_vendor_key(conn, products_df, selection)
    return(vendor_key)

def if_vendor(conn, products_df):
    vendor_key = input_vendor_key(conn, products_df)
    get_vendor_orders(conn, products_df, vendor_key)
    return