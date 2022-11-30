from django.urls import path
from django.views import View
from post import views
from post.views import PostDetail, CommentCreate,CommentDetail,CommentDelete
app_name="post"
urlpatterns = [
   path('detail/<int:pk>/', views.PostDetail.as_view(),name="Postdetail"),
   path('detail/<int:pk>/commentcreate/', views.CommentCreate.as_view(),name="Commentcreate"),
   path('detail/<int:pk>/commentdelete/', views.CommentDelete.as_view(),name="Commentdelete"),
   path('detail/<int:pk>/commentdetail/', views.CommentDetail.as_view(),name="Commentdetail"),
   path('detail/<int:pk>/commentupdate/', views.CommentUpdate.as_view(),name="Commentupdate"),
]
