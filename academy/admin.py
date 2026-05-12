from django.contrib import admin

from .models import (
    Achievement,
    ContactMessage,
    Course,
    GalleryImage,
    PageHero,
    Service,
    SiteSettings,
    Specialty,
    Testimonial,
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Brand", {"fields": ("name", "tagline", "logo")}),
        ("Contact", {"fields": ("phone", "whatsapp", "email", "address", "map_embed_url")}),
        ("Social links", {"fields": ("facebook_url", "instagram_url", "youtube_url")}),
    )


@admin.register(PageHero)
class PageHeroAdmin(admin.ModelAdmin):
    list_display = ("page", "title", "updated_at")
    list_filter = ("page",)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title", "metric", "is_featured", "display_order")
    list_editable = ("is_featured", "display_order")
    search_fields = ("title", "description")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "display_order")
    list_editable = ("is_active", "display_order")
    search_fields = ("title", "summary")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "level", "is_active", "display_order")
    list_editable = ("is_active", "display_order")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "short_description")


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "display_order")
    list_editable = ("is_active", "display_order")
    search_fields = ("title", "description")


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "display_order")
    list_editable = ("is_active", "display_order")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_active", "display_order")
    list_editable = ("is_active", "display_order")
    search_fields = ("name", "role", "quote")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "course_interest", "is_read", "created_at")
    list_editable = ("is_read",)
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "phone", "message", "course_interest")
    readonly_fields = ("created_at", "updated_at")

# Register your models here.
