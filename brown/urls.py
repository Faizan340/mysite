from django.urls import path
#from django.views.generic import IndexView
from django.views import View
from brown import views
from brown.views import UserCreate,UserList

urlpatterns = [
    path('', views.UserCreate.as_view(),name="index"),
    path('list/', views.UserList.as_view(),name="userlist"),
    path('detail/<int:pk>/', views.UserDetail.as_view(),name="userdetail"),
    path('update/<int:pk>/', views.UserUpdate.as_view(),name="userupdate"),
    path('delete/<int:pk>/', views.UserDelete.as_view(),name="userdelete"),
    path('formview/', views.UserFormView.as_view(),name="formview"),
]