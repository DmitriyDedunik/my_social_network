from asyncio.windows_events import NULL
from dataclasses import field
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist

from .models import About
from .forms import AboutForm, RigisterUserForm
from django.views.generic.edit import CreateView, UpdateView


class SignupView(generic.CreateView):
    form_class = RigisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class AboutUpdateView(UpdateView):
    template_name = 'about.html'
    form_class = AboutForm
    model = About
    
    def get_success_url(self):
        return reverse('accounts:profile')


class AboutCreateView(CreateView):
    template_name = 'about.html'
    form_class = AboutForm
    success_url = reverse_lazy('accounts:profile')


def profile(request):
    template_name = 'profile.html'
    context = {}
    return render(request, template_name, context)

def profile_update(request):
    template_name = 'about.html'
    # try:
    #     about_db = About.objects.get(user_id=request.user.id)
    #     context = {'form': AboutUpdateView.as_view()}
    #     return render(request, template_name, context)
    # except ObjectDoesNotExist:
    #     context = {'form': AboutCreateView.as_view()}
    #     return render(request, template_name, context)

    if request.method == "POST":

        about = request.POST.dict()
        about['user'] = request.user
        try:
            about_db = About.objects.get(user_id=request.user.id)
            about['id'] = about_db.id
            force_update=True
        except ObjectDoesNotExist:
            force_insert=True
        form = AboutForm(about, request.FILES)
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
                      


