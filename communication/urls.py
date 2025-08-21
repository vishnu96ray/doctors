from django.urls import path
from communication import views

urlpatterns = [
    path('', views.audiocall, name='voicecall'),

    path('galleryimage/', views.image, name='image'),
    path('galleryvideo/', views.video, name='video'),
]
