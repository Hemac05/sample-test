import pandas as pd

df = pd.read_csv(r"C:\Users\hemalatha\Downloads\archive\product_info.csv")

print(df.columns.tolist())
print(df.shape)
print(df.head(2))