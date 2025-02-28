from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    current_weight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    goal_weight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.owner.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)


class Weight(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weights')
    logged_at = models.DateField(auto_now_add=True)
    current_weight = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['-logged_at']

    def __str__(self):
        return f'{self.owner.username} - {self.date} - {self.weight}'
   

class CalorieEntry(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calories')
    logged_at = models.DateField(auto_now_add=True)
    calories = models.PositiveIntegerField()

    class Meta:
        ordering = ['-logged_at']

    def __str__(self):
        return f'{self.owner.username} - {self.date} - {self.calories}'
