import pandas as pd
from sqlalchemy import create_engine
from data_processing import load_data, store_data_to_sql, fetch_data_from_sql, find_best_ideal_functions, match_test_data
from visualization import visualize_data

def main():
  # Paths to the data files
  train_path = 'data/train.csv'
  ideal_functions_path = 'data/ideal_functions.csv'
  test_data_path = 'data/test_data.csv'
  print("Starting main process...")
  # Load data
  train_data = load_data(train_path)
  ideal_functions = load_data(ideal_functions_path)
  test_data = load_data(test_data_path)
  # Create SQLite engine
  engine = create_engine('sqlite:///data.db')
  # Store data in SQLite
  store_data_to_sql(train_data, 'train', engine)
  store_data_to_sql(ideal_functions, 'ideal_functions', engine)
  store_data_to_sql(test_data, 'test_data', engine)
  # Fetch data from SQLite to ensure it was stored correctly
  train_data = fetch_data_from_sql('train', engine)
  ideal_functions = fetch_data_from_sql('ideal_functions', engine)
  test_data = fetch_data_from_sql('test_data', engine)
  # Rename columns if necessary
  if 'X' not in test_data.columns:
      test_data.columns = ['X', 'Y']
  if 'X' not in train_data.columns:
      train_data.columns = ['X'] + [f'train_{i}' for i in range(1, len(train_data.columns))]
  if 'X' not in ideal_functions.columns:
      ideal_functions.columns = ['X'] + [f'ideal_{i}' for i in range(1, len(ideal_functions.columns))]
  # Find best ideal functions for each training dataset
  best_funcs_train = find_best_ideal_functions(train_data, ideal_functions)
  # Match test data to the best ideal functions
  matched_data = match_test_data(test_data, train_data, ideal_functions, best_funcs_train)
  # Visualize data
  visualize_data(train_data, ideal_functions, best_funcs_train, matched_data)
  print("Process completed successfully.")

if __name__ == '__main__':
    main()
