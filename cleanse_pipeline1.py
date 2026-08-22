import random
import pandas as pd

random.seed(42)

names = ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram', 'Ananya', 'Rohit', 'Neha', None, 'Pooja']
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'USB Hub', 'Webcam']
dates = ['2026-08-01', '2026-08-02', '2026-08-03', 'Invalid-Date', '2026-08-05', '08-06-2026', None]

order_ids, customer_names, product_list, prices, quantities, order_dates = [], [], [], [], [], []

for _ in range(1,60):
    order_ids.append(random.choice([101, 102, 103, 104, 105, random.randint(106, 150)]))

    name = random.choice(names)
    if name and random.random() > 0.8:
        name = name + ' '
    customer_names.append(name)

    product_list.append(random.choice(products))

    prices.append(random.choice([f"${random.randint(20, 1500)}.00", str(random.randint(20, 1500)), 'invalid_price', None]))

    quantities.append(random.choice([random.randint(1, 5), 'two', -2, 0, None]))
    
    order_dates.append(random.choice(dates))

df = pd.DataFrame({
    'order_id': order_ids,
    'customer_name': customer_names,
    'product': product_list,
    'price': prices,
    'quantity': quantities,
    'order_date': order_dates})

print(f"--- 1. RAW MESSY DATA GENERATED (Total Rows: {len(df)}) ---")
print(df.head(5))

# ==========================================
# 2. PANDAS DATA CLEANING PIPELINE
# ==========================================

# A. Remove duplicates based on order_id
df = df.drop_duplicates(subset=['order_id'], keep='first')

# B. Clean customer names
df['customer_name'] = df['customer_name'].astype(str).str.strip()
df['customer_name'] = df['customer_name'].replace('None', 'Unknown Customer')
df['customer_name'] = df['customer_name'].fillna('Unknown Customer')

# C. Clean prices
df['price'] = df['price'].astype(str).str.replace('$', '', regex=False)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['price'] = df['price'].fillna(df['price'].mean())

# D. Clean quantities
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df.loc[df['quantity'] <= 0, 'quantity'] = None
df['quantity'] = df['quantity'].fillna(1).astype(int)

# E. Clean order dates
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df = df.dropna(subset=['order_date'])

df = df.sort_values(by='order_id', ascending=True).reset_index(drop=True)

print(f"\n--- 2. DATA CLEANED SUCCESSFULLY (Valid Rows: {len(df)}) ---")
print(df.head(10))

# Save to local CSV
df.to_csv('cleaned_orders.csv', index=False)
print("\nSuccess! Cleaned data saved locally to 'cleaned_orders.csv'.")
