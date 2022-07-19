from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

User._meta.get_field('email').blank = False


class About(models.Model):
    date_birth = models.DateField(verbose_name='Дата рождения')
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, verbose_name='Город')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Пользователь', unique=True)
    hobbies = models.TextField(max_length=500, verbose_name='Хобби')
    main_photo = models.ImageField(upload_to='users_photo', verbose_name='Фотография', null=True, blank=True)

class Profile(User):
    date_birth = models.DateField(verbose_name='Дата рождения')
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, verbose_name='Город')
    hobbies = models.TextField(max_length=500, verbose_name='Хобби')
    main_photo = models.ImageField(upload_to='users_photo', verbose_name='Фотография', null=True, blank=True)


class City(models.Model):
    name = models.TextField(max_length=150)
    
    def __str__(self):
        return self.name


class Friend(models.Model):
    user_who_add = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Пользователь', related_name='User')
    user_with_add = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Друг', related_name='Friend')
    accept = models.BooleanField(verbose_name='Приглашение от пользователя', null=True)