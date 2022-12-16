from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from. models import Myform

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('success')
        else:
            messages.info(request,'invalid user')
            return  redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                print("user created")
                messages.info(request,"user created")
                return redirect('login')
        else:
           messages.info(request,'password does not match')
           return redirect('/')
    return render(request,'register.html')

def success(request):
    return render(request, 'success.html')

def myform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        myform = Myform(name=name, age=age, email=email)
        myform.save()
        return redirect('account')
    return render(request,'form.html')

def accountcreated(request):
    return render(request,'account.html')