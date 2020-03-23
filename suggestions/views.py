from django.shortcuts import render
from suggestions.forms import SuggestionForm
import logging
from django.views import View

log = logging.getLogger(__name__)


class SuggestionView(View):
    def get(self, request, error_message=None):
        return render(
            request,
            "suggestions/suggestion_form.html",
            {"form": SuggestionForm(), "error_message": error_message},
        )

    def post(self, request):
        form = SuggestionForm(request.POST)
        if form.is_valid() and form.non_field_errors() == []:
            form.save()
            return render(request, "suggestions/thank_you.html",)
        return self.get(
            request, error_message="There was an error loading data."
        )
