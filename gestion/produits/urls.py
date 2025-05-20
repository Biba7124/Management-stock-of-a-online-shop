from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('products/<int:id>',views.ProductDetail.as_view(),name='products_detail'),
    path('products/create/', views.ProductCreate.as_view(), name='product_create'),
    path('products/update/<int:id>/', views.ProductUpdate.as_view(), name='product_update'),
    path('products/delete/<int:id>/', views.ProductDelete.as_view(), name='product_delete') # Ajoute cette ligne pour la suppression
]
