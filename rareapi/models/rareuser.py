from django.db import models
from django.contrib.auth.models import User

class RareUser(models.Model):

    bio = models.CharField(max_length=300)
    profile_image_url = models.URLField()
    created_on = models.DateField(auto_now_add=True) #check if this works on the database
    active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
