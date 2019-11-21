from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BookDetails(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=50,unique=True)
    num_of_books = models.IntegerField()
    rack_number = models.IntegerField()
    published_date = models.DateField(auto_now_add=True)
    author_id = models.ForeignKey(User,related_name="author_bookdetails")
    def __str__(self):
        return self.book_name