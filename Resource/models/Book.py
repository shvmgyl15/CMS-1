from django.db import models
#from Resource.models import Resource


class BookManager(models.Manager):
    def addBook(self,request):
        B = Book(
            bookId = request['bookId'],
            name = request['name'],
            authors = request['authors'],
            edition = request['edition'],
            type = request['type'],
            publisher = request['publisher']
        )

        B.save()
        return B
class Book(models.Model):
    TEXT_BOOK = 0
    REFERENCE_BOOK = 1
    BOOK_TYPE_CHOICES = ( (TEXT_BOOK, 'Text Book'), (REFERENCE_BOOK, 'Reference Book') )

    bookId = models.ForeignKey('Resource.Resource', on_delete=models.CASCADE, default=False, primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    authors = models.CharField(max_length=50)
    edition = models.CharField(max_length=20)
    type = models.PositiveIntegerField(choices=BOOK_TYPE_CHOICES, null=False, blank=False)
    publisher = models.CharField(max_length=50)

    def __str__(self):
        return self.name+ "-" +self.authors+ "-" +self.edition