from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from siswa.models import Siswa
from .models import Tagihan, InvoiceItem, TandaTerima
from .forms import InvoiceItemFormset, TandaTerimaFormset, TandaTerimaForm
# Create your views here.

class TagihanView(LoginRequiredMixin, ListView):
    queryset = Tagihan.objects.all()
    fields = '__all__'

class TagihanBaru(LoginRequiredMixin, CreateView):
    model = Tagihan
    fields = '__all__'
    success_url = reverse_lazy('uang:index')

    def get_context_data(self, **kwargs):
        context = super(TagihanBaru, self).get_context_data(**kwargs)
        if self.request.POST:
            context['items'] = InvoiceItemFormset(
                self.request.POST, prefix='tagihanitem_set'
            )
        else:
            context['items'] = InvoiceItemFormset(
                prefix='tagihanitem_set'
            )
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['items']
        self.object = form.save()
        if self.object.id != None:
            if form.is_valid() and formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)

class TagihanDetail(LoginRequiredMixin, DetailView):
    queryset = Tagihan.objects.all()
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(TagihanDetail, self).get_context_data(**kwargs)
        context['masuk'] = TandaTerima.objects.filter(tagihan=self.object)
        context['items'] = InvoiceItem.objects.filter(tagihan=self.object)
        return context

class TagihanHapus(LoginRequiredMixin, DeleteView):
    queryset = Tagihan.objects.all()
    success_url = reverse_lazy('uang:index')
    template_name = 'utama/confirm_delete.html'

class TagihanEdit(LoginRequiredMixin, UpdateView):
    queryset = Tagihan.objects.all()
    fields = ['status']

    def get_context_data(self, **kwargs):
        context = super(TagihanEdit, self).get_context_data(**kwargs)
        if self.request.POST:
            context['masuk'] = TandaTerimaFormset(self.request.POST, instance=self.object)
        else:
            context['masuk'] = TandaTerimaFormset(instance=self.object)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['masuk']
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
        return super().form_valid(form)

class TandaTerimaAdd(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = TandaTerima
    form_class = TandaTerimaForm
    success_url = reverse_lazy('uang:index')
    success_message = 'Pembayaran telah ditambahkan'

    def get_context_data(self, **kwargs):
        context = super(TandaTerimaAdd, self).get_context_data(**kwargs)
        tagihan = Tagihan.objects.get(pk=self.request.GET['pk'])
        context['tagihan'] = tagihan
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        tagihan = Tagihan.objects.get(pk=self.request.GET['pk'])
        obj.tagihan = tagihan
        obj.save()
        return redirect('uang:index')