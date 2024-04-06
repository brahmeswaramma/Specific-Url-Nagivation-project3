from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('sindhu/',sindhu,name='sindhu'),
    path('mithaliraj/',mithaliraj,name='mithaliraj'),
]