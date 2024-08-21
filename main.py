import pandas as pd
import time
from dates import third_wed_month

URL = 'https://cdn.cboe.com/data/us/futures/market_statistics/historical_data/VX/VX_{date_str}.csv'

df = pd.read_csv(URL.format(date_str='2024-08-21'))

futures_dict = {}

for date in third_wed_month(2013, 2025):
    try:
        df = pd.read_csv(URL.format(date_str=date))
        futures_dict[date] = df
        time.sleep(3)
    except:
        print(date)

print(futures_dict)
