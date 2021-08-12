from django.db import models
from django.urls import reverse

# Create your models here.
# Create Databases.


class Book(models.Model):

    def __str__(self) -> str:
        return self.name + '-' + self.author

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    book_image = models.CharField(max_length=1000)

    
