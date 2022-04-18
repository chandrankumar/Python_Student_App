from django.contrib import admin
from django.urls import path
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('dashboard/', views.dashboard_page, name='dashboard'),
    path('attendance/', views.addAttendance_page, name='attendance'),
    path('marks/', views.addMarks_page, name='marks'),
]
