from django.urls import path
from django.views import View
from product import views

app_name="product"
urlpatterns = [
     path('', views.ProductCreate.as_view(),name="productcreate"),
     path('list/', views.ProductList.as_view(),name="productlist"),
     path('update/<int:pk>/', views.ProductUpdate.as_view(),name="productupdate"),
     path('delete/<int:pk>/', views.ProductDelete.as_view(),name="productdelete"),
    # path('formview/', views.ProductFormView.as_view(),name="productformview"),
     path('detail/<int:pk>/', views.ProductDetail.as_view(),name="productdetail"),
     path('detail/<int:pk>/ordercreate/', views.OrderCreate.as_view(),name="ordercreate"),
]