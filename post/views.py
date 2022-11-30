from django.shortcuts import render,redirect
from post.models import Postmodel,Commentmodel
from post.forms import PostForm,CommentForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect

class CommentCreate(CreateView):
    model = Commentmodel
    form_class = CommentForm
    # success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        blog = Postmodel.objects.get(id=self.kwargs['pk'])
        form.instance.blogpost = blog 
        print(form.instance.blogpost)   
        form.save()
        return redirect('post:Postdetail', pk = self.kwargs['pk'])

class CommentDelete(DeleteView):
    model = Commentmodel
    template_name = 'post/commentmodel_confirm_delete.html'

    success_url = "/"
    # pk_url_kwarg = 'pk'
    # success_url = reverse_lazy('post:Commentdelete')
    # def get_success_url(self):
    #      return reverse('post:Commentdelete', pk = self.kwargs['pk'])
    # success_url = get_success_url(self)
    # def test_func(self):
    #     comment = self.get_object()
    #     if self.request.user == comment.user:
    #         return True
    #     return False


    
    # def get_object(self, *args, **kwargs):
    #   kwargs = self.kwargs
    #   kw_id = kwargs.get('id')
    #   return Commentmodel.objects.get(id=kw_id)

class CommentUpdate(UpdateView):
    model = Commentmodel
    fields = ['comment_text']
    template_name = 'post/commentmodel_update.html'
    # form_class = CommentForm
    
    # def test_func(self):
    #     comment = self.get_object()
    #     if self.request.user == comment.user:
    #         return True
    #     return False


    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     comments_connected = Commentmodel.objects.filter(
    #         blogpost_connected=self.get_object()).order_by('-date_posted')
    #     context['comments'] = comments_connected
    #     if self.request.user.is_authenticated:
    #         context['comment_form'] = CommentForm(instance=self.request.user)
    #     return context



# class CommentCreate(CreateView):
#     def get_success_url(self):
#         form_class = CommentForm
#         return reverse_lazy('post_detail', kwargs={'pk': self.get_object(Postmodel.objects.all().pk)})

# class PostCommentView(View):
#     def get(self, request, *args, **kwargs):
#          view = PostDetail.as_view()
#          return view(request, *args, **kwargs) 

#     def post(self, request, *args, **kwargs) :
#          view = CommentCreate.as_view()
#          return view(request, *args, **kwargs) 



class PostDetail(DetailView):
   
    model = Postmodel
    # form_class = CommentForm

    template_name = "post/postmodel_detail.html"

    success_url ="/thanks/"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Post'] = Postmodel.objects.all()
        context['form'] = CommentForm()
        context['commentsname'] = Commentmodel.objects.all()
        return context

class CommentDetail(DetailView):
   
    model = Commentmodel

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['Post'] = Postmodel.objects.all()
    #     context['commentsname'] = Commentmodel.objects.all()
    #     return context

    # template_name = "post/postmodel_detail.html"
    
# class PostCommentDetail(DetailView):
   
#     model = Commentmodel
#     form_class = CommentForm

#     template_name = "post/postmodel_detail.html"

#     success_url ="/thanks/"