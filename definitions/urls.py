from django.urls import path
from .views import get_word, generator

urlpatterns = [
    path('', generator, name='gen'),
    path('<str:name>/', get_word, name='definitions'),
]