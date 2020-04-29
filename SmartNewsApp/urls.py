from django.urls import path, include
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from SmartNewsApp.forms import CommentForm
from SmartNewsApp.models import Comment
from django.views.generic.detail import DetailView
from SmartNewsApp.views import LoginRequiredCheckIsOwnerUpdateView

urlpatterns = [
 	path('', TemplateView.as_view(template_name='funcHome.html'), name='func'),
    path('service1/', TemplateView.as_view(template_name='func1.html'), name='service1'),
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
]
