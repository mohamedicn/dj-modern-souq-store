from django.shortcuts import render
from.models import Product
from django.core.paginator import Paginator

# Create your views here.

def product_list(request):
    product_list=Product.objects.all()
    paginator = Paginator(product_list, 6) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    name = ''
    if 'searchname' in request.GET:
        product_list1=Product.objects.all()
        name = request.GET['searchname']
        if name:
            product_list = product_list1.filter(PRDname__icontains=name)
    context ={'product_list' : product_list}
    return render(request, 'Product/product_list.html',context)
    
def product_detail(request,slug):
    product_detail = Product.objects.get(slug=slug)
    context ={'product_detail' : product_detail}
    return render(request, 'Product/product_detail.html',context)