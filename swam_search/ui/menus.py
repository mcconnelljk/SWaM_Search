import logic
import features

def pixify(msg):
    pixie_dust = '\n ~ * ~ * ~ * ~ \n'
    message = pixie_dust + msg + pixie_dust
    return(message)

def welcome():
    logic.globals.clear_console()
    welcome_msg = '\n WELCOME TO SWAM SEARCH\n'
    return(print(pixify(welcome_msg)))

def goodbye():
    goodbye_msg = '\n GOODBYE!\n'
    return(exit(pixify(goodbye_msg)))

def main_menu():
    message = '\n Please select from the following menu options:\n'
    options = '\n [A] - I am a Vendor \n [B] - I am a Buyer\n\n [C] - Exit\n'
    print(message + options)
    selection = input('\n Selection: ')
    return(selection)

def print_main_menu():
    visitor_type = main_menu().upper()
    if visitor_type == 'A':
        if_vendor_menu()
    elif visitor_type == 'B':
        if_buyer_menu()
    elif visitor_type == 'C':
        goodbye()
    else:
        logic.errors.invalid_selection()
        print_main_menu()
    return

def vendor_menu():
    msg = '\n Enter your Vendor Key...\n'
    print(msg)
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
    message = '\n Please select: \n'
    options = '\n [A] - Enter product code (NIGP key) \n[B] - Lookup product code \n\n[C] - Back to Main Menu \n'
    print(message + options)
    product_code = input('\nSelection: ')
    return product_code

def if_buyer_menu():
    logic.globals.clear_console()
    description = '\n With this tool, buyers can see (and filter) which registered vendors have a particular product\n'
    print(description)
    #agency_key = buyer_menu()
    product_code = product_code_menu().upper()
    if product_code == 'A':
        print(pixify('\n That\'s cool, kid\n'))
    elif product_code == 'B':
        print(pixify('\n That\'s also cool, kid-a-roo\n'))
    elif product_code == 'C':
        main_menu()
    else:
        msg = '\n Invalid entry selected\n'
        print(pixify(msg))
        if_buyer_menu()
    return


