from django.contrib import admin
from .models import Recipe, Ingredient

# Add models to admin page
admin.site.register(Recipe)
admin.site.register(Ingredient)
