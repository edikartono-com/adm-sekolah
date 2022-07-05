from django.urls import path
from . import views

app_name = 'uang'
urlpatterns = [
    path('baru/', views.TagihanBaru.as_view(), name='tagihan-baru'),
    path('detail/<int:pk>/', views.TagihanDetail.as_view(), name='tagihan-detail'),
    path('delete/<int:pk>/', views.TagihanHapus.as_view(), name='tagihan-delete'),
    path('tanda-terima/', views.TandaTerimaAdd.as_view(), name='tanda-terima'),
    path('tanda-terima/edit/<int:pk>', views.TagihanEdit.as_view(), name='ttd-edit'),
    path('', views.TagihanView.as_view(), name='index'),
]