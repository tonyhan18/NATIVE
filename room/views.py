# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import room
import random

# Create your views here.

def index(req):
    roomTemp=room.objects.all()
    roomList=[]
    if(len(roomTemp)>0):
        roomList.append(roomTemp[random.randint(0,len(roomTemp)-1)])
        for i in range(2):
            c=random.randint(0,len(roomTemp)-1)
            while(roomTemp[c] in roomList):
                c=random.randint(0,len(roomTemp)-1)
            roomList.append(roomTemp[c])
    
    return render(req,'room/main.html',{'roomList':roomList})

def detail(req,id):
    #post = get_object_or_404(room, id=id)        
    roomList = room.objects.get(id=id)
    return render(req,'room/details.html',{'roomList':roomList})

def rooms(req):
    roomList=room.objects.all()
    return render(req, "room/rooms.html", {'roomList':roomList})

def notFound(req):
    return render(req,'comingsoon.html')

def slide(req):
    return render(req,'room/slide.html')

def slide2(req):
    return render(req,'room/slide2.html')