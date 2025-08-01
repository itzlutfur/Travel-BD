from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"
    
class DestinationView(TemplateView):
    template_name = "destination.html"

class AboutView(TemplateView):
    template_name = "about.html"
    
class FeatureView(TemplateView):
    template_name = "feature.html"