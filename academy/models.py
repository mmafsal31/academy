from django.db import models
from django.urls import reverse


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SiteSettings(TimeStampedModel):
    name = models.CharField(max_length=120, default="Evren Academy")
    tagline = models.CharField(max_length=180, blank=True)
    logo = models.ImageField(upload_to="branding/", blank=True)
    phone = models.CharField(max_length=40, blank=True)
    whatsapp = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    map_embed_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"

    def __str__(self):
        return self.name


class PageHero(TimeStampedModel):
    PAGE_CHOICES = [
        ("home", "Home"),
        ("achievements", "Achievements"),
        ("services", "Services"),
        ("courses", "Courses"),
        ("specialty", "Specialty"),
        ("contact", "Contact"),
    ]

    page = models.CharField(max_length=40, choices=PAGE_CHOICES, unique=True)
    eyebrow = models.CharField(max_length=120, blank=True)
    title = models.CharField(max_length=180)
    subtitle = models.TextField(blank=True)
    image = models.ImageField(upload_to="heroes/", blank=True)
    primary_button_text = models.CharField(max_length=60, blank=True)
    primary_button_url = models.CharField(max_length=180, blank=True)

    class Meta:
        ordering = ["page"]

    def __str__(self):
        return self.get_page_display()


class Achievement(TimeStampedModel):
    title = models.CharField(max_length=140)
    metric = models.CharField(max_length=60, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="achievements/", blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title


class Service(TimeStampedModel):
    title = models.CharField(max_length=140)
    summary = models.TextField()
    icon = models.CharField(max_length=60, default="book-open")
    image = models.ImageField(upload_to="services/", blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title


class Course(TimeStampedModel):
    title = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    duration = models.CharField(max_length=80, blank=True)
    level = models.CharField(max_length=80, blank=True)
    image = models.ImageField(upload_to="courses/", blank=True)
    highlights = models.TextField(
        blank=True,
        help_text="Add one highlight per line. These appear as bullets on the course card.",
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"slug": self.slug})

    @property
    def highlight_list(self):
        return [line.strip() for line in self.highlights.splitlines() if line.strip()]


class Specialty(TimeStampedModel):
    title = models.CharField(max_length=140)
    description = models.TextField()
    image = models.ImageField(upload_to="specialties/", blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "title"]
        verbose_name_plural = "Specialties"

    def __str__(self):
        return self.title


class GalleryImage(TimeStampedModel):
    title = models.CharField(max_length=140)
    caption = models.CharField(max_length=220, blank=True)
    image = models.ImageField(upload_to="gallery/")
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title


class Testimonial(TimeStampedModel):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True)
    quote = models.TextField()
    photo = models.ImageField(upload_to="testimonials/", blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name


class ContactMessage(TimeStampedModel):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    course_interest = models.CharField(max_length=140, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.created_at:%Y-%m-%d}"

# Create your models here.
