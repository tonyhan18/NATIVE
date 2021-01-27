# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class room(models.Model):
    room_no=models.CharField(max_length=32,verbose_name="집번호")
    master_no=models.CharField(max_length=32,verbose_name="집주인 번호")
    room_name=models.CharField(max_length=64,verbose_name="집이름")
    room_location=models.CharField(max_length=256,verbose_name="집주소")
    master_name=models.CharField(max_length=65,verbose_name="집주인 이름")
    room_image=models.ImageField(upload_to='static/img/room/', blank=True, null=True)
    room_detail_s=models.TextField(max_length=128,verbose_name="방 정보(짧음)",null=True)
    room_detail=models.TextField(max_length=1024,verbose_name="방 정보(상세)",null=True)

    class Meta:
        db_table="room"
        verbose_name="방 DB"
        verbose_name_plural="방 DB"

# class roomImage(models.Model):
#     room=models.ForeignKey(room,on_delete=models.CASCADE,null=True)
    