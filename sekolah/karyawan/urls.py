from django.urls import path

from .views import StaffListView, StaffDetailView, StaffCreateView, StaffUpdateView, StaffDeleteView

app_name = 'staff'
urlpatterns = [
    path('list/', StaffListView.as_view(), name='list'),
    path('detail/<pk>/', StaffDetailView.as_view(), name='detail'),
    path('create/', StaffCreateView.as_view(), name='create'),
    path('update/<pk>/', StaffUpdateView.as_view(), name='update'),
    path('delete/<pk>/', StaffDeleteView.as_view(), name='delete'),
]