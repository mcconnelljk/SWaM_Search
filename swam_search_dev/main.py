from ui import main_menu
from data import connect
from features.get_data import if_buyer

#

def main():
    conn = connect.get_connection()
    main_menu.welcome(conn)
    products_df = get_products_df(conn)
    main_menu.print_main_menu(conn, products_df)
    return

if __name__ == "__main__":
    main()