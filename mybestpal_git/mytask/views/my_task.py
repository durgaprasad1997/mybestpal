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

class AddTask(forms.ModelForm):
    class Meta:
        model=MyTask
        exclude=['id','user']
        widgets={
            'start_date':forms.TextInput(),
            'start_time':forms.TextInput(),
            'type': forms.TextInput(),
            'description':forms.TextInput(),

        }





        
class Viewtasklist(LoginRequiredMixin,ListView):
    login_url = "/login/"
    model=MyTask
    context_object_name = 'tasks'
    template_name = 'task_list.html'

    def get_object(self,queryset=None):
        return get_object_or_404(MyTask,**self.kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(Viewtasklist,self).get_context_data(**kwargs)
        #context['cards']=self.model.objects.filter(user=self.request.user).values()

        context['object_list'] = self.model.objects.filter(user_id=self.request.user.id).values()
        context.update({'user_permissions':self.request.user.get_all_permissions})
        print(context)
        return {'tasks':context['object_list']}


class AddTaskView(LoginRequiredMixin,CreateView):
    login_url = "/login/"
    template_name = 'create_task.html'
    model = MyTask
    form_class = AddTask
    success_url = reverse_lazy('index.html')

    def get_context_data(self, **kwargs):
        context = super(AddTaskView, self).get_context_data(**kwargs)
        context.update({
            'form': context.get('form'),
            'user_permissions': self.request.user.get_all_permissions()
        })
        return context

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get('user_id'))
        userform = AddTask(request.POST)

        if userform.is_valid():
          card = userform.save(commit=False)
          card.user=user
          card.save()


          dt=userform.cleaned_data['start_date']
          tm=userform.cleaned_data['start_time']
          ty=userform.cleaned_data['type']
          des=userform.cleaned_data['description']


          start_schedule(dt.year, dt.month, dt.day, tm.hour, tm.minute, 0, 0,ty,des,user.email,user.phno)




        return redirect('/tasklist/')

class UpdateTask(LoginRequiredMixin,UpdateView):
    login_url = "/login/"
    model=MyTask
    template_name = 'create_task.html'
    form_class = AddTask
    success_url = reverse_lazy('mytask:tasklist')

class DeleteTask(LoginRequiredMixin,DeleteView):
    login_url = "/login/"
    model = MyTask
    template_name = 'delete_confirm.html'
    form_class=AddTask
    success_url = reverse_lazy('mytask:tasklist')


