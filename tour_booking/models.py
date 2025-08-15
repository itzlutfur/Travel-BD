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
