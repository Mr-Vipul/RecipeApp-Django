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
