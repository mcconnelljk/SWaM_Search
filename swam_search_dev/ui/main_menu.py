import ui
import logic
from data import connect


def welcome(conn):
    heading = '\n Welcome to Swam Search\n'
    print(logic.globals.pixify(heading))
    connect.test_connection(conn)
    return

def goodbye(conn):
    heading = '\n Goodbye!\n'
    print(logic.globals.pixify(heading))
    connect.close(conn)
    exit()

def main_menu():
    instructions = '\n Please select from the following menu options:\n'
    options = '\n [A] - I am a Vendor \n [B] - I am a Buyer\n\n [C] - Exit\n'
    print(instructions + options)
    selection = input('\n Selection: ')
    return(selection)

def print_main_menu(conn, products_df):
    visitor_type = main_menu().upper()
    if visitor_type == 'A':
        ui.vendor_menu.welcome()
        ui.vendor_menu.if_vendor(conn, products_df)
    elif visitor_type == 'B':
        ui.buyer_menu.welcome()
        ui.buyer_menu.if_buyer(conn, products_df)
    elif visitor_type == 'C':
        goodbye(conn)
    else:
        logic.errors.invalid_entry()
        print_main_menu(conn, products_df)
    return