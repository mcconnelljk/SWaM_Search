import ui
import logic
import features

def welcome(conn):
    logic.globals.clear_console()
    product_dict = features.get_data.get_products(conn)
    heading = '\n Buyer Menu\n'
    description = '\n With this tool, buyers can see (and filter) which registered vendors have a particular product\n'
    print(description)
    return

def print_product_menu():
    instructions = '\n Filter vendors by selecting an option: \n'
    options = '\n [A] - Vendor is a local business \n [B] - Vendor has set-aside(s) \n [C] - Both A and B \n [D] - None (i.e. print all vendors) \n\n [E] - Back \n'
    print(instructions + options)
    selection = input('\n Selection: ')
    return(selection)

def set_product_code():
    instructions = '\n To see available vendors, enter a 5-digit product code \n'
    product_code = input('\n NIGP Code: ')
    return(product_code)

def if_enter_product(conn):
    product_code = set_product_code() 
    #this is where I am...
    selection = print_product_menu().upper()
    if selection == 'A':
        print(selection)
    elif selection == 'B':
        print(selection)
    elif selection == 'C':
        print(selection)
    elif selection == 'D':
        print(selection)
    elif selection == 'E':
        if_buyer(conn)
    else:
        logic.errors.invalid_entry()
        if_enter_product(conn)
    return

def define_query():
    logic.globals.clear_console()
    heading = '\n Product Code Search\n'
    instructions = '\n Enter keyword phrase, or type \'B\' to go back'
    print(logic.globals.pixify(heading) + instructions)
    query = input('\n Search phrase: ')
    return (query)

def print_query_matches(conn, query):
    products_dict = features.get_data.get_products(conn)
    list_of_ranks = features.query_products.get_query_results(query, products_dict)
    if len(list_of_ranks) > 0:
        results_str = features.query_products.format_results(list_of_ranks, products_dict)
        heading = '\n RESULTS\n'
        print(logic.globals.pixify(heading))
        print(results_str + '\n')
        if_buyer(conn)
    else:
        message = '\n No results found :(\n'
        print(message)
        if_buyer(conn)
    return

def if_product_search(conn):
    query = define_query()
    if len(query) > 1:
        print_query_matches(conn, query)
        if_buyer(conn)
    else:
        logic.errors.invalid_entry()
        if_buyer(conn)
    return

def product_code_menu():
    instructions = '\n Please select: \n'
    options = '\n [A] - Enter product code (NIGP Code) \n [B] - Lookup product code \n\n [C] - Back to Main Menu \n'
    print(instructions + options)
    product_code = input('\n Selection: ')
    return product_code

def if_buyer(conn):
    product_code = product_code_menu().upper()
    if product_code == 'A':
        if_enter_product(conn)
    elif product_code == 'B':
        if_product_search(conn)
    elif product_code == 'C':
        ui.main_menu.print_main_menu(conn)
    else:
        logic.errors.invalid_entry()
        if_buyer()
    return