from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('msd/',msd,name='msd'),
    path('virat/',virat,name='virat'),
]