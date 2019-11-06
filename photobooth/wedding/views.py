from django.shortcuts import render

from .models import Collage, Picture

import os
import time

gallery_list = ['collage1',
#                'bild2',
#                'bild2',
#                'bild2',
#                'bild3',
#                'bild1',
#                'bild2',
#                'bild2',
#                'bild2',
#                'bild3',
#                'bild1',
#                'bild2',
#                'bild2',
#                'bild2',
#                'bild3',
#                'bild1',
#                'bild2',
#                'bild2',
#                'bild2',
#                'bild3',
                ]
for i in range(35):
    gallery_list.append('collage' + str(i+1))
Picture.objects.all().delete()
Collage.objects.all().delete()


c = Collage(collage_name = "test_collage")
c.save()
for i in range(len(gallery_list)):
    c.picture_set.create(picture_name = gallery_list[i],
                        picture_url = gallery_list[i])

def start(request):
    return render(request, 'wedding/start.html')

def ready(request):
    #os.system("mkdir test")
    return render(request, 'wedding/ready.html')

def countdown(request):
    return render(request, 'wedding/countdown.html')

def preview(request):
    time.sleep(5)
    return render(request, 'wedding/preview.html')

def collage(request):
    return render(request, 'wedding/collage.html')

def print(request):
    return render(request, 'wedding/print.html')

def gallery(request):

    gallery_list = Collage.objects.first()

    return render(request, 'wedding/gallery.html', {"gallery_list" : gallery_list})
