from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from .models import Ingredient, Recipe

# =====================
# HOME PAGE
# =====================

def home(request):

    # Returns an HTTP response under the hood
    return render(request, 'recipe_book/home.html', context = {
        'ingredients': Ingredient.objects.all()
    })

# =====================
# ABOUT PAGE
# =====================

def about(request):
    return render(request, 'recipe_book/about.html')

# =====================
# INGREDIENT PAGE
# =====================

class IngredientListView(ListView):

    # Model sent to the page
    model = Ingredient

    # Template for the view
    template_name = "recipe_book/ingredients.html"

    # Name of the context object passed to the template
    context_object_name = "ingredients"

