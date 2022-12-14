from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'base.html')

def blog(request):
    fm = Myblog()
    stud = Blog.objects.all()
    return render(request, 'home.html', {'form1': fm, 'stu': stud})

def sign_up(request):
    if request.method=="POST":
        data=sign(request.POST)
        if data.is_valid():
            messages.success(request,'signup Created Successfully !!')
            obj=data.save()
            group = Group.objects.get(name='blogger')
            obj.groups.add(group)

    else:
        data=sign()
    return render(request, 'signup.html', {'dt2':data})

def aboutus(request):
    return render(request,'aboutus.html')

def loginpage(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            obj = AuthenticationForm(request=request, data=request.POST)
            if obj.is_valid():
                nm=obj.cleaned_data['username']
                pw=obj.cleaned_data['password']
                user=authenticate(username=nm, password=pw)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully !!')
                    return HttpResponseRedirect('/details/')
        else:
            obj = AuthenticationForm()
        return render(request,'login.html',{'ob':obj})
    else:
        return HttpResponseRedirect('/details/')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank you for your inquiry,Your contact information and message was successfully submitted.')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)

def logoutpage(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def details(request):
    if request.method == 'POST':
        fm = Myblog(request.POST)
        if fm.is_valid():
            ti= fm.cleaned_data['title']
            bg = fm.cleaned_data['blog']

            reg = Blog(title=ti, blog=bg)
            reg.save()
            fm =Myblog()
            messages.add_message(request, messages.SUCCESS, 'you added data successfully !!!')

    else:
        fm = Myblog()
    stud = Blog.objects.all()
    return render(request, 'profile.html', {'form2':fm, 'stu':stud})


def update_data(request,id):
    if request.method == 'POST':
        pi = Blog.objects.get(pk=id)
        fm = Myblog(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, 'you updated data successfully !!!')
            messages.info(request, 'you can go back !!!')
    else:
        pi =Blog.objects.get(pk=id)
        fm = Myblog(instance=pi)

    return render(request, 'update.html', {'form3': fm})


def delete_data(request,id):
    if request.method == 'POST':
        pi = Blog.objects.get(pk=id)
        pi.delete()
        messages.info(request, 'Deleted !!!')
        return HttpResponseRedirect('/details/')

def password(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            obj=PasswordChangeForm(user=request.user,data=request.POST)
            if obj.is_valid():
                obj.save()
                update_session_auth_hash(request,obj.user)
                messages.success(request,'Password Changed Successfully')
                return HttpResponseRedirect('/details/')
        else:
            obj = PasswordChangeForm(user=request.user)
        return render(request,'psw.html',{'ob':obj})
    else:
        return HttpResponseRedirect('/login/')