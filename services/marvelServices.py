# import pyrebase
import time
import hashlib
import json
import os


script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../static/char_dict.json"
abs_file_path = os.path.join(script_dir, rel_path)

class marvelService():
    def __init__(self):
        # config = {
        #     "apiKey": "AIzaSyARyrPGjmvVTuGCJS4j-9zdIlvo8QV_gB4",
        #     "authDomain": "marvelavengers4-62451.firebaseapp.com",
        #     "databaseURL": "https://marvelavengers4-62451.firebaseio.com",
        #     "projectId": "marvelavengers4-62451",
        #     "storageBucket": "marvelavengers4-62451.appspot.com",
        #     "messagingSenderId": "816756853836"
        # }
        # firebase = pyrebase.initialize_app(config)
        # Get a reference to the database service
        # self.db = firebase.database()
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
        self.publicKey = '321ea9ac4eb42258d2f04c6e47771d76'
        self.privateKey = '500fc933f0fabfc6ca5dc9932c5c908d9f9c89c3'
        self.BASEURL = 'http://gateway.marvel.com/v1/public/'

    def getAllChars(self):
        ts = str(int(time.time()))
        SUM = ts + self.privateKey + self.publicKey
        hash_ = hashlib.md5(SUM.encode('utf-8')).hexdigest()
        opts = 'limit=100&offset=1400&'
        APIurl = self.BASEURL+'characters?'+opts+'ts='+ts+'&apikey='+self.publicKey+'&hash='+hash_
        return APIurl