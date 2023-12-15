from django.urls import path
from .views import recipes_home

app_name = 'recipes_home'

urlpatterns = [
  path('', recipes_home),
]
