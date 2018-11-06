"""practiceSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include
from django.views.generic import RedirectView
from dashBoardStudent import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #path('',RedirectView.as_view(url='/accounts/login')),
    #path('admin/', admin.site.urls),
    #path('accounts/',include('django.contrib.auth.urls')),
    # path('polls/', include('polls.urls')),
    #path('fileUploads/',include('fileUploads.urls'))

    #url(r'^dashBoardStudent/$', include(dashBoardStudent.urls))
    path('admin/', admin.site.urls),
    path('dashBoardStudent/', include('dashBoardStudent.urls')),
    path('dashBoardProvost/', include('dashBoardProvost.urls')),
    path('', RedirectView.as_view(url='/homepage/')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('polls/', include('polls.urls')),
    path('fileUploads/', include('fileUploads.urls')),
    path('homepage/', include('homepage.urls'))
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
