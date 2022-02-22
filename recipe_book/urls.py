from django.urls import path
from . import views                     # Views from "recipe_book/views.py"
from .views import (
    IngredientListView,
    IngredientCreateView,
    IngredientUpdateView,
    IngredientDeleteView,
    RecipeListView,
    RecipeCreateView,
    RecipeDeleteView,
    RecipeDetailView,
    RecipeUpdateView
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
    path('ingredients/<int:pk>/delete/', IngredientDeleteView.as_view(), name="ingredient-delete"),

    # =====================
    # RECIPES

    # List View (All recipes)
    path('recipes/', RecipeListView.as_view(), name="recipe-list"),

    # Create View 
    path('recipes/create/', RecipeCreateView.as_view(), name="recipe-create"),

    # Delete View
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name="recipe-delete"),

    # Detail View
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name="recipe-detail"),

    # Update View
    path('recipes/<int:pk>/update/', RecipeUpdateView.as_view(), name="recipe-update")

    # =====================
]