from django.shortcuts import render, redirect
from .forms import ApplicantCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import User

@login_required
def dashboardApplicant(request):
    return render(request, 'dashboard/index.html')

def userLogin(request):    
    if request.method == 'POST':                   
            user = authenticate(request, email=request.POST['email'], password=request.POST['password'])
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

def crateApplicant(request):
    if request.method == 'POST':        
        #Registrar usuario
        full_names = request.POST.get('names', '')
        name_first = full_names.split(' ')[0] if full_names else ''
        #Limpiar nombre de usuario
        cleaned_username = slugify(name_first)

        # Verificar si el usuario ya existe por correo electrónico
        if User.objects.filter(email=request.POST['email']).exists():
            return render(request, 'registration/registerApplicant.html', {
                'error': 'El correo electrónico ya existe'
            })
        try:
            user = User.objects.create_user(
                username=cleaned_username,
                password=request.POST['password'],
                first_name=request.POST['names'],
                last_name=request.POST['surnames'],
                email=request.POST['email'],
                typeUser=2)
            user.save()
            login(request, user)
            return redirect('dashboard')
            
        except:
            return render(request, 'registration/registerApplicant.html', {
                'error':'El usuario ya existe'
            })                            
    else:        
        return render(request, 'registration/registerApplicant.html')
        
def createCompany(request):
    if request.method == 'POST':
        #Registrar usuario
        company_name = request.POST.get('companyname', '')
        name_first = company_name.split(' ')[0] if company_name else ''
        #Limpiar nombre de usuario
        cleaned_companyname = slugify(name_first)

        # Verificar si el usuario ya existe por correo electrónico
        if User.objects.filter(email=request.POST['email']).exists():
            return render(request, 'registration/registerApplicant.html', {
                'error': 'El correo electrónico ya existe'
            })
        try:
            user = User.objects.create_user(
                username=cleaned_companyname,
                password=request.POST['password'],
                nameCompany=request.POST['companyname'],
                countryCompany=request.POST['countrycompany'],
                depCompany=request.POST['depcompany'],
                cityCompany=request.POST['citycompany'],
                phone=request.POST['phonecompany'],
                email=request.POST['email'],
                typeUser=1)
            user.save()
            login(request, user)
            return redirect('dashboard')
            
        except:
            return render(request, 'registration/registerCompany.html', {
                'error':'El usuario ya existe'
            })
    return render(request, 'registration/registerCompany.html')