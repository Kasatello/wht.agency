from django.db import models

from user.models import User


class Team(models.Model):
    name = models.CharField(max_length=155)
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teams")

    def __str__(self):
        return self.name
