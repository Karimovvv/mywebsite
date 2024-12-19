from django.contrib import admin
from course.models import Course,Subject

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','slug']

admin.site.register(Course)
admin.site.register(Subject)


# Register your models here.
