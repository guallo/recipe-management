from django.urls import path, include

from rest_framework import routers

from recipe_management.api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'steps', views.StepViewSet)
router.register(r'ingredient', views.IngredientViewSet)
router.register(r'recipes', views.RecipeViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
