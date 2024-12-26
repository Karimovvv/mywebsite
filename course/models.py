from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.TextField()
    description = models.TextField(max_length=500)
    image = models.ImageField(null=False,upload_to='images/')
    slug = models.SlugField(null=False,unique=True)

    def __str__(self):
        return self.title

class Subject(models.Model):
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    subject_tutor = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=False,upload_to='images/')
    price = models.CharField(max_length=50)
    detail = models.CharField(max_length=150)
    slug = models.SlugField(null=False,unique=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(null=False, upload_to='images/')
    
    def __str__(self):
        return self.name

class Tutor(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, models.CASCADE, default=1)
    description = models.TextField()
    image = models.ImageField(null=False, upload_to='images/')

    def __str__(self):
        return self.namea
    


