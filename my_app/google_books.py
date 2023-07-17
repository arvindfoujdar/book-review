import requests

API_KEY = '' 

def search_books(query=None, max_results=24 , start_index=0,orderBy='relevance'):
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q' : query ,
        'key': API_KEY,
        'maxResults': max_results,
        'startIndex': start_index,
        'printType' : 'books' ,
        'filter' : 'ebooks' ,
        'orderBy' : orderBy ,
        'projection' : 'lite',
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    books = []
    
    if 'items' in data:
        for book in data['items']:
            book_info = book['volumeInfo']
            title = book_info.get('title')
            authors = book_info.get('authors', [])
            category = book_info.get('publisher')
            book_id = book['id']
            # Extracting year of publication
            published_date = book_info.get('publishedDate')
            year_ = published_date.split('-')[0] if published_date else None
            
            thumbnail = book_info.get('imageLinks', {}).get('thumbnail')
            
            book_data = {
                'title': title,
                'authors': authors,
                'thumbnail': thumbnail ,
                'release_year' : year_ ,
                'book_id' : book_id ,
                'category' : category ,
            }
            
            books.append(book_data)
    
    return books



def book_data(volume_id=None) :
    url = f'https://www.googleapis.com/books/v1/volumes/{volume_id}'
    params = {
        'key': API_KEY,
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    book_info = data.get('volumeInfo')
    title = book_info.get('title')
    authors = book_info.get('authors', [])
    description = book_info.get('description')
    categories = book_info.get('categories', [])
    publisher = book_info.get('publisher')
    published_date = book_info.get('publishedDate')
    rating = book_info.get('averageRating')
    page_count = book_info.get('pageCount')
    thumbnail = book_info.get('imageLinks', {}).get('thumbnail')
    preview_link = book_info.get('previewLink')
    
    book = {
        'title': title,
        'authors': authors,
        'description': description,
        'categories': categories,
        'publisher': publisher,
        'published_date': published_date,
        'thumbnail': thumbnail,
        'preview_link': preview_link,
        'rating' : rating ,
        'page_count' : page_count ,
    }
    
    return book


def get_related_books(category, max_results=12):
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q' : category,
        'key': API_KEY,
        'maxResults': max_results
    }

    response = requests.get(url, params=params)
    data = response.json()

    related_books = []

    if 'items' in data:
        for book in data['items']:
            book_info = book['volumeInfo']
            title = book_info.get('title')
            authors = book_info.get('authors', [])
            category = book_info.get('categories',[])
            book_id = book['id']
            # Extracting year of publication
            published_date = book_info.get('publishedDate')
            year_ = published_date.split('-')[0] if published_date else None
            
            thumbnail = book_info.get('imageLinks', {}).get('thumbnail')
            
            book_data = {
                'title': title,
                'authors': authors,
                'thumbnail': thumbnail ,
                'release_year' : year_ ,
                'book_id' : book_id ,
                'category' : category ,
            }
            
            related_books.append(book_data)
    else: 
        print("no data")
    return related_books
