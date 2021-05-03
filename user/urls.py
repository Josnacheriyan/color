from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index1', views.index1, name='index1'),
    path('about', views.about, name='about'),
]