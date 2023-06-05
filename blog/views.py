from django.shortcuts import render, get_object_or_404

from .models import Article
# Create your views here.
def details(request, id):
    article = Article.objects.get_object_or_404(id=id)
    return render(request,'blog/details.html',{'article':article})