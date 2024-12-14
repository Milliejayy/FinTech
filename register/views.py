from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from . forms import FormData, SignInData
from . models import UserForm, SignIn, Transfer
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    users = UserForm.objects.all()
    return render(request, "register/index.html", {"users": users})

def signup(request):

    if request.method == 'POST':
        form = FormData(request.POST)
        
        if form.is_valid():
            firstname= form.cleaned_data.get('firstname')
            lastname= form.cleaned_data.get('lastname')
            username= form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            phonenumber = form.cleaned_data.get('phonenumber')
            password = form.cleaned_data.get('password')

            if UserForm.objects.filter(email=email).exists():
                raise ValidationError("This email is already registered")
            
            if UserForm.objects.filter(phonenumber=phonenumber).exists():
                raise ValidationError("This phone number is already registered")
            
            if not phonenumber.isdigit():
                raise ValidationError("Phone number must contain only digits.")
             
            if len(password) < 8 :
                raise ValidationError("Password should not be less than 8")        

             # Save user data
            user= UserForm.objects.create(firstname=firstname, lastname=lastname, username=username, phonenumber=phonenumber, email=email, password=password) 
    
            user.password = make_password(password)
            user.save()
            messages.success(request, 'Registration successful!')
            return render(request, 'register/index.html')      
        else:
            #This returns the signup page with errors if any invalid data is identified
            messages.error(request, 'There is an error in your Form!')
            return render(request, "register/signup.html")
        
    #This renders for the GET request
    form = FormData()
    return render(request, "register/signup.html", {'form': form})
    

def signin(request):
    
    if request.method == 'POST':
        form = SignInData(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = SignIn.objects.filter(username=username).first()
            if user:
                
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    request.session['username'] = user.username
                    print("user eexists")
                    #return render(request, "register/index.html")
                else:
                    print("user does not exist")
                        # return render(request, "register/login.html")

                   
    return render(request, "register/login.html")

           

def user_logout(request):

    #logout(request)
    return render(request, 'register/logout.html') 



def transfer(request):
    
    # if request.method == "POST" :

    #     if form.is_valid():
    #         form = Transfer(request.POST)

    #         account_number = form.cleaned_data.get("account_number")
    #         receiver_account = form.cleaned_data.get("account_number")

    #         #Check if the string input is/represents an integer
    #         if account_number.isdigit():
    #             account_number = int(account_number)
    #             return account_number   
            
    #         if not receiver_account.objects.filter(receiver_account=receiver_account).exists:
    #             print("The account number does not exist on our dashboard")
    #             return render(request, "register/transfer.html")
            
    #         form.save()
    #     return render(request, "register/transfer.html")

    return render(request, "register/transfer.html")


# def deposit(self, amount):
#         self.amount = amount
#         if self.amount > 0 :
#             self.balance = self.balance + self.amount
#             return f'You deposited the sum of {self.amount}. Your new balance is {self.balance}'
#         else:
#             return f'Your amount must be a positive number'

#     def withdraw(self, amount):
#         self.amount = amount
#         if self.amount < self.balance :
#             self.balance = self.balance - self.amount
#             return f'You withdrew {self.amount}. Your current balance is {self.balance}'
#         else:
#             return f"Insufficient Funds!"

#     def transfer(self, amount):
#         self.amount = amount
#         if self.amount < self.balance :
#             self.balance = self.balance - self.amount
#             return f'You transfered {self.amount}'
#     def check_balance(self):
#         return self.balance

