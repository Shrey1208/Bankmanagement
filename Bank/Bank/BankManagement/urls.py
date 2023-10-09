from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('Register_user/',Register_user),
    path('succes/', succes),
    path('login',login),
    path('logout',logout),
    path('checkpass',checkpass),
    path('profile',edit_profile),
    path('forgetpas',forgetpas),
    path('qty/<int:id>',qty),

]