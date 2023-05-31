from django.shortcuts import render

def frontpage(request):
    return render(request,'core/base.html',{'name':'German','hobbies':["Python","English","Sport"]})

# Create your views here.
