from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# ====================
# USER REGISTRATION FORM
# ====================

# Add email as an additional field

class UserRegisterForm(UserCreationForm):

    # Add the email argument to the forms fields
    # First argument of the function: required = True / False
    # By default: True
    email = forms.EmailField()

    # Nested namespace for configurations
    # (Keeps all the configurations in one place)
    class Meta: 

        # Model that we want this form to interact with
        # (Object that it will create when it submits)
        model = User

        # Fields for the model: 
        #   - Username
        #   - Email
        #   - Password1: Write password
        #   - Password2: Confirm password
        fields = ["username", "email", "password1", "password2"]


# ====================
# USER UPDATE FORM
# ====================

# Made to update the email and username of the user
#   - Model form: Form that will work with a specific database model

class UserUpdateForm(forms.ModelForm):

    # Add the email argument to the forms fields
    # First argument of the function: required = True / False
    # By default: True
    email = forms.EmailField()

    # Nested namespace for configurations
    # (Keeps all the configurations in one place)
    class Meta: 

        # Model that we want this form to interact with
        # (Object that it will create when it submits)
        model = User

        # Fields for the model: 
        #   - Username
        #   - Email
        #   - Password1: Write password
        #   - Password2: Confirm password
        fields = ["username", "email"]


# ====================
# PROFILE UPDATE FORM
# ====================

# To update the profile image

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']