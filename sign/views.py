from django.shortcuts import render,redirect,HttpResponse
from sign.models import SignModel,SignalModel
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from product.forms import ProductForm,OrderDetailForm


class SignCreate(CreateView):
    model = SignModel
    fields = "__all__"
    # template_name = ""
    

    def form_valid(self,form):
        form.save()
        return redirect('sign:signcreate')

class SignList(ListView):
 
    
    model = SignalModel
    fields = "__all__"

class SignDetail(DetailView):
   
    model = SignalModel

class SignUpdate(UpdateView):

    model = SignalModel
 
   
    fields = "__all__"

    success_url ="/"

class SignDelete(DeleteView):
    
    model = SignalModel
    
    success_url ="/"