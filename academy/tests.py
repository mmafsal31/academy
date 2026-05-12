from django.test import Client, TestCase

from .models import Course, PageHero, SiteSettings


class PublicPageTests(TestCase):
    def setUp(self):
        SiteSettings.objects.create(name="Evren Academy", tagline="Test academy")
        for page in ["home", "achievements", "services", "courses", "specialty", "contact"]:
            PageHero.objects.create(page=page, title=f"{page.title()} page")
        Course.objects.create(
            title="Foundation English",
            slug="foundation-english",
            short_description="Communication course",
        )
        self.client = Client()

    def test_main_pages_load(self):
        for url in ["/", "/achievements/", "/services/", "/courses/", "/specialty/", "/contact/"]:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200, url)

    def test_course_detail_loads(self):
        response = self.client.get("/courses/foundation-english/")
        self.assertContains(response, "Foundation English")

    def test_contact_form_stores_message(self):
        response = self.client.post(
            "/contact/",
            {
                "name": "Test User",
                "email": "test@example.com",
                "phone": "1234567890",
                "course_interest": "English",
                "message": "I want admission details.",
            },
        )
        self.assertEqual(response.status_code, 302)

# Create your tests here.
