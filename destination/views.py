from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Destination


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