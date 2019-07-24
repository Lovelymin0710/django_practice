from django.contrib import admin

from .models import Blog

admin.site.register(Blog)

def __str__(self):
    return self.title