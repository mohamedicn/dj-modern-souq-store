from django.shortcuts import render
from django.views.generic import ListView ,DetailView ,CreateView
from django.contrib.auth.models import User
from.models import *
from django.views.generic.edit import FormMixin
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from settings.models import Nav_ads
# Create your views here.


# class ProdcutListView(ListView):
#     model = Product
#     template_name = "product_list.html"
#     context_object_name='product_list'
#     def get_context_data(self, **kwargs):
#         context =super().get_context_data(**kwargs)
#         distinct_categories = context['product_list'].values_list('PRDcategory__CATName', flat=True).distinct()
#         context['category'] = distinct_categories
#         nav_img = Nav_ads.objects.all()
#         context['nav_img'] = nav_img
#         return context

class ProdcutListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = 'category_product_map'

    def get_queryset(self):
        categories = Category.objects.exclude(
            CATParent=None
        ).filter(
            CATParent__isnull=False,
            product__PRDIs_Active=True
        )
        
        category_product_map = {}
        for category in categories:
            products = Product.objects.filter(PRDcategory=category, PRDIs_Active=True)[:12]
            category_product_map[category.CATName] = products
        
        return category_product_map

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nav_img = Nav_ads.objects.all()
        context['nav_img'] = nav_img
        return context


# def product_list(request):
#     categories = Category.objects.exclude(CATParent=None).filter(CATParent__isnull=False,product__PRDIs_Active=True)
    
#     category_product_map = {}
#     for category in categories:
#         products = Product.objects.filter(PRDcategory=category, PRDIs_Active=True)[:12]
#         category_product_map[category.CATName] = products
    
#     context = {'category_product_map': category_product_map}
#     return render(request, 'products/product_list.html', context)

class ProdcutDetailView(DetailView):
    model = Product
    # template_name = "product_detail.html"
    context_object_name='product_detail'

class ProdcutListView_More(ListView):
    model = Product
    template_name = "products/product_list_more.html"
    context_object_name='product_list_more'
    paginate_by=18
    def get_queryset(self):
        category_name = self.kwargs.get('category_name')
        category = get_object_or_404(Category, CATName=category_name)
        products_in_category = Product.objects.filter(PRDcategory=category, PRDIs_Active=True)
        return products_in_category
    
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        distinct_categories = Category.objects.filter(
            product__in=context['product_list_more']
        ).distinct()
        context['category'] = distinct_categories
        return context
