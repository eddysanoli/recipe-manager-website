from django.urls import path
from . import views                     # Views from "recipe_book/views.py"
from .views import (
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView
)

# TIPS: 
# - Be clear with the naming of the paths. Avoid generic names like "home"
# - Always add a trailing slash to all routes
urlpatterns = [
    
    # Home View
    path('', views.home, name="book-home"),

    # About View
    path('about/', views.about, name="book-about"),

    # =====================
    # INGREDIENTS

    # List View
    path('ingredients/', IngredientListView.as_view(), name="ingredient-list"),

    # Create View
    path('ingredients/new/', IngredientCreateView.as_view(), name="ingredient-create"),

    # Update View
    path('ingredients/<int:pk>/edit/', IngredientUpdateView.as_view(), name="ingredient-update"),

    # Update View
    path('ingredients/<int:pk>/delete/', IngredientDeleteView.as_view(), name="ingredient-delete")


    # =====================
]