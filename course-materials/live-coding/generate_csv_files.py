import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Helper function to generate random dates
def random_dates(start, end, n):
    date_range = (end - start).days
    return [start + timedelta(days=random.randint(0, date_range)) for _ in range(n)]

# 1. basic_data.csv
def create_basic_data():
    data = {
        'Name': [f'Person_{i}' for i in range(1, 101)],
        'Age': np.random.randint(18, 80, 100),
        'City': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], 100)
    }
    df = pd.DataFrame(data)
    df.to_csv('basic_data.csv', index=False)

# 2. tab_data.tsv
def create_tab_data():
    data = {
        'Product': [f'Item_{i}' for i in range(1, 101)],
        'Price': np.random.uniform(10, 1000, 100).round(2),
        'Quantity': np.random.randint(1, 100, 100)
    }
    df = pd.DataFrame(data)
    df.to_csv('tab_data.tsv', sep='\t', index=False)

# 3. no_header.csv
def create_no_header():
    data = np.random.rand(100, 4)
    np.savetxt('no_header.csv', data, delimiter=',')

# 4. large_dataset.csv
def create_large_dataset():
    columns = [f'Column_{i}' for i in range(1, 51)]
    data = np.random.rand(1000, 50)
    df = pd.DataFrame(data, columns=columns)
    df.to_csv('large_dataset.csv', index=False)

# 5. missing_values.csv
def create_missing_values():
    data = {
        'Name': [f'Person_{i}' for i in range(1, 101)],
        'Age': np.random.randint(18, 80, 100),
        'Salary': np.random.uniform(30000, 150000, 100).round(2),
        'Department': np.random.choice(['HR', 'IT', 'Sales', 'Marketing', 'Finance'], 100)
    }
    df = pd.DataFrame(data)
    
    # Introduce missing values
    for col in df.columns:
        mask = np.random.choice([True, False], len(df), p=[0.1, 0.9])
        df.loc[mask, col] = np.random.choice([np.nan, 'N/A', 'Unknown'])
    
    df.to_csv('missing_values.csv', index=False)

# 6. date_data.csv
def create_date_data():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)
    dates = random_dates(start_date, end_date, 1000)
    
    data = {
        'Date': dates,
        'Value': np.random.uniform(0, 100, 1000).round(2),
        'Category': np.random.choice(['A', 'B', 'C'], 1000)
    }
    df = pd.DataFrame(data)
    df.to_csv('date_data.csv', index=False)

# 7. large_file.csv
def create_large_file():
    columns = [f'Column_{i}' for i in range(1, 21)]
    data = np.random.rand(100000, 20)
    # Make sure that the large_file has date information

    df = pd.DataFrame(data, columns=columns)
    df.to_csv('large_file.csv', index=False)

# Generate all files
create_basic_data()
create_tab_data()
create_no_header()
create_large_dataset()
create_missing_values()
create_date_data()
create_large_file()

print("All CSV files have been generated successfully.")