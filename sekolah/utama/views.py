from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from . import forms, models

# Create your views here.
def index_utama(request):
    return render(request, 'index.html')

@login_required
def developer(request):
    return render(request, 'developer.html')

# Tahun Pelajaran
class TahunPelajaranView(LoginRequiredMixin, ListView):
    queryset = models.TahunPelajaran.objects.all()

class TahunPelajaranAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = forms.TahunPelajaranForm
    template_name = 'utama/form_utama.html'
    success_message = 'Tahun pelajaran baru berhasil ditambah'
    success_url = reverse_lazy('utama:ta-list')
    extra_context = {
        'title': 'Tahun Pelajaran Baru'
    }

class TahunPelajaranEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    queryset = models.TahunPelajaran.objects.all()
    form_class = forms.TahunPelajaranForm
    template_name = 'utama/form_utama.html'
    success_message = 'Tahun pelajaran baru sudah diperbarui'
    success_url = reverse_lazy('utama:ta-list')
    extra_context = {
        'title': 'Update tahun pelajaran'
    }

class TahunPelajaranDel(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'utama/confirm_delete.html'
    success_message = 'Tahun pelajaran berhasil dihapus'
    success_url = reverse_lazy('utama:ta-list')
    extra_context = {
        'title': 'Hapus tahun pelajaran'
    }

    def get_queryset(self):
        self.queryset = models.TahunPelajaran.objects.filter(id=self.kwargs['pk'])
        return super().get_queryset()
    
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.sekarang == True:
            messages.warning(request, 'Tidak bisa menghapus tahun pelajaran sekarang!!')
            return redirect('utama:ta-list')
        messages.success(self.request, self.success_message.format(obj.name))
        return super(TahunPelajaranDel, self).delete(request, *args, **kwargs)

# Semester
class SemesterView(LoginRequiredMixin, ListView):
    queryset = models.Semester.objects.all()

class SemesterAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = forms.SemesterForm
    template_name = 'utama/form_utama.html'
    success_message = 'Semester baru berhasil ditambah'
    success_url = reverse_lazy('utama:smt-list')
    extra_context = {
        'title': 'Semester Baru'
    }

class SemesterEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    queryset = models.Semester.objects.all()
    form_class = forms.SemesterForm
    template_name = 'utama/form_utama.html'
    success_message = 'Semester baru sudah diperbarui'
    success_url = reverse_lazy('utama:smt-list')
    extra_context = {
        'title': 'Update semester'
    }

class SemesterDel(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'utama/confirm_delete.html'
    success_message = 'Semester berhasil dihapus'
    success_url = reverse_lazy('utama:smt-list')
    extra_context = {
        'title': 'Hapus semester'
    }

    def get_queryset(self):
        self.queryset = models.Semester.objects.filter(id=self.kwargs['pk'])
        return super().get_queryset()
    
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.sekarang == True:
            messages.warning(request, 'Tidak bisa menghapus semester sekarang!!')
            return redirect('utama:smt-list')
        messages.success(self.request, self.success_message.format(obj.name))
        return super(SemesterDel, self).delete(request, *args, **kwargs)

class KelasView(LoginRequiredMixin, ListView):
    queryset = models.Kelas.objects.all()

class KelasAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = forms.KelasForm
    template_name = 'utama/form_utama.html'
    success_message = 'Kelas baru berhasil ditambah'
    success_url = reverse_lazy('utama:kls-list')
    extra_context = {
        'title': 'Kelas Baru'
    }

class KelasEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    queryset = models.Kelas.objects.all()
    form_class = forms.KelasForm
    template_name = 'utama/form_utama.html'
    success_message = 'Kelas baru sudah diperbarui'
    success_url = reverse_lazy('utama:kls-list')
    extra_context = {
        'title': 'Update kelas'
    }

class KelasDel(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'utama/confirm_delete.html'
    success_message = 'Kelas berhasil dihapus'
    success_url = reverse_lazy('utama:kls-list')
    extra_context = {
        'title': 'Hapus kelas'
    }

    def get_queryset(self):
        self.queryset = models.Kelas.objects.filter(id=self.kwargs['pk'])
        return super().get_queryset()

class MapelView(LoginRequiredMixin, ListView):
    queryset = models.Mapel.objects.all()

class MapelAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = forms.MapelForm
    template_name = 'utama/form_utama.html'
    success_message = 'Mata Pelajaran baru ditambah'
    success_url = reverse_lazy('utama:mpl-list')
    extra_context = {
        'title': 'Mata Pelajaran'
    }

class MapelEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    queryset = models.Mapel.objects.all()
    form_class = forms.MapelForm
    template_name = 'utama/form_utama.html'
    success_message = 'Mata Pelajaran Update'
    success_url = reverse_lazy('utama:mpl-list')
    extra_context = {
        'title': 'Update Mata Pelajaran'
    }

class MapelDel(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'utama/confirm_delete.html'
    success_message = 'Mata Pelajaran berhasil dihapus'
    success_url = reverse_lazy('utama:mpl-list')
    extra_context = {
        'title': 'Hapus Mata Pelajaran'
    }

    def get_queryset(self):
        self.queryset = models.Mapel.objects.filter(id=self.kwargs['pk'])
        return super().get_queryset()

class BiayaMasuk(LoginRequiredMixin, ListView):
    queryset = models.BiayaPendaftaran.objects.all()

class BiayaAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = forms.BiayaPendaftaranForm
    template_name = 'utama/form_utama.html'
    success_message = 'Biaya Pendafaran baru ditambah'
    success_url = reverse_lazy('utama:biaya')
    extra_context = {
        'title': 'Biaya Pendaftaran'
    }

class BiayaEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    queryset = models.BiayaPendaftaran.objects.all()
    form_class = forms.BiayaPendaftaranForm
    template_name = 'utama/form_utama.html'
    success_message = 'Biaya Pendaftaran Update'
    success_url = reverse_lazy('utama:biaya')
    extra_context = {
        'title': 'Update Biaya Pendaftaran'
    }