import requests
from bs4 import BeautifulSoup
from datetime import datetime

class HistExp:
    def __init__(self, start_year:int, end_year:int) -> None:
        self.start_year = start_year
        self.end_year = end_year
        self.date_strings = []
        self.month_to_num = {
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
        self.html = self.get_website()

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

    def find_date_p(self, year: str) -> list:
        """
        Finds the dates contained within <p> for each css id = year
        """
        if int(year) >= int(datetime.now().year):
            return list(self.html.find('h2', {'id': year}).find_next('p'))
        return list(self.html.find('h3', {'id': year}).find_next('p'))

    def append_date_strings(self, date_list: list):
        """
        Appends dates to date_strings list
        """
        for date in date_list:
            if isinstance(date, str):
                self.date_strings.append(date.strip().lower())

    def correct_date_format(self) -> None:
        """
        Edits the date format to YYYY-MM-DD in date_strings list
        """
        for idx, date in enumerate(self.date_strings):
            try: 
                split_date = date.split()
                split_date[1] = self.month_to_num[split_date[1]]
                day = split_date[0]
                year = split_date[-1]
                split_date[0] = year
                split_date[-1] = day
                self.date_strings[idx] = '-'.join(split_date)
            except:
                print(date)

    def get_exp_dates(self) -> list:
        """
        Conducts whole process of requesting website to correct date format
        """
        for year in self.css_id_list:
            self.append_date_strings(self.find_date_p(year))

        self.correct_date_format()
        return self.get_date_strings()
