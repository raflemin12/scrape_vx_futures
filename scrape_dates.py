import requests
import re
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
                date_text = date.strip().lower()
                date_text_match = re.search("^([0-9]+ [A-Za-z]+ [0-9]+)", date_text)
                if date_text_match:
                    self.date_strings.append(date_text_match.group())

    def swap_year_day(self, date_string: list) -> list:
        """
        Swaps the year and day portions of a date string
        """
        day = date_string[0]
        year = date_string[-1]
        date_string[0] = year
        date_string[-1] = day
        return date_string

    def month_to_number(self, date_string:list) -> list:
        """
        Replaces the month name with a corresponding number.
        Ex: January -> 01
        """
        date_string[1] = self.month_to_num[date_string[1]]
        return date_string

    def correct_date_format(self) -> None:
        """
        Edits the date format to YYYY-MM-DD in date_strings list
        """
        for idx, date in enumerate(self.date_strings):
            split_date = date.split()
            split_date = self.swap_year_day(split_date)
            split_date = self.month_to_number(split_date)
            self.date_strings[idx] = '-'.join(split_date)

    def get_exp_dates(self) -> list:
        """
        Conducts whole process of requesting website to correct date format
        """
        for year in self.css_id_list:
            self.append_date_strings(self.find_date_p(year))

        self.correct_date_format()
        return self.get_date_strings()
