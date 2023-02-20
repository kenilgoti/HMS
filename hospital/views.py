from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *


def index(request):
    return render(request,'index.html')

def user_login(request):
    if request.user.is_superuser == True:
        return render(request,'admin_home.html')
    elif request.method == "POST":
        usernmae = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=usernmae,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Login Sucess!")
            # if request.user.category == "P":
            #     return redirect('pation-Home')
            # elif request.user.category == "S":
            #     return redirect('staff-Home')
            # elif request.user.category == "D":
            #     return redirect('doctor-Home')
            # else:

            return render(request,'admin_home.html')
        else:
            messages.error(request,"Login Fail!")
            return render(request,'admin_home.html')
    return render(request,'login.html')

#doctor login
def doctor_login(request):
    # if request.method == "POST":
    #     username= request.POST['username']
    #     password=request.POST['password']
    #     user=authenticate(username=username,password=password)
    #     if user is not None:
    #         login(request,user)
    #         messages.success("Doctor login successfull")
    #         return render(request,'Doctor_Home.html')
    #     else:
    #         messages.error("Doctor Login Faild")   
    #         return render(request,'login_doctor.html')
    return render(request,'login_doctor.html')

 
   
def staff_login(request):
       return render(request,'login_staff.html')
   
def pationt_login(request):
       return render(request,'login_pationt.html')

def user_logout(request):
    logout(request)
    messages.success(request,"Logout Sucess!")
    return redirect('/login/')


    