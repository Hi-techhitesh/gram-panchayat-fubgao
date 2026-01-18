from django.contrib import admin
from .models import VillageInfo, PanchayatMember, GovernmentScheme, GalleryImage, ContactMessage

@admin.register(VillageInfo)
class VillageInfoAdmin(admin.ModelAdmin):
    list_display = ('village_name', 'state', 'district', 'population', 'updated_at')
    search_fields = ('village_name', 'district')
    fieldsets = (
        ('Basic Info', {
            'fields': ('village_name', 'state', 'district', 'taluka')
        }),
        ('Demographics', {
            'fields': ('population', 'total_area', 'established_year')
        }),
        ('Description', {
            'fields': ('description', 'history', 'culture', 'agriculture')
        }),
        ('Contact', {
            'fields': ('phone', 'email', 'address')
        }),
        ('Media', {
            'fields': ('village_photo',)
        }),
    )

@admin.register(PanchayatMember)
class PanchayatMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'contact_number', 'is_active', 'term_start_date')
    list_filter = ('position', 'is_active')
    search_fields = ('name', 'position')
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'position', 'contact_number', 'email', 'address')
        }),
        ('Bio & Photo', {
            'fields': ('bio', 'photo')
        }),
        ('Term Details', {
            'fields': ('term_start_date', 'term_end_date')
        }),
        ('Social Links', {
            'fields': ('facebook_url', 'whatsapp_number')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

@admin.register(GovernmentScheme)
class GovernmentSchemeAdmin(admin.ModelAdmin):
    list_display = ('scheme_name', 'scheme_code', 'category', 'ministry', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('scheme_name', 'scheme_code', 'ministry')
    fieldsets = (
        ('Scheme Details', {
            'fields': ('scheme_name', 'scheme_code', 'category', 'ministry')
        }),
        ('Description', {
            'fields': ('description', 'objectives')
        }),
        ('Eligibility & Benefits', {
            'fields': ('eligibility_criteria', 'benefits')
        }),
        ('Application', {
            'fields': ('application_process', 'required_documents', 'application_link')
        }),
        ('Contact', {
            'fields': ('nodal_officer_name', 'nodal_officer_contact')
        }),
        ('Status', {
            'fields': ('is_active', 'launch_date')
        }),
    )

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'event_date', 'display_order')
    list_filter = ('category', 'featured', 'event_date')
    search_fields = ('title', 'location')
    fieldsets = (
        ('Image Info', {
            'fields': ('title', 'description', 'category', 'image')
        }),
        ('Details', {
            'fields': ('photographer_name', 'event_date', 'location')
        }),
        ('Display', {
            'fields': ('featured', 'display_order')
        }),
    )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject')
    fieldsets = (
        ('Message', {
            'fields': ('name', 'email', 'phone', 'subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'is_replied')
        }),
        ('Response', {
            'fields': ('reply_message',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at')
