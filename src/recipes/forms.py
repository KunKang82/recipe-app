from django import forms    #import django forms

CHART__CHOICES = (          #specify choices as a tuple
  ('#1', 'Bar chart'),      # when user selects "Bar chart", it is stored as "#1"
  ('#2', 'Pie chart'),
  ('#3', 'Line chart')
  )

DIFFIC__CHOICES = (         # specify choices as a tuple
    ('', ' '),  # Empty string as the value for the default (no difficulty selected)
    ('Easy', 'Easy'),           
    ('Medium', 'Medium'),
    ('Intermediate', 'Intermediate'),
    ('Hard', 'Hard')
)

#define class-based Form imported from Django forms
class RecipesSearchForm(forms.Form): 
  recipe_name= forms.CharField(max_length=120, required=False, label ='Recipe Name')
  ingredients = forms.CharField(max_length=300, required=False, label='Ingredients')
  recipe_diff = forms.ChoiceField(choices=DIFFIC__CHOICES, required=False, label='Recipe Difficulty Level')
  chart_type = forms.ChoiceField(choices=CHART__CHOICES, required=False, label='Chart Type')