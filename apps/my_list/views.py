from django.shortcuts import render
from .models import Product

def index(request):
    Product.objects.create(name = "Apple", description = "delicious", weight = 12.5, price = 11.5, cost = 10.5, category = "food")
    product = Product.objects.all()
    print (product)
    return render(request, "my_list/index.html")

# Create your views here.
