from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.order import Order


class AdminProduct(admin.ModelAdmin):
    list_display=['ProductName','ProductPrice','ProductCategory']


class AdminCategory(admin.ModelAdmin):
    list_display=['id','CategoryName']


class AdminCustomer(admin.ModelAdmin):
    list_display=['id','FirstName','LastName','CustomerEmail']


class AdminOrder(admin.ModelAdmin):
    list_display=['id','Customer_id']

# Register your models here.

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order,AdminOrder)
