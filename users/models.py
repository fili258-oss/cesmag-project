from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):        
    TYPE=(
        ('1','Company'),
        ('2','Applicant')        
    )    
    email = models.EmailField(('email address'), unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    typeUser = models.CharField('typeUser', max_length=1, choices=TYPE)
    nameCompany = models.CharField(max_length=255, null=True, blank=True)
    countryCompany = models.CharField(max_length=255, null=True, blank=True)
    depCompany = models.CharField(max_length=255, null=True, blank=True)
    cityCompany = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.user.username
    

