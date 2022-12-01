from django.urls import path
#from django.views.generic import IndexView
from django.views import View
from middle import views

app_name="middle"

urlpatterns = [
    path('', views.home,name="home"),
    path('excep/', views.excep,name="exception"),
    path('temp/', views.temp,name="template")
]