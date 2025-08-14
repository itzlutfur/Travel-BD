from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Destination

def destination_list(request):
    destinations = Destination.objects.filter(is_active=True)
    categories = [choice[0] for choice in Destination.CATEGORY_CHOICES]
    divisions = Destination.objects.values_list('division', flat=True).distinct()
    
    # Filters
    category_filter = request.GET.get('category')
    division_filter = request.GET.get('division')
    search_query = request.GET.get('search')
    
    if category_filter:
        destinations = destinations.filter(category=category_filter)
    
    if division_filter:
        destinations = destinations.filter(division=division_filter)
        
    if search_query:
        destinations = destinations.filter(name__icontains=search_query)
    
    # Pagination
    paginator = Paginator(destinations, 9)  # 9 destinations per page
    page_number = request.GET.get('page')
    destinations = paginator.get_page(page_number)
    
    context = {
        'destinations': destinations,
        'categories': categories,
        'divisions': divisions,
        'selected_category': category_filter,
        'selected_division': division_filter,
        'search_query': search_query,
    }
    return render(request, 'destination.html', context)

def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug, is_active=True)
    
    # Get related destinations
    related_destinations = Destination.objects.filter(
        category=destination.category,
        is_active=True
    ).exclude(id=destination.id)[:4]
    
    context = {
        'destination': destination,
        'related_destinations': related_destinations,
    }
    return render(request, 'destination_detail.html', context)