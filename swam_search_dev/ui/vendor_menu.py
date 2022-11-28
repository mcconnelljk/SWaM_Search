from ui import main_menu
import logic
import data.queries as queries

def welcome():
    logic.globals.clear_console()
    heading = '\n Vendor Product Recommendations\n'
    instructions = '\n With this tool, *active* vendors can see recommendations of additional products to offer.\n'
    print(logic.globals.pixify(heading) + instructions)
    return

def select_report_option(conn, vendor_key):
    instructions = '\n Please select: \n'
    options = '\n [A] - Get product recommendations based on existing products\n [B] - Get product recommendations based on existing customers\n\n [C] - Back to Main Menu\n'
    print(instructions + options)
    selection = input('\n Selection: ')
    return selection

def get_vendor_orders(vendor_key, conn):
    query = get_vendor_products_and_customers(vendor_key)
    products_dict, customers_dict = get_products_customers_lists(conn, query)
    #if vendor has no orders, print, 'no orders'
    #option to return recommendations based on existing products or existing customers
    #select_report_option(conn, vendor_key)
    return

def vendor_key_menu(conn):
    instructions = '\n Please input your unique, all-numeric vendor key, or press <<Return>> to go back...\n'
    print(instructions)
    vendor_key = input('\n Vendor Key: ')
    if len(vendor_key) > 0:
        if vendor_key.isdigit() == False:
            logic.errors.invaid_entry()
            if_vendor(conn)
        else:
            return (vendor_key)
    else:
        logic.errors.invalid_entry()
        main_menu.print_main_menu(conn)

def if_vendor(conn):
    vendor_key = vendor_key_menu(conn)
    #query database to return lists of vendor's products and vendor's customers
    #validate vendor_key is in database
    get_vendor_orders(vendor_key, conn)
    return