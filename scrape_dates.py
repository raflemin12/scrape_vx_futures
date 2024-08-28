import requests
from bs4 import BeautifulSoup

URL = 'https://www.macroption.com/vix-expiration-calendar/#history'

css_id_list = ['2013', '2014', '2015', '2016'
               '2017', '2018', '2019', '2020'
               '2021', '2022', '2023', '2024', '2025']
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
paragraph = soup.find('h3', {'id': '2013'}).find_next('p')
