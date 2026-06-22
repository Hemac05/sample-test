import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(r"C:\Users\hemalatha\Downloads\archive\product_info.csv")

engine = create_engine('postgresql://postgres:ribhub1977@localhost:5432/sephora_db')

df.to_sql('sephora_products', engine, if_exists='replace', index=False)

print("Data pushed successfully!")
print(f"Total rows pushed: {len(df)}")