from pyclbr import Class
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('ok')
    template_name = 'signup.html'

def ok(request):
    return HttpResponse('ok')


