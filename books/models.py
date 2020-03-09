from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from .enums import EnumBookRates


class BookTag(models.Model):
    keyword = models.CharField(null=False, unique=True, max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=300, null=False)
    created_date = models.DateTimeField(null=False, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    summary = models.TextField(null=False)
    rate = models.IntegerField(choices=EnumBookRates.book_rates(), null=False)
    tags = models.ManyToManyField(BookTag, related_name="book_tags")
    link = models.CharField(max_length=700, null=False)
    author = models.CharField(max_length=200, null=False)
    edition = models.CharField(max_length=200, null=False)
