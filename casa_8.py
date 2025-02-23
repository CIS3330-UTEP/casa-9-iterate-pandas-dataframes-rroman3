import pandas as pd

# Load the dataset
file_path = 'big-mac-full-index.csv'
df = pd.read_csv(file_path)

# Method 1: Using iterrows()
print('\nMethod 1: Using iterrows()')
for index, row in df.head().iterrows():
    price_diff = row['local_price'] - row['dollar_price']
    print(f"On {row['date']} in {row['name']}, price difference: ${price_diff:.2f}")

# Method 2: Using apply()
print('\nMethod 2: Using apply()')
def calculate_price_diff(row):
    return f"On {row['date']} in {row['name']}, price difference: ${row['local_price'] - row['dollar_price']:.2f}"

result = df.apply(calculate_price_diff, axis=1)
for res in result.head():
    print(res)
