from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class AppUser(AbstractUser):
    # add any other extra attribute if required
    pass
