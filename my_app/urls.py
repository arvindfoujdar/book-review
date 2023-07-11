from django.urls import path
from . import views
from django.contrib import admin 


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('books/<str:book_id>/', views.book_detail, name='book_detail'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('search/', views.search, name='search'),
]