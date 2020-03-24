from django.shortcuts import render
from suggestions.forms import SuggestionForm
import logging
from django.views import View
from django.http import HttpRequest, HttpResponse

log = logging.getLogger(__name__)


class SuggestionView(View):
    def get(
        self, request: HttpRequest, error_message: str = None
    ) -> HttpResponse:
        """When the suggestion endpoint is requested by a get it Render
        suggestion form to be completed. If an error was received show it.

        Parameters
        ----------
        request : HttpRequest
            Get request to require suggestion view.
        error_message: str
            An error received from a previous wrong post.

        Returns
        -------
        HttpResponse
            HTTP package with view requested.
        """
        return render(
            request,
            "suggestions/suggestion_form.html",
            {"form": SuggestionForm(), "error_message": error_message},
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        """Render the about me view.

        Parameters
        ----------
        request : HttpRequest
            Post request sending the information filled in suggestion form.

        Returns
        -------
        HttpResponse
            HTTP package with thank you view if everything was right.
        or
        HttpResponse
            HTTP package with suggestion form view + error message displayed.
        """
        form = SuggestionForm(request.POST)
        if form.is_valid() and form.non_field_errors() == []:
            form.save()
            return render(request, "suggestions/thank_you.html",)
        return self.get(
            request, error_message="There was an error loading data."
        )
