from django.shortcuts import render
from django.http import HttpResponse
from services.marvelServices import marvelService
from services.newsServices import newsService
import random

def homeView(request):

    ms = marvelService()
    ns = newsService()
    allHeroNames = ms.getAllHeroNames()
    news_list = ns.getNewsList()[:3]
    hero_list = []

    while len(hero_list) < 3 :
        name = allHeroNames[random.randint(0,1490)]
        hero = ms.getHeroByName(name)
        if hero['thumbnail'] != 'http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available.jpg':
            if hero['series']:
                if hero['description']:
                    if hero not in hero_list:
                        hero_list.append(hero)


    return render(request, 'home.html', {'hero_list' : hero_list, 'news_list' : news_list})

def newsView(request):
    
    ns = newsService()
    news_list = ns.getNewsList()
    
    return render(request, 'news.html', {'news_list':news_list})

def heroView(request):

    ms = marvelService()
    allHeroNames = ms.getAllHeroNames()
    hero_list = []

    while len(hero_list) < 9 :
        name = allHeroNames[random.randint(0,1490)]
        hero = ms.getHeroByName(name)
        if hero['thumbnail'] != 'http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available.jpg':
            if hero['series']:
                if hero['description']:
                    if hero not in hero_list:
                        hero_list.append(hero)

    return render(request, 'hero.html', {'hero_list' : hero_list})