# scrape_vx_futures

Project to scrape historical VX futures data from this[link](https://www.cboe.com/us/futures/market_statistics/historical_data/)

## Step 1

- The csv files we want have a consistent url of "cdn.cboe.com/data/us/futures/market_statistics/historical_data/VX/VX_[Date].csv"
    - Where "Date" is a string in the format of 'yyyy-mm-dd' and represents the third Wednesday of every month
- Create function to extract third Wednesday of every month from 2013 to 2025 in the specified format
    - Note: Function worked, but didn't account for holidays, so missed a few csv files from source
- Redirect: Found a website that has historical expiration dates for VX futures.
    - Looks relatively easy to scrape
    - Will try and scrape website and get dates in text format. Ex = '18 October 2023'
    - Need to convert month to number
    - Then convert to date data type
    - Then format date type to string 'yyyy-mm-dd'

## Step 2

- Read the CSV files into a Pandas Dataframe

## Step 3

- Store CSV files in a data structure or GCP

## Step 4

- Clean the dataframes to include only the data we need

## Step 5

- Do some analysis?