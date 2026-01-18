from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponseForbidden
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import VillageInfo, PanchayatMember, GovernmentScheme, GalleryImage, ContactMessage
from .serializers import (
    VillageInfoSerializer, PanchayatMemberSerializer, 
    GovernmentSchemeSerializer, GalleryImageSerializer, ContactMessageSerializer
)
from .permissions import IsAdminOrReadOnly, IsAdmin

# ==================== FRONTEND VIEWS ====================

def index(request):
    """Home page with village overview"""
    village = VillageInfo.objects.first()
    featured_images = GalleryImage.objects.filter(featured=True)[:6]
    recent_schemes = GovernmentScheme.objects.filter(is_active=True)[:3]
    
    context = {
        'village': village,
        'featured_images': featured_images,
        'schemes': recent_schemes,
    }
    return render(request, 'index.html', context)

def about(request):
    """Village information page"""
    village = VillageInfo.objects.first()
    return render(request, 'about.html', {'village': village})

def members_view(request):
    """Display all panchayat members"""
    members = PanchayatMember.objects.filter(is_active=True)
    sarpanch = members.filter(position='sarpanch').first()
    other_members = members.exclude(position='sarpanch')
    
    context = {
        'sarpanch': sarpanch,
        'members': other_members,
    }
    return render(request, 'members.html', context)

def schemes_view(request):
    """Display government schemes"""
    category = request.GET.get('category', None)
    
    if category:
        schemes = GovernmentScheme.objects.filter(category=category, is_active=True)
    else:
        schemes = GovernmentScheme.objects.filter(is_active=True)
    
    categories = GovernmentScheme._meta.get_field('category').choices
    
    context = {
        'schemes': schemes,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'schemes.html', context)

def gallery_view(request):
    """Display photo gallery"""
    category = request.GET.get('category', None)
    
    if category:
        images = GalleryImage.objects.filter(category=category)
    else:
        images = GalleryImage.objects.all()
    
    categories = GalleryImage._meta.get_field('category').choices
    
    context = {
        'images': images,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'gallery.html', context)

def contact_view(request):
    """Contact page - handle messages"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        contact_msg = ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        
        # Send email notification
        try:
            send_mail(
                f'New Message: {subject}',
                f'From: {name}\nEmail: {email}\nPhone: {phone}\n\n{message}',
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=True,
            )
        except:
            pass
        
        return render(request, 'contact.html', {'success': True})
    
    village = VillageInfo.objects.first()
    return render(request, 'contact.html', {'village': village})

# ==================== ADMIN DASHBOARD ====================

@login_required
def admin_dashboard(request):
    """Admin dashboard - view statistics and manage content"""
    if not request.user.is_staff:
        return HttpResponseForbidden("Access Denied")
    
    stats = {
        'members_count': PanchayatMember.objects.count(),
        'schemes_count': GovernmentScheme.objects.count(),
        'gallery_count': GalleryImage.objects.count(),
        'messages_count': ContactMessage.objects.filter(is_read=False).count(),
    }
    
    recent_messages = ContactMessage.objects.all()[:5]
    
    context = {
        'stats': stats,
        'recent_messages': recent_messages,
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def admin_village(request):
    """Manage village information"""
    if not request.user.is_staff:
        return HttpResponseForbidden("Access Denied")
    
    village = VillageInfo.objects.first()
    
    if request.method == 'POST':
        if village:
            village.village_name = request.POST.get('village_name')
            village.state = request.POST.get('state')
            village.district = request.POST.get('district')
            village.taluka = request.POST.get('taluka')
            village.population = request.POST.get('population') or None
            village.total_area = request.POST.get('total_area') or None
            village.established_year = request.POST.get('established_year') or None
            village.description = request.POST.get('description')
            village.history = request.POST.get('history')
            village.culture = request.POST.get('culture')
            village.agriculture = request.POST.get('agriculture')
            village.phone = request.POST.get('phone')
            village.email = request.POST.get('email')
            village.address = request.POST.get('address')
            
            if 'village_photo' in request.FILES:
                village.village_photo = request.FILES['village_photo']
            
            village.save()
        else:
            village = VillageInfo.objects.create(
                village_name=request.POST.get('village_name'),
                state=request.POST.get('state'),
                district=request.POST.get('district'),
                taluka=request.POST.get('taluka'),
                description=request.POST.get('description'),
            )
        
        return redirect('admin_dashboard')
    
    return render(request, 'admin_village.html', {'village': village})

@login_required
def admin_members(request):
    """Manage panchayat members"""
    if not request.user.is_staff:
        return HttpResponseForbidden("Access Denied")
    
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        
        if member_id:
            member = get_object_or_404(PanchayatMember, id=member_id)
        else:
            member = PanchayatMember()
        
        member.name = request.POST.get('name')
        member.position = request.POST.get('position')
        member.contact_number = request.POST.get('contact_number')
        member.email = request.POST.get('email')
        member.address = request.POST.get('address')
        member.bio = request.POST.get('bio')
        
        if 'photo' in request.FILES:
            member.photo = request.FILES['photo']
        
        member.term_start_date = request.POST.get('term_start_date') or None
        member.term_end_date = request.POST.get('term_end_date') or None
        
        member.save()
        return redirect('admin_members')
    
    members = PanchayatMember.objects.all()
    return render(request, 'admin_members.html', {'members': members})

@login_required
def delete_member(request, member_id):
    """Delete a panchayat member"""
    if not request.user.is_staff:
        return HttpResponseForbidden("Access Denied")
    
    member = get_object_or_404(PanchayatMember, id=member_id)
    member.delete()
    return redirect('admin_members')

# ==================== REST API VIEWSETS ====================

class VillageInfoViewSet(viewsets.ModelViewSet):
    queryset = VillageInfo.objects.all()
    serializer_class = VillageInfoSerializer
    permission_classes = [IsAdminOrReadOnly]

class PanchayatMemberViewSet(viewsets.ModelViewSet):
    queryset = PanchayatMember.objects.filter(is_active=True)
    serializer_class = PanchayatMemberSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['position']
    search_fields = ['name', 'position']

class GovernmentSchemeViewSet(viewsets.ModelViewSet):
    queryset = GovernmentScheme.objects.filter(is_active=True)
    serializer_class = GovernmentSchemeSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['category']
    search_fields = ['scheme_name', 'ministry']

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['category']
    
    def get_queryset(self):
        # Only show featured images for non-staff on main query
        if self.request.user and self.request.user.is_staff:
            return GalleryImage.objects.all()
        return GalleryImage.objects.filter(featured=True)

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        """Allow anyone to create messages"""
        return super().create(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        """Only admins can view messages"""
        if not (request.user and request.user.is_authenticated and request.user.is_staff):
            return Response({'detail': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
        return super().list(request, *args, **kwargs)
    
    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        """Mark a message as read"""
        if not (request.user and request.user.is_staff):
            return Response({'detail': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
        
        message = self.get_object()
        message.is_read = True
        message.save()
        return Response({'status': 'message marked as read'})
