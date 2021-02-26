from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import Register_form
# Create your views here.
def loginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username,password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            messages.info(request,'Invalid user')
            return redirect('/')
    else:
        return render(request,'accounts/loginPage.html')
    return render(request,'accounts/loginPage.html')

def registerPage(request):
    form=Register_form()
    if request.method=='POST':
        form=Register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context={
            'form':form
            }
    return render(request,'accounts/registerPage.html',context)

def logout(request):
    auth.logout(request)
    return redirect('/')