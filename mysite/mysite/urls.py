"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from app1 import views
from django.contrib.auth import views as auth_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register('persons', views.PersonViewSet)
router.register('stations', views.StationViewSet, basename='station')
router.register('journeys', views.JourneyViewSet, basename='journey')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('submit/', views.submit_form),
    path('api/register/', views.register),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('api/login/', views.user_login),
    path('api/logout/', views.user_logout, name='logout'),
    path('api/login-set-cookie/', views.set_csrf_cookie, name='set-csrf-cookie'),
    path('api/current-user/', views.current_user, name='current-user'),
    path('api/autocomplete/', views.autocomplete, name='current-user'),
]
