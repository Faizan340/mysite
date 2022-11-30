from django import forms
from .models import BlogPost1,Comment1
from django.forms import ModelForm

class BlogPostingForm(forms.ModelForm):
    class Meta:
        model = BlogPost1
        fields = "__all__"

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment1
        fields = "__all__"