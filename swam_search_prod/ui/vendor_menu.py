from ui import main_menu
import logic

def welcome():
    logic.globals.clear_console()
    heading = '\n Vendor Menu\n'
    instructions = '\n Enter your Vendor Key...\n'
    print(logic.globals.pixify(heading) + instructions)
    return

def if_vendor(conn):
    agency_key = input('\n Vendor Key:')
    if len(agency_key) > 0:
        print(agency_key)
    else:
        logic.errors.invalid_entry()
        main_menu.print_main_menu(conn)
    return