from django.urls import path
from . import views                 # Views from "recipe_book/views.py"

# TIPS: 
# - Be clear with the naming of the paths. Avoid generic names like "home"
# - Always add a trailing slash to all routes
urlpatterns = [
    
    # Home View
    path('', views.home, name="book-home")
]