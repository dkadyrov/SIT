from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings # new
from django.conf.urls.static import static # new
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.profile, name='user'),
    path('art/<int:art_id>/', views.art, name='art'),
    path('art/new/', views.art_new, name='art_new'),
    path('art/<int:art_id>/delete', views.art_delete, name="art_delete"),
    path('art/<int:art_id>/like', views.art_like, name="art_like")
    # path('login', auth_views.login, name='login'),
    # path('logout', auth_views.logout, name='logout'),
    # path('register', views.register, name='register')
    #path('art/like/<int:art_id>/', views.art_like, name='art_like'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)