from django.urls import path

from . import views

app_name = 'utama'
urlpatterns = [
    path('dev/', views.developer, name='dev'),
    path('setting/tahun-pelajaran/', views.TahunPelajaranView.as_view(), name='ta-list'),
    path('setting/tahun-pelajaran/add/', views.TahunPelajaranAdd.as_view(), name='ta-add'),
    path('setting/tahun-pelajaran/<int:pk>/edit/', views.TahunPelajaranEdit.as_view(), name='ta-edit'),
    path('setting/tahun-pelajaran/<int:pk>/del/', views.TahunPelajaranDel.as_view(), name='ta-del'),
    path('setting/semester/', views.SemesterView.as_view(), name='smt-list'),
    path('setting/semester/add/', views.SemesterAdd.as_view(), name='smt-add'),
    path('setting/semester/<int:pk>/edit/', views.SemesterEdit.as_view(), name='smt-edit'),
    path('setting/semester/<int:pk>/del/', views.SemesterDel.as_view(), name='smt-del'),
    path('setting/kelas/', views.KelasView.as_view(), name='kls-list'),
    path('setting/kelas/add/', views.KelasAdd.as_view(), name='kls-add'),
    path('setting/kelas/<int:pk>/edit/', views.KelasEdit.as_view(), name='kls-edit'),
    path('setting/kelas/<int:pk>/del/', views.KelasDel.as_view(), name='kls-del'),
    path('setting/mapel/', views.MapelView.as_view(), name='mpl-list'),
    path('setting/mapel/add/', views.MapelAdd.as_view(), name='mpl-add'),
    path('setting/mapel/<int:pk>/edit/', views.MapelEdit.as_view(), name='mpl-edit'),
    path('setting/mapel/<int:pk>/del/', views.MapelDel.as_view(), name='mpl-del'),
    path('setting/biaya/', views.BiayaMasuk.as_view(), name='biaya'),
    path('setting/biaya/pendaftaran/', views.BiayaAdd.as_view(), name='bi-add'),
    path('setting/biaya/<int:pk>/edit/', views.BiayaEdit.as_view(), name='bi-edit'),
    path('', views.index_utama, name='index'),
]