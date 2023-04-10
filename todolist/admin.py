from django.contrib import admin

from .models import ToDo, Post

# Register your models here.

admin.site.register(ToDo)
admin.site.register(Post)
