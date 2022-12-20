from django.shortcuts import HttpResponse, render
from posts.models import Product
# Create your views here.

def Products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request,"products/products.html",context={
            'products':products
        })
