import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import plotly.express as px

load_dotenv()


db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "tutorial_db")

db_connection_str = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"
db_engine = create_engine(db_connection_str)


query = "SELECT * FROM ecommers_orders"
df = pd.read_sql(query, con=db_engine)

df['total_revenue'] = df['price'] * df['quantity']

print(f"--- Analysis started on {len(df)} rows from Database ---")


fig1 = px.bar(df, x='product', y='total_revenue', 
             title='Total Revenue by Product',
             color='product',
             labels={'total_revenue': 'Revenue ($)', 'product': 'Product Name'})

fig1.write_image("revenue_by_product.png")
print("Chart Exported: revenue_by_product.png")


fig2 = px.bar(df, x='product', y='quantity', 
             title='Quantity Sold by Product',
             color='product',
             labels={'quantity': 'Units Sold', 'product': 'Product Name'})

fig2.write_image("quantity_by_product.png")
print("Chart Exported: quantity_by_product.png")



print("\n--- EXECUTIVE SUMMARY ---")
print(f"Total Revenue: ${df['total_revenue'].sum():,.2f}")
print(f"Avg Order Value (AOV): ${df['total_revenue'].mean():,.2f}")
print(f"Top Product by Qty: {df.groupby('product')['quantity'].sum().idxmax()}")















