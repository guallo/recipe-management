from rest_framework import serializers

from django.contrib.auth.models import User

from recipe_management.api.models import Step, Ingredient, Recipe


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name', 'recipe')


class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ('url', 'step_text', 'recipe')


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('url', 'text', 'recipe')


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('url', 'name', 'user', 'step_set', 'ingredient_set')
