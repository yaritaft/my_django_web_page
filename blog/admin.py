from django.contrib import admin
from .models import (
    BlogTag,
    BlogPost,
    User,
    Role,
)


models_to_register = (BlogTag, BlogPost, User, Role)
for one_model in models_to_register:
    admin.site.register(one_model)
