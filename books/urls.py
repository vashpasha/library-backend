from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    BookListAPI,
    BookDetailAPI,
    BookCreateAPI,
    BookUpdateAPI, 
    BookDeleteAPI,
    UserBookRelationAPI
)

urlpatterns = [
    path('', BookListAPI.as_view(), name='book-list'),
    path('create/', BookCreateAPI.as_view(), name='book-create'),

    path('<int:pk>/', BookDetailAPI.as_view(), name='book-detail'),
    path('<int:pk>/update/', BookUpdateAPI.as_view(), name='book-update'),
    path('<int:pk>/delete/', BookDeleteAPI.as_view(), name='book-delete'),

    path('r/', UserBookRelationAPI.as_view(), name='relation'),
]
