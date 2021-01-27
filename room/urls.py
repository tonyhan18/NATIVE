from  django.urls import path
from django.contrib import admin
from . import views

# 이미지를 업로드 하자
from django.conf.urls.static import static
from django.conf import settings
from .models import room

urlpatterns=[
    path('',views.index),
    
    path('room/<int:id>/',views.rmDetail,name='rmDetail'),
    path('room/',views.rmDetail,name='rmDetail'),
    #path('rmDetail',views.rmDetail,name='rmDetail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)