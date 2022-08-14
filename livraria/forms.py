from django import forms
from .models import livro

class livroForm(forms.ModelForm):
    class Meta:
        model = livro
        fields = '__all__'
