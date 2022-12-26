from django.shortcuts import HttpResponse, render
from products.models import Product, Review, Category


# Create your views here.
def main_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        categories_id = int(request.GET.get("category_id", 0))
        if categories_id:
            product = Product.objects.filter(category__in=[categories_id])
        else:
            product = Product.objects.all()
        return render(request, 'products/products.html', context={
            'products': product
        })


def product_detail_view(request, id):
    if request.method == 'GET':
        data = {
            'product': Product.objects.get(id=id),
            'reviews': Review.objects.all()
        }
        return render(request, 'products/detail.html', context=data)

def categories_view(request):
    if request.method =='GET':
        return render(request, 'categories/categories.html', context={
            'categories': Category.objects.all()
        })