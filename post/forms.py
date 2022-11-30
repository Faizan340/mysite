from django import forms
from .models import Postmodel,Commentmodel
from django.forms import ModelForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Postmodel
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentmodel
        fields = ['comment_text']