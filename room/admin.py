# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import room

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display=('house_no','master_no','house_name','house_location','master_name','house_image')
    pass

admin.site.register(room)