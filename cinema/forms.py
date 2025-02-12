# forms.py 
from django import forms 
from.models import estrenos

class estrenosForm(forms.ModelForm): 
    class Meta: 
        model = estrenos
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'imagen']