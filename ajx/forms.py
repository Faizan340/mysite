from django import forms
from product.models import ProductModel,CategoryModel,OrderDetailModel
from django.forms import ModelForm

class ProductFormName(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['productname','price','description','companyname','colour','quantity']