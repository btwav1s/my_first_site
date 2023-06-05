from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='URL')
    content_preview = models.TextField(verbose_name='Превью статьи')
    content = models.TextField(verbose_name='Текст статьи')
    picture = models.TextField(verbose_name='Картинка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата написания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега')
    slug = models.SlugField(default='', verbose_name='URL')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"