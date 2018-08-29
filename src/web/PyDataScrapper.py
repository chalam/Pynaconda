import pandas as pd
import requests
from bs4 import BeautifulSoup
import re, time
# import pygal
# import scattertext as st
# from IPython.display import IFrame
# from IPython.core.display import display, HTML
# import seaborn as sns
# # display(HTML("<style>.container { width:98% !important; }</style>"))
# import spacy
# import scattertext as st
# %matplotlib inline

def parse_talk(url):
    d = {}
    try:
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        content = soup.find_all('div', class_='container')[1]
        d['author'] = content.find_all('a')[0].contents[0]
        d['title'] = content.find_all('h2')[0].contents[0]
        d['level'] = content.find_all('dd')[0].contents[0]
        d['description'] = soup.find_all('div', class_='description')[0].get_text()
        d['abstract'] = soup.find_all('div', class_='abstract')[0].get_text()
    except:
        print('bad', url)
        return None

    return d


def pull_pydata_schedule(loc, year):
    url = 'https://pydata.org/' + loc + str(year) + '/schedule/'
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    content = soup.find_all('div', class_='container')[1]
    talks = []
    for slot in content.find_all('td', class_='slot'):
        for link in slot.find_all('a'):
            d = parse_talk('https://pydata.org' + link.attrs['href'])
            if d is not None:
                d['location'] = loc
                d['year'] = str(year)
                talks.append(d)
    time.sleep(5)  # for politeness
    print(loc, year)
    return pd.DataFrame(talks)