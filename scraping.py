from __future__ import print_function, division
import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from fake_useragent import UserAgent
import random

ua = UserAgent()
user_agent = {'User-agent': ua.random}
print(user_agent)
chromedriver = '/Applications/chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver

driver = webdriver.Chrome(chromedriver)

driver.get(url)
next_page = driver.find_element_by_xpath("//a[contains(text(), 'Next page')]")
next_page.click()

td = driver.find_element_by_tag_name('td')
stat = td.get_attribute('data-stat')
print(stat)

url = "https://www.basketball-reference.com/play-index/draft_finder.cgi?request=1&year_min=2005&year_max=2015&round_min=1&round_max=2&college_id=0&pick_overall_min=1&pick_overall_max=60&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&order_by=year_id"

def get_next_page(soup):
    next_page = soup.find('a', text="Next page")['href']
    header = 'https://www.basketball-reference.com'
    next_page = header + next_page
    return next_page

def get_page_stats(soup, attributes):
    new_df = pd.DataFrame()
    for attribute in attributes:
        values = [val.text for val in soup.find_all(attrs={'data-stat': attribute})]
        values = pd.Series(values)
        new_df[attribute] = values
    return new_df

def get_rookie_data(url):
    attributes = ['year_id', 'round', 'pick_overall', 'team_id', 'player', 'age', 'pos', 'birth_country',
    'college']
    dfs = []
    new_url = url
    soup = BeautifulSoup(requests.get(new_url).text, 'lxml')
    dfs.append(get_page_stats(soup, attributes))
    for page in range(0,6):
        new_url = get_next_page(soup)
        soup = BeautifulSoup(requests.get(new_url).text, 'lxml')
        dfs.append(get_page_stats(soup, attributes))
    df = pd.concat(dfs)
    return df

df = get_rookie_data(url)
df
df['year_id'].unique()

def get_rookie_stats(url):

    driver.get(url)

    df_stats = pd.DataFrame(columns = ['year_id', 'round', 'pick_overall', 'team_id', 'player', 'age', 'pos', 'birth_country',
    'college'])

    for page in range(0,12):
        time.sleep(3 + random.random())
    #next_page = driver.find_element_by_xpath("//a[contains(text(), 'Next page')]")
        next_page = driver.find_element_by_link_text("Next page")

        try:
            next_page.click()
            url = driver.current_url
        except:
            df_stats = df_stats.append(get_page_stats(url))


    df_stats = df_stats.append(get_page_stats(url))
    return df_stats
df = pd.DataFrame()
df = get_rookie_stats(url)

df.drop_duplicates(inplace=True)
len(df)
df.drop(0, axis=0, inplace=True).reset_index(inplace=True)
df
next_page = driver.find_element_by_link_text("Next page")
next_page.click()


next_page = driver.find_element_by_xpath("//a[contains(text(), 'Next page')]")
next_page = driver.find_element_by_link_text("Next page")
next_page.click()
print(url)
next_page = driver.find_element_by_xpath("//a[contains(text(), 'Next page')]")
print(next_page)
next_page.click()
df
response = requests.get(url)

response.status_code

print(response.text)

soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())
soup.find_all("table")
attributes = ['year_id', 'round', 'pick_overall', 'team_id', 'player', 'age', 'pos', 'birth_country',
'college']

df = pd.DataFrame(columns = ['year_id', 'round', 'pick_overall', 'team_id', 'player', 'age', 'pos', 'birth_country',
'college'])

def get_page_stats(url):
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    new_df = pd.DataFrame()
    for attribute in attributes:
        values = [val.text for val in soup.find_all(attrs={'data-stat': attribute})]
        values = pd.Series(values)
        new_df[attribute] = values
    return new_df

df = df.append(get_page_stats(url))
df
df

values = [val.text for val in soup.find_all(attrs={'data-stat': 'player'})]
values = pd.Series(values)
print(values)

for value in soup.find_all(attrs={"data-stat": 'player'}):
    print(value.text)


driver.get(url)

td = driver.find_element_by_tag_name('td')
stat = td.get_attribute('data-stat')
print(stat)
