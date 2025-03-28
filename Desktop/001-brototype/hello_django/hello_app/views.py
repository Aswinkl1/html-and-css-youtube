from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_hello(request):
    movie_details = {
        "movie":[
        {
        "title":"titanic",
        "year": "1909",
        "ott": True
        },
        {
        "title":"god father",
        "year": "1229",
        "plot": "story of a don"
        },
        {
        "title":"one piece",
        "year": "1999",
        "plot": "pirate boy"
        },
        {
        "title":"death note",
        "year": "2003",
        "plot": "shinigami"
        },
        {
        "title":"titanic",
        "year": "1909",
        "plot": "lovers sank in na ship"
        },
        {
        "title":"titanic",
        "year": "1909",
        "plot": "lovers sank in na ship"
        },
        {
        "title":"titanic",
        "year": "1909",
        "plot": "lovers sank in na ship"
        },
        {
        "title":"titanic",
        "year": "1909",
        "plot": "lovers sank in na ship"
        },
        {
        "title":"titanic",
        "year": "1909",
        "plot": "lovers sank in na ship"
        },

        ]
        
    }
    return render(request,"helo.html",movie_details)
