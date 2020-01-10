from django.shortcuts import render, HttpResponse, redirect
from lor_deckcodes import LoRDeck, CardCodeAndCount
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'static/returning_app/js/set1-en_us.json')
with open(file_path, 'r') as f:
    data = json.load(f)

deck = LoRDeck.from_deckcode('CEBAGAIDBMKS6BYBAUGBEFIXFAXC6AIEAECQIKRLGEBACAIDFIAQCBID')


def index(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 42)
    try:
        cards = paginator.page(page)
    except PageNotAnInteger:
        cards = paginator.page(1)
    except EmptyPage:
        cards = paginator.page(paginator.num_pages)

    return render(request, "returning_app/index.html", { 'cards' : cards} )

