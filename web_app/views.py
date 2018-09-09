from django.shortcuts import render
from django.shortcuts import HttpResponse
from web_app import models

# Create your views here.



def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #添加数据到数据库
        models.UserInfo.objects.create(user=username, password=password)
    #从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()


    return render(request,'home.html',{"data":user_list},)