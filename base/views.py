from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

class Customloginview(LoginView):
    template_name='base/login.html'
    fields='__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class Registerpage(FormView):
    template_name='base/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('tasks')

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request, user)
        return super(Registerpage,self).form_valid(form)

    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Registerpage,self).get(*args,**kwargs)

class TaskList(LoginRequiredMixin,ListView):
    model=Task

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['object_list']=context['object_list'].filter(user=self.request.user)
        context['count']=context['object_list'].filter(complete=False).count()

        search_input = self.request.GET.get('search_input') or ''
        if search_input:
            context['object_list']=context['object_list'].filter(title__icontains=search_input)
        context['search_input']=search_input
        return context

class DetailList(LoginRequiredMixin,DetailView):
    model=Task

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title','description','complete']
    success_url=reverse_lazy('tasks')

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)

class Taskupdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete']
    success_url=reverse_lazy('tasks')

class Taskdelete(LoginRequiredMixin,DeleteView):
    model=Task
    success_url=reverse_lazy('tasks')
