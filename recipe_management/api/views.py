from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import viewsets

from recipe_management.api.models import Step, Ingredient, Recipe
from recipe_management.api.serializers import UserSerializer, StepSerializer, \
    IngredientSerializer, RecipeSerializer
from recipe_management.api.filters import ListOnlyFilterBackend


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all().order_by('id')
    serializer_class = StepSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all().order_by('id')
    serializer_class = IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer
    filter_backends = (ListOnlyFilterBackend, )
    filterset_fields = ('user', )
