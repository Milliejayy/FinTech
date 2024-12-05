from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#app_name = 'register'

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('transfer/', views.transfer, name="transfer"),

]



