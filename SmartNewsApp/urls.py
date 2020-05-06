from django.urls import path, include
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from SmartNewsApp.forms import CommentForm
from SmartNewsApp.models import Comment
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from SmartNewsApp.views import LoginRequiredCheckIsOwnerUpdateView
from django.utils import timezone
from SmartNewsApp import views

urlpatterns = [
 	path('', TemplateView.as_view(template_name='funcHome.html'), name='func'),
    path('sources/', TemplateView.as_view(template_name='sources.html'), name='sources'),
    path('service2/', TemplateView.as_view(template_name='func2.html'), name='service2'),
    #Crear restaurants
    path('service3/',
        CreateView.as_view(
            model=Comment,
            template_name='comments.html',
            form_class=CommentForm),
        name='comment_create'),
    #Visualitzar restaurants
    path('comments/<int:pk>',
        DetailView.as_view(
            model=Comment,
            template_name='comment_detail.html'),
        name='comment_detail'),
    #Editar un comentari realitzat
    path('comment/<int:pk>/edit',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Comment,
            form_class=CommentForm),
        name='comment_edit'),

    #Llistar els 5 últims comentaris
    path('comment_list/',
        ListView.as_view(
            queryset=Comment.objects.filter(date__lte=timezone.now()).order_by('date')[:10],
            context_object_name='latest_comment_list',
            template_name='comment_list.html'),
        name='comment_list'),

    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='delete_comment'),
    path('news/', views.topnews, name='news'),
    path('sources/', views.sources, name='sources'),
    path('sources/BBC/', views.newsBBC, name='BBC'),
    path('sources/USATODAY/', views.newsUSATODAY, name='USATODAY'),
    path('sources/GoogleNews/', views.newsGoogleNews, name='GoogleNews'),
]
