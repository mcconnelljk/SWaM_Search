import ui
import logic
import features

def welcome(conn):
    logic.globals.clear_console()
    product_dict = features.get_data.get_products(conn)
    heading = '\n Buyer Menu\n'
    description = '\n With this tool, buyers can see (and filter) which registered vendors have a particular product.\n'
    print(description)
    return

def print_product_menu():
    instructions = '\n Filter vendors by selecting an option: \n'
    options = '\n [A] - Vendor is a local business \n [B] - Vendor has set-aside(s) \n [C] - Both A and B \n [D] - None (i.e. print all vendors) \n\n [E] - Back \n'
    print(instructions + options)
    selection = input('\n Selection: ')
    return(selection)

def print_states_menu(conn, selection, product_code):
    instructions = '\n Filter vendors by entering a 2-letter state abbreviation: \n'
    state_input = input('\n State Abbrev: ')
    if len(state_input) == 2:
        states = globals.load_states()
        if state_input in states:
            return (state_input)
        else:
            logic.errors.invalid_entry()
            if_local_filter(conn, selection, product_code)
            return
    
def if_local_filter(conn, selection, product_code):
    state_abbr = print_states_menu(conn, selection, product_code)
    if selection == 'A':
        query = data.queries.vendors_are_local(product_code, state_abbr)
        report = features.get_data.get_vendors_report(conn, query)
        #format report
        print(report)
        if_buyer(conn)
    elif selection == 'C':
        query = data.queries.vendors_local_and_set_aside(product_code, state_abbr)
        report = features.get_data.get_vendors_report(conn, query)
        #format report
        print(report)
        if_buyer(conn)
    return

def if_enter_product(conn, product_code):
    selection = print_product_menu().upper()
    if selection == 'A' or selection == 'C':
        if_local_filter(conn, selection, product_code)
    elif selection == 'B':
        query = data.queries.vendors_have_set_asides(product_code)
        report = features.get_data.get_vendors_report(conn, query)
        #format report
        print(report)
        if_buyer(conn)
    elif selection == 'D':
        query = data.queries.all_vendors(product_code)
        report = features.get_data.get_vendors_report(conn, query)
        #format report
        print(report)
        if_buyer(conn)
    elif selection == 'E':
        if_buyer(conn)
    else:
        logic.errors.invalid_entry()
        if_enter_product(conn)
    return

def set_product_code():
    instructions = '\n To see available vendors, enter a 5-digit product code \n'
    product_code = input('\n NIGP Code: ')
    return(product_code)

def define_query():
    logic.globals.clear_console()
    heading = '\n Product Code Search\n'
    instructions = '\n Enter keyword phrase, or press <<Return>> to go back'
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
    if len(query) > 2:
        print_query_matches(conn, query)
        if_buyer(conn)
    elif len(query) == 0:
        if_buyer(conn)
    else:
        logic.errors.invalid_entry()
        if_buyer(conn)
    return

def product_code_menu():
    instructions = '\n Please select: \n'
    options = '\n [A] - Enter product code (NIGP Code)\n [B] - Lookup product code\n\n [C] - Back to Main Menu\n'
    print(instructions + options)
    product_code = input('\n Selection: ')
    return product_code

def if_buyer(conn):
    product_code = product_code_menu().upper()
    if product_code == 'A':
        product_code = set_product_code()
        if_enter_product(conn, product_code)
    elif product_code == 'B':
        if_product_search(conn)
    elif product_code == 'C':
        ui.main_menu.print_main_menu(conn)
    else:
        logic.errors.invalid_entry()
        if_buyer()
    return