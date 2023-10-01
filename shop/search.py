from django.db.models import Q
from django.shortcuts import render

from shop.models import products



def searching(request, q=None):
    prod=None
    query=None
    if q in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc_contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})