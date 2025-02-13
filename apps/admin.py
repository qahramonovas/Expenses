from distutils.command.register import register

from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'type')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_editable = ('name', 'icon', 'type')
    list_per_page = 20