from django.shortcuts import render                         #imported by default
from django.views.generic import ListView, DetailView       #to display lists
from .models import Recipe                                  #to access recipe model
from django.contrib.auth.mixins import LoginRequiredMixin   #to protect class-based view
from django.contrib.auth.decorators import login_required   #to protect function-based view

# Create your views here.
def recipes_home(request):
  return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):         #class-based view
  model = Recipe                                            #specify model
  template_name = 'recipes/main.html'                       #specity template
  
class RecipeDetailView(LoginRequiredMixin, DetailView):     #class-based view
  model = Recipe                                            #specify model
  template_name = 'recipes/detail.html'                     #specify template

#define function-based view - records(request)  
#keep protected
@login_required
def records(request):
#do nothing, simply display page    
  return render(request, 'recipes/records.html')