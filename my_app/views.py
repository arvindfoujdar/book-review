from django.shortcuts import render,get_object_or_404
from .models import Book, Category
from .google_books import search_books
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    categories = Category.objects.all()
    books = search_books(query='latest release best')
    context = {
        'books': books,
    }
    return render(request, 'my_app/home.html', context)

def login(request):
    return render(request, 'my_app/login.html') 

def about(request):
    return render(request, 'my_app/about.html')

def book_detail(request):
    book_id = request.Get.get('book_id')

    return render(request, 'my_app/book_detail.html', {'book': book})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    books = search_books(category)
    return render(request, 'my_app/category_detail.html', {'category': category, 'books': books})

def base(request):
    categories = Category.objects.all()
    return render(request, 'my_app/base.html', {'categories': categories})




def search(request):
    query = request.GET.get('q')
    page_number = request.GET.get('page', 1) 
    
    books_per_page = 8  # Number of books to display per page
    start_index = (int(page_number) - 1) * books_per_page
    
    books = search_books(query, max_results=books_per_page, start_index=start_index)
    
    context = {
        'books': books,
        'query': query,
        'page' : int(page_number) ,
        # 'total_pages': total_pages,
        'previous_page': int(page_number) - 1,
        'next_page': int(page_number) + 1,
    }
    return render(request, 'my_app/search_results.html', context)
