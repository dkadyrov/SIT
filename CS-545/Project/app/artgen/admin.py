from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Art)
# admin.site.register(Profile)
admin.site.register(Like)