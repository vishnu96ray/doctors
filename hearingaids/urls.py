from django.urls import path
from hearingaids import views

urlpatterns = [
    path('hearingaids/', views.hearingaids, name='hearingaids'),
    path('hearingcare/', views.hearingcare, name='hearingcare'),
    path('digital_hearing/', views.digital_hearing, name='digital_hearing'),
    path('evaluate/', views.evaluate, name='evaluate'),
    path('hearingaidshelp/', views.hearingaidshelp, name='hearingaidshelp'),
    path('hearingaids_types/', views.hearingaids_types, name='hearingaids_types'),
    path('wireless_hearingads/', views.wireless_hearingads, name='wireless_hearingads'),

]
