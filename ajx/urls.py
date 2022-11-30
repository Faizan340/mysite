from django.urls import path
from . import views

app_name="ajx"
urlpatterns = [
    path('', views.index, name='index'), 
    path('like/', views.like, name='like'), 
    path('delete/<int:pk>/', views.Delete, name='delete'), 
    path('update/<int:pk>/', views.Update, name='update'), 

    # path('like/',views.Like.as_view(),name="like")
]
