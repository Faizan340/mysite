from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.title)
      return super().save(*args, **kwargs)


class ProductModel(models.Model):
    product_user = models.ForeignKey(User,default=None,related_name='product_user',on_delete=models.DO_NOTHING)
    productname = models.CharField(max_length=100,null = True, blank=True)
    price = models.IntegerField(null = True, blank=True)
    category = models.ForeignKey(CategoryModel, related_name='category',on_delete=models.CASCADE )
    description = models.CharField(max_length=200,null = True, blank=True)
    image = models.ImageField(upload_to = 'images',default="",null = True, blank=True)
    companyname = models.CharField(max_length=100,null = True, blank=True)
    colour = models.CharField(max_length=100,null = True, blank=True)
    quantity = models.IntegerField(null = True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
      return self.productname

    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.productname)
         
      return super().save(*args, **kwargs)


class OrderDetailModel(models.Model):
    ordered_by = models.ForeignKey(User,default=None,related_name='ordered_by',on_delete=models.DO_NOTHING)
    product = models.ForeignKey(ProductModel,related_name='product',on_delete=models.CASCADE)
    email = models.EmailField(null = True, blank=True)
    mobile_number = models.IntegerField(null = True, blank=True)
    shipping_address = models.CharField(max_length=200,null = True, blank=True)
    total_amount = models.PositiveIntegerField(null = True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(null = True, blank=True)
    slug = models.SlugField( unique=True)

    def __str__(self):
      return self.product.productname + "_" + self.ordered_by.username

    def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(self.ordered_by)
      return super().save(*args, **kwargs)

