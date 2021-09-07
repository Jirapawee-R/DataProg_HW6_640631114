# %%
import pandas as pd

df = pd.read_csv("~/Downloads/avocado.csv")
print(df.dtypes)

# %%
# Create DataFrame of sales amount and detail grouped by region
df_by_region = df.groupby(['region'], sort=False)[['4046', '4225', '4770', 'Total Volume']].sum()

