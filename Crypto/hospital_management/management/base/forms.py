from django import forms
from .models import Pharmacy, Feedback

class PharmaForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        fields = '__all__'


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'