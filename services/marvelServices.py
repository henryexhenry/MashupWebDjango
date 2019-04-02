# import pyrebase
import time
import hashlib
import json
import os
from static.configs import MarvelAPI

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../static/char_dict.json"
abs_file_path = os.path.join(script_dir, rel_path)

class marvelService():
    def __init__(self):
        self.HERO_NAMES = []
        
        with open(abs_file_path, 'r') as f:
            char_dict = f.read()
        self.db = json.loads(char_dict)

    def getAllHeroNames(self): # -> [str]
        if self.HERO_NAMES:
            return self.HERO_NAMES
        else:
            all_hero = self.db["CHARS"]
            hero_names = []
            for h in all_hero:
                hero_names.append(h['name'])
            self.HERO_NAMES = hero_names
            return hero_names
    
    def getHeroByName(self, heroName):
        hero_index = self.HERO_NAMES.index(heroName)
        hero = self.db["CHARS"][hero_index]
        return hero

class marvelAPI():
    def __init__(self):
        self.publicKey = MarvelAPI.publicKey
        self.privateKey = MarvelAPI.privateKey
        self.BASEURL = MarvelAPI.BASEURL

    def getAllChars(self):
        ts = str(int(time.time()))
        SUM = ts + self.privateKey + self.publicKey
        hash_ = hashlib.md5(SUM.encode('utf-8')).hexdigest()
        opts = 'limit=100&offset=1400&'
        APIurl = self.BASEURL+'characters?'+opts+'ts='+ts+'&apikey='+self.publicKey+'&hash='+hash_
        return APIurl