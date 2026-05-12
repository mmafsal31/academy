from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("achievements/", views.achievements, name="achievements"),
    path("services/", views.services, name="services"),
    path("courses/", views.courses, name="courses"),
    path("courses/<slug:slug>/", views.course_detail, name="course_detail"),
    path("specialty/", views.specialty, name="specialty"),
    path("contact/", views.contact, name="contact"),
]
