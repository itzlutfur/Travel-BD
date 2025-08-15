from django.urls import path
from . import views

app_name = 'hire_guide'

urlpatterns = [
    path('', views.guide_list, name='guides'),
    path('<slug:slug>/', views.guide_detail, name='guide_detail'),
]