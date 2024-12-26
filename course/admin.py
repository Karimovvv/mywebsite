from django.contrib import admin
from course.models import Course,Subject,Student,Tutor

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','slug']

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Tutor)




# Register your models here.
