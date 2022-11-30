from django.urls import path
#from django.views.generic import IndexView
from django.views import View
from blog import views
from blog.views import BlogCreate,CommentCreate

urlpatterns = [
    path('', views.BlogCreate.as_view(),name="index"),
    path('list/', views.BlogList.as_view(),name="Bloglist"),
    path('detail/<int:pk>/', views.BlogDetail.as_view(),name="Blogdetail"),
    path('commentdetail/<int:pk>/', views.CommentDetail.as_view(),name="Commentdetail"),
    path('update/<int:pk>/', views.BlogUpdate.as_view(),name="Blogupdate"),
    path('delete/<int:pk>/', views.BlogDelete.as_view(),name="Blogdelete"),
    path('formview/', views.BlogFormView.as_view(),name="Blogformview"),
    path('detail/<int:pk>/comment/', views.CommentCreate.as_view(),name="Commentcreate"),
]
