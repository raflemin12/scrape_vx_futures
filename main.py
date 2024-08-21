import pandas as pd
from dates import third_wed_month

URL = 'https://cdn.cboe.com/data/us/futures/market_statistics/historical_data/VX/VX_{date}.csv'

df = pd.read_csv(URL.format(date='2024-08-21'))

print(df)
