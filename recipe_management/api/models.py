from django.db import models
from django.db.models import constraints
from django.contrib.auth.models import User

from recipe_management.api import validators as custom_validators


class Step(models.Model):
    step_text = models.CharField(max_length=80)
    recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True, blank=True)


class Ingredient(models.Model):
    text = models.CharField(max_length=30, validators=[
        custom_validators.validate_slug_with_spaces, 
    ])
    recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        constraints = [
            # To avoid specify the same ingredient twice for the same recipe.
            constraints.UniqueConstraint(fields=['text', 'recipe'], name='unique_text_recipe'),
        ]


class Recipe(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
