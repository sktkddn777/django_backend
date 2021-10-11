from django.contrib import auth 
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate 
# Create your views here.


def signup(request): 
  if request.method == 'POST': 
    try:
      user = User.objects.create_user( 
          username=request.POST['username'], 
          password=request.POST['password1'], 
          email=request.POST['email'],
        ) 
      auth.login(request, user) 
      return redirect('home')
    except:
      return render(request, 'user/signup.html')
  else: 
    return render(request, 'user/signup.html')

# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'user/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'user/login.html')


# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('home')

# home
def home(request):
    return render(request, 'user/home.html')