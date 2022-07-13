from django.db import models
from django.conf import settings

class About(models.Model):
    date_birth = models.DateField(verbose_name='Дата рождения')
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, verbose_name='Город')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Пользователь')
    hobbies = models.TextField(max_length=500, verbose_name='Хобби')
    main_photo = models.ImageField(upload_to='users_photo', verbose_name='Фотография')

class City(models.Model):
    name = models.TextField(max_length=150)
    
    def __str__(self):
        return self.name