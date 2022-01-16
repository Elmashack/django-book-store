from django.urls import path
from .views import BookListView, BookDetailView, SearchListView, AddBookView

urlpatterns = [
    path('', BookListView.as_view(), name='books'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_page'),
    path('search/', SearchListView.as_view(), name='search'),
    path('add/', AddBookView.as_view(), name='add_book')
]
