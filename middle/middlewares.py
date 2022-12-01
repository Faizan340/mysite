from django.shortcuts import HttpResponse
from django.template.response import TemplateResponse 

###########################
# Function based middleware-------

# def exampleMiddleware(get_response):
#     print("One Time Initialization")

#     def midFunction(request):
#         print("Before View.......")
#         response = get_response(request)
#         print("After View.........")
#         return response
#     return midFunction



########################
# Class based middleware---------
# Multiple Middlewares

class SonMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Son Initialization |||")
        print("#################")

    def __call__(self,request):
        print("Son Before executing view |||")
        response = self.get_response(request)     # this statement continues the flow to next middleware or view
        print("Son After executing view |||")
        return response

class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Father Initialization |||")

    def __call__(self,request):
        print("Father Before executing view |||")
        # response = HttpResponse("Exitttt")       # due to this next middleware and view function will no get executed 
        response = self.get_response(request)    
        print("Father After executing view |||")
        return response

class MotherMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One Time Mother Initialization |||")

    def __call__(self,request):
        print("Mother Before executing view |||")
        response = self.get_response(request)
        print("##################")
        print("Mother After executing view |||")
        return response



###########################
# Middleware Hooks---------

class HookMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print(" One time Hooks initialization ")

    def __call__(self, request):
        response = self.get_response(request)
        return response

###############
# process_view

    # def process_view(self,request, view_func,  *args, **kwargs):
    #     print("Process - before view")
    #     print(f'view name : {view_func.__name__}')
    #     return HttpResponse("Process_view before view")
    #     # return None                                       # this statement continues the flow to next middleware or view
        
##################
# process_exception :-
# to handle exceptions

    def process_exception(self, request, exception):
        print("Exception Occured...........")
        message = exception
        class_name = exception.__class__.__name__
        print(class_name)
        return HttpResponse(message)

##################
# process_template_response :-
# to change the data passed to the template

    def process_template_response(self, request, response):
        print("Process template response .... ")
        response.context_data['name'] = 'Prince'
        return response

#################
# get user data
class UserMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("##################")
        print(" One time user initialization ")

    def __call__(self, request):
        print("##################")
        print(request.path)
        print(request.headers['Host'])
        print(request.META['REQUEST_METHOD'])
        print(request.META['HTTP_USER_AGENT'])
        print("###############")
        response = self.get_response(request)
        return response