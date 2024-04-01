from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

    
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


def login(request):
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")
        
        # checking if the username already exists or not
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "Username Already Taken")
            return redirect("/register/")

        user  = User.objects.create(
                first_name = first_name ,
                last_name = last_name,
                username = username
                 )

        # Encrypted password setter by default  Django
        user.set_password(password)
        user.save()
        
        messages.info(request, "Successfully Created Account")
        return redirect("/register/")
    return render(request, "register.html")








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