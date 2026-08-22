import pandas as pd
from sqlalchemy import create_engine

df_final_data = pd.read_csv('cleaned_orders.csv')
print(f"Loaded {len(df_final_data)} Messy Data Cleaned on Local Storage.")

db_connection_str = 'mysql+pymysql://db_importer:12345@localhost/tutorial_db'
db_engine = create_engine(db_connection_str)

table_name = 'ecommers_orders'
df_final_data.to_sql(table_name, con=db_engine, if_exists='replace', index=False)

print(f"\nSuccess! Data Successfully Loaded into Table '{table_name}' By Client > db_importer")
