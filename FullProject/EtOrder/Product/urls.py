from django.urls import path

from Product import views 
urlpatterns = [
    
     # urls for Product
   
    path('', views.CompanyListView.as_view(), name='Company_company_list'),
    path('products/company/<slug:slug>/', views.ProductListView.as_view(), name='Product_product_list'),
    path('product/detail/<slug:slug>/', views.ProductDetailView.as_view(), name='Product_product_detail'),

    # urls for order
    path('orders/', views.OrderListView.as_view(), name='Product_order_list'),
    #path('order/conformed/', views.order_conform, name='Product_order_conform'),
    path('order/create/<slug:slug>', views.OrderCreateView.as_view(), name='Product_order_create'),
    path('order/detail/<slug:slug>/', views.OrderDetailView.as_view(), name='Product_order_detail'),
   
]
