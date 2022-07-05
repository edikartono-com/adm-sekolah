from django.db import models
from django.shortcuts import reverse

from utama.models import Semester, TahunPelajaran, Kelas, BiayaPendaftaran
from siswa.models import Siswa

# Create your models here.
class Tagihan(models.Model):
    murid = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    tahun = models.ForeignKey(TahunPelajaran, on_delete=models.CASCADE)
    smester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    untuk_kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    dari_semester_sebelumnya = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=[('aktif', 'Aktif'), ('lunas', 'Lunas')], default='aktif')

    class Meta:
        ordering = ['murid', 'smester']
    
    def __str__(self):
        return self.murid.nama

    # yang belum dibayar
    def balance(self):
        harus_dibayar = self.total_harus_dibayar()
        dibayarkan = self.jumlah_total_dibayar()
        return harus_dibayar - dibayarkan
    
    def yang_harus_dibayar(self):
        items = InvoiceItem.objects.filter(tagihan=self)
        total = 0
        for item in items:
            total += int(item.jumlah.uang_masuk)
        return total
    
    def total_harus_dibayar(self):
        return self.dari_semester_sebelumnya + self.yang_harus_dibayar()
    
    def jumlah_total_dibayar(self):
        terima = TandaTerima.objects.filter(tagihan=self)
        jumlah = 0
        for tanda in terima:
            jumlah += tanda.jumlah_dibayar
        return jumlah
    
    def get_absolute_url(self):
        return reverse('uang:tagihan-detail', kwargs={'pk': self.id})

class InvoiceItem(models.Model):
    tagihan = models.ForeignKey(Tagihan, on_delete=models.CASCADE)
    deskripsi = models.CharField(max_length=100)
    jumlah = models.ForeignKey(BiayaPendaftaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.deskripsi

class TandaTerima(models.Model):
    tagihan = models.ForeignKey(Tagihan, on_delete=models.CASCADE)
    jumlah_dibayar = models.IntegerField()
    tanggal_bayar = models.DateField()
    keterangan = models.CharField(max_length=125, null=True, blank=True)

    def __str__(self):
        return 'Tanda terima pada {}'.format(self.tagihan)