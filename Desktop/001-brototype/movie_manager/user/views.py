from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def signup(request):
    error_message = None
    new_user = None

    if request.POST:
        user_name = request.POST.get('Username')
        password = request.POST.get('password')
        try:
            new_user = User.objects.create_user(username=user_name, password=password)
        except Exception as e:
            error_message = str(e)
        
    return render(request,'user/signup.html',{'error_message':error_message,'user':new_user})


def user_login(request):
    error_message = None
    if request.POST:
        user_name = request.POST.get('Username')
        password = request.POST.get('password')
        # returns a user object if the cridentials are right
        user = authenticate(username=user_name,password=password)
        if user:
            login(request,user)
            return redirect('list')
        else:
            error_message = 'invalid credentials'
    return render(request,'user/login.html',{'error_message':error_message})

def user_logout(request):
    logout(request)
    return redirect('login')


