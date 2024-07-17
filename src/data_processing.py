import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data(file_path):
    print(f"Loading data from {file_path}")
    return pd.read_csv(file_path)

def store_data_to_sql(df, table_name, engine):
    print(f"Storing data to SQLite table '{table_name}'")
    df.to_sql(table_name, con=engine, index=False, if_exists='replace')

def fetch_data_from_sql(table_name, engine):
    print(f"Fetching data from SQLite table '{table_name}'")
    query = f"SELECT * FROM {table_name}"
    return pd.read_sql(query, con=engine)

def find_best_ideal_functions(train_df, ideal_df):
    print("Finding best ideal functions for each training dataset")
    best_functions = []
    for col in train_df.columns[1:]:
        min_error = float('inf')
        best_func = None
        for ideal_col in ideal_df.columns[1:]:
            error = np.sum((train_df[col] - ideal_df[ideal_col]) ** 2)
            if error < min_error:
                min_error = error
                best_func = ideal_col
        best_functions.append(best_func)
    print(f"Best ideal functions: {best_functions}")
    return best_functions

def match_test_data(test_df, train_df, ideal_df, best_funcs):
    print("Matching test data to best ideal functions")
    results = []
    for _, test_row in test_df.iterrows():
        x_test, y_test = test_row
        for i, best_func in enumerate(best_funcs):
            train_col = train_df.columns[i+1]
            max_dev = np.max(np.abs(train_df[train_col] - ideal_df[best_func]))
            if np.abs(y_test - ideal_df.loc[ideal_df['X'] == x_test, best_func].values[0]) <= max_dev * np.sqrt(2):
                results.append([x_test, y_test, np.abs(y_test - ideal_df.loc[ideal_df['X'] == x_test, best_func].values[0]), best_func])
                break
    result_df = pd.DataFrame(results, columns=['X', 'Y', 'Delta Y', 'Ideal Function'])
    print(f"Matched data:\n{result_df.head()}")
    return result_df

def main():
    train_path = 'data/train.csv'
    
    # Load the training data
    train_data = load_data(train_path)
    print("Loaded training data:")
    print(train_data.head())
    
    # Create SQLite engine
    engine = create_engine('sqlite:///data.db')
    
    # Store training data in SQLite
    store_data_to_sql(train_data, 'train', engine)
    print("Stored training data to SQLite.")
    
    # Fetch data back to ensure it was stored correctly
    train_data = fetch_data_from_sql('train', engine)
    print("Fetched training data from SQLite:")
    print(train_data.head())

if __name__ == '__main__':
    main()
