from django.shortcuts import render
from django.http import HttpResponse


def hearingaids(request):
	return render(request, 'hearing_aids/hearing_aids.html')

def hearingcare(request):
	return render(request, 'hearing_aids/hearing_care.html')

def digital_hearing(request):
	return render(request, 'hearing_aids/digital_hearing_aids.html')

def evaluate(request):
	return render(request, 'hearing_aids/evaluate.html')

def hearingaidshelp(request):
	return render(request, 'hearing_aids/how_we_do_here.html')


def hearingaids_types(request):
	return render(request, 'hearing_aids/types_of_hearing_aids.html')

def wireless_hearingads(request):
	return render(request, 'hearing_aids/wireless_hearing_aids.html')



