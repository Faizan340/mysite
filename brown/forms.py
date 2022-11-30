from django import forms
from .models import UserProfile,Usersignup
from django.forms import ModelForm,widgets

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_name','user_id','user_image','user_gender','user_location','user_job_role','user_bio')
        

class Usersign(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields = ('signin_name',)