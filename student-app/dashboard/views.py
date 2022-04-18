from django.shortcuts import render

# Create your views here.

def addAttendance_page(request):
    return render('home.html')


def addMarks_page(request):
    return render('home.html')

def dashboard_page(request):
    if request.method == 'POST':
      return render(request, 'dashboard.html')
    else:
      return render(request, 'dashboard.html')