import pandas as pd
import time
from ui import main_menu
import data.queries as queries
import logic
import features

def welcome():
    heading = '\n Vendor Menu\n'
    instructions = '\n With this tool, *active* vendors can see recommendations of additional products to offer.\n'
    print(logic.globals.pixify(heading) + instructions)
    return

#option to return recommendations based on existing products or existing customers
def print_option_menu():
    instructions = '\n\n Please Select:\n'
    options = '\n [A] - Get product recommendations based on existing products\n [B] - Get product recommendations based on existing customers\n\n [C] - Back\n'
    print(instructions + options)
    selection = input('\n Selection: ')
    #given selected option, run queries and print formatted results
    return selection

#vendor_key = 959360

def add_results_to_df(results_list):
    my_df = pd.DataFrame(columns = ['CURRENT_PRODUCT', 'RECOMMENDED', 'CONFIDENCE (%)', 'LIFT'])
    row = -1
    recommended_items = set()
    for i in results_list:
        row += 1
        current_str = results_list[row][0]
        current_list = current_str.strip('][').split(', ')
        current_item = current_list[0]
        recommended_str = results_list[row][1]
        recommended_list = recommended_str.strip('][').split(', ')
        for i in recommended_list:
            recommended_items.add(i)
        confidence = round((results_list[row][2] * 100),1)
        lift = round(results_list[row][3],1)
        temp_list = [current_item, recommended_list, confidence, lift]
        my_df.loc[len(my_df)] = temp_list
    return(my_df, recommended_items)

def print_recommendations(results_list, products_dict, products_df):
    my_df, recommended_items = add_results_to_df(results_list)
    products_unique = list(my_df['CURRENT_PRODUCT'].unique())
    recommended_unique = list(recommended_items)
    key_df = pd.DataFrame(columns = ['NIGP_KEY', 'NIGP_CODE', 'NIGP_DESC'])
    logic.globals.print_results_heading()
    for i in products_unique:
        pd.options.mode.chained_assignment = None 
        name = products_dict.get(i)
        msg = '\n\n Because you sell [{}], you might also sell:\n'.format(name.upper())
        print(msg)
        my_df_filtered = my_df[my_df['CURRENT_PRODUCT'] == i]
        my_df_filtered.drop('CURRENT_PRODUCT', axis=1, inplace=True)
        print(my_df_filtered.to_string(index=False))
        if i in recommended_items:
            recommended_items.remove(i)
    for i in recommended_unique:
        products_filtered = products_df[products_df['NIGP_KEY'] == i]
        key_df = pd.concat([products_filtered, key_df], ignore_index=True)
    print('\n\n Recommended Key:\n')
    key_df.sort_values('NIGP_KEY', ascending=True, inplace=True)
    #key_df.sort_values(by=['NIGP_KEY'], ascending=True, inplace=True)
    print(key_df)
    if len(recommended_items)>0:
        print('\n\n Of these recommendations, you have not recently sold:\n')
        print(sorted(list(recommended_items)))
    return

def get_results_list(conn, selection, products_list):
    results_list = []
    print('\n Query running...\n\n')
    start_time = time.perf_counter()
    for nigp_key in products_list:
        if selection == 'A':                
            query = queries.get_associations_per_order(nigp_key)
            temp_list = features.get_data.get_vendors_report(conn, query)
        elif selection == 'B':
            #msg = '\n ...Retrieving for product \'{}\''.format(nigp_key)
            #print(msg)
            query = queries.get_associations_per_agency(nigp_key)
            temp_list = features.get_data.get_vendors_report(conn, query)
        for row in temp_list:
            results_list.append(row)
    end_time = time.perf_counter()
    total_time = logic.globals.print_total_time_minutes(start_time, end_time)
    msg = '\n Query completed in ' + total_time
    print(msg)
    return(results_list)

def report_option_menu(conn, products_df, vendor_key, products_dict):
    selection = print_option_menu().upper()
    if selection == 'A' or selection == 'B':
        products_list = list(products_dict.keys())
        results_list = get_results_list(conn, selection, products_list)
        if len(results_list) > 0:
            print_recommendations(results_list, products_dict, products_df)
            selection = input('\n Press any key to continue...\n')
            report_option_menu(conn, products_df, vendor_key, products_dict)    
        else:
            print('\n\n No recommendations found at this time :(\n\n')
            selection = input('\n Press any key to continue...\n')
            report_option_menu(conn, products_df, vendor_key, products_dict)
    elif selection == 'C':
        main_menu.print_main_menu(conn, products_df)
    else:
        logic.errors.invalid_entry()
        report_option_menu(conn, products_df, vendor_key, products_dict)
    return

#query database to return lists of vendor's products and vendor's customers
def get_vendor_orders(conn, products_df, vendor_key):
    products_dict = features.get_data.get_products_list(conn, vendor_key)
    if len(products_dict) == 0:
        #if vendor has no orders, print, 'no orders'
        msg= '\n No transactions found. Unable to recommend associated products...\n'
        print(msg)
        main_menu.print_main_menu(conn, products_df)
    else:
        report_option_menu(conn, products_df, vendor_key, products_dict)
    return

def validate_vendor_key(conn, products_df, vendor_key):
    vendors_list = features.get_data.get_vendors_list(conn)
    is_valid = vendor_key in vendors_list
    del(vendors_list)
    if len(vendor_key) > 0:
        if is_valid == True:
            if vendor_key.isdigit() == False:
                logic.errors.invaid_entry()
                if_vendor(conn, products_df)
            else:
                return (vendor_key)
        else:
            logic.errors.invalid_entry()
            input_vendor_key(conn, products_df)
    else:
        main_menu.print_main_menu(conn, products_df)

def input_vendor_key(conn, products_df):
    instructions = '\n Please input your unique, all-numeric vendor key, or press <<Return>> to go back...\n'
    print(instructions)
    selection = input('\n Vendor Key: ')
    vendor_key = validate_vendor_key(conn, products_df, selection)
    return(vendor_key)

def if_vendor(conn, products_df):
    vendor_key = input_vendor_key(conn, products_df)
    get_vendor_orders(conn, products_df, vendor_key)
    return