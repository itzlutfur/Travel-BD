from django.views.generic import TemplateView
from destination.models import Destination
from hire_guide.models import Guide


class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get featured guides (limit to 3 for homepage)
        featured_guides = Guide.objects.filter(
            is_active=True, 
            featured=True
        ).select_related().order_by('-rating')[:3]
        
        # If not enough featured guides, get top-rated ones
        if featured_guides.count() < 4:
            featured_guides = Guide.objects.filter(
                is_active=True
            ).select_related().order_by('-rating')[:4]
        
        # Get featured destinations (limit to 4 for homepage)
        featured_destinations = Destination.objects.filter(
            is_active=True,
            featured=True
        ).select_related()[:4]
        
        # If not enough featured destinations, get popular ones
        if featured_destinations.count() < 4:
            featured_destinations = Destination.objects.filter(
                is_active=True
            ).select_related()[:4]
        
        # Add statistics for homepage
        context.update({
            'featured_guides': featured_guides,
            'featured_destinations': featured_destinations,
            'total_guides': Guide.objects.filter(is_active=True).count(),
            'total_destinations': Destination.objects.filter(is_active=True).count(),
        })
        
        return context
    
class DestinationView(TemplateView):
    template_name = "destination.html"

class AboutView(TemplateView):
    template_name = "about.html"