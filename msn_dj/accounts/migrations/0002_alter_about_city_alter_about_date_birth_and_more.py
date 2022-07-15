# Generated by Django 4.0.6 on 2022-07-14 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.city', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='about',
            name='date_birth',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='about',
            name='hobbies',
            field=models.TextField(max_length=500, verbose_name='Хобби'),
        ),
        migrations.AlterField(
            model_name='about',
            name='main_photo',
            field=models.ImageField(null=True, upload_to='users_photo', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='about',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
