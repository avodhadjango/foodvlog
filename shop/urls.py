from django.urls import path
from.import views

urlpatterns=[
    path('<slug:c_slug>/',views.products,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.prodDetails,name='details'),
    path('search',views.searching,name='search'),
]
