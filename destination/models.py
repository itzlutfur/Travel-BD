from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class Destination(models.Model):
    CATEGORY_CHOICES = [
        ('beach', 'Beach'),
        ('mountain', 'Mountain'),
        ('historical', 'Historical'),
        ('cultural', 'Cultural'),
        ('adventure', 'Adventure'),
        ('religious', 'Religious'),
        ('nature', 'Nature'),
        ('waterfall', 'Waterfall'),
        ('forest', 'Forest'),
        ('archaeological', 'Archaeological'),
    ]
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    
    # Images - Make main_image optional too
    main_image = models.ImageField(upload_to='destinations/images/', blank=True, null=True)
    gallery_image_1 = models.ImageField(upload_to='destinations/images/', blank=True, null=True)
    gallery_image_2 = models.ImageField(upload_to='destinations/images/', blank=True, null=True)
    gallery_image_3 = models.ImageField(upload_to='destinations/images/', blank=True, null=True)
    
    # Details
    best_time_to_visit = models.CharField(max_length=200)
    entry_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    duration = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=50, choices=[
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('hard', 'Hard'),
    ], default='easy')
    
    # Location coordinates
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    # SEO and metadata
    meta_description = models.CharField(max_length=160, blank=True)
    featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinations', null=True, blank=True)
    
    class Meta:
        ordering = ['-featured', '-created_at']
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Destination.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('destination:destination_detail', kwargs={'slug': self.slug})
    
    def get_gallery_images(self):
        """Return list of non-empty gallery images"""
        images = []
        if self.gallery_image_1:
            images.append(self.gallery_image_1)
        if self.gallery_image_2:
            images.append(self.gallery_image_2)
        if self.gallery_image_3:
            images.append(self.gallery_image_3)
        return images