from django.shortcuts import render, redirect

# Create your views here.


def product_create(request):
    return render(request, 'erp/product_create.html')
