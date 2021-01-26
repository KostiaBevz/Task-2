# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: ds_env
#     language: python
#     name: ds_env
# ---

# %%
import pandas as pd
from datetime import datetime

# %%
price = 9.99
dev_proc = 0.7

# %%
df = pd.read_csv('data_analytics.csv')

# %%
# Data type formatting
df['Event Date'] = df['Event Date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

# %%
# Let's group data by unique customer id and count how many times it does conversion action
grouped = df.groupby(by='Subscriber ID', as_index=False)['Event Date'].count()-1
grouped.rename(columns={'Event Date': 'Purchase'}, inplace=True)

# %%
# Using formula to calculate LTV
first = dev_proc*price
grouped['LTV'] = grouped['Purchase']*first

# %%
print(grouped)

# %%
# Let's get average value
LTV_for_6_weeks = grouped['LTV'].mean()

# %%
print(LTV_for_6_weeks)

# %% [markdown]
# <b> It means that in period of 6 weeks marketing team need to spend not more than 9.34 to attract new  unique
# customers
