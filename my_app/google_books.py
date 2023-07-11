import requests

API_KEY = ' ' # API key here

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
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    books = []
    
    if 'items' in data:
        for book in data['items']:
            book_info = book['volumeInfo']
            title = book_info.get('title')
            authors = book_info.get('authors', [])
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
            }
            
            books.append(book_data)
    
    return books
