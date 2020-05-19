from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import Http404
from SmartNewsApp.models import Comment
from SmartNewsApp.forms import CommentForm
from django.shortcuts import render
import requests
import os
import dotenv
from datetime import date

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'comments.html'

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('func')

def topnews(request):
    apiKey = os.getenv('API_KEY')
    response = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey='+apiKey)
    news = response.json()
    return render(request, 'news.html', {
        'title': news['articles'][0]['title'][:105],
        'description': news['articles'][0]['description'],
        'author': news['articles'][0]['author'],
        'publisher': news['articles'][0]['source']['name'],
        'date': date.today(),
        'dateModified': date.today(),
        'image': news['articles'][0]['urlToImage'],
        'title2': news['articles'][1]['title'],
        'description2': news['articles'][1]['description'],
        'date2': date.today(),
        'dateModified2': date.today(),
        'author2': news['articles'][1]['author'],
        'publisher2': news['articles'][1]['source']['name'],
        'image2': news['articles'][1]['urlToImage']
    })

def sources(request):
    return render(request, 'sources.html')

def newsBBC(request):
    apiKey = os.getenv('API_KEY')
    response = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey='+apiKey)
    news = response.json()
    return render(request, 'BBC.html', {
        'title': news['articles'][0]['title'][:105],
        'description': news['articles'][0]['description'],
        'author': news['articles'][0]['author'],
        'publisher': news['articles'][0]['source']['name'],
        'date': date.today(),
        'dateModified': date.today(),
        'image': news['articles'][0]['urlToImage'],
        'title2': news['articles'][1]['title'],
        'description2': news['articles'][1]['description'],
        'date2': date.today(),
        'dateModified2': date.today(),
        'author2': news['articles'][1]['author'],
        'publisher2': news['articles'][1]['source']['name'],
        'image2': news['articles'][1]['urlToImage']
    })

def newsUSATODAY(request):
    apiKey = os.getenv('API_KEY')
    response = requests.get('https://newsapi.org/v2/top-headlines?sources=usa-today&apiKey='+apiKey)
    news = response.json()
    return render(request, 'USATODAY.html', {
        'title': news['articles'][0]['title'][:105],
        'description': news['articles'][0]['description'],
        'author': news['articles'][0]['author'],
        'publisher': news['articles'][0]['source']['name'],
        'date': date.today(),
        'dateModified': date.today(),
        'image': news['articles'][0]['urlToImage'],
        'title2': news['articles'][1]['title'],
        'description2': news['articles'][1]['description'],
        'date2': date.today(),
        'dateModified2': date.today(),
        'author2': news['articles'][1]['author'],
        'publisher2': news['articles'][1]['source']['name'],
        'image2': news['articles'][1]['urlToImage']
    })

def newsGoogleNews(request):
    apiKey = os.getenv('API_KEY')
    response = requests.get('https://newsapi.org/v2/top-headlines?sources=google-news&apiKey='+apiKey)
    news = response.json()
    return render(request, 'GoogleNews.html', {
        'title': news['articles'][0]['title'][:105],
        'description': news['articles'][0]['description'],
        'author': news['articles'][0]['author'],
        'date': date.today(),
        'dateModified': date.today(),
        'image': news['articles'][0]['urlToImage'],
        'title2': news['articles'][1]['title'],
        'description2': news['articles'][1]['description'],
        'date2': date.today(),
        'dateModified2': date.today(),
        'author2': news['articles'][1]['author'],
        'publisher2': news['articles'][1]['source']['name'],
        'image2': news['articles'][1]['urlToImage']
    })
