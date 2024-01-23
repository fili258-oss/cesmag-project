from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('auth', views.userLogin, name='login'),
    path('applicant/register', views.crateApplicant, name='registerApplicant'),
    #path('applicant/create', views.crateApplicant, name='saveApplicant'),
    path('company/register', views.createCompany, name='registerCompany'),
    path('logout', views.userLogin, name='logout'),
    path('dashboard', views.dashboardApplicant, name='dashboard')
]
