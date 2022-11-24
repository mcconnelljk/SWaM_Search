import pandas as pd

def load_data(target_path):
    str = '\n Loading data...\n'
    print(str)
    orders_df = pd.read_csv(target_path, encoding='ISO-8859-1', low_memory=False)

