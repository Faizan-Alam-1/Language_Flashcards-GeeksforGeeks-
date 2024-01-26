from django import forms
from .models import Addcard

class Addcardform(forms.ModelForm):
    class Meta:
        model = Addcard
        fields = ['input_box', 'text_area']