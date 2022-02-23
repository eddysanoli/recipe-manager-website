from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# ====================
# CREATE PROFILE SIGNAL
# ====================

# Before this, when a new user is created via the registration process, the admin
# had to manually create the associated profile via the admin page. To prevent this
# we use a signal that creates an associated profile when a user is created.

# Steps:
# When a user (sender = User) is saved, send the "post_save" signal to the 
# "create_profile" function below, passing the "post_save" parameters to it
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    # If a user is created
    if created: 

        # Create a profile where the one to one relationship is with the current instance
        # of a user.
        Profile.objects.create(user = instance)

# ====================
# SAVE PROFILE
# ====================

# Save the profile when the user is saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):

    # Save the profile
    instance.profile.save()