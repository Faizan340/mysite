from django.urls import path
from django.views import View
from sign import views

app_name="sign"

urlpatterns = [
     path('', views.SignCreate.as_view(),name="signcreate"),
     path('list/', views.SignList.as_view(),name="signlist"),
     path('detail/<int:pk>/', views.SignDetail.as_view(),name="signdetail"),
     path('update/<int:pk>/', views.SignUpdate.as_view(),name="signupdate"),
     path('delete/<int:pk>/', views.SignDelete.as_view(),name="signdelete"),
     # path('formview/', views.UserFormView.as_view(),name="formview"),
]