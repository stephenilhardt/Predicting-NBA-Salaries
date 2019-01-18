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
import re

def get_unique_stats(soup_url):
    unique_stats = []
    for stat in soup_url.find_all(attrs={'data-stat': True}):
        unique_stats.append(stat['data-stat'])

    unique_stats = set(unique_stats)
    unique_stats = list(unique_stats)

    return unique_stats

def get_player_stats(soup_url, stats):
    new_df = pd.DataFrame()

    for stat in stats:
        values = [val.text for val in soup_url.find_all(attrs={'data-stat': stat})]
        values = pd.Series(values)
        new_df[stat] = values

    return new_df

url = 'https://www.basketball-reference.com/leagues/NBA_{}_totals.html'

def get_player_data(url):
    years = [range(2006, 2020)]
    dfs = []
    for year in years:

        file_url = url.format(year)
        response = requests.get(file_url)
        soup = BeautifulSoup(response.text, 'lxml')

        datastats = get_unique_stats(soup)

        year_df = get_player_stats(soup, datastats)
        year_df['year'] = year

        dfs.append(year_df)

    frame = pd.concat(dfs)
    return frame

df = get_player_data(url)
len(df)

def get_stats(year):

    new_df = pd.DataFrame()

    for stat in datastats:
        values = [val.text for val in soup.find_all(attrs={'data-stat': stat})]
        values = pd.Series(values)
        df[stat] = values

    new_df['year'] = year

    return new_df
