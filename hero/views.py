from django.shortcuts import render
from django.http import HttpResponse
from services.marvelServices import marvelService
import random

def heroView(request):

    ms = marvelService()
    allHeroNames = ms.getAllHeroNames()
    Heroes = []
    hero_list = []

    for _ in range(6):
        hero_list.append(allHeroNames[random.randint(0,1490)])

    for h_name in hero_list:
        h = ms.getHeroByName(h_name)
        Heroes.append(h)

    return render(request, 'hero.html', {'hero_list' : Heroes})