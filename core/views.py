from django.shortcuts import render

def frontpage(request):
    articles = [
        {'id': 1, 'tittle': 'First article', 'content':'This is a first article'},
        {'id': 2, 'tittle': 'Second article', 'content':'This is a second article'},
        {'id': 3, 'tittle': 'Third article', 'content':'This is a third article'},
        {'id': 1, 'tittle': 'Fourth article', 'content':'This is a fourth article'},
        {'id': 2, 'tittle': 'Fifth article', 'content':'This is a fifth article'},
        {'id': 3, 'tittle': 'Sixth article', 'content':'This is a sixth article'}
    ]
    return render(request,'core/frontpage.html',{'articles': articles})

# Create your views here.
