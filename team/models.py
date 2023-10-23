from django.db import models

from user.models import User


class Team(models.Model):
    name = models.CharField(max_length=155, unique=True)
    members = models.ManyToManyField(User, related_name="members")

    def __str__(self):
        return self.name
