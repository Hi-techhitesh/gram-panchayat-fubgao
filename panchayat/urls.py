from django.urls import path, include
from rest_framework.routers import DefaultRouter
from panchayat import views

# REST API Router
router = DefaultRouter()
router.register(r'village', views.VillageInfoViewSet, basename='village')
router.register(r'members', views.PanchayatMemberViewSet, basename='member')
router.register(r'schemes', views.GovernmentSchemeViewSet, basename='scheme')
router.register(r'gallery', views.GalleryImageViewSet, basename='gallery')
router.register(r'messages', views.ContactMessageViewSet, basename='message')

# URL patterns
urlpatterns = [
    # Frontend URLs
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('members/', views.members_view, name='members'),
    path('schemes/', views.schemes_view, name='schemes'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('contact/', views.contact_view, name='contact'),
    
    # Admin URLs
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/village/', views.admin_village, name='admin_village'),
    path('admin/members/', views.admin_members, name='admin_members'),
    path('admin/member/delete/<int:member_id>/', views.delete_member, name='delete_member'),
    
    # Django Admin
    path('admin-login/', views.admin_dashboard, name='admin_login'),
    
    # API endpoints
    path('api/', include(router.urls)),
]
