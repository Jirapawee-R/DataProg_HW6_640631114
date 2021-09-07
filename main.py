# %%
import pandas as pd

df = pd.read_csv("~/Downloads/avocado.csv")
print(df.dtypes)

# %%
# Create DataFrame of sales amount and detail grouped by region
df_sold_by_region = df.groupby(['region'], sort=False)[['4046', '4225', '4770', 'Total Volume']].sum()

# %%
# Average sales price grouped by region
df_price_by_region = df.groupby(['region'], sort=False)[['AveragePrice']].mean()

# %%
# Create DataFrame contain average sales price and total volume grouped by region
df_income_by_region = df.groupby(['region'], sort=False).agg({'AveragePrice': 'mean', 'Total Volume': 'sum'})

# Create new column named "Total Income" whose value came from multiplying price with volume to the dataframe
df_income_by_region['TotalIncome'] = df_income_by_region['AveragePrice'] * df_income_by_region['Total Volume']
