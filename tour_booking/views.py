from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TourBooking
from destination.models import Destination, Payment
import uuid


@login_required
def tour_booking_view(request, destination_id):
    """Regular tour booking for destinations"""
    destination = get_object_or_404(Destination, id=destination_id)
    
    if request.method == 'POST':
        user = request.user
        
        # Calculate total amount
        people = int(request.POST.get('number_of_people', 1))
        total_amount = destination.tour_price * people
        
        booking = TourBooking.objects.create(
            user=user,
            destination=destination,
            tour_date=request.POST.get('tour_date'),
            number_of_people=people,
            total_amount=total_amount,
            contact_phone=request.POST.get('contact_phone'),
            special_requests=request.POST.get('special_requests', ''),
        )
        
        # Redirect to payment
        return redirect('tour_booking:payment', booking_id=booking.id)
    
    context = {
        'destination': destination,
    }
    return render(request, 'tour_booking_form.html', context)


@login_required
def payment_view(request, booking_id):
    """Handle payment for tour booking"""
    booking = get_object_or_404(TourBooking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        
        # Create payment record
        payment = Payment.objects.create(
            transaction_id=str(uuid.uuid4()),
            amount=booking.total_amount,
            payment_method=payment_method,
            status='completed'  # In real app, this would be pending until payment gateway confirms
        )
        
        # Update booking
        booking.payment = payment
        booking.status = 'confirmed'
        booking.save()
        
        messages.success(request, 'Payment successful! Your booking is confirmed.')
        return redirect('tour_booking:booking_confirmation', booking_id=booking.id)
    
    context = {
        'booking': booking,
    }
    return render(request, 'payment.html', context)


@login_required
def booking_confirmation(request, booking_id):
    """Tour booking confirmation"""
    booking = get_object_or_404(TourBooking, id=booking_id, user=request.user)
    context = {
        'booking': booking,
    }
    return render(request, 'booking_confirmation.html', context)