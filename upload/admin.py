from django.contrib import admin
from .models import Document


class ModelDocument(admin.ModelAdmin):
    list_display = ('title', 'author', 'email1', 'email2', 'email3', 'email4', 'email5', 'pdf')
    search_fields = ('author', 'title')
    list_filter = ('title', 'author')


admin.site.register(Document, ModelDocument)
