from django.db import models
from django.core.validators import URLValidator
from django.utils import timezone
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# Village Information Model
class VillageInfo(models.Model):
    village_name = models.CharField(max_length=200, unique=True)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    taluka = models.CharField(max_length=100)
    population = models.IntegerField(null=True, blank=True)
    total_area = models.FloatField(help_text="Area in square kilometers", null=True, blank=True)
    established_year = models.IntegerField(null=True, blank=True)
    
    # Description and Details
    description = models.TextField(blank=True)
    history = models.TextField(blank=True)
    culture = models.TextField(blank=True)
    agriculture = models.TextField(blank=True)
    
    # Contact
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    
    # Images
    village_photo = models.ImageField(upload_to='village/', null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Village Info"
    
    def __str__(self):
        return self.village_name
    
    def save(self, *args, **kwargs):
        # Optimize image on save
        if self.village_photo:
            self.optimize_image(self.village_photo)
        super().save(*args, **kwargs)
    
    @staticmethod
    def optimize_image(image_field):
        """Compress and optimize village photo"""
        img = Image.open(image_field)
        img.thumbnail((1200, 800))
        img_format = 'JPEG' if img.mode == 'RGB' else 'PNG'

        buffer = BytesIO()
        img.save(buffer, format=img_format, quality=85)
        buffer.seek(0)

        image_field.save(
            image_field.name,
            ContentFile(buffer.getvalue()),
            save=False
        )



# Panchayat Member Model
class PanchayatMember(models.Model):
    POSITION_CHOICES = [
        ('sarpanch', 'Sarpanch (Village Head)'),
        ('upsarpanch', 'Up-Sarpanch (Deputy Head)'),
        ('member', 'Ward Member'),
        ('secretary', 'Secretary'),
        ('treasurer', 'Treasurer'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    contact_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    
    # Bio and Photo
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='members/')
    
    # Term Information
    term_start_date = models.DateField(null=True, blank=True)
    term_end_date = models.DateField(null=True, blank=True)
    
    # Social Links
    facebook_url = models.URLField(blank=True)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['position', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.get_position_display()}"
    
    def save(self, *args, **kwargs):
        if self.photo:
            self.optimize_image(self.photo)
        super().save(*args, **kwargs)
    
    @staticmethod
    def optimize_image(image_field):
        """Compress member photos"""
        # Open the image
        img = Image.open(image_field)

        # Resize / compress
        img.thumbnail((400, 500))

        buffer = BytesIO()
        img.save(buffer, format='JPEG', quality=80)
        buffer.seek(0)

        # Replace the file with optimized content
        image_field.save(
            image_field.name,              # keep the same filename
            ContentFile(buffer.getvalue()),# new file content
            save=False                     # don’t trigger another model save yet
        )



# Government Schemes Model
class GovernmentScheme(models.Model):
    CATEGORY_CHOICES = [
        ('health', 'Health & Wellness'),
        ('education', 'Education'),
        ('agriculture', 'Agriculture'),
        ('infrastructure', 'Infrastructure'),
        ('social', 'Social Security'),
        ('skill', 'Skill Development'),
        ('other', 'Other'),
    ]
    
    scheme_name = models.CharField(max_length=200)
    scheme_code = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    ministry = models.CharField(max_length=200)
    
    # Description
    description = models.TextField()
    objectives = models.TextField()
    eligibility_criteria = models.TextField()
    benefits = models.TextField()
    
    # Application Details
    application_process = models.TextField()
    required_documents = models.TextField()
    application_link = models.URLField(blank=True)
    
    # Contact
    nodal_officer_name = models.CharField(max_length=200, blank=True)
    nodal_officer_contact = models.CharField(max_length=20, blank=True)
    
    # Additional Info
    launch_date = models.DateField(null=True, blank=True)
    last_updated = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-launch_date']
    
    def __str__(self):
        return f"{self.scheme_name} ({self.scheme_code})"


# Gallery Images Model
class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('event', 'Events'),
        ('infrastructure', 'Infrastructure'),
        ('agriculture', 'Agriculture'),
        ('festival', 'Festivals'),
        ('ceremony', 'Ceremonies'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='gallery/%Y/%m/')
    
    # Metadata
    photographer_name = models.CharField(max_length=200, blank=True)
    event_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    
    # Display
    featured = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-featured', '-display_order', '-event_date', '-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.image:
            self.optimize_image(self.image)
        super().save(*args, **kwargs)
    
    @staticmethod
    def optimize_image(image_field):
        """Compress gallery images"""
        # Open the image
        img = Image.open(image_field)

        # Resize / compress
        img.thumbnail((1200, 800))

        buffer = BytesIO()
        img.save(buffer, format='JPEG', quality=85)
        buffer.seek(0)

        # Replace the file with optimized content
        image_field.save(
            image_field.name,              # keep the same filename
            ContentFile(buffer.getvalue()),# new file content
            save=False                     # don’t trigger another model save yet
        )



# Contact Message Model
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    
    # For tracking
    is_read = models.BooleanField(default=False)
    is_replied = models.BooleanField(default=False)
    reply_message = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
