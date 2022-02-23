from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from .models import Ingredient, Recipe
import pint

# =====================
# VIEW: HOME
# =====================

def home(request):

    # Returns an HTTP response under the hood
    return render(request, 'recipe_book/ingredient_list.html', context = {
        'ingredients': Ingredient.objects.all()
    })

# =====================
# VIEW: ABOUT
# =====================

def about(request):
    return render(request, 'recipe_book/about.html')

# =====================
# VIEW: INGREDIENT LIST
# =====================

class IngredientListView(ListView):

    # Model sent to the page
    model = Ingredient

    # Template for the view
    template_name = "recipe_book/ingredient_list.html"

    # Name of the context object passed to the template
    context_object_name = "ingredients"

    # Send the search term through a POST request to "ingredient-search"
    def post(self, request, *args, **kwargs):

        search_term = request.POST.get('search_term')
        print(f"[DEBUG] SEARCH TERM: ", search_term)
        
        # Reverse returns a string, causing the backend to reject the response
        # Here we convert the string into a proper response to prevent errors
        return HttpResponseRedirect(reverse('ingredient-search', kwargs = {
            'search_term': search_term 
        }))

# =====================
# VIEW: INGREDIENT SEARCH
# =====================

class IngredientSearchListView(ListView):

    # Model sent to the page
    model = Ingredient

    # Template for the view
    template_name = 'recipe_book/ingredient_search.html'

    # Context object name
    context_object_name = 'ingredients'

    # Send the search term through a POST request to "ingredient-search"
    def post(self, request, *args, **kwargs):

        search_term = request.POST.get('search_term')
        
        # Redirect back to this page with the new search term
        return HttpResponseRedirect(reverse('ingredient-search', kwargs = {
            'search_term': search_term 
        }))

    # Filter the model results
    def get_queryset(self):

        search_term = self.kwargs.get('search_term')

        # Return results that match the article ID
        # (If search term is convertible to int)
        if search_term.isdigit():
            return Ingredient.objects \
                .filter(article_id__contains = int(search_term)) \
                .order_by("article_id")

        # Return results that match the ingredient name
        else:
            return Ingredient.objects \
                .filter(name__contains = search_term) \
                .order_by("article_id")
                                 

# =====================
# VIEW: CREATE INGREDIENT
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
# VIEW: UPDATE INGREDIENT
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
# VIEW: INGREDIENT DELETE
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

# =====================
# VIEW: RECIPE LIST
# =====================

class RecipeListView(ListView):

    # Model sent to the page
    model = Recipe

    # Template for the view
    template_name = "recipe_book/recipe_list.html"

    # Name of the context object passed to the template
    context_object_name = "recipes"

# =====================
# VIEW: RECIPE DETAIL
# =====================

class RecipeDetailView(DetailView):

    # Model sent to the page
    model = Recipe

    # Template for the view
    template_name = "recipe_book/recipe_detail.html"

# =====================
# VIEW: RECIPE DELETE
# =====================

# Class based view will look for a template called:
#   recipe_book/recipe_confirm_delete.html

class RecipeDeleteView(DeleteView):

    # Model sent to the page
    model = Recipe

    # Redirect to the ingredient list
    success_url = "/recipes/"

    # Object passed to the template
    context_object_name = "recipe"

    # Check if the user is the author of the current recipe
    def test_func(self):

        # Get the current ingredient
        recipe = self.get_object()

        # If current user == current ingredient author
        if self.request.user == recipe.author:
            return True
        else:
            return False

# =====================
# VIEW: CREATE RECIPE
# =====================

# Create and update views will look for a template called:
#   <app>/<model>_form.html = recipe_book/recipe_form.html

class RecipeCreateView(CreateView):

    # Model sent to the page
    model = Recipe

    # Template for the view
    template_name = "recipe_book/recipe_create.html"

    # Template for the view
    fields = ['title', 'description', 'image']

    # =====================
    # METHODS

    # Overwrite "form_valid" method of parent to add the author
    def form_valid(self, form):

        # Parse the ingredient inputs and calculate the costs
        ingredients, total_cost = parse_ingredients(self)

        # Model: Save ingredient properties (now with cost) and total cost of recipe
        form.instance.ingredients = ingredients
        form.instance.total_cost = total_cost

        # ---------------------
        # AUTHOR

        # Model: Set the author of the new ingredient
        # TODO: CHANGE THIS ASSIGNMENT AFTER IMPLEMENTING LOGIN
        # form.instance.author = self.request.user
        form.instance.author = User.objects.first()

        # Run the parent class "form_valid" method
        return super().form_valid(form)

    # New redirect url after a successful post
    def get_success_url(self):
        return reverse('recipe-list', kwargs={})


# =====================
# VIEW: UPDATE RECIPE
# =====================

