from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.urls import reverse_lazy

from .models import Staff

class StaffListView(ListView):
    model = Staff

class StaffDetailView(DetailView):
    model = Staff

class StaffCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Staff
    fields = '__all__'
    success_message = 'Karyawan sudah ditambah'

    def get_form(self):
        form = super(StaffCreateView, self).get_form()
        form.fields['tanggal_lahir'].widget = widgets.DateInput(
            attrs={'type': 'date'}
        )
        form.fields['tanggal_masuk'].widget = widgets.DateInput(
            attrs={'type': 'date'}
        )
        form.fields['alamat'].widget = widgets.Textarea(
            attrs={'rows': '1'}
        )
        form.fields['catatan'].widget = widgets.Textarea(
            attrs={'rows': '1'}
        )
        return form

class StaffUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Staff
    fields = '__all__'
    success_message = 'Karyawan sudah diubah'

    def get_form(self):
        form = super(StaffUpdateView, self).get_form()
        form.fields['tanggal_lahir'].widget = widgets.DateInput(
            attrs={'type': 'date'}
        )
        form.fields['tanggal_masuk'].widget = widgets.DateInput(
            attrs={'type': 'date'}
        )
        form.fields['alamat'].widget = widgets.Textarea(
            attrs={'rows': '1'}
        )
        form.fields['catatan'].widget = widgets.Textarea(
            attrs={'rows': '1'}
        )
        return form

class StaffDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Staff
    success_url = reverse_lazy('staff:list')