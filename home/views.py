from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q, Sum
from django.core.paginator import Paginator

    
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

def get_student(request):
    
    queryset = Student.objects.all()
    
    
    # using Q to search from multiple attributes
    if request.GET.get("search"):
        search = request.GET.get("search")
        queryset = queryset.filter(
            Q(student_name__icontains = search) | Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) 
        )
        
    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    queryset = paginator.get_page(page_number)
        
    
    return render(request,"report/student.html", {"student": queryset} )


# from home.seed import generate_report_card

def student_marks(request, student_name):
    # generate_report_card()
    
    queryset = SubjectMarks.objects.filter(student__student_name = student_name)
    total_marks = queryset.aggregate(total_marks = Sum('marks'))
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','-student_age')
    # current_rank = -1 
    # i = 1
    
    # for rank in ranks:
    #     if rank.student_name == student_name:
    #         current_rank = i  
    #         print(current_rank)
    #         break
    #     i=i+1
    return render(request, "report/student_marks.html",{'queryset': queryset, 
                                                        'total_marks':total_marks, 
                                                        'current_rank': current_rank})
    