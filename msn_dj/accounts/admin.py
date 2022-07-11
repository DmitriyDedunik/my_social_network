from pyexpat import model
from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
    pass

admin.site.register(City, CityAdmin)

