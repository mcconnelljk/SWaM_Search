from data import connect
import logic
import features

def pixify(heading):
    pixie_dust = '\n ~ * ~ * ~ * ~ \n'
    message = pixie_dust + heading.upper() + pixie_dust
    return(message)

def welcome(conn):
    logic.globals.clear_console()
    heading = '\n welcome to Swam Search\n'
    print(pixify(heading))
    connect.test_connection(conn)
    return

def goodbye(conn):
    logic.globals.clear_console()
    heading = '\n Goodbye!\n'
    print(pixify(heading))
    connect.close(conn)
    exit()

def main_menu():
    instructions = '\n Please select from the following menu options:\n'
    options = '\n [A] - I am a Vendor \n [B] - I am a Buyer\n\n [C] - Exit\n'
    print(instructions + options)
    selection = input('\n Selection: ')
    return(selection)

def print_main_menu(conn):
    visitor_type = main_menu().upper()
    if visitor_type == 'A':
        if_vendor_menu()
    elif visitor_type == 'B':
        if_buyer_menu(conn)
    elif visitor_type == 'C':
        goodbye(conn)
    else:
        logic.errors.invalid_entry()
        print_main_menu(conn)
    return

def vendor_menu():
    heading = '\n Vendor Menu\n'
    instructions = '\n Enter your Vendor Key...\n'
    print(pixify(heading) + instructions)
    agency_key = input('\n Vendor Key:')
    return

def if_vendor_menu():
    logic.globals.clear_console()
    description = '\n With this tool, SWaM-registered vendors can see recommendations for additional products to sell.\n'
    print(description)
    vendor_key = vendor_menu()
    return
 
''' 
def buyer_menu():
    msg = '\n Enter your Agency Key...\n'
    print(msg)
    agency_key = input('\n Agency Key:')
    return
'''

def product_code_menu():
    logic.globals.clear_console()
    instructions = '\n Please select: \n'
    options = '\n [A] - Enter product code (NIGP key) \n[B] - Lookup product code \n\n[C] - Back to Main Menu \n'
    print(instructions + options)
    product_code = input('\n Selection: ')
    return product_code

def collect_query(conn):
    query = input('\n Search phrase:')
    if query == "":
        logic.errors.invalid_entry()
        collect_query(conn)
    elif query == "B" or "b":
        if_buyer_menu(conn)
    else:
        return(query)

def no_results_found(conn):
    retry = input('\n Would you like to search again? [Y/N]')
    if retry == 'Y' or 'y':
        collect_query(conn)
    elif retry == 'N' or 'n':
        if_buyer_menu(conn)
    else:
        logic.errors.invalid_entry()
        no_results_found(conn)

def if_product_search(conn):
    logic.globals.clear_console()
    heading = '\n Product Code Search\n'
    instructions = '\n Enter keyword phrase, or type \'B\' to go back'
    print(pixify(heading) + instructions)
    query = collect_query(conn)
    products_dict = features.get_product(conn)
    list_of_ranks = get_query_results(query, products_dict)
    if len(list_of_ranks) > 0:
        results_str = format_results(list_of_ranks, products_dict)
        print(results_str)
        no_results_found(conn)
    else:
        message = '\n No results found :(\n'
        no_results_found(conn)
    return

def if_buyer_menu(conn):
    logic.globals.clear_console()
    product_dict = features.get_products(conn)
    heading = '\n Buyer Menu\n'
    description = '\n With this tool, buyers can see (and filter) which registered vendors have a particular product\n'
    print(description)
    #agency_key = buyer_menu()
    product_code = product_code_menu().upper()
    if product_code == 'A':
        print(pixify('\n That\'s cool, kid\n'))
    elif product_code == 'B':
        #building this now...
        if_product_search(conn)
    elif product_code == 'C':
        main_menu()
    else:
        msg = '\n Invalid entry selected\n'
        print(pixify(msg))
        if_buyer_menu()
    return