from django.shortcuts import render

def home(request):
   return render(request, 'recipes/pages/home.html', context={
       'name': 'Rafael Santos',
   })

def recipe(request, id):
   return render(request, 'recipes/pages/recipe-view.html', context={
       'name': 'Rafael Santos',
   })
