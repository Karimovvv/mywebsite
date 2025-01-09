from django.contrib import admin
from home.models import Setting,ContactMessage,Language,SettingLang

admin.site.register(Setting)
admin.site.register(ContactMessage)
admin.site.register(Language)
admin.site.register(SettingLang)



# Register your models here.
