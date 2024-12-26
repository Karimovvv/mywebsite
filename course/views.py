from django.shortcuts import render
from home.models import Setting
# from django.http import HttpResponse


def index(request):
    setting = Setting.objects.get()
    context = {'setting':setting}
    return render(request,'course.html',context)

