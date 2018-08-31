from django.urls import path
from . import views
app_name = 'fileUploads'
urlpatterns = [
    path('',views.modelFormUpload, name = 'index'),
]