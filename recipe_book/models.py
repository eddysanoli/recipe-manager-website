from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# =====================
# INGREDIENT MODEL
# =====================

class Ingredient(models.Model):

    # Name
    name = models.CharField(max_length=100)

    # Article Number
    article_id = models.AutoField(primary_key=True)

    # Unit Cost
    unit_cost = models.DecimalField(max_digits=6, decimal_places=2)

    # Unit
    unit = models.CharField(max_length=100)

    # Ingredient Image
    # - default: Default image if none is given (add the default to the MEDIA_ROOT directory)
    # - upload_to: Directory in which the image will be saved
    image = models.ImageField(default='default-ingredient.jpg', upload_to='ingredient-pics')

    # Description
    # Unrestricted text
    description = models.TextField(default="Delicious cooking ingredient")

    # Recipe author
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    # ==========
    # METHODS

    # Default object name
    def __str__(self) -> str:
        return f'{self.name}-{self.article_id}'

    # Where a user should be redirected after a post
    def get_absolute_url(self):
        return reverse('ingredient-detail', kwargs={})


# =====================
# RECIPE MODEL
# =====================

class Recipe(models.Model):

    # Name
    title = models.CharField(max_length=100)

    # Recipe ID
    recipe_id = models.AutoField(primary_key=True)

    # Description
    # Unrestricted text
    description = models.TextField(default=f'A fantastic recipe!')

    # Set the recipe creation date
    # (Wont use a datetime field to allow for future edits to the field)
    date_posted = models.DateTimeField(default = timezone.now)

    # Recipe Preview Image
    # - default: Default image if none is given (add the default to the MEDIA_ROOT directory)
    # - upload_to: Directory in which the image will be saved
    image = models.ImageField(default='default-recipe.jpg', upload_to='recipe-pics')

    # Ingredient list
    ingredients = models.JSONField()

    # Recipe author
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    # ======================
    # METHODS

    # Default object name
    def __str__(self) -> str:
        return f'{self.title}-{self.recipe_id}'

    # Where a user should be redirected after a post
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={})
