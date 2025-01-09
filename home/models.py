from django.db import models
from django.forms import ModelForm, TextInput, Textarea

class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    smptserver = models.CharField(max_length=50,blank=True)
    smptemail = models.EmailField(max_length=50,blank=True)
    smptpassword = models.CharField(max_length=10,blank=True)
    smptport = models.CharField(max_length=5,blank=True)
    youtube = models.URLField(blank=True,max_length=50)
    instagram = models.URLField(blank=True,max_length=50)
    facebook = models.URLField(blank=True,max_length=50)
    icon = models.ImageField(blank=True,upload_to='images/')
    aboutus = models.TextField(max_length=255,default="Default Address")
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('New','New'),
        ('Read','Read'),
        ('Closed','Closed'),
    )

    name = models.CharField(blank=True,max_length=20)
    phone = models.CharField(blank=True,max_length=50)
    subject = models.CharField(blank=True,max_length=50)
    message = models.TextField(blank=True,max_length=255)
    status = models.EmailField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=20)
    note = models.CharField(blank=True,max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
  

    def __str__(self):
        return self.name
  

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','phone','subject','message']
        widgets = {
            'name': TextInput(attrs={'class':'input','placeholder':'Name & Surname'}),
            'phone': TextInput(attrs={'class':'input','placeholder':'Phone number'}),
            'subject': TextInput(attrs={'class':'input','placeholder':'Subject'}),
            'message': Textarea(attrs={'class':'input','placeholder':'Your message','rows':'5'}),
        }

class Language(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5)
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

llist = Language.objects.all()
list1 = []
for rs in llist:
    list1.append((rs.code, rs.name))
langlist = (list1)


class SettingLang(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    lang = models.CharField(max_length=6,choices=langlist)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    smptserver = models.CharField(max_length=50,blank=True)
    smptemail = models.EmailField(max_length=50,blank=True)
    smptpassword = models.CharField(max_length=10,blank=True)
    smptport = models.CharField(max_length=5,blank=True)
    youtube = models.URLField(blank=True,max_length=50)
    instagram = models.URLField(blank=True,max_length=50)
    facebook = models.URLField(blank=True,max_length=50)
    icon = models.ImageField(blank=True,upload_to='images/')
    aboutus = models.TextField(max_length=255,default="Default Address")
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.title