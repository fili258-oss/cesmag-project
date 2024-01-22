from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('auth', views.userLogin, name='login'),
    path('applicant/register', views.newApplicant, name='registerApplicant'),
    path('company/register', views.newCompany, name='registerCompany'),
    path('logout', views.userLogin, name='logout'),
    path('dashboard', views.dashboardApplicant, name='dashboard')
]
