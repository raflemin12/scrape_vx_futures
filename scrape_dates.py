import requests
from bs4 import BeautifulSoup
import datetime

class HistExp:
    def __init__(self, start_year:int, end_year:int) -> None:
        self.start_year = start_year
        self.end_year = end_year
        self.date_strings = []
        self.MONTH_TO_NUM = {
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
        self.css_id_list = [str(year) for year in range(self.start_year, self.end_year + 1)]
        self.URL = 'https://www.macroption.com/vix-expiration-calendar/#history'
        self.html = self.get_website

    def get_website(self):
        '''
        Requests html from URL and returns BeautifulSoup object for scraping
        '''
        try:
            r = requests.get(self.URL, timeout = 5)
            return BeautifulSoup(r.content, 'html.parser')
        except BaseException:
            print('Could not request from website')
            return None

    def get_date_strings(self) -> list:
        """
        Returns date_strings list
        """
        return self.date_strings

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
