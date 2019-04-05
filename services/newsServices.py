import requests as rq
from bs4 import BeautifulSoup as bs
import os
import json

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../static/news_dict.json"
abs_file_path = os.path.join(script_dir, rel_path)

class newsService():
    def __init__(self):
        self.newsList = []
        
        with open(abs_file_path, 'r') as f:
            newsList = f.read()
        self.newsList = json.loads(newsList)

    def getNewsList(self):
        return self.newsList['NEWS']
    
    # def getNewsByUrl(self, url):
    #     res = rq.get(url)
    #     soup = bs(res.text, 'html.parser')
    #     newsDetail = {}
            
