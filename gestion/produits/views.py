from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

from .models import Product
from .products import products
from .forms import ProductForm

from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

#from .serializers import ProductSerializer
#from rest_framework.response import Response

# Create your views here.

class Home(View):
    def get(self,request):
        return render(request,'hello.html',{})
    

class ProductList(View):
    def get(self, request):
        products = Product.objects.all()

        # Recherche par nom
        query = request.GET.get('q')
        if query:
            products = products.filter(name__icontains=query)

        # Filtre par catégorie
        category = request.GET.get('category')
        if category and category != 'all':
            products = products.filter(category=category)

        # Filtre par stock
        stock = request.GET.get('stock')
        if stock == 'available':
            products = products.filter(countInStock__gt=0)
        elif stock == 'out':
            products = products.filter(countInStock=0)

        # Obtenir les catégories distinctes pour le filtre
        categories = Product.objects.values_list('category', flat=True).distinct()

        context = {
            'produits': products,
            'categories': categories,
            'search_query': query or '',
            'selected_category': category or 'all',
            'selected_stock': stock or '',
        }
        return render(request, 'listproducts.html', context)

    
class ProductDetail(View):
    def get(self, request, id):  
        produit = Product.objects.get(id=id)
        return render(request, 'ProductDetail.html', {'produit': produit})

class ProductCreate(View):
    def get(self,request):
        form=ProductForm()
        return render(request,'productCreate.html',{'form':form})
    
    def post(self,request):
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/')
        return render(request,'productCreate.html',{'form':form})
    
class ProductUpdate(View):
    def get(self,request,id):
        product = Product.objects.get(id=id)
        form=ProductForm(instance=product)
        return render(request,'productCreate.html',{'form':form})
    
    def post(self,request,id):
        product = Product.objects.get(id=id)
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/')
        return render(request,'productCreate.html',{'form':form})
    

class ProductDelete(View):
    def post(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect('/products/')

    
    def get(self, request, id):
        # Render a confirmation page (optional)
        product = Product.objects.get(id=id)
        return render(request, 'productDeletConfirm.html', {'product': product})

@require_POST
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')
