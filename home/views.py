
from django.contrib import messages 
from django.shortcuts import render
# from django.http import HttpResponse
from home.models import ContactForm, ContactMessage, Setting
from course.models import Course,Subject,Tutor
# TELEGRAM_BOT_TOKEN = ''
# TELEGRAM_CHANNEL = ''

def index(request):
    setting = Setting.objects.get()
    course = Course.objects.all()
    course_cr = Course.objects.all().order_by('id')[:4]
    subject_cr = Subject.objects.all().order_by('id')[:3]
    tutor_cr = Tutor.objects.all().order_by('id')[:3]
    page = "home"
    context = {'setting': setting,
               'page': page,
               'subject_cr': subject_cr,
               'course_cr': course_cr,
               'tutor_cr': tutor_cr,
               'course':course,
               }
    return render(request,'index.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Thanks, " + data.name + "We received your message and will respond shortly...")


    setting = Setting.objects.get()
    form = ContactForm()
    context = {'setting': setting}
    return render(request, 'contact.html', context)

    # if request.method == 'POST':
    #     form = ContactForm(request.Post)
    #     if form.is_valid():
    #         name = request.POST['name']
    #         phone = request.POST['phone']
    #         subject = request.POST['subject']
    #         message = request.POST['message']
    #         message_text = f'New message:\n\nName: {name} \nPhone: {phone} \nsubject: {subject} \nMessage: {message}'
    #         telegram_api_url = f''
    #         telegram_params = {'chat_id': {TELEGRAM_CHANNEL},'text': message_text}
    #         request.post{telegram_api_url},telegram_params
def about(request):
   setting = Setting.objects.get()
   context = {'setting': setting}
   return render(request, 'about.html', context)

def tutors(request):
    tutor_cr = Tutor.objects.all().order_by('id')
    setting = Setting.objects.get()
    context = {'tutor_cr': tutor_cr,
               'setting': setting
               }

    return render(request, 'tutor.html', context)




