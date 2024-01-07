from bs4 import BeautifulSoup
import requests
import pandas as pd 

all_details = []

try:
    html_code = requests.get('https://en.wikipedia.org/wiki/Pok%C3%A9mon_(TV_series)').text


    soup = BeautifulSoup(html_code, 'lxml')

    content_table = soup.find('table', class_ = 'wikitable plainrowheaders')


    td_tag = content_table.find_all('td')
    td_datas = [td_data.text for td_data in td_tag]

    season_names = td_datas[::4]

    n_episodes = td_datas[1::4]

    released_dates = td_datas[2::4]
    released_dates = [released_date[-11:-1] for released_date in released_dates]
    released_dates[-1] = '2023-04-14'

    end_dates = td_datas[3::4]
    end_dates = [end_date[-11:-1] for end_date in end_dates]
    end_dates[-1] = 'Not Announced'

    for i in range(len(season_names)):
        episode = {}

        episode["Season No."] = i+1
        episode["Season Name"] = season_names[i]
        episode["No. of Episodes"] = n_episodes[i]
        episode["Release Date"] = released_dates[i]
        episode["End Date"] = end_dates[i]

        all_details.append(episode)

    data = pd.DataFrame(all_details)
    data.to_csv('PokemonScraping/pokemon_data.xlsx')

except Exception as e:
    print(e)
