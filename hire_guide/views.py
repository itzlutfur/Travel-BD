from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from .models import Guide, Booking


def guide_list(request):
    guides = Guide.objects.filter(is_active=True)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        guides = guides.filter(
            Q(name__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(district__icontains=search_query)
        )
    
    # Filter by specialization
    selected_specialization = request.GET.get('specialization')
    if selected_specialization:
        guides = guides.filter(specialization=selected_specialization)
    
    # Filter by division
    selected_division = request.GET.get('division')
    if selected_division:
        guides = guides.filter(division=selected_division)
    
    # Filter by experience
    selected_experience = request.GET.get('experience')
    if selected_experience:
        guides = guides.filter(experience_level=selected_experience)
    
    # Get filter options
    specializations = Guide.objects.values_list('specialization', flat=True).distinct()
    divisions = Guide.objects.values_list('division', flat=True).distinct()
    
    # Pagination
    paginator = Paginator(guides, 6)
    page_number = request.GET.get('page')
    guides = paginator.get_page(page_number)
    
    context = {
        'guides': guides,
        'specializations': specializations,
        'divisions': divisions,
        'search_query': search_query,
        'selected_specialization': selected_specialization,
        'selected_division': selected_division,
        'selected_experience': selected_experience,
    }
    
    return render(request, 'guides.html', context)


def guide_detail(request, slug):
    guide = get_object_or_404(Guide, slug=slug, is_active=True)
    
    if request.method == 'POST':
        # Process booking form
        try:
            customer_name = request.POST.get('customer_name')
            customer_email = request.POST.get('customer_email')
            customer_phone = request.POST.get('customer_phone')
            start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
            end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
            group_size = int(request.POST.get('group_size', 1))
            special_requirements = request.POST.get('special_requirements', '')
            
            # Calculate total amount
            total_days = (end_date - start_date).days + 1
            total_amount = total_days * guide.daily_rate
            
            # Validate dates
            if start_date <= timezone.now().date():
                messages.error(request, 'Start date must be in the future.')
                return render(request, 'guide_detail.html', {'guide': guide})
            
            if end_date <= start_date:
                messages.error(request, 'End date must be after start date.')
                return render(request, 'guide_detail.html', {'guide': guide})
            
            # Create booking
            booking = Booking.objects.create(
                guide=guide,
                customer_name=customer_name,
                customer_email=customer_email,
                customer_phone=customer_phone,
                start_date=start_date,
                end_date=end_date,
                group_size=group_size,
                special_requirements=special_requirements,
                total_amount=total_amount,
            )
            
            # Redirect to payment page
            return redirect('hire_guide:booking_payment', booking_id=booking.booking_id)
            
        except Exception as e:
            messages.error(request, f'Error creating booking: {str(e)}')
    
    context = {
        'guide': guide,
        'today': timezone.now().date(),
    }
    return render(request, 'guide_detail.html', context)


def booking_payment(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, payment_status='pending')
    
    if request.method == 'POST':
        # Process payment
        payment_method = request.POST.get('payment_method')
        
        # Here you would integrate with actual payment gateway
        # For demo purposes, we'll simulate payment processing
        
        if payment_method in ['bkash', 'nagad', 'rocket', 'card']:
            # Simulate successful payment
            import uuid
            booking.transaction_id = str(uuid.uuid4())[:12].upper()
            booking.payment_status = 'completed'
            booking.status = 'confirmed'
            booking.save()
            
            messages.success(request, 'Payment successful! Your booking has been confirmed.')
            return redirect('hire_guide:booking_confirmation', booking_id=booking.booking_id)
        else:
            messages.error(request, 'Please select a valid payment method.')
    
    context = {
        'booking': booking,
    }
    return render(request, 'booking_payment.html', context)


def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, payment_status='completed')
    
    context = {
        'booking': booking,
    }
    return render(request, 'booking_confirmation.html', context)
