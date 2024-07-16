from django.shortcuts import render,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm 
from.models import Post
from .form import SignupForm,LoginForm,PostForm,contactForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def about(request):
    return render(request,'blog/about.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()
        return render(request,'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect("/login/")

def newcontact(request):
    if request.method=="POST":
        form=contactForm(request.POST)
        if form.is_valid():
            fstname=form.cleaned_data['Full_name']
            lstname=form.cleaned_data['last_name']
            email=form.cleaned_data['email_address']
            message=form.cleaned_data['content']  
            print(f'{fstname} {lstname} {email} {message}')
            subject='Python (Selenium) Assignment - [fstname]'
            message=f'hi {fstname} {lstname}, you has been registered successfully! '
            email_form='mayankmisra00@gmail.com'
            recipent_list=['tech@themedius.ai','hr@themedius.ai','mayankmisra00@gmail.com']
            send_mail(subject,message,email_form,recipent_list)
            return HttpResponseRedirect("/dashboard/")
            messages.success(request,f" {uname} " 'Thank you for your suggestion....')
    else:
        form=contactForm()
    return render(request,'blog/newcontact.html',{'form':form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,f" {uname} " 'Welcome back to Your Dahsboard....')
                    return HttpResponseRedirect('/dashboard/')
        else:        
            form=LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,'you are register! Now you can login........')
            # return HttpResponseRedirect('/login/')
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
            
            form=SignupForm()
    else:
        form=SignupForm()
    return render(request,'blog/signup.html',{'form':form})

def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=Post(title=title,desc=desc)
                pst.save()
                form=PostForm()
        else:
            form=PostForm()    
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)                      
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
