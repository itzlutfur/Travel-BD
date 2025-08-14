from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class Destination(models.Model):
    CATEGORY_CHOICES = [
        ('beach', 'Beach'),
        ('mountain', 'Mountain'),
        ('historical', 'Historical'),
        ('cultural', 'Cultural'),
        ('adventure', 'Adventure'),
        ('religious', 'Religious'),
    ]
    
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('hard', 'Hard'),
    ]
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    description = models.TextField()
    short_description = models.TextField(max_length=300, blank=True)
    location = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='easy')
    
    # Basic info
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    duration = models.CharField(max_length=100, default="1 Day")
    best_time_to_visit = models.CharField(max_length=200)
    
    # Tour package info
    tour_price = models.DecimalField(max_digits=10, decimal_places=2)
    tour_duration_days = models.IntegerField(default=1)
    max_group_size = models.IntegerField(default=10)
    tour_includes = models.TextField(blank=True)
    tour_excludes = models.TextField(blank=True)
    
    # Images
    main_image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    
    # Location
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    # Meta
    featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('bkash', 'bKash'),
        ('nagad', 'Nagad'),
        ('card', 'Credit/Debit Card'),
        ('bank', 'Bank Transfer'),
    ]
    
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Payment {self.transaction_id} - {self.amount}"