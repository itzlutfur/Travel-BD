from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm


class CustomLoginView(LoginView):
    """Custom login view"""
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('authentication:dashboard')
    
    def dispatch(self, request, *args, **kwargs):
        # Redirect authenticated users to dashboard
        if request.user.is_authenticated:
            return redirect('authentication:dashboard')
        
        # Clear any existing messages when accessing login page
        if hasattr(request, '_messages'):
            list(messages.get_messages(request))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, f'Welcome back, {form.get_user().first_name}!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid email or password. Please try again.')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('authentication:dashboard')


class RegisterView(CreateView):
    """Registration view"""
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = reverse_lazy('authentication:dashboard')
    
    def dispatch(self, request, *args, **kwargs):
        # Redirect authenticated users to dashboard
        if request.user.is_authenticated:
            return redirect('authentication:dashboard')
        
        # Clear any existing messages when accessing register page
        if hasattr(request, '_messages'):
            list(messages.get_messages(request))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, f'Welcome to Travel BD, {self.object.first_name}!')
        return response
    
    def form_invalid(self, form):
        # Add error message for registration failure
        messages.error(self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


class CustomLogoutView(View):
    """Custom logout view that handles both GET and POST requests"""
    
    def get(self, request, *args, **kwargs):
        return self.logout_user(request)
    
    def post(self, request, *args, **kwargs):
        return self.logout_user(request)
    
    def logout_user(self, request):
        # Clear all messages before logout
        if hasattr(request, '_messages'):
            list(messages.get_messages(request))
        logout(request)
        messages.success(request, 'You have been successfully logged out.')
        return redirect('home')


class DashboardView(TemplateView):
    """Customer dashboard view"""
    template_name = 'dashboard.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('authentication:login')
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Mock data for hotel and guide bookings
        context.update({
            'user': user,
            'hotel_bookings': [
                {
                    'id': 1,
                    'hotel_name': 'Grand Hotel Dhaka',
                    'location': 'Dhaka, Bangladesh',
                    'check_in': '2024-08-15',
                    'check_out': '2024-08-20',
                    'status': 'Confirmed',
                    'total_cost': '$250'
                },
                {
                    'id': 2,
                    'hotel_name': 'Sea Pearl Resort',
                    'location': "Cox's Bazar, Bangladesh",
                    'check_in': '2024-09-10',
                    'check_out': '2024-09-15',
                    'status': 'Pending',
                    'total_cost': '$400'
                }
            ],
            'guide_bookings': [
                {
                    'id': 1,
                    'guide_name': 'Rashid Ahmed',
                    'location': 'Sylhet, Bangladesh',
                    'date': '2024-08-25',
                    'duration': '3 days',
                    'rating': 4.8,
                    'total_cost': '$150'
                },
                {
                    'id': 2,
                    'guide_name': 'Fatima Khan',
                    'location': 'Chittagong Hill Tracts',
                    'date': '2024-09-05',
                    'duration': '5 days',
                    'rating': 4.9,
                    'total_cost': '$300'
                }
            ],
            'total_bookings': 4,
            'total_spent': '$1100'
        })
        
        return context