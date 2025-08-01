from django.urls import path
from . import views

app_name = 'destination'

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('<slug:slug>/', views.destination_detail, name='destination_detail'),
    path('<slug:slug>/book/', views.book_tour, name='book_tour'),
    path('payment/<int:booking_id>/', views.payment_view, name='payment'),
    path('booking-confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]