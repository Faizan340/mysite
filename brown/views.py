from django.shortcuts import render
from brown.models import UserProfile
from brown.forms import UserForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
class UserCreate(CreateView):
    model = UserProfile
    #templates = "templates/userprofile_form.html"
    fields = "__all__"
    success_url ="/"
    
class UserList(ListView):
 
    
    model = UserProfile
    fields = "__all__"

class UserDetail(DetailView):
   
    model = UserProfile

class UserUpdate(UpdateView):

    model = UserProfile
 
   
    fields = "__all__"

    success_url ="/"

class UserDelete(DeleteView):
    
    model = UserProfile
    
    success_url ="/"

class UserFormView(FormView):
    form_class = UserForm

    template_name = "brown/userprofile_form.html"

    success_url ="/thanks/"
