# Gram Panchayat Website - Django Backend

This is a complete production-ready Django project for Gram Panchayat (Village Council) management.

## Features

✅ **Village Information Management** - Edit village details, history, demographics  
✅ **Panchayat Members** - Manage member profiles, roles, contact details  
✅ **Government Schemes** - Display and manage schemes information  
✅ **Photo Gallery** - Upload and manage village photos  
✅ **Contact & Messaging** - Collect messages from citizens  
✅ **Admin Dashboard** - Custom web-based admin panel (not just Django admin)  
✅ **Responsive Design** - Mobile, tablet, desktop compatible  
✅ **Authentication** - Secure login for admin (you only)  
✅ **Production Ready** - Deployed on cloud with proper configuration  

## Quick Start (Local Development)

### 1. Extract and Setup
```bash
cd gram_panchayat
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your settings
```

### 3. Initialize Database
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

### 4. Run Locally
```bash
python manage.py runserver
```

Open http://127.0.0.1:8000

## Project Structure

```
gram_panchayat/
├── gram_panchayat/          # Project settings
├── panchayat/               # Main app
│   ├── models.py            # Database models
│   ├── views.py             # Views & APIs
│   ├── urls.py              # URL routing
│   ├── admin.py             # Django admin
│   └── serializers.py       # REST serializers
├── templates/               # HTML templates
├── static/                  # CSS, JS, images
├── media/                   # Uploaded files
├── manage.py                # Django management
└── requirements.txt         # Dependencies
```

## Database Models

### VillageInfo
- Village name, state, district, taluka
- Population, area, administrative details
- Description, established year
- Contact information

### PanchayatMember
- Name, position/role, contact
- Photo, bio, email
- Term start/end dates

### Scheme
- Scheme name, description
- Ministry/Department
- Eligibility criteria
- Benefits and application process

### GalleryImage
- Image file, title
- Description, category
- Upload date

### ContactMessage
- Name, email, phone
- Subject, message
- Timestamp

## API Endpoints

All endpoints are read-only for public except admin-only edit endpoints:

### Public (GET only)
- `GET /api/village/` - Get village info
- `GET /api/members/` - List panchayat members
- `GET /api/schemes/` - List schemes
- `GET /api/gallery/` - Get gallery images
- `GET /api/members/<id>/` - Get member details

### Admin Protected (POST, PUT, DELETE)
- `POST /api/village/` - Create/Update village info
- `POST /api/members/` - Add/Edit members
- `POST /api/schemes/` - Add/Edit schemes
- `POST /api/gallery/` - Upload gallery images
- `DELETE /api/*` - Delete items

## Deployment Options

### Option 1: Render.com (Recommended - Free)
1. Push code to GitHub
2. Connect Render.com to your GitHub repo
3. Set environment variables
4. Deploy automatically

### Option 2: Railway.app
1. Connect GitHub repo
2. Add PostgreSQL database
3. Deploy with one click

### Option 3: PythonAnywhere (Free tier)
1. Upload files to PythonAnywhere
2. Configure WSGI file
3. Set up database
4. Run web app

See `deployment_guide.md` for detailed steps.

## Admin Dashboard

Access admin dashboard at `/admin/dashboard/`

Features:
- Edit village information
- Manage panchayat members with photos
- Add/Edit government schemes
- Upload and organize photos
- View contact messages
- User statistics

## Security Features

✅ CSRF Protection  
✅ SQL Injection Prevention  
✅ Session-based Authentication  
✅ Password Hashing  
✅ CORS Configuration  
✅ Environment Variable Protection  
✅ Static Files Optimization  

## Support & Customization

The code is well-commented and follows Django best practices. You can easily:
- Add more fields to models
- Customize templates
- Add new features
- Modify admin dashboard

## License

This project is custom-built for Gram Panchayat Fungao.

---

**Need help?** Refer to Django documentation: https://docs.djangoproject.com/
