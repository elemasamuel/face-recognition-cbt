from django.db import models
from django.db.models.signals import post_save

class UserProfile(models.Model):
    reg_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name