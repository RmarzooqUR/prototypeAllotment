from django.urls import path
from . import views
app_name = 'fileUploads'
urlpatterns = [
    path('',views.IndexView.as_view(),name = 'index'),
    path('upload/',views.modelFormUpload, name = 'upload'),
]