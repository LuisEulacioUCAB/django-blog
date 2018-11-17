from django.db import models
from django.contrib.auth.models import User
from posts import models as posts_models

# Create your models here.






class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,  null=True)
    location = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(null=True, blank=True)
