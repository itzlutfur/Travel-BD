from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Destination, TourBooking, Payment
import json
from datetime import datetime
import uuid


def destination_list(request):
    """View to display all destinations with pagination and filtering"""
    destinations = Destination.objects.filter(is_active=True).order_by('-featured', '-created_at')
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        destinations = destinations.filter(
            Q(name__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(district__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Category filtering
    category = request.GET.get('category')
    if category:
        destinations = destinations.filter(category=category)
    
    # Division filtering
    division = request.GET.get('division')
    if division:
        destinations = destinations.filter(division=division)
    
    # Pagination - 9 destinations per page
    paginator = Paginator(destinations, 9)
    page = request.GET.get('page')
    
    try:
        destinations = paginator.page(page)
    except PageNotAnInteger:
        destinations = paginator.page(1)
    except EmptyPage:
        destinations = paginator.page(paginator.num_pages)
    
    # Get unique categories and divisions for filters
    categories = Destination.objects.filter(is_active=True).values_list('category', flat=True).distinct()
    divisions = Destination.objects.filter(is_active=True).values_list('division', flat=True).distinct()
    
    context = {
        'destinations': destinations,
        'categories': categories,
        'divisions': divisions,
        'search_query': search_query,
        'selected_category': category,
        'selected_division': division,
    }
    
    return render(request, 'destination.html', context)


def destination_detail(request, slug):
    """View to display individual destination details"""
    destination = get_object_or_404(Destination, slug=slug, is_active=True)
    
    # Get related destinations (same category or division)
    related_destinations = Destination.objects.filter(
        Q(category=destination.category) | Q(division=destination.division)
    ).exclude(id=destination.id).filter(is_active=True)[:4]
    
    context = {
        'destination': destination,
        'related_destinations': related_destinations,
    }
    
    return render(request, 'destination_detail.html', context)


def featured_destinations(request):
    """View to display featured destinations"""
    destinations = Destination.objects.filter(featured=True, is_active=True)
    
    context = {
        'destinations': destinations,
    }
    
    return render(request, 'destination.html', context)


@login_required
def book_tour(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    
    if request.method == 'POST':
        tour_date = request.POST.get('tour_date')
        number_of_people = int(request.POST.get('number_of_people', 1))
        contact_phone = request.POST.get('contact_phone')
        special_requests = request.POST.get('special_requests', '')
        
        total_amount = destination.tour_price * number_of_people
        
        booking = TourBooking.objects.create(
            user=request.user,
            destination=destination,
            tour_date=tour_date,
            number_of_people=number_of_people,
            total_amount=total_amount,
            contact_phone=contact_phone,
            special_requests=special_requests
        )
        
        return redirect('destination:payment', booking_id=booking.id)
    
    return render(request, 'book_tour.html', {'destination': destination})

@login_required
def payment_view(request, booking_id):
    booking = get_object_or_404(TourBooking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        
        # Create payment record
        payment = Payment.objects.create(
            booking=booking,
            amount=booking.total_amount,
            payment_method=payment_method,
            transaction_id=str(uuid.uuid4()),
            status='completed'  # In real app, this would be 'pending' until payment gateway confirms
        )
        
        # Update booking status
        booking.status = 'confirmed'
        booking.save()
        
        messages.success(request, 'Payment successful! Your tour is booked.')
        return redirect('destination:booking_confirmation', booking_id=booking.id)
    
    return render(request, 'payment.html', {'booking': booking})

@login_required
def booking_confirmation(request, booking_id):
    booking = get_object_or_404(TourBooking, id=booking_id, user=request.user)
    return render(request, 'booking_confirmation.html', {'booking': booking})