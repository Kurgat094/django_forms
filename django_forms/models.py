from django.db import models

# Create your models here.
from django.db import models

class UserData(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True)  # Optional bio field
    def __str__(self):
        return self.named