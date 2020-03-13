from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
 	path('', TemplateView.as_view(template_name='funcHome.html'), name='func'),
    path('service1/', TemplateView.as_view(template_name='func1.html'), name='service1'),
    path('service2/', TemplateView.as_view(template_name='func2.html'), name='service2'),
]
