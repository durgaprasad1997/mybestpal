from django.views import View

from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages



from django.views import View
from login_signup.models import *
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.forms import ModelForm
from django import forms
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from mytask.views.alert import *
from main.models import MyTask


class Index_View_Game2048(LoginRequiredMixin,View):
    login_url = "/login/"

    def get_object(self, queryset=None):
        return get_object_or_404(MyTask, **self.kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(View, self).get_context_data(**kwargs)

        return render(

            'index_game2048.html',

        )


    def get(self,request,*args,**kwargs):

        return render(
            request,
            'index_game2048.html',

        )