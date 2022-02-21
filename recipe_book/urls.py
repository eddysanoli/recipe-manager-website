from django.urls import path
from . import views                     # Views from "recipe_book/views.py"
from .views import (
    IngredientListView
)

# TIPS: 
# - Be clear with the naming of the paths. Avoid generic names like "home"
# - Always add a trailing slash to all routes
urlpatterns = [
    
    # Home View
    path('', views.home, name="book-home"),

    # Ingredients View
    path('ingredients/', IngredientListView.as_view(), name="book-ingredients"),

    # About View
    path('about/', views.about, name="book-about")
]