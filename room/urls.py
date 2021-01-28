from  django.urls import path
from django.contrib import admin
from . import views

# 이미지를 업로드 하자
from django.conf.urls.static import static
from django.conf import settings
from .models import room

urlpatterns=[
    path('',views.index),
    path('rooms',views.rooms),
    path('room/<int:id>/',views.detail,name='details'),
    path('room/',views.detail,name='details'),
    path('room/slide/',views.slide,name='slide'),
    path('room/slide2/',views.slide2,name='slide2'),
    #path('rmDetail',views.rmDetail,name='rmDetail'),
    path('404/',views.notFound,name='404'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)