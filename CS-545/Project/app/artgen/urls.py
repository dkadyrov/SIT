from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.profile, name='user'),
    path('art/<int:art_id>/', views.art, name='art'),
    path('art/new/', views.art_new, name='art_new'),
    # path('login', auth_views.login, name='login'),
    # path('logout', auth_views.logout, name='logout'),
    # path('register', views.register, name='register')
]
