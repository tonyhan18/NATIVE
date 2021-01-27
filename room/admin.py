# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import room

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display=('room_no','room_no','room_name','room_location','room_name','room_image')
    pass

admin.site.register(room)