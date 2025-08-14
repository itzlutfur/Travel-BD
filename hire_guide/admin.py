from django.contrib import admin
from .models import Guide


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'division', 'experience_level', 'rating', 'featured', 'is_active']
    list_filter = ['specialization', 'division', 'experience_level', 'featured', 'is_active']
    search_fields = ['name', 'location', 'district']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']



