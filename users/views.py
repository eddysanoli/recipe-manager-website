from django.shortcuts import render, redirect

# To make certain views only accesible while logged in
from django.contrib.auth.decorators import login_required

# Import flash messages (They dissapear after the next request)
# Types of message:
#   - messages.debug
#   - messages.info
#   - messages.success
#   - messages.warning
#   - messages.error
from django.contrib import messages

# Use pre-defined class for a User Creation form
from django.contrib.auth.forms import UserCreationForm

# Use custom form
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# ==========================
# REGISTER VIEW
# ==========================

def register(request):

    # POST: Request to add a new user
    if request.method == "POST":

        # Pass the post request data to the user creation form
        # (If the form data is not valid, the following if statement wont execute
        # and the registration page will reload with the corresponding errors)
        form = UserRegisterForm(request.POST)

        # Validate the form data
        if form.is_valid():

            # Save the user to the database
            form.save()

            # Get the username from the form data
            username = form.cleaned_data.get('username')

            # Create success message
            messages.success(request, f'Your account has been created! You are now able to login')
            
            # Redirect back to the "login" page after Sign Up
            # (Blog-home is the alias given to the url pattern present in urls.py inside the blog app)
            return redirect('login')

    # GET (Or any other request): Display the user sign up page
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', context ={
        'form': form
    })


# ==========================
# USER PROFILE VIEW
# ==========================

# Its necessary to add a decorator to require a login to access the login page
# (By default the decorator will redirect the user to "accounts/login". This can
# be changed inside the settings)

@login_required
def profile(request):


    if request.method == 'POST':

        # If a post request is received, validate the POST info, also, fill unchanged
        # parameters with the default user data.
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(
            request.POST,
            request.FILES,  
            instance=request.user.profile)

        # If the data in both forms is correct, save it
        if user_update_form.is_valid() and profile_update_form.is_valid():

            # Save data
            user_update_form.save()
            profile_update_form.save()

             # Create success message
            messages.success(request, f'Profile info updated successfully!')
            
            # Redirect back to the profile page
            return redirect('profile')

    else:

        # Get the update form for both the profile and the user
        # (These are model forms, so you can populate the fields of the forms by passing them
        # an object or an instance of the model that it expects. In other words: Pass a user
        # object to the UserUpdateForm )
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', context = {
        'u_form': user_update_form,
        'p_form': profile_update_form
    })
