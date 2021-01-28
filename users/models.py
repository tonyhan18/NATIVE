from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator

class Users(models.Model):
    userId=models.CharField(max_length=64, verbose_name="사용자 ID")
    userPw=models.CharField(max_length=64, verbose_name="사용자 PW")
    userName=models.CharField(max_length=64, verbose_name="사용자 이름")
    userAddress=models.CharField(max_length=256, verbose_name="사용자주소")
    userPhone=models.CharField(max_length=64, verbose_name="사용자 전화번호", null=True, blank=True)

    class Meta:
        db_table = "users"
        verbose_name ="개인 사용자들"
        verbose_name_plural="개인 사용자들"