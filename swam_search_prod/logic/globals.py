import os
import logic.globals as globals

def pixify(heading):
    globals.clear_console()
    pixie_dust = '\n ~ * ~ * ~ * ~ \n'
    message = pixie_dust + heading.upper() + pixie_dust
    return(message)

def clear_console():
    os.system('clear')

def list_dict_values(dict):
    values_list = list(dict.values())
    return(values_list)

def print_total_time_seconds(start_time, end_time):
    total_time = (end_time - start_time)
    output_str = "{} seconds".format(round(total_time, 2))
    return (output_str)

def print_total_time_minutes(start_time, end_time):
    total_time = (end_time - start_time)/60
    output_str = "{} minutes".format(total_time)
    return (output_str)

def load_states():
    states_list = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 
                    'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 
                    'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 
                    'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 
                    'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
    return(states_list)

def return_dict(rows, key_col_num, val_col_num):
    my_dict = {}
    for r in rows:
        key = r[key_col_num]
        value = r[val_col_num]
        kv_pair = {key: value}
        my_dict.update(kv_pair)
    return (my_dict)

def print_results_heading():
    heading = '\n RESULTS\n'
    print(pixify(heading))
    return