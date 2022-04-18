import email
from django.shortcuts import render
from authapp.forms import StudentRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def student_reg_form(request):
    if request.method == 'POST':
        print("Student registration post")
        student = StudentRegisterForm(request.POST)
        form = {'form':student}
        if student.is_valid():
            print("Student post valid")
            print("Student "+ student.cleaned_data['student_name'])
            user = User.objects.save(username = student.cleaned_data(''))
            messages.success(request, 'Account created successfully')
        else:
            print('invalid form data.........')
            form = {'form':student}
            return render(request=request, template_name="register.html", context=form)   
    else:
       print('printing....else')
       student = StudentRegisterForm()
       form = {'form':student}
       return render(request=request, template_name="register.html", context=form)

# Create your views here.
def student_login_form(request):
    student = StudentRegisterForm()
    form = {'form':student}
    if request.method == 'POST':
        print("Student login post")
    else:
        return render(request=request, template_name="login.html", context=form)
