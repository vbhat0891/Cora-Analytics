"""untitled7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'coraapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('visualization/', views.visualization, name='visualization'),
    path('datasource/', views.datasource, name='datasource'),
    path('analysis/', views.analysis, name='analysis'),
    path('dataStudio_viz/', views.dataStudio_viz, name='dataStudio_viz'),
    path('vizData/', views.vizData, name='vizData'),
    path('sbData/', views.sbData, name='sbData'),
    path('seData/', views.seData, name='seData'),
    # path('forceNode/', views.forceNode, name='forceNode'),
    path('forceLink.json/', views.forceLink, name='forceLink'),
    path('sbart/', views.sbArt, name='sbArt'),
]
