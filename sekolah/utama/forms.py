from django.forms import ModelForm
from . import models

class TahunPelajaranForm(ModelForm):
    prefix = 'tahun_pelajaran'
    class Meta:
        model = models.TahunPelajaran
        fields = '__all__'

class SemesterForm(ModelForm):
    prefix = 'semester'
    class Meta:
        model = models.Semester
        fields = '__all__'

class KelasForm(ModelForm):
    prefix = 'kelas'
    class Meta:
        model = models.Kelas
        fields = '__all__'

class MapelForm(ModelForm):
    prefix = 'mata_pelajaran'
    class Meta:
        model = models.Mapel
        fields = '__all__'

class BiayaPendaftaranForm(ModelForm):
    prefix = 'biaya_pendaftaran'
    class Meta:
        model = models.BiayaPendaftaran
        fields = '__all__'