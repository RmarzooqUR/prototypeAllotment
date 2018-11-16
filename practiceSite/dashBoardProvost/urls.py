from django.urls import path
from . import views

app_name = 'dashBoardProvost'

urlpatterns = [
    path('', views.IndexView.as_view(), name='provostIndex'),
    path('upload/', views.modelFormUpload, name='upload'),
    path('login/', views.login_view, name='login_view'),
    path('logged_in/', views.logged_in, name='logged_in'),
    path('InitializeHostelForm/',views.InitializeHostelView,name='InitializeHostelForm'),
    path('Allotment/',views.AllotmentView,name='Allotment')
]
