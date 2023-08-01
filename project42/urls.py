"""
URL configuration for project42 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Data_render/',Data_render.as_view(),name='Data_render'),
    path('fbv_form/',fbv_form,name='fbv_form'),
    path('Cbv_form/',Cbv_form.as_view(),name='Cbv_form'),
    path('Temp/',Temp.as_view(),name='Temp'),
    path('cbv_direct/',TemplateView.as_view(template_name='cbv_direct.html'),name='cbv_direct'),


]
