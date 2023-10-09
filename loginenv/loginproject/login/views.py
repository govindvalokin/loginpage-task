from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('userpage')#urlnames
        else:
            messages.error(request, 'Invalid Username or Password')

    return render(request,"login.html")
def userpage(request):
    return render(request,"userpage.html")
def logout(request):
    auth.logout(request)
    return redirect('signup')