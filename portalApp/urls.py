from django.urls import path
from .views import home,about,news_detail

app_name='portalApp'
urlpatterns=[
    path('',home,name='home'),
    path('about',about,name='about'),
    path('news_detail/<int:id>',news_detail,name='news_detail'),
]