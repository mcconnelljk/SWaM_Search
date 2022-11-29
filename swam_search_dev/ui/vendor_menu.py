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
    options = '\n [A] - Get product recommendations based on existing products\n [B] - Get product recommendations based on existing customers\n\n [C] - Back to Main Menu\n'
    print(logic.globals.pixify(instructions) + options)
    selection = input('\n Selection: ')
    #given selected option, run queries and print formatted results
    return selection

def report_option_menu(conn, products_df, vendor_key):
    selection = print_option_menu().upper()
    if selection == 'A':
        query = queries.get_associations_per_agency(nigp_key)
        report = features.get_data.get_vendors_report(conn, query)
        #format report
        print(report)
        report_option_menu(conn, products_df, vendor_key)
    elif selection == 'B':
        query = queries.get_vendor_products_and_customers(vendor_key)
        report = features.get_data.get_vendors_report(conn, query)
        #format report
        print(report)
        report_option_menu(conn, products_df, vendor_key)
    elif selection == 'C':
        del(product_code)
        main_menu.print_main_menu(conn, products_df)
    else:
        logic.errors.invalid_entry()
        report_option_menu(conn, products_df, vendor_key)
    return

#query database to return lists of vendor's products and vendor's customers
def get_vendor_orders(conn, products_df, vendor_key):
    products_dict, customers_dict = get_products_customers_lists(conn)
    if len(products_dict) == 0:
        #if vendor has no orders, print, 'no orders'
        msg= '\n No transactions found. Unable to recommend associated products...\n'
        print(msg)
        main_menu.print_main_menu(conn, products_df)
    else:
        report_option_menu(conn, products_df, vendor_key)
    return

def validate_vendor_key(conn, products_df, vendor_key):
    vendors_list = features.get_data.get_vendors_list(conn)
    is_valid = vendor_key in vendors_list
    del(vendors_list)
    if is_valid == True:
        if len(vendor_key) > 0:
            if vendor_key.isdigit() == False:
                logic.errors.invaid_entry()
                if_vendor(conn, products_df)
            else:
                return (vendor_key)
        else:
            main_menu.print_main_menu(conn, products_df)
    else:
        logic.errors.invalid_entry()
        vendor_key_menu(conn, products_df)

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