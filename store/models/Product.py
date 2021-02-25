from django.db import models
from.Category import Category

class Product(models.Model):
    name= models.CharField(max_length=50)
    price= models.IntegerField(default=0)
    descrition= models.CharField(max_length=200, default='')
    category= models.ForeignKey(Category, on_delete= models.CASCADE, null=True)
    image= models.ImageField(upload_to= 'uploads/product', blank=True,null=True)

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)
