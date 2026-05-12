from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactMessageForm
from .models import Achievement, Course, GalleryImage, PageHero, Service, SiteSettings, Specialty, Testimonial


def site_settings():
    return SiteSettings.objects.first()


def hero_for(page):
    return PageHero.objects.filter(page=page).first()


def base_context(page):
    return {
        "settings": site_settings(),
        "hero": hero_for(page),
        "page_key": page,
    }


def home(request):
    context = base_context("home")
    context.update(
        achievements=Achievement.objects.filter(is_featured=True)[:4],
        services=Service.objects.filter(is_active=True)[:4],
        courses=Course.objects.filter(is_active=True)[:3],
        specialties=Specialty.objects.filter(is_active=True)[:4],
        gallery=GalleryImage.objects.filter(is_active=True)[:6],
        testimonials=Testimonial.objects.filter(is_active=True)[:3],
    )
    return render(request, "academy/home.html", context)


def achievements(request):
    context = base_context("achievements")
    context.update(
        achievements=Achievement.objects.all(),
        gallery=GalleryImage.objects.filter(is_active=True),
        testimonials=Testimonial.objects.filter(is_active=True),
    )
    return render(request, "academy/achievements.html", context)


def services(request):
    context = base_context("services")
    context.update(services=Service.objects.filter(is_active=True))
    return render(request, "academy/services.html", context)


def courses(request):
    context = base_context("courses")
    context.update(courses=Course.objects.filter(is_active=True))
    return render(request, "academy/courses.html", context)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_active=True)
    context = base_context("courses")
    context.update(course=course, courses=Course.objects.filter(is_active=True).exclude(pk=course.pk)[:3])
    return render(request, "academy/course_detail.html", context)


def specialty(request):
    context = base_context("specialty")
    context.update(specialties=Specialty.objects.filter(is_active=True))
    return render(request, "academy/specialty.html", context)


def contact(request):
    context = base_context("contact")
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you. Your enquiry has been received.")
            return redirect("contact")
    else:
        form = ContactMessageForm()
    context["form"] = form
    return render(request, "academy/contact.html", context)

# Create your views here.
