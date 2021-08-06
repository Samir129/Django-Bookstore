from django.db import models

# Create your models here.
# Create Databases.


class Book(models.Model):

    def __str__(self) -> str:
        return self.name + '-' + self.author

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    book_image = models.CharField(max_length=1000)
