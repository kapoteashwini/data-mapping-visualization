from bokeh.plotting import figure, show, output_file
from bokeh.layouts import gridplot
import pandas as pd

def create_plot(train_df, ideal_df, best_funcs, title):
  print(f"Creating plot: {title}")
  p = figure(title=title, x_axis_label='X', y_axis_label='Y')
  for col in train_df.columns[1:]:
      p.line(train_df['X'], train_df[col], legend_label=col, line_width=2)
  for best_func in best_funcs:
      p.line(ideal_df['X'], ideal_df[best_func], legend_label=best_func, line_width=2, line_dash='dashed')
  return p

def visualize_data(train_data, ideal_functions, best_funcs_train, matched_data):
  print("Starting data visualization...")
  
  plot1 = create_plot(train_data, ideal_functions, best_funcs_train, 'Training Data and Ideal Functions')

  # Create a plot for matched test data
  print("Creating plot for matched test data...")
  p_test = figure(title='Matched Test Data', x_axis_label='X', y_axis_label='Y')
  p_test.scatter(matched_data['X'], matched_data['Y'], size=8, color='red', legend_label='Test Data')
  for best_func in best_funcs_train:
      p_test.line(ideal_functions['X'], ideal_functions[best_func], legend_label=best_func, line_width=2, line_dash='dashed')

  # Arrange plots in a grid
  print("Arranging plots in a grid...")
  grid = gridplot([[plot1], [p_test]])

  # Save and show the plots
  output_file("data_visualization.html", mode='inline')
  print("Saving visualization to data_visualization.html...")
  show(grid)
  
  print("Visualization completed and saved to data_visualization.html")

# Example usage (this part is for testing purposes, remove when integrating with main.py)
# if __name__ == "__main__":
  # Example data
  # train_data = pd.DataFrame({'X': [1, 2, 3], 'Y1': [2, 3, 4], 'Y2': [5, 6, 7]})
  # ideal_functions = pd.DataFrame({'X': [1, 2, 3], 'ideal1': [2, 3, 4], 'ideal2': [5, 6, 7]})
  # best_funcs_train = ['ideal1', 'ideal2']
  # matched_data = pd.DataFrame({'X': [1, 2], 'Y': [2, 6], 'Delta Y': [0, 0], 'Ideal Function': ['ideal1', 'ideal2']})
  
  # visualize_data(train_data, ideal_functions, best_funcs_train, matched_data)
