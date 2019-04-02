from django.shortcuts import render
from django.http import HttpResponse
from services.marvelServices import marvelService
import random

def heroView(request):

    ms = marvelService()
    allHeroNames = ms.getAllHeroNames()
    hero_list = []

    while len(hero_list) < 6 :
        name = allHeroNames[random.randint(0,1490)]
        hero = ms.getHeroByName(name)
        if hero['thumbnail'] != 'http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available.jpg':
            if hero['series']:
                if hero['description']:
                    if hero not in hero_list:
                        hero_list.append(hero)

    return render(request, 'hero.html', {'hero_list' : hero_list})