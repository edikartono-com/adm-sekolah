from django.urls import path

from . import views

app_name = 'siswa'

urlpatterns = [
    path('baru/', views.SiswaAdd.as_view(), name='baru'),
    path('update/<int:pk>/', views.SiswaEdit.as_view(), name='update'),
    path('detail/<int:pk>/', views.SiswaDetail.as_view(), name='detail'),
    path('', views.SiswaList.as_view(), name='murid'),
]