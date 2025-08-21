from django.urls import path
from cochler import views


urlpatterns = [
    path('cochalar_impliments/', views.cochalar_impliments, name='cochalar_impliments'),
    path('cochalar_mapping/', views.cochalar_mapping, name='cochalar_mapping'),
    path('cochalar_parts/', views.cochalar_parts, name='cochalar_parts'),
    path('cochalar_service/', views.cochalar_service, name='cochalar_service'),
    path('cochalar_works/', views.cochalar_works, name='cochalar_works'),
    path('cochalar_maintines/', views.cochalar_maintines, name='cochalar_maintines'),
    path('cochalar_benefits/', views.cochalar_benefits, name='cochalar_benefits'),
    path('cochalar_auditoring/', views.cochalar_auditoring, name='cochalar_auditoring'),


]