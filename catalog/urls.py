from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name="home"),
    path('upload/', views.upload, name='upload-book'),
    path('update/<int:book_id>/', views.update_book,  name='update-book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete-book')
]

