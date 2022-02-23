"""recipe_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    
    path('admin/', admin.site.urls),

    # =====================
    # LOGIN / REGISTER

    # Register page
    path('register/', user_views.register, name='register'),

    # Login page
    # Use default django login (Class based views)
    #   - template_name: Name of the template to render when using the login page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # Logout page
    # Use default django logout (Class based views)
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # User Profile
    path('profile/', user_views.profile, name='profile'),

    # ====================
    # PASSWORD RESET

    # 1. Password Reset Page
    #    Page where the user writes the user where the reset email will be sent
    #    (NOTE: The name must use underscores or it wont work)
    path(
        "password-reset/", 
        auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), 
        name="password_reset"
    ),

    # 2. Password Reset Success
    #    If the email was sent successfully, the user is redirected here
    #    (NOTE: The name must use underscores or it wont work)
    path(
        "password-reset/done/", 
        auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), 
        name="password_reset_done"
    ),

    # 3. Password Reset Confirm
    #    If the user clicks on the link on the email, the user will be redirected here
    #    (NOTE: The name must use underscores or it wont work)
    #    
    #    Parameters:
    #       - uidb64: User ID enconded in base 64
    #       - token: Token to validate if the form POST is legitimate
    path(
        "password-reset-confirm/<uidb64>/<token>/", 
        auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), 
        name="password_reset_confirm"
    ),

    # 4. Password Reset Complete
    #    If the password was reset successfully on the backend, the user lands here
    path(
        "password-reset-complete/", 
        auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), 
        name="password_reset_complete"
    ),

    # ====================
    # RECIPE BOOK

    # Root Route:
    # Managed by the "urls.py" file inside recipe_book
    path('', include('recipe_book.urls'))
]

# Route for static files (Images)
# Add static file path for debug mode
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
