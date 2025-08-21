from django.shortcuts import render
from django.http import HttpResponse


def cochalar_impliments(request):
	return render(request, 'cochalar_impliments/cochalar_impliments.html')

def cochalar_mapping(request):
	return render(request, 'cochalar_impliments/cochalar_mapping.html')

def cochalar_parts(request):
	return render(request, 'cochalar_impliments/cochalar_parts.html')

def cochalar_service(request):
	return render(request, 'cochalar_impliments/cochalar_service.html')

def cochalar_works(request):
	return render(request, 'cochalar_impliments/cochalar_works.html')


def cochalar_maintines(request):
	return render(request, 'cochalar_impliments/cochalar_care_maintines.html')

def cochalar_benefits(request):
	return render(request, 'cochalar_impliments/cochalar_benefits.html')

def cochalar_auditoring(request):
	return render(request, 'cochalar_impliments/cochalar_auditoring.html')


