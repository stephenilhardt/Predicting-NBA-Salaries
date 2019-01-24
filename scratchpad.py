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
