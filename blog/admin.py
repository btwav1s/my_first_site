from django.contrib import admin
# Register your models here.
from .models import Article, Category, Tag

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title__iexact', 'content_preview', 'category__name']
    list_display = ['title','category','created_at',"updated_at"]

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)

