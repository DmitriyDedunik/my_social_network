from .models import About
from django.forms import HiddenInput, ModelForm, SelectDateWidget, DateInput
from datetime import datetime

class AboutForm(ModelForm):
    
    class Meta:
        
        cur_year = datetime.today().year
        year_range = tuple([i for i in range(cur_year - 100, cur_year + 1)])

        model = About
        fields = ('date_birth', 'city', 'hobbies', 'main_photo', 'user')
        widgets = {
            'date_birth': SelectDateWidget(years=year_range),
            'user': HiddenInput(),
            # 'date_birth': DateInput(attrs={'type':'date'})
            }