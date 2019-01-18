from __future__ import print_function, division
import pandas as pd
from bs4 import BeautifulSoup
import requests

def get_page_salaries(url):
    frame = pd.DataFrame()
    soup = BeautifulSoup(requests.get(url).text, 'html5')
    rows = soup.find('table').find_all('tr')
    for row in rows:
        data = row.find_all('td')
        data_row = []
        for datum in data:
            data_row.append(datum.text)
        series_row = pd.Series(data_row)
        frame = frame.append(series_row, ignore_index=True)
    return frame

url = 'http://www.espn.com/nba/salaries/_/year/{}/page/{}'

def get_salary_data(url):
    dfs = []
    years = range(2005, 2020)
    pages = range(1,13)

    for year in years:
        for page in pages:
            new_df = get_page_salaries(url.format(year, page))
            new_df['YEAR'] = year
            dfs.append(new_df)

    df = pd.concat(dfs)
    return df

df = get_salary_data(url)

df
