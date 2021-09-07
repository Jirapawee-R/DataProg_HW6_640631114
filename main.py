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
df_income_by_region['Total Income'] = df_income_by_region['AveragePrice'] * df_income_by_region['Total Volume']

# %%
# Create DataFrame contain value of avocado volume of grade '4046', '4225', and '4770' grouped by region
df_NumberOfAvocado_by_region = df.groupby(['region'], sort=False)[['4046', '4225', '4770']].sum()

# Calculate the number of avocado by dividing volume with average weight of each grade.
# Assume that average weight of the grade 4046, 4225, and 4770 are 4 Oz, 9 Oz, and 12 Oz in order.
df_NumberOfAvocado_by_region['4046'] = df_NumberOfAvocado_by_region['4046']/4
df_NumberOfAvocado_by_region['4225'] = df_NumberOfAvocado_by_region['4225']/9
df_NumberOfAvocado_by_region['4770'] = df_NumberOfAvocado_by_region['4770']/12

# Rename Column
df_NumberOfAvocado_by_region = df_NumberOfAvocado_by_region.rename(columns={'4046': '#4046', '4225': '#4225', '4770': '#4770'})

# Calculate Total number of avocado produced from each region and insert as new column named "TotalNumberOfAvocado"
df_NumberOfAvocado_by_region['TotalNumberOfAvocado'] = df_NumberOfAvocado_by_region['#4046'] + df_NumberOfAvocado_by_region['#4225'] + df_NumberOfAvocado_by_region['#4770']