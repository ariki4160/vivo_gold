# -*- coding: utf-8 -*-

from django.contrib import admin
from myproject.myapp.models import Author

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Blog, Comment)
