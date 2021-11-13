import os
import pandas as pd
from data_accessor import fetch_data

def serve_dataframe():
    fetch_data()
    csv_path = os.path.join(os.path.dirname(__file__), 'data/data_gcl.csv')
    df = pd.read_csv(csv_path)
    df['Assigned to'].fillna('Unassigned', inplace=True)
    return df


if __name__ == '__main__':
    df = serve_dataframe()
    print(df.head())