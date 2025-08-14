from django.contrib import admin
from .models import Destination


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