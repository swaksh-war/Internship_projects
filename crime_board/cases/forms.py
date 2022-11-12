from django.forms import ModelForm
from . models import Crimecase

class crimeaddform(ModelForm):
    class Meta:
        model = Crimecase
        fields = '__all__'
