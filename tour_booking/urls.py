from django.urls import path
from . import views

app_name = 'tour_booking'

urlpatterns = [
    # Regular tour booking
    path('tour/<int:destination_id>/', views.tour_booking_view, name='tour_booking'),
    path('payment/<int:booking_id>/', views.payment_view, name='payment'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]