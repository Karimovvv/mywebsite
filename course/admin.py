from django.contrib import admin
from course.models import Course,Subject,Student,Tutor

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag']

admin.site.register(Course,CourseAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Student)
admin.site.register(Tutor)




# Register your models here.
