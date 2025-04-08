from django.db import models
from django.contrib.auth.models import User


class Weight(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weights')
    logged_at = models.DateField(auto_now_add=True)
    current_weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['-logged_at']

    def __str__(self):
        return f'{self.owner.username} - {self.date} - {self.weight}'
