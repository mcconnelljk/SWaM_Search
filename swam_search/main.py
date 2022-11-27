from ui import main_menu
from data import connect

#

def main():
    conn = connect.get_connection()
    main_menu.welcome(conn)
    main_menu.print_main_menu(conn)
    return

if __name__ == "__main__":
    main()