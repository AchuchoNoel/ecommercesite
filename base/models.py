from django.db import models

# Create your models here.

class Item_type(models.Model):
    product_name = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name


class Shop(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    item_type = models.ForeignKey(Item_type, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    visited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    



    
    