<<<<<<< HEAD
# from django.conf.urls import url
from django.urls import path
from dashBoardStudent import views

app_name='dashBoardStudent'

urlpatterns=[
    path('login/', views.login_view, name='login_view'),
    path('logged_in/', views.logged_in, name='logged_in'),
]

=======
from django.urls import path
from . import views

app_name = 'dashBoardStudent'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]
>>>>>>> f87c35cdfb41f00f791689f123adeff759519f8f
