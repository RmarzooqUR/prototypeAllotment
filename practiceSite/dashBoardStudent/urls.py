# from django.conf.urls import url
from django.urls import path
from dashBoardStudent import views

from . import views

app_name='dashBoardStudent'

urlpatterns=[
    path('login/', views.login_view, name='login_view'),
    path('logged_in/', views.logged_in, name='logged_in'),
    # path('', views.index, name='studentIndex')
]