# Create and update views will look for a template called:
#   <app>/<model>_form.html = recipe_book/recipe_form.html

class RecipeUpdateView(UpdateView):

    # Model sent to the page
    model = Recipe

    # Template for the view
    template_name = "recipe_book/recipe_update.html"

    # Template for the view
    fields = ['title', 'description', 'image']

    # Name of the object passed to the template
    context_object_name = "recipe"

    # =====================
    # METHODS

    # To avoid repetition, we use the form valid method from the Create view
    def form_valid(self, form):
        
        # Parse the ingredient inputs and calculate the costs
        ingredients, total_cost = parse_ingredients(self)

        # Model: Save ingredient properties (now with cost) and total cost of recipe
        form.instance.ingredients = ingredients
        form.instance.total_cost = total_cost

        # ---------------------
        # AUTHOR

        # Model: Set the author of the new ingredient
        # TODO: CHANGE THIS ASSIGNMENT AFTER IMPLEMENTING LOGIN
        # form.instance.author = self.request.user
        form.instance.author = User.objects.first()

        # Run the parent class "form_valid" method
        return super().form_valid(form)


# =====================
# FUNC: INGREDIENT PARSING
# =====================

def parse_ingredients(self):

    # ---------------------
    # INGREDIENTS

    # Get all the input fields related to ingredient info
    ingredient_inputs = [POST_key for POST_key in self.request.POST.keys() if "ingredient" in POST_key]

    # Initialize control variables:
    #   - ingredients: List for all ingredient details
    #   - ingredient-count: Number of ingredients in list
    #   - ingredient-details: Dictionary with the properties of a single ingredient
    ingredients = []
    ingredient_count = 0
    ingredient_details = {}

    # For every input field that has "ingredient" in its name
    for input in ingredient_inputs:
        
        # Split the field name
        #   ingredient-name-0 = ingredient-<property>-<number>
        _, property, ingredient_number = input.split("-")

        # If the ingredient number is different from the current count
        # add the current ingredient details to the list and start filling a new one
        if ingredient_count != int(ingredient_number):
            ingredient_details["list_id"] = ingredient_count
            ingredients.append(ingredient_details)
            ingredient_details = {}
            ingredient_count += 1
        
        # Add the value of the field under the "property" name
        ingredient_details[property] = self.request.POST[input]

    # Add the remaining ingredient details
    ingredient_details["list_id"] = ingredient_count
    ingredients.append(ingredient_details)
    print("[DEBUG] RECIPE INGREDIENTS: ", ingredients) 

    # ---------------------
    # INGREDIENT OBJECT

    for ingredient in ingredients:

        # Store a reference to the ingredient object
        # inside the ingredients list
        try:   
            ingredient_object = Ingredient.objects.filter(name = ingredient["name"]).first()
            ingredient["article_id"] = ingredient_object.article_id
        except Exception as e:
            print(f"[DEBUG] ERROR: No DB match was found for {ingredient['name']}")

    # ---------------------
    # TOTAL COST

    # Map strings to "pint" units
    ureg = pint.UnitRegistry()
    pint_units = {
        "kilograms": ureg.kilogram,
        "grams": ureg.gram,
        "liters": ureg.liter,
        "pounds": ureg.pound,
        "centiliters": ureg.centiliter
    }

    # Initial cost: $0
    total_cost = 0

    # Add the cost of every ingredient
    for idx, ingredient in enumerate(ingredients):

        # Extract the first database object with a matching ingredient name
        # (If no match is found, the ingredient is skipped)
        try: 
            ingredient_object = Ingredient.objects.filter(name = ingredient["name"]).first()
        except Exception as e:
            continue
        
        # Units and unit cost present on the DB
        db_unit_cost = ingredient_object.unit_cost
        db_unit = ingredient_object.unit

        # Amount and unit used in the recipe
        recipe_amount = int(ingredient["amount"])
        recipe_unit = ingredient["unit"]

        # Add unit to the recipe amount
        recipe_amount = recipe_amount * pint_units[recipe_unit]

        # Convert the recipe amount to the ingredient units listed on the DB
        try:
            db_amount = recipe_amount.to(pint_units[db_unit])
        except Exception as e:
            db_amount = recipe_amount

        # Individual ingredient cost
        # (Rounded to two decimal places)
        ingredient_cost = float(db_unit_cost) * float(db_amount.magnitude)
        ingredient_cost = round(ingredient_cost, 2)

        # Add the ingredient cost to the ingredients list
        ingredients[idx]["cost"] = ingredient_cost
        print(f'[DEBUG] INGREDIENT COST: ({ingredient["name"]})', db_amount, db_unit_cost)

        # Add individual cost to the total
        total_cost += ingredient_cost

    return ingredients, total_cost