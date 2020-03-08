from django.contrib import admin
from .models import (
    Tag,
    BlogPost,
    User,
    Role,
)


models_to_register = (Tag, BlogPost, User, Role)
for one_model in models_to_register:
    admin.site.register(one_model)
