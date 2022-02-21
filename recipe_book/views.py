from django.shortcuts import render, get_object_or_404
from django.urls import reverse
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
# HOME
# =====================

def home(request):

    # Returns an HTTP response under the hood
    return render(request, 'recipe_book/home.html', context = {
        'ingredients': Ingredient.objects.all()
    })

# =====================
# ABOUT
# =====================

def about(request):
    return render(request, 'recipe_book/about.html')

# =====================
# INGREDIENT LIST
# =====================

class IngredientListView(ListView):

    # Model sent to the page
    model = Ingredient

    # Template for the view
    template_name = "recipe_book/ingredient_list.html"

    # Name of the context object passed to the template
    context_object_name = "ingredients"

# =====================
# CREATE INGREDIENT
# =====================

# Create and update views will look for a template called:
#   <app>/<model>_form.html = recipe_book/ingredient_form.html
class IngredientCreateView(CreateView):

    # Model sent to the page
    model = Ingredient

    # Template for the view
    fields = ['name', 'unit_cost', 'unit', 'description', 'image']

    # =====================
    # METHODS

    # Overwrite "form_valid" method of parent to add the author
    def form_valid(self, form):

        # Set the author of the new ingredient
        # TODO: CHANGE THIS ASSIGNMENT AFTER IMPLEMENTING LOGIN
        # form.instance.author = self.request.user
        form.instance.author = User.objects.first()

        # Run the parent class "form_valid" method
        return super().form_valid(form)

    # New redirect url after a successful post
    def get_success_url(self):
        return reverse('ingredient-list', kwargs={})

# =====================
# UPDATE INGREDIENT
# =====================

# Create and update views will look for a template called:
#   <app>/<model>_form.html = recipe_book/ingredient_form.html

class IngredientUpdateView(UserPassesTestMixin, UpdateView):
    
    # Model sent to the page
    model = Ingredient

    # Template for the view
    fields = ['name', 'unit_cost', 'unit', 'description', 'image']

    # =====================
    # METHODS

    def get_success_url(self):
        return reverse('ingredient-list', kwargs={})

    # Overwrite the "form_valid" method of parent class
    def form_valid(self, form):

        # Set author
        # TODO: Change once the login system has been created
        form.instance.author = User.objects.first()

        # "form_valid" method from the parent class
        return super().form_valid(form)

    # Check if the current user created the ingredient
    def test_func(self):

        # Get the current ingredient
        ingredient = self.get_object()

        # If current user == current ingredient author
        if self.request.user == ingredient.author:
            return True
        else:
            return False

# =====================
# INGREDIENT DELETE
# =====================

# Class based view will look for a template called:
#   recipe_book/ingredient_confirm_delete.html

class IngredientDeleteView(UserPassesTestMixin, DeleteView):
    
    model = Ingredient

    # Redirect to the ingredient list
    success_url = "/ingredients/"

    # Object passed to the template
    context_object_name = "ingredient"

    # Check if the user is the author of the current ingredient
    def test_func(self):

        # Get the current ingredient
        ingredient = self.get_object()

        # If current user == current ingredient author
        if self.request.user == ingredient.author:
            return True
        else:
            return False