from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.timezone import now


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class User(AbstractUser):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=True)
    email = models.EmailField(null=False)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return "%s: %s %s" % (
            str(self.username),
            str(self.first_name),
            str(self.last_name),
        )


class Tag(models.Model):
    keyword = models.CharField(null=False, unique=True, max_length=100)


class BlogPost(models.Model):
    title = models.CharField(max_length=300, null=False)
    created_date = models.DateTimeField(null=False, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(null=False)
    hidden = models.BooleanField(default=False, null=False)
    tags = models.ManyToManyField(Tag, related_name="post_tags")
    author = models.ForeignKey(
        User, related_name="post_author", on_delete=models.CASCADE
    )
