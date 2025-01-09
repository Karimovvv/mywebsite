
from gettext import translation
from django.conf import settings
from django.contrib import messages 
from django.shortcuts import render
from django.http import HttpResponseRedirect
from home.models import ContactForm, ContactMessage, Setting,SettingLang
from course.models import Course,Subject,Tutor,Student
from django.utils.translation import activate

import requests

def index(request):
    setting = Setting.objects.get()
    course = Course.objects.all()
    course_cr = Course.objects.all().order_by('id')[:4]
    subject_cr = Subject.objects.all().order_by('id')[:3]

    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]
    if defaultlang != currentlang:
        setting = SettingLang.objects.filter(lang=currentlang).first()
        if not setting:
            setting = Setting.objects.get() 

    tutor_cr = Tutor.objects.all().order_by('id')[:3]
    page = "home"
    context = {'setting': setting,
               'page': page,
               'subject_cr': subject_cr,
               'course_cr': course_cr,
               'tutor_cr': tutor_cr,
               'course': course,
               }
    return render(request,'index.html', context)


TELEGRAM_BOT_TOKEN = '7656829792:AAHcBKou7ww_0NeU5unXWRXPKV4-Yum4Mps'
TELEGRAM_CHANNEL = '@orders_channel1'
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
            messages.success(request,"Thanks, " + data.name + " We received your message and will respond shortly...")


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            phone = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']
            message_text = f'New message:\n\nName: {name} \nPhone: {phone} \nsubject: {subject} \nMessage: {message}'
            telegram_api_url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
            telegram_params = {'chat_id': {TELEGRAM_CHANNEL},'text': message_text}
            requests.post(telegram_api_url,params=telegram_params)

    setting = Setting.objects.get()
    form = ContactForm()
    context = {'setting': setting}
    return render(request, 'contact.html', context)

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

def students(request):
    student_cr = Student.objects.all()
    setting = Setting.objects.get()
    context = {
        'student_cr': student_cr,
         'setting':setting,
     }
    return render(request,'students.html',context)

def subject(request):
    subject_cr = Subject.objects.all()
    setting = Setting.objects.get()
    context = {
        'subject_cr': subject_cr,
        'setting':setting
    }
    return render(request,'subject.html', context)

def subject_detail(request,id,slug):
    subject_c = Subject.objects.all().order_by('id')[:4]
    subject = Subject.objects.get(pk=id)
    course = Course.objects.all()
    context = {
        'subject_c': subject_c,
        'subject':subject,
        'course':course
    }
    return render(request,'subject_detail.html', context)

def selectlanguage(request):
    if request.method == 'POST':
        lang = request.POST['language']
        activate(lang)
        request.session[settings.LANGUAGE_COOKIE_NAME] = lang
        return HttpResponseRedirect('/' + lang)


