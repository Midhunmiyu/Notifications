from django.contrib import admin
from .models import *


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message',)

