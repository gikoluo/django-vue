from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

class LoginView(APIView):

    def get(self,request,*args,**kwargs):
        ret = {
            'code':111,
            'data':'在知识的海洋里一路向前'
        }

        response =  JsonResponse(ret)
        response['Access-Control-Allow-Origin']='*'
        return response

    def post(self,request,*args,**kwargs):
        print(request.body)  #在body里面有值
        print(request.POST)   #在post里面是没有值的
        ret = {
            'code':1000,
            'username':'haiyn',
            'token':'sdswr3fdfsdfdxqw2fgh',
        }
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = "*"
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        # response['Access-Control-Allo w-Methods'] = 'PUT'
        return response
