from ui import main_menu
from data import connect
import features.get_data as data

def main():
    conn = connect.get_connection()
    main_menu.welcome(conn)
    products_df = data.get_products_df(conn)
    main_menu.print_main_menu(conn, products_df)
    return

if __name__ == "__main__":
    main()