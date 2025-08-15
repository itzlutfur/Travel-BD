from django.urls import path
from . import views

app_name = 'hire_guide'

urlpatterns = [
    path('', views.guide_list, name='guides'),
    path('<slug:slug>/', views.guide_detail, name='guide_detail'),
    path('booking/payment/<str:booking_id>/', views.booking_payment, name='booking_payment'),
    path('booking/confirmation/<str:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]