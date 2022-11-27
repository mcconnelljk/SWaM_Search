import os

def clear_console():
    os.system('clear')

def list_dict_values(dict):
    values_list = list(dict.values())
    return(values_list)

def print_total_time_seconds(start_time, end_time):
    total_time = (end_time - start_time)
    output_str = "{} seconds".format(total_time)
    return (output_str)

def print_total_time_minues(start_time, end_time):
    total_time = (end_time - start_time)/60
    output_str = "{} minutes".format(total_time)
    return (output_str)