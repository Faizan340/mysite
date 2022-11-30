from django.shortcuts import render,redirect,HttpResponse
from inheritApp.models import SameModel, StudentModel,TeacherModel,ParentModel,LaptopModel,LaptopUserModel,LocationModel
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from product.forms import ProductForm,OrderDetailForm


class InheritCreate(CreateView):
    model = StudentModel
    fields = "__all__"
    # template_name = ""
    

    def form_valid(self,form):
        form.save()
        return redirect('inheritApp:inheritcreate')



class InheritList(ListView):
 
    
    model = StudentModel
    fields = "__all__"

class InheritDetail(DetailView):
   
    model = StudentModel
    fields = "__all__"


class InheritTeachCreate(CreateView):
    model = TeacherModel
    fields = "__all__"
    # template_name = ""
    

    def form_valid(self,form):
        form.save()
        return redirect('inheritApp:inheritteachcreate')

class InheritParentCreate(CreateView):
    model = ParentModel
    fields = "__all__"
    # template_name = ""
    

    def form_valid(self,form):
        form.save()
        return redirect('inheritApp:inheritparcreate')

class LapCreate(CreateView):
    model = LaptopModel
    fields = "__all__"
    # template_name = ""
    

    def form_valid(self,form):
        form.save()
        return redirect('inheritApp:inheritlapcreate')

class LapDetail(DetailView):
   
    model = LaptopModel
    fields = "__all__"

class LapUserCreate(CreateView):
    model = LaptopUserModel
    fields = "__all__"
    # template_name = ""

class LapUserDetail(DetailView):
   
    model = LaptopUserModel
    fields = "__all__"
    

    def form_valid(self,form):
        form.save()
        return redirect('inheritApp:inheritlapusercreate')

class LocaionCreate(CreateView):
    model = LocationModel
    fields = "__all__"
    # template_name = ""
    

    def form_valid(self,form):
        form.save()
        return redirect('inheritApp:inheritlocationcreate')

class LocationDetail(DetailView):
   
    model = LocationModel
    fields = "__all__"