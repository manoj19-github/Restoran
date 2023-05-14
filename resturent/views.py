from django.shortcuts import render
from .models import Products
def index(request):
    product1 = Products()
    product1.name = 'chicken tadka'
    product1.price = 456
    product1.desc =  'an awesome indian poroduct'
    product1.img = 'menu-1.jpg'
    
    product2 = Products()
    product2.name = 'chicken Biriyani'
    product2.price = 560
    product2.desc =  'chicken Biriyani'
    product2.img = 'menu-2.jpg'
    
    product3 = Products()
    product3.name = 'chicken Chap'
    product3.price = 900
    product3.desc =  'chicken chap'
    product3.img = 'menu-4.jpg'
    
    product4 = Products()
    product4.name = 'Paneer Tikka'
    product4.price = 150
    product4.desc =  'Paneer Tikka'
    product4.img = 'menu-5.jpg'
    
    product5 = Products()
    product5.name = 'Paneer Masala'
    product5.price = 850
    product5.desc =  'Paneer Masala'
    product5.img = 'menu-6.jpg'
    products = [product1, product2, product3, product4, product5]
    return render(request,"index.html",{'products':products})
# Create your views here.
