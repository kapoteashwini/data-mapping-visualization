# Data Processing and Visualization Project

This project processes training data, stores it in an SQLite database, and generates visualizations using Bokeh.

## Project Structure

├── data
│ └── train.csv
├── src
│ ├── data_processing.py
│ ├── main.py
│ └── visualization.py
├── data.db
└── README.md

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.10+
- SQLite
- Pip

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. Create a Virtual Environment:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies:
pip install -r requirements.txt

4. Before running the scripts, make sure the data.db is cleared

5. This step will load the training data from train.csv, split it into four datasets, and store it in an SQLite database.

	`sh python3 src/data_processing.py`

6. This step will read the data from the SQLite database and generate visualizations, saving the output to data_visualization.html.

	`sh python3 src/main.py`

7. Before running the scripts, make sure the data.db is cleared

8. Open the data_visualization.html file in your web browser to see the visualizations.