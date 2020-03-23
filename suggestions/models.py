from django.db import models
from django.utils import timezone


class Suggestion(models.Model):
    created_date = models.DateField(blank=True, auto_now_add=True)
    suggestion_text = models.TextField()
    contact_email = models.EmailField()

    def __str__(self):
        return "Contact: %s - %s" % (str(self.contact_email), str(self.id),)
