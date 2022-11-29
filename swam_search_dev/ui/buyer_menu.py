from ui import main_menu
import data.queries as queries
import logic
import features

def welcome(conn):
    logic.globals.clear_console()
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

def print_states_menu(conn, selection, product_code, products_df):
    instructions = '\n Filter vendors by entering a 2-letter state abbreviation: \n'
    state_input = input('\n State Abbrev: ').upper()
    if len(state_input) == 2:
        states = logic.globals.load_states()
        if state_input in states:
            return (state_input)
        else:
            logic.errors.invalid_entry()
            if_local_filter(conn, selection, product_code, products_df)
            return
    
def if_local_filter(conn, selection, product_code, products_df):
    state_abbr = print_states_menu(conn, selection, product_code, products_df)
    if selection == 'A':
        query = queries.vendors_are_local(product_code, state_abbr)
        report_list = features.get_data.get_vendors_report(conn, query)
        #format report
        print(report_list)
        del(state_abbr)
        if_enter_product(conn, product_code, products_df)
    elif selection == 'C':
        query = queries.vendors_local_and_set_aside(product_code, state_abbr)
        report_list = features.get_data.get_vendors_report(conn, query)
        #format report
        print(report_list)
        del(state_abbr)
        if_enter_product(conn, product_code, products_df)
    return

def if_enter_product(conn, product_code, products_df):
    selection = print_product_menu().upper()
    if selection == 'A' or selection == 'C':
        if_local_filter(conn, selection, product_code, products_df)
    elif selection == 'B':
        query = queries.vendors_have_set_asides(product_code)
        report_list = features.get_data.get_vendors_report(conn, query)
        #format report
        print(report_list)
        if_enter_product(conn, product_code, products_df)
    elif selection == 'D':
        query = queries.vendors_no_filter(product_code)
        report_list = features.get_data.get_vendors_report(conn, query)
        #format report
        print(report_list)
        if_enter_product(conn, product_code, products_df)
    elif selection == 'E':
        del(product_code)
        if_buyer(conn, products_df)
    else:
        logic.errors.invalid_entry()
        if_enter_product(conn, product_code, products_df)
    return

def set_product_code(conn, products_df):
    product_code_list = list(products_df['NIGP_CODE'])
    instructions = '\n To see available vendors, enter a product code \n'
    product_code = input('\n NIGP Code: ')
    if len(product_code) > 0:
        if product_code.isdigit() == True:
            is_valid = product_code in product_code_list
            del(product_code_list)
            if is_valid:
                return(product_code)
        else:
            logic.errors.invalid_entry()
            set_product_code(conn, products_df)
    else:
        if_buyer(conn, products_df)

def define_query():
    logic.globals.clear_console()
    heading = '\n Product Code Search\n'
    instructions = '\n Enter keyword phrase, or press <<Return>> to go back'
    print(logic.globals.pixify(heading) + instructions)
    query = input('\n Search phrase: ')
    return (query)

def print_query_matches(conn, query, products_df):
    products_dict = dict(zip(products_df.NIGP_CODE, products_df.NIGP_DESC))
    list_of_ranks = features.query_products.get_query_results(query, products_dict)
    if len(list_of_ranks) > 0:
        results_str = features.query_products.format_results(list_of_ranks, products_dict)
        heading = '\n RESULTS\n'
        print(logic.globals.pixify(heading))
        print(results_str + '\n')
        if_buyer(conn, products_df)
    else:
        message = '\n No results found :(\n'
        print(message)
        if_buyer(conn, products_df)
    return

def if_product_search(conn, products_df):
    query = define_query()
    if len(query) > 2:
        print_query_matches(conn, query, products_df)
        if_buyer(conn, products_df)
    elif len(query) == 0:
        if_buyer(conn, products_df)
    else:
        logic.errors.invalid_entry()
        if_buyer(conn, products_df)
    return

def product_code_menu():
    instructions = '\n Please select: \n'
    options = '\n [A] - Enter product code (NIGP Code)\n [B] - Lookup product code\n\n [C] - Back to Main Menu\n'
    print(instructions + options)
    product_code = input('\n Selection: ')
    return product_code

def if_buyer(conn, products_df):
    selection = product_code_menu().upper()
    if selection == 'A':
        product_code = set_product_code(conn, products_df)
        if_enter_product(conn, product_code, products_df)
    elif selection == 'B':
        if_product_search(conn, products_df)
    elif selection == 'C':
        main_menu.print_main_menu(conn, products_df)
    else:
        logic.errors.invalid_entry()
        if_buyer(conn, products_df)
    return