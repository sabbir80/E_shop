from django.db import models
import datetime

from.Product import Product
from.Customer import Customer
class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price= models.IntegerField()
    address= models.CharField(max_length=50,default='',null=True)
    phone=models.CharField(max_length=50,default='',null=True)
    date=models.DateField(default=datetime.datetime.today())