from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# =====================
# HOME PAGE
# =====================

def home(request):

    # Returns an HTTP response under the hood
    return render(request, 'recipe_book/home.html', context = {
        'recipes': "recipe"
    })