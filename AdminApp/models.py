from django.db import models

# Create your models here.
class Category(models.Model):
    categoryname=models.CharField(max_length=200)
    categoryimage=models.ImageField(upload_to='images',default='null.jpg')
    description=models.TextField()
class Product(models.Model):
    productname=models.CharField(max_length=300)
    productcategory=models.CharField(max_length=200)
    productimage=models.ImageField(upload_to='images',default='null.jpg')
    productprice=models.IntegerField()

