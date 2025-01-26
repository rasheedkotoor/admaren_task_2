from django.contrib import admin
from .models import Snippet, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_by', 'created_at')
    search_fields = ('title', 'note', 'tags')
    list_filter = ('created_by', 'tags')
