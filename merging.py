import numpy as np
import pandas as pd

import rookies
import salaries
import playerstats

rookie_url = 'https://www.basketball-reference.com/play-index/draft_finder.cgi?request=1&year_min=2005&year_max=2015&round_min=1&round_max=2&college_id=0&pick_overall_min=1&pick_overall_max=60&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&order_by=year_id'
stats_url = 'https://www.basketball-reference.com/leagues/NBA_{}_totals.html'
salaries_url = 'http://www.espn.com/nba/salaries/_/year/{}/page/{}'


rookies = rookies.get_rookie_data(rookie_url)
rookies

stats = playerstats.get_player_data(stats_url)
stats

salaries = salaries.get_salary_data(salaries_url)
