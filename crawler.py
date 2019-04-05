import os
import json
import requests as rq
from bs4 import BeautifulSoup as bs

class newsCrawler():
    def __init__(self):
        res = rq.get('https://editorial.rottentomatoes.com/more-related-content/?relatedmovieid=771432224')
        self.soup = bs(res.text, 'html.parser')
        self.newsList = []

    def getNewsList(self):
        for item in self.soup.find_all('div', {'class' : 'newsItem'}):
            self.newsList.append(
                {
                    'title': item.find_all('p')[0].text,
                    'date': item.find_all('p')[1].text,
                    'image': item.find('img').get('src'),
                    'url': item.find('a').get('href')
                }
            )
        return self.newsList
    
class heroCrawler():
    with open('chars.json', 'rb') as f:
        all_hero = f.read()
    all_hero= all_hero.decode("utf-8")
    json_hero = json.loads(all_hero)

    char_list = []

    for hero in json_hero['data']:
        char_list.append({
            'id':hero['id'],
            'name':hero['name'],
            'description':hero['description'],
            'thumbnail':hero['thumbnail']['path'] + '.' + hero['thumbnail']['extension'],
            'series':hero['series']['items'][0:1]
            })
    char_dict = {'CHARS' : char_list}

    with open('char_dict.json', 'w') as f:
        json.dump(char_dict, f)




nc = newsCrawler()
with open('static/news_dict.json', 'w') as f:
    json.dump({'NEWS':nc.getNewsList()}, f, indent=4)