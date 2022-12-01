from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse 

def home(request):
    print("I am a View")
    return HttpResponse("This is home page.")

def excep(request):
    print("I am exception view")
    a = 10/0
    return HttpResponse("Exception Page")

def temp(request):
    print("Template response view")
    context = {'name':'James'}
    return TemplateResponse (request, 'middle/temp.html', context)