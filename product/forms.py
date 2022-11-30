from django import forms
from .models import ProductModel,CategoryModel,OrderDetailModel
from django.forms import ModelForm

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = "__all__"

class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetailModel
        fields = "__all__"