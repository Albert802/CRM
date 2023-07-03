from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    tag  = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.tag

class Product(models.Model):
    CATEGORY =(('Indoor','Indoor'),
               ('Out Door','Out Door'),
               )
    tag = models.ManyToManyField(Tag)
    name = models.CharField(max_length=250,null=True)
    price = models.FloatField(max_length=250,null=True)
    category = models.CharField(max_length=250,null=True,choices=CATEGORY)
    description = models.CharField(max_length=250,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name



class Customer(models.Model):
    profile_pic = models.FileField(default='dijo.jpg',null=True,blank=True)
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=250,null=True)
    phone = models.CharField(max_length=250,null=True)
    email = models.CharField(max_length=250,null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)

class Order(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('Out for delivery','Out for delivery')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=250, null=True,choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    product= models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.product)


















