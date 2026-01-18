from rest_framework import serializers
from .models import VillageInfo, PanchayatMember, GovernmentScheme, GalleryImage, ContactMessage

class VillageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillageInfo
        fields = '__all__'

class PanchayatMemberSerializer(serializers.ModelSerializer):
    position_display = serializers.CharField(source='get_position_display', read_only=True)
    
    class Meta:
        model = PanchayatMember
        fields = ['id', 'name', 'position', 'position_display', 'contact_number', 'email', 
                  'address', 'bio', 'photo', 'term_start_date', 'term_end_date', 
                  'facebook_url', 'whatsapp_number', 'is_active']

class GovernmentSchemeSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    
    class Meta:
        model = GovernmentScheme
        fields = ['id', 'scheme_name', 'scheme_code', 'category', 'category_display', 
                  'ministry', 'description', 'objectives', 'eligibility_criteria', 
                  'benefits', 'application_process', 'required_documents', 
                  'application_link', 'nodal_officer_name', 'nodal_officer_contact', 'is_active']

class GalleryImageSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    
    class Meta:
        model = GalleryImage
        fields = ['id', 'title', 'description', 'category', 'category_display', 'image', 
                  'photographer_name', 'event_date', 'location', 'featured', 'display_order']

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'phone', 'subject', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']
