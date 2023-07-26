from django.db import models
from .category import Category



class Product(models.Model):
    ProductName=models.CharField(max_length=20)
    ProductPrice=models.IntegerField(default=0)
    ProductDescription=models.CharField(max_length=100, null=True)
    ProductImage=models.ImageField(upload_to='uploads/productsImages/')
    ProductCategory=models.ForeignKey(Category, on_delete=models.CASCADE) 

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_id(category_id):
        return Product.objects.filter(ProductCategory=category_id)
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)


    
    




