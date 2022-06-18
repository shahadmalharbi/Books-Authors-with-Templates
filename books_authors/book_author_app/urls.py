from django.urls import path  
from . import views         
urlpatterns = [
    path('', views.books),
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.view_book),
    path('add_auth_to_book/<int:book_id>', views.add_auth_to_book), #Adding an author to a single Book
    path('authors', views.authors), #Main Authors page
    path('add_author', views.add_author), #Adding a single author on the Main Authors page
    path('authors/<int:author_id>', views.view_author), #The page for a single Author
    path('add_book_to_auth/<int:author_id>', views.add_book_to_auth) 
]