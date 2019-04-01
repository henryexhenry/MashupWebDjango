import pyrebase
import time
import hashlib

class marvelService():
    def __init__(self):
        config = {
            "apiKey": "AIzaSyARyrPGjmvVTuGCJS4j-9zdIlvo8QV_gB4",
            "authDomain": "marvelavengers4-62451.firebaseapp.com",
            "databaseURL": "https://marvelavengers4-62451.firebaseio.com",
            "projectId": "marvelavengers4-62451",
            "storageBucket": "marvelavengers4-62451.appspot.com",
            "messagingSenderId": "816756853836"
        }
        firebase = pyrebase.initialize_app(config)
        # Get a reference to the database service
        self.db = firebase.database()
        self.HERO_NAMES = []

    def getAllHeroNames(self): # -> [str]
        if self.HERO_NAMES:
            return self.HERO_NAMES
        else:
            all_hero = self.db.child("data").get().val()
            hero_names = []
            for h in all_hero:
                try:
                    h['name'].encode("gbk")
                    hero_names.append(h['name'])
                except:
                    hero_names.append('unk')
            self.HERO_NAMES = hero_names
            return hero_names
    
    def getHeroByName(self, heroName):
        hero_index = self.HERO_NAMES.index(heroName)
        hero = self.db.child("data").get().val()[hero_index]
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