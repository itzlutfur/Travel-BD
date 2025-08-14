from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Guide


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
    paginator = Paginator(guides, 12)
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
    context = {
        'guide': guide,
    }
    return render(request, 'guide_detail.html', context)
