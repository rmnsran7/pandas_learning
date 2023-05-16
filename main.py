import pandas as pd

csv_file = "datasets/choclate protfolio project - 11.csv"

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    print("Error: CSV file not found.")
    exit(1)

# Convert 'cost per unit' column to numeric format
try:
    df['cost per unit'] = pd.to_numeric(df['cost per unit'], errors='coerce')
except ValueError:
    print("Error: Invalid values found in 'cost per unit' column.")
    exit(1)

# Create a new DataFrame with 'Product Name' and 'Price' columns
new_df = pd.DataFrame({'Product Name': df['Product'], 'Price': df['cost per unit']})

# Print the new DataFrame
print(new_df.head())
