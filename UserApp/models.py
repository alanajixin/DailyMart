from django.db import models
from AdminApp.models import Product
# Create your models here.

class Contact(models.Model):
    Name=models.CharField(max_length=300)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    Subject=models.CharField(max_length=400)
    Message=models.TextField()

class Register(models.Model):
    Name=models.CharField(max_length=400)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
class Cart(models.Model):
    userid=models.ForeignKey(Register,on_delete=models.CASCADE)
    productid=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    status=models.IntegerField(default=0)
    
class Checkout(models.Model):
    userid=models.ForeignKey(Register,on_delete=models.CASCADE)
    cartid=models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    
    
    country=models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=200)
    district=models.CharField(max_length=300)
    state=models.CharField(max_length=200)
    zip=models.CharField(max_length=20)
    status=models.IntegerField(default=0)

class Complaint(models.Model):
    userid=models.ForeignKey(Register,on_delete=models.CASCADE)
    compid=models.ForeignKey(Checkout,on_delete=models.CASCADE,null=True)
    issue=models.TextField()
    status=models.IntegerField(default=0)

class Replay(models.Model):
    userid=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    complaintid=models.ForeignKey(Complaint,on_delete=models.CASCADE,null=True)
    message=models.TextField()
   