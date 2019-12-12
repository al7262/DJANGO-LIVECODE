from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, default=0, max_digits=10)
    photo = models.CharField(max_length=1000, name='Photo URL', default=None)
    detail = models.TextField()
    
    def __str__(self):
        return self.name