from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(models.Model):
    user = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def is_adult(self):
        # Check if the user is an adult (e.g., 18 years or older)
        return (timezone.now().date() - self.date_of_birth).days >= 365 * 18
    


class CustomUser(AbstractUser, UserProfile):
    pass