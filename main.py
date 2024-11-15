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
    print(large_df)

if __name__ == "__main__":
    main()
