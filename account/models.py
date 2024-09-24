from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
