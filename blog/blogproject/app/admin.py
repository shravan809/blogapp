from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Blog)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','title','blog')

@admin.register(Contact)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email')





