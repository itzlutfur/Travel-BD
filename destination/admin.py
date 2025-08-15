from django.contrib import admin
from .models import Destination, Payment


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'division', 'featured', 'is_active', 'created_at']
    list_filter = ['category', 'division', 'difficulty_level', 'featured', 'is_active']
    search_fields = ['name', 'location', 'district']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'short_description', 'description')
        }),
        ('Location', {
            'fields': ('location', 'district', 'division', 'latitude', 'longitude')
        }),
        ('Category & Difficulty', {
            'fields': ('category', 'difficulty_level')
        }),
        ('Tour Details', {
            'fields': ('entry_fee', 'duration', 'best_time_to_visit', 'tour_price', 
                      'tour_duration_days', 'max_group_size', 'tour_includes', 'tour_excludes')
        }),
        ('Media', {
            'fields': ('main_image',)
        }),
        ('Settings', {
            'fields': ('featured', 'is_active', 'created_at', 'updated_at')
        }),
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'amount', 'payment_method', 'status', 'created_at']
    list_filter = ['payment_method', 'status', 'created_at']
    search_fields = ['transaction_id', 'amount']
    readonly_fields = ['transaction_id', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Payment Information', {
            'fields': ('transaction_id', 'amount', 'payment_method')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    # Additional admin options
    list_per_page = 25
    ordering = ['-created_at']
    
    # Custom actions
    actions = ['mark_as_completed', 'mark_as_failed', 'mark_as_refunded']
    
    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
        self.message_user(request, f'{queryset.count()} payments marked as completed.')
    mark_as_completed.short_description = "Mark selected payments as completed"
    
    def mark_as_failed(self, request, queryset):
        queryset.update(status='failed')
        self.message_user(request, f'{queryset.count()} payments marked as failed.')
    mark_as_failed.short_description = "Mark selected payments as failed"
    
    def mark_as_refunded(self, request, queryset):
        queryset.update(status='refunded')
        self.message_user(request, f'{queryset.count()} payments marked as refunded.')
    mark_as_refunded.short_description = "Mark selected payments as refunded"