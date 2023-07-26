from django.db import models


class Customer(models.Model):
    FirstName=models.CharField(max_length=15)
    LastName=models.CharField(max_length=15)
    CustomerEmail=models.EmailField()
    CustomerPassword=models.CharField(max_length=200)
    CustomerPhoneNumber=models.CharField(max_length=15)


    def ifExists(self):
        return Customer.objects.filter(CustomerEmail=self.CustomerEmail)
    
    @staticmethod

    def get_customer_by_email(CustomerEmail):
        return Customer.objects.get(CustomerEmail=CustomerEmail)