import pandas as pd
from scrape_dates import ExpDates, WebHTML


URL = 'https://cdn.cboe.com/data/us/futures/market_statistics/historical_data/VX/VX_{date_str}.csv'

# df = pd.read_csv(URL.format(date_str='2024-08-21'))



def main():
    expiration_html = WebHTML('https://www.macroption.com/vix-expiration-calendar/#history')
    hist_exp = ExpDates(2013, 2026, expiration_html.get_website())
    exp_dates = hist_exp.get_exp_dates()
    df_list = []
    for date in exp_dates:
        try:
            df = pd.read_csv(URL.format(date_str=date))
            df_list.append(df)
        except:
            print(date)
    large_df = pd.concat(df_list)
    future_expiration = list(large_df['Futures'].unique())
    slice_exp_dates = exp_dates[:len(future_expiration)+1]
    exp_date_dict = dict(zip(future_expiration, slice_exp_dates))
    large_df['Futures'].replace(exp_date_dict, inplace=True)
    print(large_df)

if __name__ == "__main__":
    main()
