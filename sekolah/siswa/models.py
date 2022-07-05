from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from utama.models import Kelas, Mapel

# Create your models here.
class Siswa(models.Model):
    STATUS = [
        ('aktif', 'Aktif'),
        ('lulus', 'Lulus'),
    ]
    GENDER = [
        ('pria', 'Pria'),
        ('wanita', 'Wanita'),
    ]

    status = models.CharField(choices=STATUS, max_length=20, default='aktif')
    nomor_pendaftaran = models.CharField(max_length=50, unique=True)
    nama = models.CharField(max_length=100)
    nama_panggilan = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=30)
    tanggal_lahir = models.DateField()
    kelas_sekarang = models.ForeignKey(Kelas, on_delete=models.SET_NULL, null=True, blank=True)
    tanggal_daftar = models.DateField(auto_now_add=True)
    hp_regex = RegexValidator(regex='^[0-9]{10-15}$', message='HP Tidak sesuai')
    hp_orang_tua = models.CharField(validators=[hp_regex], max_length=15, blank=True, null=True)
    alamat = models.TextField(blank=True)
    keterangan = models.TextField(blank=True)
    photo = models.ImageField(upload_to='siswa/photo', blank=True, null=True)

    class Meta:
        ordering = ['nama', 'nomor_pendaftaran']
    
    def __str__(self):
        return self.nama
    
    def get_absolute_url(self):
        return reverse('siswa:detail', kwargs={'pk': self.pk})