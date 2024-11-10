from django.db import models
from django.contrib.auth.models import User

class Hamsafar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hamsafars")
    name = models.CharField(max_length=100)
    start_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    seats = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.start_location} to {self.destination} on {self.date}"

