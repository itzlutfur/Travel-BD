from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import TourBooking, LocalGuideBooking
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
    # Use a simple booking template in the root templates folder
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
    # Use the existing payment.html template
    return render(request, 'payment.html', context)

@login_required
def booking_confirmation(request, booking_id):
    """Tour booking confirmation"""
    booking = get_object_or_404(TourBooking, id=booking_id, user=request.user)
    context = {
        'booking': booking,
    }
    # Use the existing booking_confirmation.html template
    return render(request, 'booking_confirmation.html', context)

@login_required
def tour_package_booking(request, destination_id=None):
    """View for booking tour packages"""
    destination = None
    if destination_id:
        destination = get_object_or_404(Destination, id=destination_id)
    
    if request.method == 'POST':
        user = request.user
        destination_id = request.POST.get('destination')
        destination = get_object_or_404(Destination, id=destination_id)
        
        booking = TourBooking.objects.create(
            user=user,
            destination=destination,
            package_name=request.POST.get('package_name'),
            tour_date=request.POST.get('tour_date'),
            number_of_people=int(request.POST.get('number_of_people', 1)),
            duration_days=int(request.POST.get('duration_days', 1)),
            total_amount=float(request.POST.get('total_amount')),
            contact_phone=request.POST.get('contact_phone'),
            special_requests=request.POST.get('special_requests', ''),
            includes_accommodation=request.POST.get('includes_accommodation') == 'on',
            includes_meals=request.POST.get('includes_meals') == 'on',
            includes_transport=request.POST.get('includes_transport') == 'on',
            includes_guide=request.POST.get('includes_guide') == 'on',
        )
        
        messages.success(request, 'Tour package booked successfully!')
        return redirect('tour_booking:package_confirmation', booking_id=booking.id)
    
    destinations = Destination.objects.filter(is_active=True)
    context = {
        'destinations': destinations,
        'selected_destination': destination,
    }
    return render(request, 'tour_booking/tour_package_booking.html', context)

@login_required
def local_guide_booking(request):
    """View for booking local guides"""
    if request.method == 'POST':
        user = request.user
        
        booking = LocalGuideBooking.objects.create(
            user=user,
            guide_name=request.POST.get('guide_name'),
            location=request.POST.get('location'),
            guide_type=request.POST.get('guide_type'),
            service_date=request.POST.get('service_date'),
            duration_hours=int(request.POST.get('duration_hours', 4)),
            hourly_rate=float(request.POST.get('hourly_rate')),
            total_cost=float(request.POST.get('total_cost')),
            contact_phone=request.POST.get('contact_phone'),
            special_requirements=request.POST.get('special_requirements', ''),
            languages_spoken=request.POST.get('languages_spoken', 'Bengali, English'),
            experience_years=int(request.POST.get('experience_years', 1)),
        )
        
        messages.success(request, 'Local guide booked successfully!')
        return redirect('tour_booking:guide_confirmation', booking_id=booking.id)
    
    return render(request, 'tour_booking/local_guide_booking.html')

@login_required
def package_confirmation(request, booking_id):
    """Tour package booking confirmation"""
    booking = get_object_or_404(TourBooking, id=booking_id, user=request.user)
    return render(request, 'tour_booking/package_confirmation.html', {'booking': booking})

@login_required
def guide_confirmation(request, booking_id):
    """Local guide booking confirmation"""
    booking = get_object_or_404(LocalGuideBooking, id=booking_id, user=request.user)
    return render(request, 'tour_booking/guide_confirmation.html', {'booking': booking})

def calculate_total_cost(request):
    """AJAX view to calculate total cost"""
    if request.method == 'GET':
        duration_hours = int(request.GET.get('duration_hours', 4))
        hourly_rate = float(request.GET.get('hourly_rate', 0))
        total_cost = duration_hours * hourly_rate
        
        return JsonResponse({'total_cost': total_cost})
    
    return JsonResponse({'error': 'Invalid request'})
