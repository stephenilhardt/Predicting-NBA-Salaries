from __future__ import print_function, division
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests


def get_next_page(soup):
    '''
    Returns string containing URL of next page of data
    '''
    next_page = soup.find('a', text="Next page")['href']
    header = 'https://www.basketball-reference.com'
    next_page = header + next_page
    return next_page


def get_page_stats(soup, attributes):
    '''
    Retrieves all HTML data where attributes contains 'data-stat'
    Returns DataFrame
    '''
    new_df = pd.DataFrame()
    for attribute in attributes:
        values = [val.text for val in soup.find_all(
            attrs={'data-stat': attribute})]
        values = pd.Series(values)
        new_df[attribute] = values
    return new_df


def get_rookie_data(url):
    '''
    Retrieves all rookie data from the passed basketball-reference.com URL
    Returns DataFrame
    '''
    attributes = ['year_id', 'round', 'pick_overall', 'team_id', 'player', 'age', 'pos', 'birth_country',
                  'college']
    dfs = []
    new_url = url
    soup = BeautifulSoup(requests.get(new_url).text, 'lxml')
    dfs.append(get_page_stats(soup, attributes))
    for page in range(0, 6):
        new_url = get_next_page(soup)
        soup = BeautifulSoup(requests.get(new_url).text, 'lxml')
        dfs.append(get_page_stats(soup, attributes))
    df = pd.concat(dfs)
    return df


rookies_url = "https://www.basketball-reference.com/play-index/draft_finder.cgi?request=1&year_min=2005&year_max=2015&round_min=1&round_max=2&college_id=0&pick_overall_min=1&pick_overall_max=60&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&order_by=year_id"

if __name__ == "__main__":
    get_rookie_data(rookies_url)
