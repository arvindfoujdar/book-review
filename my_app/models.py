from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    pages = models.IntegerField()
    review = models.TextField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title