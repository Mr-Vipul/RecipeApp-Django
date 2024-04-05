from django.db import models
from django.contrib.auth.models import User
# django has inbuilt user models like name username password email and many more



# Create your models here.
class Recipe(models.Model):
    # it will delete all data related to that user 
    # 1.-> SET_NULL : put null value to that user
    # 2.->SET_DEFAULT :put some default value to that user
    # 3.->CASCADE : delete all data related to that user
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank = True)
    
    recipe_name = models.CharField(max_length=200)
    recipe_description = models.TextField(max_length=200)
    recipe_image = models.ImageField(upload_to='recipe_images')
    recipe_view_count = models.IntegerField(default = 1)
    
class Department(models.Model):
    department = models.CharField(max_length=200)
    
    def __str__(self):
        return self.department
    
    class Meta :
        ordering = ["department"]

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)
    
    def __str__(self):
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name = "depart", on_delete = models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name ="studentid", on_delete = models.CASCADE)
    student_name = models.CharField(max_length = 100)
    student_email = models.EmailField(unique = True)
    student_age = models.IntegerField(default = 18)
    student_address = models.TextField()
    
    def __str__(self):
        return self.student_name
    
    # This is use for ordering the student name in admin panel
    class Meta :
        ordering = ["student_name"]
        verbose_name =  "student"    

    
   
