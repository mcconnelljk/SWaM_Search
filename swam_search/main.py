import ui
from data import connect

#

def main():
    conn = connect.get_connection()
    ui.menus.welcome(conn)
    ui.menus.print_main_menu(conn)
    return

if __name__ == "__main__":
    main()