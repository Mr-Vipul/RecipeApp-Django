from django.contrib import admin
from .models import *
from django.db.models import Sum

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentID)
admin.site.register(Subject)


class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register(SubjectMarks, SubjectMarkAdmin)


class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student','student_rank', 'total_marks', 'date_of_generation']
    
    def total_marks(self, obj):
        subject_marks = SubjectMarks.objects.filter(student = obj.student)
        marks = (subject_marks.aggregate(marks = Sum('marks')))
        return marks['marks']
    
admin.site.register(ReportCard, ReportCardAdmin)
