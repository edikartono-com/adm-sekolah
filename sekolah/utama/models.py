from django.db import models

# Create your models here.
class TahunPelajaran(models.Model):
    name = models.CharField(max_length=200, unique=True)
    sekarang = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ['-name']
    
    def __str__(self):
        return str(self.name)

class Semester(models.Model):
    SEMETER = {
        ('genap', 'Genap'),
        ('ganjil', 'Ganjil'),
    }
    name = models.CharField(choices=SEMETER, max_length=10)
    sekarang = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Kelas(models.Model):
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Mapel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class BiayaPendaftaran(models.Model):
    tahun_pelajaran = models.OneToOneField(TahunPelajaran, on_delete=models.CASCADE)
    uang_masuk = models.CharField(max_length=200)

    class Meta:
        ordering = ['tahun_pelajaran']
    
    def __str__(self):
        return self.tahun_pelajaran