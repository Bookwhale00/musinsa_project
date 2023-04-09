from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

# 상품 등록
@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            print(form)
            return redirect('product-list')
        else:
            # 유효성 오류일 때 메시지
            error_msg = '올바른 상품정보를 입력해주세요.'
            return render(request, 'erp/product_create.html',{'form':form, 'error_msg':error_msg})
    else:
        form = ProductForm()
    return render(request, 'erp/product_create.html', {'form':form})

# 등록된 상품 보여주기
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'erp/product_list.html', {'products': products})