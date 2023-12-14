from django.test import TestCase
from .models import Recipe #to access Recipe model

# Create your tests here.
class RecipeModelTest(TestCase):
  def setUpTestData():
    # Set up mon-modified objects used by all test methods
    Recipe.objects.create(name='Cheeseburger',
                          cooking_time = 10,
                          ingredients = 'beef patty, bun, cheese', 
                          difficulty = 'hard',
                          )
    
  def test_recipe_name(self):
    # Get a recipe object to test
    recipe = Recipe.objects.get(id=1)
    
    # Get the metadata for the 'name' field and use it to query its data
    field_label = recipe._meta.get_field('name').verbose_name

    # Compare the value to the expected result
    self.assertEqual(field_label, 'name')
    
  def test_ingredients_max_length(self):
    ingredient = Recipe.objects.get(id=1)
    max_length = ingredient._meta.get_field('ingredients').max_length
    self.assertEqual(max_length, 300)
          
  def test_cookingtime_helptext(self):
    recipe = Recipe.objects.get(id=1)
    recipe_cookingtime = recipe._meta.get_field('cooking_time').help_text
    self.assertEqual(recipe_cookingtime, 'in minutes')
        
  def test_difficulty_calculation(self):
    recipe = Recipe.objects.get(id=1)
    self.assertEqual(recipe.difficulty, 'hard')