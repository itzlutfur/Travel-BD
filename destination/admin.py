from django.contrib import admin
from django.utils.html import format_html
from .models import Destination


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