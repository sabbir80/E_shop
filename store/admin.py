from django.contrib import admin
from .models import Product, Category
from .models.Customer import Customer
from.models.orders import Orders

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
class AdminCustomer(admin.ModelAdmin):
    list_display=['first_name','last_name' ,'email', 'phone']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Orders)