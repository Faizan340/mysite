from django.urls import path
from django.views import View
from inheritApp import views

app_name="inheritApp"
urlpatterns = [
     path('', views.InheritCreate.as_view(),name="inheritcreate"),
     path('teach/', views.InheritTeachCreate.as_view(),name="inheritteachcreate"),
     path('parent/', views.InheritParentCreate.as_view(),name="inheritparcreate"),
     path('list/', views.InheritList.as_view(),name="inheritlist"),
     path('lap/', views.LapCreate.as_view(),name="inheritlapcreate"),
     path('lapuser/', views.LapUserCreate.as_view(),name="inheritlapusercreate"),
     path('lap/detail/<int:pk>/', views.LapDetail.as_view(),name="lapdetail"),
     path('location/detail/<int:pk>/', views.LocationDetail.as_view(),name="inheritlocationdetail"),
     path('lapuser/detail/<int:pk>/', views.LapUserDetail.as_view(),name="inheritlapuserdetail"),

    #  path('update/<int:pk>/', views.ProductUpdate.as_view(),name="productupdate"),
    #  path('delete/<int:pk>/', views.ProductDelete.as_view(),name="productdelete"),

     path('detail/<int:pk>/', views.InheritDetail.as_view(),name="inheritdetail"),

    #  path('detail/<int:pk>/ordercreate/', views.OrderCreate.as_view(),name="ordercreate"),
]