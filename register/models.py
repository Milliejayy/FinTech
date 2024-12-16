from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save
import uuid
from . utils import random_account_number #This imports our function module

# Create your models here.
#=================== Create an Account =====================
class UserForm(models.Model):

    firstname = models.CharField(max_length=50, default="firstname")

    lastname = models.CharField(max_length=50, default="lastname")

    username = models.CharField(max_length=50, default="username")

    email = models.EmailField(max_length=70, unique=True, default="email")

    password = models.CharField(max_length=15, default="password")

    phonenumber = models.CharField(max_length=15, unique=True, default="phonenumber")
        
        

#================ Account ============      
class Account(models.Model):
    user = models.OneToOneField(UserForm, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=255, null=True, unique=True, editable=False) # Unique account number
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

 
    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = random_account_number()
            super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.user}'




#================ Sign IN ================================
class SignIn(models.Model):
    username = models.CharField(max_length=50, default="username")
    password = models.CharField(max_length=15, default="password")
    
    # def check_password(self, raw_password):
    #     return check_password(raw_password, self.password)
        
    # def check_username():


#================ Transfer ================================
class Transfer(models.Model):
    sender_name = models.ForeignKey(Account, related_name='sender_name', on_delete=models.CASCADE)
    receiver_name = models.ForeignKey(Account, related_name='receiver_name', on_delete=models.CASCADE)
    account_number = models.ForeignKey(Account, related_name='account', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    
