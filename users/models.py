from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    # pass

    # add additional fields in here

    def __str__(self):
        return self.email 
#self.first_name self.last_name

"""    def __str__(first_name):
        return self.first_name
    def __str__(last_name):
        return self.last_name
"""