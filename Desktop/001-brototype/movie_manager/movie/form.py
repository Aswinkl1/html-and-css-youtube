
from django.forms import ModelForm
from .models import movie_info

class movieForm(ModelForm):
    class Meta:
        model = movie_info
        fields = '__all__'
