from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Staff(models.Model):
    STATUS = {
        ('active', 'Active'),
        ('inactive', 'Inactive')
    }
    GENDER = {
        ('pria', 'Pria'),
        ('wanita', 'Wanita')
    }
    status_sekarang = models.CharField(max_length=10, choices=STATUS, default='active')
    nama = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='pria')
    tanggal_lahir = models.DateField()
    tanggal_masuk = models.DateField()
    nomor_hp = models.CharField(max_length=15, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    catatan = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.nama, self.status_sekarang)
    
    def get_absolute_url(self):
        return reverse('staff:detail', kwargs={'pk': self.pk})