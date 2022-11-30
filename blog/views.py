from django.shortcuts import render

from blog.models import BlogPost1,Comment1
from blog.forms import BlogPostingForm,BlogCommentForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BlogCreate(CreateView):
    model = BlogPost1
    fields = "__all__"
    success_url ="/"

class CommentCreate(CreateView):
    model = Comment1
    templates = "templates/blogpost_detail.html"
    fields = "__all__"
    success_url ="/"



class BlogList(ListView):
 
    
    model = BlogPost1
    fields = "__all__"

class CommentList(ListView):
 
    
    model = Comment1
    fields = "__all__"
    
    # def get_context_data(self, *args, **kwargs):
    #     template_name = "blog/blogpost_detail.html"
    #     context = super(CommentList, self).get_context_data(*args, **kwargs)
    #     context['commentslist'] = BlogPost.objects.all()
    #     return context

class BlogDetail(DetailView):
   
    model = BlogPost1
    
class CommentDetail(DetailView):
   
    model = Comment1
    form_class = BlogCommentForm

    template_name = "blog/blogpost_detail.html"

    success_url ="/thanks/"

class BlogUpdate(UpdateView):

    model = BlogPost1
 
   
    fields = "__all__"

    success_url ="/"

class BlogDelete(DeleteView):
    
    model = BlogPost1
    
    success_url ="/"

class BlogFormView(FormView):
    form_class = BlogPostingForm

    template_name = "blog/blogpost_form.html"

    success_url ="/thanks/"