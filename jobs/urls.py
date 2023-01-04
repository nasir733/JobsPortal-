from django.urls import path
from.views import wwwrScrapper

urlpatterns=[
    path('',wwwrScrapper,name='indeedScrapper'),
]