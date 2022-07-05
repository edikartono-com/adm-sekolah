from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Siswa
from keuangan.models import Tagihan
from .forms import SiswaForm

# Create your views here.
class SiswaList(LoginRequiredMixin, ListView):
    queryset = Siswa.objects.all()

class SiswaAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = SiswaForm
    success_message = 'Siswa baru terdaftar'
    success_url = reverse_lazy('siswa:murid')
    template_name = 'utama/form_utama.html'
    extra_context = {
        'title': 'Pendaftaran Siswa'
    }

class SiswaEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    queryset = Siswa.objects.all()
    form_class = SiswaForm
    success_message = 'Siswa berhasil diupdate'
    success_url = reverse_lazy('siswa:murid')
    template_name = 'utama/form_utama.html'
    extra_context = {
        'title': 'Update Siswa'
    }

class SiswaDetail(LoginRequiredMixin, DetailView):
    queryset = Siswa.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SiswaDetail, self).get_context_data(**kwargs)
        context['pembayaran'] = Tagihan.objects.filter(murid=self.object)
        return context