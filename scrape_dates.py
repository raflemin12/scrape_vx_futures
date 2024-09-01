import requests
from bs4 import BeautifulSoup

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
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
paragraph = soup.find('h3', {'id': '2013'}).find_next('p')

date_strings = [date.strip().replace(' ', '-').lower() 
                for date in list(paragraph) if isinstance(date, str)]
