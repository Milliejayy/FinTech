from django.contrib import admin
from. models import UserForm, Transfer#This is how we import from our models.py, so we can be able to view the models we created from our user adminttttttttt

# Register your models here.
class MemberUF(admin.ModelAdmin):
    list_display= ("firstname", "email", "password")

admin.site.register(UserForm, MemberUF),
admin.site.register(Transfer)