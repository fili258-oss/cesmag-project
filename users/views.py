from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def dashboardApplicant(request):
    return render(request, 'dashboard/index.html')

def userLogin(request):    
    if request.method == 'POST':                   
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    return render(request, 'registration/login.html', {
                        'error': 'El usuario no esta activo'})
            else:
                return render(request, 'registration/login.html', {
                        'error': 'Usuario o contraseña incorrectos'})        
    else:
        return render(request, 'registration/login.html')

def newApplicant(request):
    return render(request, 'registration/registerApplicant.html')

def newCompany(request):
    return render(request, 'registration/registerCompany.html')