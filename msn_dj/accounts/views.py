from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist

from .models import About
from .forms import AboutForm
from django.views.generic.edit import CreateView, UpdateView

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def profile(request):
    template_name = 'profile.html'
    context = {}
    return render(request, template_name, context)

def profile_update(request):
    template_name = 'about.html'
    if request.method == "POST":
        form = AboutForm(request.POST)
        form.user = request.user
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
        else:
            error = 'Форма была не верной'
            context = {'form': form, 'error': error}
            return render(request, template_name, context)
    else:
        try:
            about = About.objects.get(user_id=request.user.id)
            form = AboutForm(instance=about)           
        except ObjectDoesNotExist:
            form = AboutForm()
        
        context = {'form': form}
        return render(request, template_name, context)   
                      


