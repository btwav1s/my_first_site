from django.contrib import admin
# Register your models here.
from .models import Article, Category, Tag

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title__iexact', 'content_preview', 'category__name']
    list_display = ['title','category','created_at',"updated_at"]
    list_filter = ['tags']

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name',"slug"]
    list_filter = ['name']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)

