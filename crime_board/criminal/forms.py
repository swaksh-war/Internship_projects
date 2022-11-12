from django.forms import ModelForm
from .models import Criminal
class criminaladdform(ModelForm):
    class Meta:
        model = Criminal
        fields = '__all__'
