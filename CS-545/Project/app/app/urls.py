from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('artgen.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
]
