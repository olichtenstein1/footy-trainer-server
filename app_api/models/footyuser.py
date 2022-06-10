from django.db import models
from django.contrib.auth.models import User


class FootyUser(models.Model):

     user = models.OneToOneField(User, on_delete=models.CASCADE)
     bio = models.TextField()
     years_of_experience = models.IntegerField()
     favorite_player = models.CharField(max_length=50)
     favorite_player_image = models.URLField(max_length=200)
     profile_picture = models.URLField(max_length=200)