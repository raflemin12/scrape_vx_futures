import pandas as pd
from dates import third_wed_month

url = 'https://cdn.cboe.com/data/us/futures/market_statistics/historical_data/VX/VX_{date}.csv'

df = pd.read_csv('https://cdn.cboe.com/data/us/futures/market_statistics/historical_data/VX/VX_2024-08-21.csv')

print(df)
