from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "course_interest", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone or WhatsApp"}),
            "course_interest": forms.TextInput(attrs={"placeholder": "Course you are interested in"}),
            "message": forms.Textarea(attrs={"placeholder": "Tell us what you would like to learn", "rows": 5}),
        }
