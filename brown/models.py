from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user_name = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    user_id = models.IntegerField()
    user_image = models.ImageField(upload_to = 'images',default="")
    user_gender = models.CharField(max_length=300)
    user_location = models.TextField(max_length=300)
    user_job_role = models.CharField(max_length=300)
    user_bio = models.CharField(max_length=300)

class Usersignup(models.Model):
    signin_name = models.ForeignKey(User,default=None,on_delete=models.DO_NOTHING)

    # def __str__(self):
    #     return self.user_id
