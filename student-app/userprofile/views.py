from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserExtCreationForm, UserProfilerForm

# Create your views here.

def registration_page(request):
    if request.method == 'POST':
        form = UserExtCreationForm(request.POST)
        userprofiler_form = UserProfilerForm(request.POST)
        context = {'form': form,'userprofiler_form':userprofiler_form}  
        if form.is_valid() and userprofiler_form.is_valid():
            user = form.save()

            profile = userprofiler_form.save(commit=False)
            profile.user = user
            profile.save()
            return render(request, 'home.html', context)

        else:
            context = {'form': form,'userprofiler_form':userprofiler_form}
            return render(request, 'register.html', context)
    
    else:
            form = UserExtCreationForm()
            userprofiler_form = UserProfilerForm()
            context = {'form': form,'userprofiler_form':userprofiler_form}
            return render(request, 'register.html', context)  


def login_page(request):
    form = LoginForm()
    context = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
          login(request, user)
          last_login = user.last_login.strftime('%y-%m-%d %H:%M:%S')
          request.session['last_login'] = last_login
          print(request.session.get('last_login'))
          return redirect('/account/dashboard')
        return render(request, 'login.html', context)
    else:
      return render(request, 'login.html', context)

def logout_page(request):
    if request.method == 'POST':
      return render(request, 'home.html')
    else:
      return redirect('/login')

def home_page(request):
    if request.method == 'POST':
      return render(request, 'home.html')
    else:
      return render(request, 'home.html')
   