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

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'my_app/book_detail.html', {'book': book})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    books = search_books(category)
    return render(request, 'my_app/category_detail.html', {'category': category, 'books': books})

def base(request):
    categories = Category.objects.all()
    return render(request, 'my_app/base.html', {'categories': categories})


# def search(request):
#     query = request.GET.get('q')
#     results = Book.objects.filter(title__icontains=query)
#     return render(request, 'my_app/search_results.html', {'results': results, 'query': query})

# def search(request):
#     query = request.GET.get('q')
#     books = search_books(query)

#     context = {
#         'books': books,
#         'query': query
#     }
#     return render(request, 'my_app/search_results.html', context)

def search(request):
    query = request.GET.get('q')
    page_number = request.GET.get('page', 1)  
    
    books_per_page = 16  # Number of books to display per page
    start_index = (page_number - 1) * books_per_page
    
    books = search_books(query, max_results=books_per_page, start_index=start_index)
    
    books_per_page = 8
    paginator = Paginator(books, books_per_page)
    page_obj = paginator.get_page(page_number)

    total_pages = paginator.num_pages
    has_previous_page = page_obj.has_previous()
    has_next_page = page_obj.has_next()
    
    context = {
        'books': page_obj,
        'query': query,
        'total_pages': total_pages,
        'has_previous_page': has_previous_page,
        'has_next_page': has_next_page,
    }
    return render(request, 'my_app/search_results.html', context)
