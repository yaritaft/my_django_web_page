from suggestions.models import Suggestion
from django import forms
from django.contrib import admin
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class SuggestionForm(forms.ModelForm):
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox(attrs={"data-theme": "dark"})
    )
    suggestion_text = forms.TextInput(attrs={"required": True})
    contact_email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "contact-form"})
    )

    class Meta:
        model = Suggestion
        fields = ["suggestion_text", "contact_email"]
        widgets = {"tags": admin.widgets.AdminTextareaWidget}
