from django.db import models
from django.utils import timezone


class Suggestion(models.Model):
    created_date = models.DateTimeField(blank=True, default=timezone.now)
    suggestion_text = models.TextField()
    contact_email = models.EmailField()

    def __str__(self):
        return "Contact: %s - %s" % (str(self.contact_email), str(self.id),)
