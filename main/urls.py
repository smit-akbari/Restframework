from django.urls import path
from .views import BookList, BookDetail


urlpatterns = [
    path('books/', BookList, name='BookList'),
    path('books/<int:id>/', BookDetail, name='BookDetail'),
]
