from django.urls import path

from .views import details

urlpatterns = [
    path('<int:id>/', details, name='details'),
]