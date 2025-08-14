from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from destination.models import TourBooking
# Import other models as needed

@login_required
def dashboard_view(request):
    user = request.user
    
    # Get user's bookings
    tour_bookings = TourBooking.objects.filter(user=user).order_by('-booking_date')
    # hotel_bookings = HotelBooking.objects.filter(user=user).order_by('-created_at')
    # guide_bookings = GuideBooking.objects.filter(user=user).order_by('-created_at')
    
    # Calculate total spent
    total_spent = tour_bookings.aggregate(
        total=Sum('total_amount')
    )['total'] or 0
    
    context = {
        'tour_bookings': tour_bookings[:5],  # Latest 5 bookings
        # 'hotel_bookings': hotel_bookings[:5],
        # 'guide_bookings': guide_bookings[:5],
        'total_spent': total_spent,
    }
    
    return render(request, 'dashboard/dashboard.html', context)
