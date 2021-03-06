
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


from .models import *
from .forms import  CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib.auth.decorators import login_required
from .forms import MyCommentForm2


# Create your views here.
#@login_required(login_url='login')
def index(req):
	return render(req, 'myweb/index.html')

def united(req):
	return render(req, 'myweb/united.html')

def shopping1(req):
    return render(req, 'myweb/shopping1.html')

def shopping2(req):
    return render(req, 'myweb/shopping2.html')

def shopping3(req):
    return render(req, 'myweb/shopping3.html')

def sell01(req):
    return render(req, 'myweb/sell01.html')

def completed(req):
    return render(req, 'myweb/completed.html')



def loginPage(request):

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')

            else:
                messages.info(request,'  ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')



        context = {}
        return render(request, 'myweb/login.html', context)



def logout(req):
    user_logout(req)
    return redirect('login')


def registerPage(request):
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + {user})

                return redirect('login')



        context = {'form':form}
        return render(request, 'myweb/register.html', context)

def add_model2(request):
     
    if request.method == "POST":
        form = MyCommentForm2(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('completed')
 
    else:
 
        form = MyCommentForm2()
 
        return render(request, "myweb/my_template.html", {'form': form})
        
def show(testrequestreq):
    show = Comment2.objects.all()
    return render(testrequestreq ,'myweb/showdata.html' ,{'show':show})

def detail(request, question_id):
    return render(request, 'myweb/detail.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)