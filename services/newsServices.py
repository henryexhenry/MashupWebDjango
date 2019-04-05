import requests as rq
from bs4 import BeautifulSoup as bs

class newsService():
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
    
    # def getNewsByUrl(self, url):
    #     res = rq.get(url)
    #     soup = bs(res.text, 'html.parser')
    #     newsDetail = {}


            
