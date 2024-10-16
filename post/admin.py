from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'rate', 'created_at', 'updated_at', 'category']
    list_filter = ['rate']
    search_fields = ['title', 'content']
    list_editable = ['rate']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(models.Comment)
