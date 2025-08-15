from django.contrib import admin
from .models import Guide, Booking


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'division', 'experience_level', 'rating', 'featured', 'is_active']
    list_filter = ['specialization', 'division', 'experience_level', 'featured', 'is_active']
    search_fields = ['name', 'location', 'district']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'guide', 'customer_name', 'start_date', 'end_date', 'total_amount', 'payment_status', 'status', 'created_at')
    list_filter = ('payment_status', 'status', 'start_date', 'created_at')
    search_fields = ('booking_id', 'customer_name', 'customer_email', 'guide__name')
    readonly_fields = ('booking_id', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Booking Information', {
            'fields': ('booking_id', 'guide', 'status')
        }),
        ('Customer Details', {
            'fields': ('customer_name', 'customer_email', 'customer_phone')
        }),
        ('Trip Details', {
            'fields': ('start_date', 'end_date', 'group_size', 'special_requirements')
        }),
        ('Payment Information', {
            'fields': ('total_amount', 'payment_status', 'transaction_id')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

