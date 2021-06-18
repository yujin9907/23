from django.db import models

# Create your models here.

class Mall(models.Model):
    product = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    description = models.TextField() 

    def __str__(self):
        return self.product