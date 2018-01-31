from django.contrib import admin
from . import models

# Register your models here.

class TPersonAdmin(admin.ModelAdmin):
    fields = ['p_name','first_name','last_name']
    list_display = ('p_name','first_name','last_name')


admin.site.register(models.TPerson,TPersonAdmin)