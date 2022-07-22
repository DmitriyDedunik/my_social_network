from asyncio.windows_events import NULL
from dataclasses import field
from distutils.log import error
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from .models import About, Friend
from .forms import AboutForm, RigisterUserForm, FriendAddForm
from django.views.generic.edit import CreateView, UpdateView
from django.db import transaction
from django.http import HttpResponseRedirect


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
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def profile(request):
   
    template_name = 'profile.html'
    
    about = About.objects.get(user_id=request.user.id)

    invitation_friends = Friend.objects.filter(user_with_add=request.user.id)
    invitation_friends = invitation_friends.filter(accept=False)
    invitation_friends_id = []
    for invitation_friend in invitation_friends:
        invitation_friends_id.append(invitation_friend.user_who_add_id)

    invitation_friends_inc = Friend.objects.filter(user_who_add_id=request.user.id)
    invitation_friends_inc = invitation_friends_inc.filter(accept=False)
    invitation_friends_id_inc = []
    for invitation_friend_inc in invitation_friends_inc:
        invitation_friends_id_inc.append(invitation_friend_inc.user_with_add_id)

    friends = Friend.objects.filter(user_with_add=request.user.id)
    friends = friends.filter(accept=True)
    friends_id = []
    for friend in friends:
        friends_id.append(friend.user_who_add_id)

    friend_candidat_list = User.objects.exclude(pk=request.user.id)
    friend_candidat_list = friend_candidat_list.exclude(pk__in=invitation_friends_id)
    friend_candidat_list = friend_candidat_list.exclude(pk__in=friends_id)
    friend_candidat_list = friend_candidat_list.exclude(pk__in=invitation_friends_id_inc)
    
    context = {'friends' : friends,
               'invitation_friends' : invitation_friends,
               'invitation_friends_inc' : invitation_friends_inc,
               'friend_candidat_list' : friend_candidat_list,
               'about' : about
               }
               
    return render(request, template_name, context)

def profile_update(request):
    try:
        about_db = About.objects.get(user_id=request.user.id)
        return HttpResponseRedirect(reverse('accounts:aboutupdate', kwargs={'pk':about_db.id}))
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('accounts:aboutcreate'))
                     
def friend_add(request, pk):
    
    friend = User.objects.get(pk=pk)
    model_friend = Friend()
    model_friend.user_who_add = request.user
    model_friend.user_with_add = friend
    model_friend.accept = True

    model_friend2 = Friend()
    model_friend2.user_who_add = friend
    model_friend2.user_with_add = request.user
    model_friend2.accept = NULL

    try:
        with transaction.atomic():
            model_friend.save()
            model_friend2.save()

    except error as e:
        print(e)
    
    return redirect(reverse_lazy('accounts:profile'))

def friends_confirmation(request, pk):
    model_friend = Friend()
    model_friend.accept = True
    model_friend.pk = pk
    model_friend.save(update_fields=['accept'])

    return redirect(reverse_lazy('accounts:profile'))

def friends(request):
    pass
