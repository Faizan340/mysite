from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from product.models import ProductModel,CategoryModel,OrderDetailModel
from product.forms import ProductForm,OrderDetailForm
from django.urls import reverse_lazy,reverse

class ProductCreate(CreateView):
    model = ProductModel
    form_class = ProductForm
    template_name = "product/productmodel_form.html"
    

    def form_valid(self,form):
        form.save()
        return redirect('product:productcreate')



class ProductDetail(DetailView):
    model = ProductModel
    

class ProductList(ListView):
    model = ProductModel
    template_name = 'product/product.html'

class ProductDelete(DeleteView):
    model = ProductModel
    template_name = "product/productmodel_confirm_delete.html"

    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('product:productlist')

    # def get_success_url(self,pk):
    #      return reverse('product:productlist', pk = self.kwargs['pk'])

    # def form_valid(self, form):  
    #     form.save()
    #     return redirect('product:productlist', pk = self.kwargs['pk'])

class ProductUpdate(UpdateView):
    model = ProductModel
    form_class: ProductForm
    fields = "__all__"

    
    def form_valid(self, form):  
        form.save()
        return redirect('product:productdetail', pk = self.kwargs['pk'])


class OrderCreate(CreateView):
    model = OrderDetailModel
    form_class = OrderDetailForm
    template_name = "product/orderdetailmodel_form.html"
    
    def form_valid(self,form):
        order = form.save()
        print(order.quantity)
        print('helloooooooooooooooooooo')
        product = ProductModel.objects.get(id=order.product.id)
        product.quantity = product.quantity - order.quantity
        product.save()

        return redirect('product:ordercreate', pk = self.kwargs['pk'])

    def remaining_quantity(self):
        return self.productname.quantity - self.quantity




# class UserFormView(FormView):
#     form_class = ProductForm

#     template_name = "product/productmodel_form.html"
