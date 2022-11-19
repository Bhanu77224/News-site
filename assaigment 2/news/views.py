from django.shortcuts import render
import requests
import json


# Create your views here.

def homepage(request):
    # news_api = requests.get(
    #     "http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9144bd1952654f95a5597b25a44e8e59")
    # news_api=requests.get("https://inshortsapi.vercel.app/news?category")
    # api = json.loads(news_api.content)
    records = {}
    url = "https://inshortsapi.vercel.app/news?category"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['alldata'] = inshort_data
    return render(request, 'home.html', records)
  


def business(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=business"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['businessdata'] = inshort_data

   
    return render(request, 'business.html', records)

# def sports(request):
#     s_news_api= requests.get("https://inshortsapi.vercel.app/news?category=sports")
#     s_api = json.loads(s_news_api.content)
#     return render(request, 'sports.html', {'s_api': s_api})


def sports(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=sports"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['sportsdata'] = inshort_data

    return render(request, 'sports.html', records)

def Entertainment(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=entertainment"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['Entertainmentdata'] = inshort_data

    return render(request, 'Entertainment.html', records)    

def Science(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=science"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['Sciencedata'] = inshort_data

    return render(request, 'Science.html', records)

def Automobile(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=automobile"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['Automobiledata'] = inshort_data

    return render(request, 'Automobile.html', records)

def Politics(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=politics"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['Politicsdata'] = inshort_data

    return render(request, 'Politics.html', records)

def startup(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=startup"
    responce = requests.get(url)
    inshort_data = responce.json()
    records['startupdata'] = inshort_data

    return render(request, 'startup.html', records)
