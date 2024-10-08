"""
URL configuration for recipeApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home, name="home"),
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("delete_recipe/<id>/", delete_recipe, name="delete_recipe"),
    path("update_recipe/<id>/", update_recipe, name="update_recipe"),
    path("student/", get_student, name="get_student"),
    path("student-marks/<student_name>/", student_marks, name="student_marks"),
    path("send_email/", send_email, name="send_email"),
    
    # path("url_name that we want", function_name, name="function_name")
]
