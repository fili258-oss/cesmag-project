from django.shortcuts import render

def formLogin(request):
    return render(request, 'auth/loginCompanie.html')

