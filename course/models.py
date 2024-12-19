from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    image = models.ImageField(null=False,upload_to='images/')
    slug = models.SlugField(null=False,unique=True)

class Subject(models.Model):
    name = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subject_tutor = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    image = models.ImageField(null=False,upload_to='images/')
    price = models.CharField(max_length=50)
    detail = models.CharField(max_length=150)
    slug = models.SlugField(null=False,unique=True)

    def __str__(self):
        return self.title

