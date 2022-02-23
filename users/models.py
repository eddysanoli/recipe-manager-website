from django.db import models
from django.contrib.auth.models import User

# Model for the user profile info
# (Must have a one to one relationship with the User model)
class Profile(models.Model):

    # Generate a one to one relationship with the User model
    #   - on_delete: If the user is deleted, the profile is also deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Image field for the profile picture
    #   - default: Default image if no image exists (Add the image inside the MEDIA_ROOT directory)
    #   - upload_to: Directory in which the new image will be saved
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # Default name of profile object: Username
    def __str__(self):
        return f'{self.user.username} Profile'
