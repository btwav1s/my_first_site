from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='URL')
    content_preview = models.TextField(verbose_name='Превью статьи')
    content = models.TextField(verbose_name='Текст статьи')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='articles', default=1, verbose_name='Категория')
    tags = models.ManyToManyField('Tag', related_name="articles", verbose_name= "Теги", null=True)
    picture = models.TextField(verbose_name='Картинка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата написания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-created_at']

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(default='', verbose_name='URL')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название тега')
    slug = models.SlugField(default='', verbose_name='URL')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"