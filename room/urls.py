from  django.urls import path
from django.contrib import admin
from . import views

# 이미지를 업로드 하자
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)