from django import forms
from django.forms import ModelForm
from .models import Siswa

class SiswaForm(ModelForm):
    prefix = 'siswa'
    class Meta:
        model = Siswa
        fields = '__all__'
        widgets = {
            'tanggal_lahir': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
            'alamat': forms.Textarea(
                attrs={
                    'rows': '2'
                }
            ),
            'keterangan': forms.Textarea(
                attrs={
                    'rows': '2'
                }
            ),
        }