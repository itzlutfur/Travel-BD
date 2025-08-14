from django.db import models
from django.utils.text import slugify


class Guide(models.Model):
    CATEGORY_CHOICES = [
        ('beach', 'Beach'),
        ('mountain', 'Mountain'),
        ('historical', 'Historical'),
        ('cultural', 'Cultural'),
        ('adventure', 'Adventure'),
        ('religious', 'Religious'),
    ]
    
    EXPERIENCE_CHOICES = [
        ('beginner', '1-2 Years'),
        ('intermediate', '3-5 Years'),
        ('experienced', '6-10 Years'),
        ('expert', '10+ Years'),
    ]
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    bio = models.TextField()
    short_bio = models.TextField(max_length=300, blank=True)
    location = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    specialization = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='beginner')
    
    # Contact info
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    languages = models.CharField(max_length=100, help_text="Comma-separated languages")
    
    # Profile
    profile_image = models.ImageField(upload_to='guides/', blank=True, null=True)
    
    # Ratings
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    total_tours = models.IntegerField(default=0)
    
    # Meta
    featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-rating', 'name']