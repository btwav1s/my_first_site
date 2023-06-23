from django.contrib import admin
# Register your models here.
from .models import Article, Category, Tag, Comment

class CommentItemInLine(admin.TabularInline):
    model = Comment
    raw_id_fields = ['article']
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title__iexact', 'content_preview', 'category__name']
    list_display = ['title','category','created_at',"updated_at"]
    list_filter = ['tags']
    prepopulated_fields = {'slug':("title",)}
    inlines = [CommentItemInLine]

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name',"slug"]
    list_filter = ['name']
    prepopulated_fields = {'slug':("name",)}

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email','content',"article"]
    list_display = ['name','email',"content","article"]
    list_filter = ['created_at','article']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)

