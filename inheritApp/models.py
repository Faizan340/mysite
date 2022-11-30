from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Model Inheritance

#####################
# Abstract Base Class
# Parent Model table will not be created

class SameModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank= True)
    age = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.name)
         
      return super().save(*args, **kwargs) 

    class Meta:
        abstract = True

class StudentModel(SameModel):
    fees = models.IntegerField(null=True, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    date = None                                           # Field Overriding

    # Meta Class Ineritance
    # class Meta:
    #     abstract = False

class TeacherModel(SameModel):
    salary = models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank= True)

class ParentModel(SameModel):
    occupation = models.CharField(max_length=100, null=True, blank= True)
    date = models.DateTimeField()                           # Field Overriding


########################
# Multi Table Ineritance
# Parent Model table will be created

class LaptopModel(models.Model):
    laptop_name = models.CharField(max_length=100, null=True, blank= True)
    price = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.laptop_name)
         
      return super().save(*args, **kwargs)

class LaptopUserModel(LaptopModel):
    name = models.CharField(max_length=100, null=True, blank= True)
    age = models.IntegerField(null=True, blank=True)


###################
# Proxy Models
# Proxy Model similar to Parent Model

class LocationModel(models.Model):
    city = models.CharField(max_length=100, null=True, blank= True)
    country = models.CharField(max_length=100, null=True, blank= True)
    continent = models.CharField(max_length=100, null=True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.city)
         
      return super().save(*args, **kwargs)

class LocProxyModel(LocationModel):
    class Meta:
        proxy = True
        
# class Employee(User):
#     class Meta:
#         proxy = True

#     def full_name(self):
#         return self.first_name + " " + self.last_name