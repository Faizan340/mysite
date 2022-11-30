from django.db import models
from django.contrib.auth.models import User

class Postmodel(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    user_image = models.ImageField(upload_to = 'images',default="")
    author = models.ForeignKey(User,default=None,on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

class Commentmodel(models.Model):
    author = models.ForeignKey(User,default=None,on_delete=models.DO_NOTHING)
    blogpost = models.ForeignKey(Postmodel,related_name='commentsname',on_delete=models.CASCADE)
    comment_text = models.TextField()