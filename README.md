# Evren Academy Django Website

A dynamic academy/business website built with Django. The admin panel controls the public content, images, courses, services, specialties, achievements, gallery, testimonials, and contact enquiries.

## Pages

- Home: hero, highlights, courses, services, specialty preview, gallery
- Achievements: milestone cards and gallery showcase
- Services: editable service list with icons and photos
- Courses: editable course cards and course detail pages
- Specialty: academy strengths and differentiators
- Contact: enquiry form, address, phone, email, WhatsApp, optional map

## Run Locally

```powershell
cd c:\Users\dell\evren
python manage.py migrate
python manage.py seed_academy
python manage.py runserver
```

Open the website:

```text
http://127.0.0.1:8000/
```

Open the admin panel:

```text
http://127.0.0.1:8000/admin/
```

Starter admin login:

```text
Username: admin
Password: admin12345
```

Change this password before using the project publicly.

## Admin Editing Guide

1. Go to `/admin/` and log in.
2. Open `Site settings` to update the academy name, logo, phone, email, address, WhatsApp, and social links.
3. Open `Page heroes` to update the hero title, subtitle, button, and image for each page.
4. Open `Courses` to add or edit course names, descriptions, durations, levels, photos, and highlights.
5. Open `Achievements` to add result statistics, event milestones, awards, and showcase images.
6. Open `Services` and `Specialties` to update academy offerings and strengths.
7. Open `Gallery images` to replace brochure placeholders with real campus, event, or student photos.
8. Open `Contact messages` to view enquiries submitted from the public contact form.

## Development Commands

Create new database tables after model changes:

```powershell
python manage.py makemigrations
python manage.py migrate
```

Run tests:

```powershell
python manage.py test
```

Check the Django project:

```powershell
python manage.py check
```

## Main Files

- `academy/models.py`: database models for editable content
- `academy/admin.py`: admin panel configuration
- `academy/views.py`: public page views
- `academy/forms.py`: contact enquiry form
- `templates/academy/`: website HTML templates
- `static/css/site.css`: website styling
- `static/js/site.js`: mobile menu and icons
- `academy/management/commands/seed_academy.py`: starter content loader
