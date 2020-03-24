from django.contrib import admin
from .models import (
    BookTag,
    Book,
)


models_to_register = (BookTag, Book)
for one_model in models_to_register:
    admin.site.register(one_model)
