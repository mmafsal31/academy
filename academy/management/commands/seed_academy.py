from django.core.management.base import BaseCommand

from academy.models import Achievement, Course, GalleryImage, PageHero, Service, SiteSettings, Specialty, Testimonial


class Command(BaseCommand):
    help = "Create starter content for the Evren Academy website."

    def handle(self, *args, **options):
        settings, _ = SiteSettings.objects.update_or_create(
            pk=1,
            defaults={
                "name": "Evren Academy",
                "tagline": "A future-focused academy for confident learners",
                "logo": "seed/evren-logo.png",
                "phone": "+91 00000 00000",
                "whatsapp": "910000000000",
                "email": "info@evrenacademy.com",
                "address": "Update the academy address from Django admin.",
            },
        )

        heroes = {
            "home": (
                "Admissions open",
                "Build skill, confidence, and academic success",
                "A dynamic academy website with editable courses, achievements, photos, services, specialties, and enquiries.",
                "seed/1.png",
                "Explore courses",
                "/courses/",
            ),
            "achievements": (
                "Achievement showcase",
                "Results and milestones worth celebrating",
                "Add exam results, events, awards, student stories, and academy milestones from the admin panel.",
                "seed/2.png",
                "",
                "",
            ),
            "services": (
                "Student support",
                "Services that keep learning organized",
                "From academic guidance to structured training, every service can be edited and expanded in admin.",
                "seed/3.png",
                "",
                "",
            ),
            "courses": (
                "Courses",
                "Programs for school, college, and career growth",
                "Create unlimited courses with duration, level, images, and learning highlights.",
                "seed/4.png",
                "",
                "",
            ),
            "specialty": (
                "Why choose us",
                "A learning experience shaped around students",
                "Showcase the teaching strengths, facilities, mentoring style, and unique promise of the academy.",
                "seed/5.png",
                "",
                "",
            ),
            "contact": (
                "Contact",
                "Talk to us about admissions and course guidance",
                "Enquiries submitted here are stored safely in the Django admin panel.",
                "seed/6.png",
                "",
                "",
            ),
        }

        for page, values in heroes.items():
            PageHero.objects.update_or_create(
                page=page,
                defaults={
                    "eyebrow": values[0],
                    "title": values[1],
                    "subtitle": values[2],
                    "image": values[3],
                    "primary_button_text": values[4],
                    "primary_button_url": values[5],
                },
            )

        services = [
            ("Academic Coaching", "Structured lessons, regular practice, and clear feedback for steady improvement.", "graduation-cap", "seed/3.png"),
            ("Exam Preparation", "Focused revision plans, model tests, and performance tracking for important exams.", "clipboard-check", "seed/4.png"),
            ("Career Guidance", "Support for choosing courses, planning next steps, and building confidence.", "compass", "seed/5.png"),
            ("Parent Updates", "Transparent progress updates so families understand each student's journey.", "messages-square", "seed/6.png"),
        ]
        for index, item in enumerate(services, start=1):
            Service.objects.update_or_create(
                title=item[0],
                defaults={"summary": item[1], "icon": item[2], "image": item[3], "display_order": index},
            )

        courses = [
            (
                "Foundation English",
                "foundation-english",
                "Develop speaking, grammar, vocabulary, and confident communication.",
                "3 months",
                "Beginner to intermediate",
                "Grammar fundamentals\nSpeaking practice\nVocabulary building\nWeekly assessments",
                "seed/1.png",
            ),
            (
                "Competitive Exam Training",
                "competitive-exam-training",
                "Targeted preparation for students who need discipline, speed, and accuracy.",
                "6 months",
                "Exam focused",
                "Model tests\nDaily practice plan\nDoubt-clearing sessions\nProgress reports",
                "seed/2.png",
            ),
            (
                "Skill Development Program",
                "skill-development-program",
                "A practical program for communication, presentation, and workplace readiness.",
                "8 weeks",
                "All levels",
                "Presentation skills\nInterview preparation\nConfidence building\nPractical tasks",
                "seed/3.png",
            ),
        ]
        for index, item in enumerate(courses, start=1):
            Course.objects.update_or_create(
                slug=item[1],
                defaults={
                    "title": item[0],
                    "short_description": item[2],
                    "duration": item[3],
                    "level": item[4],
                    "highlights": item[5],
                    "image": item[6],
                    "display_order": index,
                },
            )

        specialties = [
            ("Personal mentoring", "Each learner gets guidance that matches their current level, goals, and pace.", "seed/4.png"),
            ("Result-focused practice", "Practice sessions, reviews, and feedback loops help students understand progress clearly.", "seed/5.png"),
            ("Modern learning environment", "The website is built to showcase classrooms, events, student work, and academy updates.", "seed/6.png"),
        ]
        for index, item in enumerate(specialties, start=1):
            Specialty.objects.update_or_create(
                title=item[0],
                defaults={"description": item[1], "image": item[2], "display_order": index},
            )

        achievements = [
            ("Student Success Stories", "100+", "Showcase admissions, exam wins, placement stories, and learner transformations.", "seed/1.png"),
            ("Academic Events", "25+", "Add workshops, seminars, competitions, and public programs with photos.", "seed/2.png"),
            ("Course Completion", "500+", "Highlight batches completed, certificates issued, and student participation.", "seed/3.png"),
            ("Community Reach", "Local", "Use this space to present social initiatives and academy partnerships.", "seed/4.png"),
        ]
        for index, item in enumerate(achievements, start=1):
            Achievement.objects.update_or_create(
                title=item[0],
                defaults={"metric": item[1], "description": item[2], "image": item[3], "display_order": index},
            )

        for index in range(1, 7):
            GalleryImage.objects.update_or_create(
                title=f"Brochure highlight {index}",
                defaults={
                    "caption": "Replace this caption in admin with the real photo story.",
                    "image": f"seed/{index}.png",
                    "display_order": index,
                },
            )

        Testimonial.objects.update_or_create(
            name="Student testimonial",
            defaults={
                "role": "Learner",
                "quote": "The academy gave me structure, confidence, and regular support throughout my learning journey.",
                "display_order": 1,
            },
        )

        self.stdout.write(self.style.SUCCESS(f"Seeded starter content for {settings.name}."))
