import requests
from bs4 import BeautifulSoup
import datetime

URL = 'https://www.macroption.com/vix-expiration-calendar/#history'

css_id_list = ['2013', '2014', '2015', '2016'
               '2017', '2018', '2019', '2020'
               '2021', '2022', '2023', '2024', '2025']

month_to_num = {
    'january': '01'
    ,'february': '02'
    ,'march': '03'
    ,'april':'04'
    ,'may': '05'
    ,'june': '06'
    ,'july': '07'
    ,'august': '08'
    ,'september': '09'
    ,'october': '10'
    ,'november': '11'
    ,'december': '12'
}
r = requests.get(URL, timeout= 5)
soup = BeautifulSoup(r.content, 'html.parser')
# TODO Need to also find 'h2' for years >= current year
paragraph = soup.find('h3', {'id': '2023'}).find_next('p')

date_strings = [date.strip().lower()
                for date in list(paragraph) if isinstance(date, str)]

# TODO Break this down into a functions
for idx, date in enumerate(date_strings):
    split_date = date.split()
    split_date[1] = month_to_num[split_date[1]]
    day = split_date[0]
    year = split_date[-1]
    split_date[0] = year
    split_date[-1] = day
    date_strings[idx] = '-'.join(split_date)

# TODO create loop to get all historical dates using css ids
print(date_strings)
