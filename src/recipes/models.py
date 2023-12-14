from django.db import models

# Create your models here.
difficulty_choices = (
  ('easy', 'Easy'), 
  ('medium', 'Medium'), 
  ('intermediate', 'Intermediate'), 
  ('hard', 'Hard'),
)
# Create your models here.
class Recipe(models.Model):
    name= models.CharField(max_length=120)
    cooking_time = models.PositiveIntegerField(help_text = 'in minutes')
    ingredients = models.CharField(max_length=300)
    difficulty = models.CharField(max_length=12, choices=difficulty_choices)


    def __str__(self):
        return str(self.name)