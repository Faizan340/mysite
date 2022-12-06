from django.urls import path
#from django.views.generic import IndexView
from django.views import View
from authh import views
from authh.views import Todo, SignUpView, UserLogin
from django.urls import reverse_lazy
# from authh.views import ForgetPassword,ChangePassword


from django.contrib.auth.views import LogoutView,PasswordChangeView
from django.contrib.auth import views as auth_views

app_name="authh"

urlpatterns = [
    path('', views.Todo.as_view(),name="base"),
    # path('excep/', views.excep,name="exception"),
    # path('temp/', views.temp,name="template")
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
    # path('logout/',views.signout, name="signout")
    path('logout/', LogoutView.as_view(next_page='authh:login'), name='logout'),

    path('change/', auth_views.PasswordChangeView.as_view(template_name="authh/password_change_form.html",success_url=reverse_lazy('authh:password_change_done')), name='password_change'),
    path('change_done/', auth_views.PasswordChangeDoneView.as_view(template_name="authh/password_change_done.html",), 
    name='password_change_done'),

    # path('forget-password/' , ForgetPassword , name="forget_password"),
    # path('change-password/<token>/' , ChangePassword , name="change_password"),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="authh/password_reset_form.html",success_url=reverse_lazy('authh:password_reset_done')), 
    name = 'password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="authh/password_reset_done.html"), 
    name = 'password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="authh/password_reset_confirm.html",success_url=reverse_lazy('authh:password_reset_complete')), 
    name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="authh/password_reset_complete.html"), 
    name = 'password_reset_complete')
]


