import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_project.settings")
django.setup()

from my_app.models import Category, Book

# create your objects here
from my_app.models import Category, Book

# Create some categories
fiction = Category.objects.create(name="Fiction")
nonfiction = Category.objects.create(name="Non-Fiction")
mystery = Category.objects.create(name="Mystery")

# Create some books and assign them to categories
book1 = Book.objects.create(title="To Kill a Mockingbird", author="Harper Lee", pages=281, review="A classic novel about racial inequality in the American South.")
book1.category.add(fiction)

book2 = Book.objects.create(title="The Catcher in the Rye", author="J.D. Salinger", pages=224, review="A coming-of-age novel about a teenage boy struggling with his identity.")
book2.category.add(fiction)

book3 = Book.objects.create(title="Sapiens: A Brief History of Humankind", author="Yuval Noah Harari", pages=443, review="A thought-provoking book about the history of our species.")
book3.category.add(nonfiction)

book4 = Book.objects.create(title="The Da Vinci Code", author="Dan Brown", pages=489, review="A thrilling mystery novel about a secret society and the Holy Grail.")
book4.category.add(fiction, mystery)
