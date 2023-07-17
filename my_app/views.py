from django.shortcuts import render,get_object_or_404
from .models import Book, Category
from .google_books import search_books,book_data,get_related_books
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    categories = Category.objects.all()
    books = search_books(query='latest release best')
    context = {
        'books': books,
        'categories' : categories,
    }
    return render(request, 'my_app/home.html', context)


def about(request):
    return render(request, 'my_app/about.html')

def book_detail(request,book_id):
    book = book_data(volume_id = book_id)
    if book['categories'] :
                            query = book["categories"][0]
    else : query = book['authors'][0]

    related_books= get_related_books(category = query) 
    return render(request, 'my_app/book_detail.html', {'book': book,'related_books':related_books})

def category_detail(request,category_name):
    category = category_name
    cat ="+subject:" + category
    page_number =int( request.GET.get('page', 1) )
    
    books_per_page = 24  # Number of books to display per page
    start_index = (page_number - 1) * books_per_page

    books = search_books(cat, max_results=books_per_page, start_index=start_index)

    context = {
        'books': books,
        'category' : category ,
        'page': page_number ,
        'previous_page': int(page_number) - 1,
        'next_page': int(page_number) + 1,
    }
    return render(request, 'my_app/category_detail.html', context)

def base(request):
    categories = Category.objects.all()
    return render(request, 'my_app/base.html', {'categories': categories})




def search(request):
    query = request.GET.get('q')
    page_number = request.GET.get('page', 1) 
    
    books_per_page = 24  # Number of books to display per page
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
