import pandas as pd
from sqlalchemy import create_engine

# 1. Secure connection string (User: db_worker, Password: 12345)
db_connection_str = 'mysql+pymysql://db_worker:12345@localhost/tutorial_db'
db_connection = create_engine(db_connection_str)

# 2. SQL query chalakar Pandas DataFrame mein data lao
query = "SELECT * FROM users;"
df = pd.read_sql(query, db_connection)

# 3. Data check karo
print("Data successfully fetched into Pandas DataFrame!")
print(df.head())
