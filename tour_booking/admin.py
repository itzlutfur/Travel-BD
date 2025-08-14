from django.contrib import admin
from .models import TourBooking, LocalGuideBooking

@admin.register(TourBooking)
class TourBookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'destination', 'tour_date', 'number_of_people', 'total_amount', 'status', 'booking_date']
    list_filter = ['status', 'tour_date', 'booking_date', 'destination__district']
    search_fields = ['user__username', 'user__email', 'destination__name', 'contact_phone']
    readonly_fields = ['booking_date']
    date_hierarchy = 'tour_date'
    
    fieldsets = (
        ('Booking Information', {
            'fields': ('user', 'destination', 'tour_date', 'number_of_people')
        }),
        ('Contact & Requests', {
            'fields': ('contact_phone', 'special_requests')
        }),
        ('Payment & Status', {
            'fields': ('total_amount', 'status', 'payment', 'booking_date')
        }),
    )

