from django.contrib import admin
from django.utils.html import format_html
from .models import Destination, TourBooking, Payment


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'district', 'category', 'featured', 'is_active', 'created_at']
    list_filter = ['category', 'division', 'district', 'featured', 'is_active', 'difficulty_level']
    search_fields = ['name', 'location', 'district', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['featured', 'is_active']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'short_description')
        }),
        ('Location', {
            'fields': ('location', 'district', 'division', 'latitude', 'longitude')
        }),
        ('Classification', {
            'fields': ('category', 'difficulty_level')
        }),
        ('Images', {
            'fields': ('main_image', 'gallery_image_1', 'gallery_image_2', 'gallery_image_3')
        }),
        ('Details', {
            'fields': ('best_time_to_visit', 'entry_fee', 'duration')
        }),
        ('SEO & Status', {
            'fields': ('meta_description', 'featured', 'is_active')
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new object
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
        
@admin.register(TourBooking)
class TourBookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'user', 'destination', 'tour_date', 'number_of_people', 'total_amount', 'status', 'booking_date']
    list_filter = ['status', 'tour_date', 'booking_date', 'destination__category']
    search_fields = ['user__username', 'user__email', 'destination__name', 'contact_phone']
    readonly_fields = ['booking_date']
    list_editable = ['status']
    date_hierarchy = 'tour_date'
    
    fieldsets = (
        ('Booking Information', {
            'fields': ('user', 'destination', 'tour_date', 'number_of_people')
        }),
        ('Contact & Details', {
            'fields': ('contact_phone', 'special_requests')
        }),
        ('Payment & Status', {
            'fields': ('total_amount', 'status')
        }),
        ('Timestamps', {
            'fields': ('booking_date',),
            'classes': ('collapse',)
        }),
    )
    
    def booking_id(self, obj):
        return f"#{obj.id:05d}"
    booking_id.short_description = "Booking ID"
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('user', 'destination')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'booking_info', 'amount', 'payment_method', 'status', 'created_at']
    list_filter = ['status', 'payment_method', 'created_at']
    search_fields = ['booking__user__username', 'booking__destination__name', 'transaction_id']
    readonly_fields = ['created_at', 'updated_at', 'transaction_id']
    
    fieldsets = (
        ('Payment Information', {
            'fields': ('booking', 'amount', 'payment_method', 'transaction_id')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def payment_id(self, obj):
        return f"PAY-{obj.id:05d}"
    payment_id.short_description = "Payment ID"
    
    def booking_info(self, obj):
        return format_html(
            '<strong>{}</strong><br><small>{} - {}</small>',
            obj.booking.user.username,
            obj.booking.destination.name,
            obj.booking.tour_date
        )
    booking_info.short_description = "Booking Details"
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('booking__user', 'booking__destination')


# Inline admin for Payment in TourBooking
class PaymentInline(admin.StackedInline):
    model = Payment
    extra = 0
    readonly_fields = ['created_at', 'updated_at', 'transaction_id']
    
    fieldsets = (
        ('Payment Details', {
            'fields': ('amount', 'payment_method', 'transaction_id', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

# Update TourBookingAdmin to include Payment inline
TourBookingAdmin.inlines = [PaymentInline]