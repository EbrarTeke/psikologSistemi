from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm,EditProfileForm


def home(request):
    return render(request,'website/templates/home.html',{})

def contact(request):
    if request.method=="POST":
        message_name=request.POST['message_name']
        email_adress=request.POST['email_adress']
        phone_number=request.POST['phone_number']
        message=request.POST['message']

        #send an email
        send_mail(
            message_name,# subject
            message,#message
            email_adress,#from email
            phone_number,#phone
            ['ebrarclinic@gmail.com'],#to email
            )

        return render(request,'website/templates/contact.html',{'message_name':message_name})  

    else:
        return render(request,'website/templates/contact.html',{})    

def about(request):
    return render(request,'website/templates/about.html',{})

def gallery(request):
    return render(request,'website/templates/gallery.html',{})

def booking(request):
    return render(request,'website/templates/booking.html',{})

def blog(request):
    return render(request,'website/templates/blog.html',{})

def services(request):
    return render(request,'website/templates/services.html',{})    
def personelinf(request):
    if request.method=='POST':
        form= EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,('You Have Edited Your Profile...'))
            return redirect('personelinf')
    else:
        form= EditProfileForm(instance=request.user)    
    context={'form':form}
    
    return render(request,'website/templates/personelinf.html',context)    
     

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            messages.success(request,('You have been logged in'))
            return redirect('home')
        else:
            messages.success(request,('Error Logging In - Please Try Again...'))
            return redirect('login_user')
    else:
        return render(request,'website/templates/login_user.html',{})    
     
def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out!') )
    return redirect('home')
def register(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,('You Have Registered'))
            return redirect('home')
    else:
        form=SignUpForm()    
    context={'form':form}
    
    return render(request,'website/templates/register.html',context)     
        
# Create your views here.

def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,('You Have Changed Password Successfully..'))
            return redirect('change_password')
    else:
        form=PasswordChangeForm(user=request.user)    
    context={'form':form}
    return render(request,'website/templates/change_password.html',context)


