from __future__ import print_function, division
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests


def get_unique_stats(soup_url):
    '''
    Create a list of all of the unique player statistics on a web page
    Returns a list
    '''
    unique_stats = []
    for stat in soup_url.find_all(attrs={'data-stat': True}):
        unique_stats.append(stat['data-stat'])

    unique_stats = set(unique_stats)
    unique_stats = list(unique_stats)

    return unique_stats


def get_player_stats(soup_url, stats):
    '''
    Creates a table containing all of the HTML data with the data-stat attribute
    Returns a DataFrame
    '''
    new_df = pd.DataFrame()

    for stat in stats:
        values = [val.text for val in soup_url.find_all(
            attrs={'data-stat': stat})]
        values = pd.Series(values)
        new_df[stat] = values

    return new_df


def get_player_data(url):
    '''
    Retrieves player statistics from all of the web pages specified
    Returns a DataFrame
    '''
    years = [2006, 2007, 2008, 2009, 2010, 2011, 2012,
             2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    dfs = []
    for year in years:

        file_url = url.format(year)
        response = requests.get(file_url)
        soup = BeautifulSoup(response.text, 'lxml')

        datastats = get_unique_stats(soup)

        year_df = get_player_stats(soup, datastats)
        year_df['year'] = year

        dfs.append(year_df)

    frame = pd.concat(dfs, sort=False)
    return frame


stats_url = 'https://www.basketball-reference.com/leagues/NBA_{}_totals.html'

if __name__ == "__main__":
    get_player_data(stats_url)
