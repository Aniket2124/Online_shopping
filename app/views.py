from unicodedata import category
from django.shortcuts import render
from .models import Customer,Product,Cart,OrderPlaced
from django.views import View

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        topwear = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BM')
        mobile = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')
        return render(request,'app/home.html',{'topwear':topwear,'bottomwear':bottomwear,'mobile':mobile,'laptop':laptop})

# def product_detail(request):
#     return render(request, 'app/productdetail.html')


class ProductDetailView(View):
    def get(self,request,pk): 
        product =Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if data==None:
        mobiles = Product.objects.filter(category='M')
    elif data== 'Xiomi' or data== 'Samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'Realme' or data=='Apple':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)    
    
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)

    return render(request, 'app/mobile.html',{'mobiles':mobiles})

def laptop(request,data=None):
    if data==None:
        laptop = Product.objects.filter(category='L')
    elif data== 'Dell' or data== 'Lenovo':
        laptop = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'above':
        laptop = Product.objects.filter(category='L').filter(discounted_price__gt=50000)    
    
    elif data == 'below':
        laptop = Product.objects.filter(category='L').filter(discounted_price__lt=50000)

    return render(request, 'app/laptop.html',{'laptop':laptop})

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
