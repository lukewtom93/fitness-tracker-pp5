from django.db import models
from django.contrib.auth.models import User


class CalorieEntry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calories')
    logged_at = models.DateField(auto_now_add=True)
    calories = models.PositiveIntegerField()

    class Meta:
        ordering = ['-logged_at']

    def __str__(self):
        return f'{self.owner.username} - {self.date} - {self.calories}'
