from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Customer_address=models.CharField(max_length=100,default="")
    Customer_Phone_Number=models.CharField(max_length=15,default="")
    ProductQuantity=models.IntegerField(default=1)
    Price=models.IntegerField()
    date=models.DateField(default=datetime.datetime.today)
    Order_status=models.BooleanField(default=False)



    @staticmethod
    def get_orders_by_customerid(customer_id):
        return Order.objects.filter(Customer=customer_id)