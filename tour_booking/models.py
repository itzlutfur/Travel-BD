from django.db import models
from django.contrib.auth.models import User
from destination.models import Destination, Payment
import uuid

class TourBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    tour_date = models.DateField()
    number_of_people = models.IntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    booking_date = models.DateTimeField(auto_now_add=True)
    contact_phone = models.CharField(max_length=15)
    special_requests = models.TextField(blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.destination.name} - {self.tour_date}"
    
    class Meta:
        ordering = ['-booking_date']
        verbose_name = "Tour Booking"
        verbose_name_plural = "Tour Bookings"

class LocalGuideBooking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    GUIDE_TYPE_CHOICES = [
        ('city_tour', 'City Tour Guide'),
        ('adventure', 'Adventure Guide'),
        ('cultural', 'Cultural Guide'),
        ('nature', 'Nature Guide'),
        ('historical', 'Historical Guide'),
        ('photography', 'Photography Guide'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guide_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    guide_type = models.CharField(max_length=50, choices=GUIDE_TYPE_CHOICES)
    booking_date = models.DateTimeField(auto_now_add=True)
    service_date = models.DateField()
    duration_hours = models.IntegerField(default=4)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    contact_phone = models.CharField(max_length=15)
    special_requirements = models.TextField(blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Guide details
    languages_spoken = models.CharField(max_length=200, default="Bengali, English")
    experience_years = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.user.username} - {self.guide_name} - {self.service_date}"
    
    class Meta:
        ordering = ['-booking_date']
        verbose_name = "Local Guide Booking"
        verbose_name_plural = "Local Guide Bookings"
