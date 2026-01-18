# Generated migration file

from django.db import migrations, models
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VillageInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village_name', models.CharField(max_length=200, unique=True)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('taluka', models.CharField(max_length=100)),
                ('population', models.IntegerField(blank=True, null=True)),
                ('total_area', models.FloatField(blank=True, help_text='Area in square kilometers', null=True)),
                ('established_year', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('history', models.TextField(blank=True)),
                ('culture', models.TextField(blank=True)),
                ('agriculture', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.TextField(blank=True)),
                ('village_photo', models.ImageField(blank=True, null=True, upload_to='village/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Village Info',
            },
        ),
        migrations.CreateModel(
            name='PanchayatMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(choices=[('sarpanch', 'Sarpanch (Village Head)'), ('upsarpanch', 'Up-Sarpanch (Deputy Head)'), ('member', 'Ward Member'), ('secretary', 'Secretary'), ('treasurer', 'Treasurer'), ('other', 'Other')], max_length=50)),
                ('contact_number', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.TextField(blank=True)),
                ('bio', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='members/')),
                ('term_start_date', models.DateField(blank=True, null=True)),
                ('term_end_date', models.DateField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True)),
                ('whatsapp_number', models.CharField(blank=True, max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['position', 'name'],
            },
        ),
        migrations.CreateModel(
            name='GovernmentScheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_name', models.CharField(max_length=200)),
                ('scheme_code', models.CharField(max_length=100, unique=True)),
                ('category', models.CharField(choices=[('health', 'Health & Wellness'), ('education', 'Education'), ('agriculture', 'Agriculture'), ('infrastructure', 'Infrastructure'), ('social', 'Social Security'), ('skill', 'Skill Development'), ('other', 'Other')], max_length=50)),
                ('ministry', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('objectives', models.TextField()),
                ('eligibility_criteria', models.TextField()),
                ('benefits', models.TextField()),
                ('application_process', models.TextField()),
                ('required_documents', models.TextField()),
                ('application_link', models.URLField(blank=True)),
                ('nodal_officer_name', models.CharField(blank=True, max_length=200)),
                ('nodal_officer_contact', models.CharField(blank=True, max_length=20)),
                ('launch_date', models.DateField(blank=True, null=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-launch_date'],
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(choices=[('event', 'Events'), ('infrastructure', 'Infrastructure'), ('agriculture', 'Agriculture'), ('festival', 'Festivals'), ('ceremony', 'Ceremonies'), ('other', 'Other')], max_length=50)),
                ('image', models.ImageField(upload_to='gallery/%Y/%m/')),
                ('photographer_name', models.CharField(blank=True, max_length=200)),
                ('event_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('featured', models.BooleanField(default=False)),
                ('display_order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-featured', '-display_order', '-event_date', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('is_replied', models.BooleanField(default=False)),
                ('reply_message', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
