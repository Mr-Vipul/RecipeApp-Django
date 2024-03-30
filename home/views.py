from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        
        # print(recipe_name)
        # print(recipe_description)
        # print(recipe_image)
        
        Recipe.objects.create(
            recipe_image = recipe_image,
            recipe_name = recipe_name ,
            recipe_description = recipe_description, 
        )
        return redirect("/home/")
    
    queryset = Recipe.objects.all()
    
    
    # We are here searching our content in recipe_name using "__icontains"
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    
    context = {"recipe" : queryset}

    return render(request, "recipe.html", context)


# Deleting the recipe here
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    queryset.save()
    return redirect("/home")


# Updating the Recipe name and its description also image 
def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    
    
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        
        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
    
        if recipe_image:
            queryset.recipe_image = recipe_image
            
        queryset.save()
        return redirect("/home")
    
    context = {"recipe": queryset}
    
    return render(request, "update.html", context)