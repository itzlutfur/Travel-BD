from django.urls import path
from . import views

app_name = 'tour_booking'

urlpatterns = [
    # Regular tour booking
    path('tour/<int:destination_id>/', views.tour_booking_view, name='tour_booking'),
    path('payment/<int:booking_id>/', views.payment_view, name='payment'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    
    # Tour package booking
    path('package/', views.tour_package_booking, name='tour_package_booking'),
    path('package/<int:destination_id>/', views.tour_package_booking, name='tour_package_booking_with_destination'),
    path('package/confirmation/<int:booking_id>/', views.package_confirmation, name='package_confirmation'),
    
    # Local guide booking
    path('guide/', views.local_guide_booking, name='local_guide_booking'),
    path('guide/confirmation/<int:booking_id>/', views.guide_confirmation, name='guide_confirmation'),
    
    # Utilities
    path('calculate-cost/', views.calculate_total_cost, name='calculate_total_cost'),
]