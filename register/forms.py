#Here we are going to import 2 things; the django form and the models we created cos we'd be using them
from django import forms
from . models import UserForm, SignIn, Transfer
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
#create our django form by using the fields/attributes we listed in our models page


class FormData(forms.ModelForm):
   
    class Meta:
        model = UserForm #Here, we just linked/mapped our model fields to this django inbuilt form
        fields = ["firstname", "lastname", "username", "email", "password", "phonenumber"]

    # def email(self):
    #     email = UserForm.objects.get('email')
    #     if UserForm.objects.filter(email=email).exists():
    #         raise forms.ValidationError("This email is already registered")
    #     return email.save()
    
class SignInData(forms.ModelForm):

    class Meta:
        model = SignIn
        fields = ["username", "password"]


class Transfer(forms.ModelForm):

    class Meta:
        model = Transfer
        fields = ["sender_name", "receiver_name", "amount"]
