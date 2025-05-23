# Generated by Django 4.2 on 2025-04-08 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logged_at', models.DateField(auto_now_add=True)),
                ('current_weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weights', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-logged_at'],
            },
        ),
    ]
