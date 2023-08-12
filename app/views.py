from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class SchoolList(ListView):
    model=School
    context_object_name='allSO'
    #template_name='app/school_list.html'

class SchoolDetail(DetailView):
    model=School
    context_object_name='DOSI'
    #template_name='app/school_detail.html'
    
class SchoolCreate(CreateView):
    model=School
    fields='__all__'
    #template_name='app/school_form.html'#without instance

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
    #template_name='app/school_form.html'#with instance

class SchoolDelete(DeleteView):
    model=School
    context_object_name="DSO" #delete selected object 
    #success_url='SchoolList' #cant take directly its a url name
    success_url=reverse_lazy('SchoolList')
    #template_name='app/school_confirm_delete.html'#with instance