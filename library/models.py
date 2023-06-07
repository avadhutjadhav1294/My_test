from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.IntegerField()
    author = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta: 
        db_table = 'book'