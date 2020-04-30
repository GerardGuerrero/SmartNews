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
    response = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=d7014a6a6e3e4289aaa3a37ca2a42416')
    news = response.json()
    return render(request, 'news.html', {
        'title': news['articles'][0]['title'],
        'description': news['articles'][0]['description']
    })
