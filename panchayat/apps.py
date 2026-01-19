from django.apps import AppConfig


class PanchayatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'panchayat'
    verbose_name = 'Gram Panchayat Management'


    # At the bottom of settings.py (or in a separate startup script)
import os
from django.contrib.auth import get_user_model

if os.getenv("DJANGO_SUPERUSER_USERNAME") and os.getenv("DJANGO_SUPERUSER_PASSWORD"):
    User = get_user_model()
    if not User.objects.filter(username=os.getenv("DJANGO_SUPERUSER_USERNAME")).exists():
        User.objects.create_superuser(
            username=os.getenv("DJANGO_SUPERUSER_USERNAME"),
            email=os.getenv("DJANGO_SUPERUSER_EMAIL", ""),
            password=os.getenv("DJANGO_SUPERUSER_PASSWORD"),
        )
