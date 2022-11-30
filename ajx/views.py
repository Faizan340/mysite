from django.shortcuts import render
from django.http import HttpResponse
from product.models import ProductModel,CategoryModel
from product.forms import ProductForm
from .forms import ProductFormName
from django.views import View
from django.http import JsonResponse
from django.core import serializers

def index(request):
    return render(request,"ajx/ajx.html")

# class Like(View):
#     def get(self):
#         print("nonono")
#         products = ProductModel.objects.all()
#         return JsonResponse( status = 1)

def like(request):
    if request.method == "GET":
        print("none")
        products = ProductModel.objects.all()
        # ser_instance = serializers.serialize('json', [ products, ])
        return JsonResponse( data=1, safe=False)

    if request.method == "POST":
        message = "morning"
        # new_form = ProductForm(
        #      productname = request.POST['productname'],
        #      price = request.POST['price'],
        #      description = request.POST['description'],
        #      companyname = request.POST['companyname'],
        #      colour = request.POST['colour'],
        #      quantity = request.POST['quantity']
        # )
        # form = ProductForm(request.POST)
        # form = ProductForm({'productname':productname,'price':price,'description':description,'companyname':companyname,'colour':colour,'quantity':quantity})
        # form = ProductForm({productname=productname,price=price,description=description,companyname=companyname,colour=colour,quantity=quantity})
        
        # productname = request.POST['productname']
        # price = request.POST['price']
        # description = request.POST['description']
        # companyname = request.POST['companyname']
        # colour = request.POST['colour']
        # quantity = request.POST['quantity']
        if request.user.username:
            user = request.user
            category = CategoryModel.objects.all()[0]
            form = ProductFormName(request.POST)
            form.instance.product_user=user
            form.instance.category=category
            print("halooooooooooooooooooooooooooooooooooooooo")
            print(request.POST)
            print(form.data)
            if form.is_valid():
                print("!1111111111122222222")
                text = form.save()
            return JsonResponse(data=2, safe=False)






def  Delete(request,pk):
    if request.method == "GET": 
        # pk = request.GET.get('id', None)
        ProductModel.objects.get(id=pk).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


def Update(request,pk):
    if request.method == "POST":
        new = ProductModel.objects.get(id=pk)
        form = ProductFormName(request.POST,instance=new)
        form.save()
        return JsonResponse(data=3, safe=False)
      







# def index(request):
#     posts = Post.objects.all()  # Getting all the posts from database
#     return render(request, 'ajx/ajx.html', { 'posts': posts })

# def likePost(request):
#     if request.method == 'GET':
#            post_id = request.GET['post_id']
#            likedpost = Post.objects.get(pk=post_id) #getting the liked posts
#            m = Like(post=likedpost) # Creating Like Object
#            m.save()  # saving it to store in database
#            return HttpResponse("Success!") # Sending an success response
#     else:
#            return HttpResponse("Request method is not a GET")

