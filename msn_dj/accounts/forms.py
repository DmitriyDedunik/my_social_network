from pyexpat import model
from .models import About
from django.forms import HiddenInput, ModelForm, SelectDateWidget, DateInput
from datetime import datetime
from django.contrib.auth.forms import UserModel, UserCreationForm
from django.db import models

class AboutForm(ModelForm):
    
    class Meta:
        
        cur_year = datetime.today().year
        year_range = tuple([i for i in range(cur_year - 100, cur_year + 1)])

        model = About
        fields = ('date_birth', 'city', 'hobbies', 'main_photo')
        widgets = {
            'date_birth': SelectDateWidget(years=year_range),
            # 'user': HiddenInput(),
            # 'id': HiddenInput(),
            # 'date_birth': DateInput(attrs={'type':'date'})
            }


class RigisterUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')


class FriendAddForm(ModelForm):
    class Meta:
        fields = ('user_who_add', 'user_with_add', 'accept')



