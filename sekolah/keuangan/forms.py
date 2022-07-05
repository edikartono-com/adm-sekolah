from django import forms
from django.forms import inlineformset_factory

from .models import Tagihan, InvoiceItem, TandaTerima

InvoiceItemFormset = inlineformset_factory(
    Tagihan, InvoiceItem, fields=['deskripsi', 'jumlah'], extra=1, can_delete=True
)

TandaTerimaFormset = inlineformset_factory(
    Tagihan, TandaTerima, fields=[
        'jumlah_dibayar',
        'tanggal_bayar',
        'keterangan',
    ],
    widgets={
        'tanggal_bayar': forms.DateInput(
            attrs={
                'type': 'date'
            }
        )
    },
    extra=0, can_delete=True
)

class TandaTerimaForm(forms.ModelForm):
    class Meta:
        model = TandaTerima
        fields = ['jumlah_dibayar', 'tanggal_bayar', 'keterangan']
        widgets = {
            'tanggal_bayar': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }