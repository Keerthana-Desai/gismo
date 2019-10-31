from django.urls import path

from . import views

app_name = 'wedding'
urlpatterns = [
    path('', views.start, name='start'),
    path('ready/', views.ready, name='ready'),
    path('countdown/', views.countdown, name='countdown'),
    path('preview/', views.preview, name='preview'),
    path('collage/', views.collage, name='collage'),
    path('print/', views.print, name='print'),
    path('gallery/',views.gallery, name='gallery'),
]
