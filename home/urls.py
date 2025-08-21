from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='homepage'),

    path('newappointment/', views.appointment, name='appointment'),

    path('voicetherepy/', views.voicetherepy, name='voicetherepy'),

    path('speechtherepy/', views.speechtherepy, name='speechtherepy'),
    path('sp_classes/', views.speechclasses, name='speechclasses'),
    path('sp_benefits/', views.speechbenefits, name='speechbenefits'),

    path('hearingtest/', views.hearingtest, name='hearingtest'),
    path('pta_hearingtest/', views.pta_hearingtest, name='pta_hearingtest'),
    path('oae_hearingtest/', views.oae_hearingtest, name='oae_hearingtest'),
    path('bera_hearingtest/', views.bera_hearingtest, name='bera_hearingtest'),
    path('assr_hearingtest/', views.assr_hearingtest, name='assr_hearingtest'),

    path('fluency/', views.fluency, name='fluency'),
    
    path('language/', views.language, name='language'),

    path('baha/', views.baha, name='baha'),
    path('wireless/', views.wireless, name='wireless'),



]
