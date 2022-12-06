from django.shortcuts import render,redirect 
from django.urls import reverse_lazy
from django.views.generic import CreateView
from authh.forms import SignUpForm
from authh.models import Task,Profile
from django.contrib.auth.models import User
from django.contrib import messages
from .helpers import send_forget_password_mail

from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView

class UserLogin(LoginView):            # By default LoginView provide us with a form
    template_name = 'authh/login.html'
    fields = "__all__"
    redirect_authenticated_user = True
    success_url = reverse_lazy('authh:base')

# def signout(request):
#     logout(request)
#     return redirect('/')

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('authh:base')
    template_name = 'authh/signup.html'

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignUpView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('authh:base')
        return super(SignUpView, self).get(*args, **kwargs)

class Todo(CreateView):
    model = Task
    fields = "__all__"


# def ChangePassword(request , token):
#     context = {}
    
    
#     try:
#         profile_obj = Profile.objects.filter(forget_password_token = token).first()
#         context = {'user_id' : profile_obj.user.id}
        
#         if request.method == 'POST':
#             new_password = request.POST.get('new_password')
#             confirm_password = request.POST.get('reconfirm_password')
#             user_id = request.POST.get('user_id')
            
#             if user_id is  None:
#                 messages.success(request, 'No user id found.')
#                 return redirect(f'/change-password/{token}/')
                
            
#             if  new_password != confirm_password:
#                 messages.success(request, 'both should  be equal.')
#                 return redirect(f'/change-password/{token}/')
                         
            
#             user_obj = User.objects.get(id = user_id)
#             user_obj.set_password(new_password)
#             user_obj.save()
#             return redirect('/login/')
            
            
            
        
        
#     except Exception as e:
#         print(e)
#     return render(request , 'change-password.html' , context)


# import uuid
# def ForgetPassword(request):
#     try:
#         if request.method == 'POST':
#             username = request.POST.get('username')
            
#             if not User.objects.filter(username=username).first():
#                 messages.success(request, 'Not user found with this username.')
#                 return redirect('/forget-password/')
            
#             user_obj = User.objects.get(username = username)
#             token = str(uuid.uuid4())
#             profile_obj= Profile.objects.get(user = user_obj)
#             profile_obj.forget_password_token = token
#             profile_obj.save()
#             send_forget_password_mail(user_obj.email , token)
#             messages.success(request, 'An email is sent.')
#             return redirect('/authh/forget-password/')
                
    
    
#     except Exception as e:
#         print(e)
#     return render(request , 'authh/forget-password.html')