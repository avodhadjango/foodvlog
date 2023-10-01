from django.shortcuts import render, get_object_or_404
from unicodedata import category

from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def allProdCat(request, c_slug=None,products=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        products_list=products.objects.filter(category=c_page,available=True)
    else:
        products_list=products.objects.all().filter(available=True)
        paginator=Paginator(products_list,3)
        try:
            page=int(request.GET.get('page','1'))
        except:
            page=1
        try:
            products=paginator.page(page)
        except (EmptyPage,InvalidPage):
            products=paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'category': c_page ,'products':products})


def prodDetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category_slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'pr':prod})


def searching():
    return None