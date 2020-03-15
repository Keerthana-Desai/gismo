from django.shortcuts import render

from .models import Collage, Picture

import os
import time
import sys

folder_name = "test"
triggerCommand = "gphoto2 --capture-image-and-download"

nb_images = 1
listofimages = []

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
    os.system("mkdir " + str(folder_name))

    global nb_images
    nb_images = 0

    return render(request, 'wedding/start.html')

def ready(request):

    global nb_images
    if nb_images < 4:
        return render(request, 'wedding/ready.html')
    else:
        nb_images = 0
        sys.stdout.write("Collage wird erstellt!\n")
        return render(request, 'wedding/ready.html')

def countdown(request):
    return render(request, 'wedding/countdown.html')

def preview(request):

    #os.system(triggerCommand)
    #time.sleep(1)

    global nb_images
    nb_images += 1

    sys.stdout.write("Bild " + str(nb_images) +  " wurde geschossen\n")

    global c
    c.picture_set.create(picture_name = "bild" + str(nb_images),
                         picture_url = "bild" + str(nb_images))
    return render(request, 'wedding/preview.html')

def collage(request):
    return render(request, 'wedding/collage.html')

def print(request):
    return render(request, 'wedding/print.html')

def gallery(request):

    gallery_list = Collage.objects.first()

    return render(request, 'wedding/gallery.html', {"gallery_list" : gallery_list})
