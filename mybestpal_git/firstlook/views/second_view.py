from django.views import View

from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

class Second_View(View):
    def get(self,request,*args,**kwargs):

        return render(
            request,
            'second_index.html',

        )