from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from tour_booking.models import TourBooking, LocalGuideBooking

@login_required
def dashboard(request):
    user = request.user  # This gets the currently logged-in user
    
    # These queries ONLY get data for the authenticated user
    tour_bookings = TourBooking.objects.filter(user=user).select_related('destination', 'payment').order_by('-booking_date')
    guide_bookings = LocalGuideBooking.objects.filter(user=user).order_by('-booking_date')
    
    # All calculations are based on the filtered data for this user only
    tour_total = tour_bookings.aggregate(total=Sum('total_amount'))['total'] or 0
    guide_total = guide_bookings.aggregate(total=Sum('total_cost'))['total'] or 0
    total_spent = tour_total + guide_total
    
    tour_count = tour_bookings.count()
    guide_count = guide_bookings.count()
    total_bookings = tour_count + guide_count
    
    print(" the data", tour_count, guide_count)
    
    
    tour_status_counts = tour_bookings.values('status').annotate(count=Count('status'))
    
    recent_tour_bookings = tour_bookings[:5]
    recent_guide_bookings = guide_bookings[:5]
    
    context = {
        'tour_bookings': tour_bookings,
        'tour_count': tour_count,
        'tour_total': tour_total,
        'recent_tour_bookings': recent_tour_bookings,
        'guide_bookings': guide_bookings,
        'guide_count': guide_count,
        'guide_total': guide_total,
        'recent_guide_bookings': recent_guide_bookings,
        'total_spent': total_spent,
        'total_bookings': total_bookings,
        'tour_status_counts': tour_status_counts,
        'user': user,
    }
    
    return render(request, 'dashboard.html', context)
