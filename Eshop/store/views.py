from django.shortcuts import render,HttpResponse, redirect
from django.shortcuts import render
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.order import Order
from django.views import View
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password,check_password
import requests

# Create your views here.

class Index(View):


    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    cart[product]= quantity-1
                    if quantity<=1:
                        cart.pop(product)
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1


        request.session['cart']=cart
        return redirect('http://127.0.0.1:8000/')



    def get(self, request):
        cart=request.session.get('cart')
        if not cart:
            request.session.cart={}
        product=None
        category=Category.get_all_categories()
        categoryId=request.GET.get('category')
        if categoryId:
            product=Product.get_all_products_by_id(categoryId)
        else:
            product=Product.get_all_products()
        data={}
        data['Products']=product
        data['Categories']=category
        return render(request,'index.html',data)

 
class SignUp(View):
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self,request):
        first_name=request.POST.get("FirstName")
        last_name=request.POST.get('LastName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        number=request.POST.get('PhoneNumber')

        customer=Customer(FirstName=first_name, LastName=last_name, CustomerEmail=email, CustomerPassword=password, CustomerPhoneNumber=number )
        value={
            'first_name':first_name,
            'last_name':last_name,
            'email':email,
            'number':number
        }

        error=None
        if (not first_name):
            error='FirstName required'
        elif (not last_name):
            error='LastName required'
        elif (not email):
            error='Email required'
        elif (not password):
            error='Password is Requires'
        elif(len(password)<8):
            error='Password must be greater than 8 characters'
        elif (not number):
            error="Phone Number is required"
        elif customer.ifExists():
            error="Email Already exists"
        else:
            error=None


        if (not error):
            customer.CustomerPassword=make_password(customer.CustomerPassword)
            customer.save()
            return render(request,'signup.html')
        else:
            data ={
                'error':error,
                'value':value
            }
            return render(request,'signup.html',data)


class Login(View):

    def get(self,request):
        return render(request,'login.html')
    

    def post(self,request):
        error=None
        email=request.POST.get('email')
        password=request.POST.get('password')
        NewCustomer=Customer.get_customer_by_email(email)
        if NewCustomer:
            flag= check_password(password,NewCustomer.CustomerPassword)
            if flag:
                request.session['customer']=NewCustomer.pk
                return redirect('http://127.0.0.1:8000/')
            else:
                error='Password is incorrect!'
                return render(request,'login.html',{'error':error})
        else:
            error="Account Does not exist"
            return render(request,'login.html',{'error':error})


def logout(request):
    request.session.clear()
    return redirect('login')


class cart(View):
    def get(self,request):
        ids=(list(request.session.get('cart').keys()))
        products=Product.get_products_by_id(ids)
        return render(request ,'cart.html',{'products' : products})
    

class checkout(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))

        for product in products:
            order=Order(Customer_id=customer,
                        Customer_address=address,
                        Customer_Phone_Number=phone,
                        Product_id=product.pk,
                        Price=product.ProductPrice,
                        ProductQuantity=cart.get(str(product.pk)))
            order.save()

        request.session['cart']={}
        return redirect('cart')
    
class order(View):

    @method_decorator(auth_middleware)
    def get(self,request):
        customer=request.session.get('customer')
        orders=Order.get_orders_by_customerid(customer)
        print(orders)
        return render(request,'order.html',{'orders':orders})