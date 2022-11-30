from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save,pre_delete,post_delete
from django.dispatch import receiver
from datetime import datetime
import json

class SignModel(models.Model):
    product_name = models.CharField(null = True, blank=True, max_length=50)
    product_price = models.IntegerField(null = True, blank=True)
    product_category = models.CharField(null = True, blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.product_name)
         
      return super().save(*args, **kwargs)


class SignalModel(models.Model):
    product = models.OneToOneField(SignModel, on_delete=models.CASCADE,related_name='product_signmodel')
    product_description = models.CharField(null = True, blank=True, max_length=100)
    product_colour = models.CharField(null = True, blank=True, max_length=50)
    product_company = models.CharField(null = True, blank=True, max_length=50)
    product_image = models.ImageField(upload_to = 'images',default="",null = True, blank=True)
    product_quantity = models.IntegerField(null = True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug =  models.SlugField(unique=True)


    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.product_description)
         
      return super().save(*args, **kwargs)

class LinkModel(models.Model):
    product_made_in = models.CharField(null = True, blank=True, max_length=50)
    product_warranty_months = models.IntegerField(null = True, blank=True)
    slug =  models.SlugField(unique=True)

    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.product_made_in)
         
      return super().save(*args, **kwargs)
    

# @receiver(post_save, sender = SignModel)
# def create_sign(sender, instance, created, **kwargs):
#     if created:
#         print(instance)
#         print("000000000000000000000")
#         SignalModel.objects.create(product=instance)
#         print("Product Created")

# post_save.connect(create_sign,sender=SignModel)

# @receiver(pre_save, sender = SignModel)
# def sign_pre(sender, instance, **kwargs):
#     print("prreeee saavvvvvveeeee")
#     print(instance)
#     LinkModel.objects.create()
#     print("Product Created")

#     print(slugify(instance.name))
#     instance.slug = (slugify(instance.name))

# @receiver(pre_delete,sender = SignModel)
# def sign_predelete(sender,instance,**kwargs):
#     print("Do you want to delete this")

# @receiver(post_delete,sender = SignModel)
# def sign_postdelete(sender,instance,**kwargs):
#     print("you have deleted.....")



# @receiver(post_save, sender = SignModel)
# def update_sign(sender, instance, created, **kwargs):
#     if created == False:
#         instance.SignalModel.save()
#         print("Product Updated")



# 

# class Task(models.Model):
#     task_name = models.CharField(max_length=100, null = True, blank=True)
#     task_description = models.CharField(max_length=200, null = True, blank=True)
#     slug = models.SlugField(unique= True)

#     def __str__(self):
#         return self.task_name

# class Taskdate(models.Model):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     date = models.CharField(max_length=100)

# class Archive(models.Model):
#     detail = models.CharField(default='{}', max_length=200)

# @receiver(pre_save, sender=Task)
# def task_pre(sender,instance,**kwargs):
#     print("prreeee saavvvvvveeeee")
#     print(instance)
#     print(slugify(instance.name))
#     instance.slug = (slugify(instance.name))


# @receiver(post_save, sender = Task)
# def task_post(sender,instance,**kwargs):
#     print("pooosssssstt saavvvvvveeeee")
#     Taskdate.objects.create(task = instance, date = datetime.now())




# @receiver(pre_delete,sender = Task)
# def task_predelete(sender,instance,**kwargs):
#     print("Do you want to delete this")
#     data={'task':instance.task_name, 'desc': instance.task_description, 'slug': instance.slug}
#     Archive.objects.create(detail = json.dump(data))

# @receiver(post_delete,sender = Task)
# def task_postdelete(sender,instance,**kwargs):
#     print("you have deleted.....")