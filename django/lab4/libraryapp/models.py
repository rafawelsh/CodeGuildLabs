from django.db import models
from datetime import datetime

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now=False)
    author_name =  models.ManyToManyField('Author', related_name='books')

    def __str__(self):
        return self.title

class Author(models.Model):
    author_name = models.CharField(max_length=100)
    # books = models.ForeignKey('Book', on_delete=models.CASCADE)

    def __str__(self):
        return self.author_name

class Checks(models.Model):
    books = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.TextField(max_length=70)
    checkout = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.user



# Author: a model representing an author of a book, one author can have multiple books

# Version 2
# Add another model to keep track of who checked out a book and when. When a user checks a book back in, record that too. Add a text input on the 'checkout' page to record the name of who checked out the book. Have a page to show all the checkouts and returns.
#
# The new model can have the following fields:
#
# book: the book that the user checked out or checked in
# user: a text field containing the name of the user that checked out or checked in the book
# checkout: a boolean indicating whether the book was checked out or checked in
# timestamp: a datetime that records when the book was checked out or in
