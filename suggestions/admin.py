from django.contrib import admin
from .models import Suggestion


models_to_register = (Suggestion,)
for one_model in models_to_register:
    admin.site.register(one_model)
