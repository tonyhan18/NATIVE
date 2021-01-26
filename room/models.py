# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class room(models.Model):
    house_no=models.CharField(max_length=32,verbose_name="집번호")
    master_no=models.CharField(max_length=32,verbose_name="집주인 번호")
    house_name=models.CharField(max_length=64,verbose_name="집이름")
    house_location=models.CharField(max_length=256,verbose_name="집주소")
    master_name=models.CharField(max_length=65,verbose_name="집주인 이름")
    class Meta:
        db_table="room"
        verbose_name="방 DB"
        verbose_name_plural="방 DB"