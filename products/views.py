from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .forms import ProductForm
from django.http import Http404
# Create your views here.
def product_view(request):
    obj= Product.objects.get(id=1)
    context={
        'Object':obj
    }
    return render(request,"product/detail.html", context)



#create
def product_create_view(request):
    form =ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ProductForm()
    context={
        'form': form
    }
    return render(request,"product/create.html", context)


#dynamic rendering
def dynamic_lookup_view(request,id):
    obj=Product.objects.get(id=id)
    try:
        obj=Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404

    context={
        "Object":obj
    }
    return render(request,"product/detail.html",context)



#product deletion
def product_delete_view(request,id):
    obj=get_object_or_404(Product,id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context={
        "Object":obj
    }
    return render(request,"product/delete.html",context)


#update
def product_update_view(request,id):
    obj=get_object_or_404(Product,id=id)
    form=ProductForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
    context={
        'form':form
    }
    return render(request,"product/create.html",context)


#rendering products in listFormat
def product_list_view(request):
    queryset = Product.objects.all()
    context={
        "object_list":queryset
    }
    return render(request,"product/list.html",context)
