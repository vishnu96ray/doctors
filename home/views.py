from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment
from .choices import *
from .service import *
import datetime

def home(request):
	return render(request, 'index.html')


def appointment(request):
	if request.method == 'POST':

		department = request.POST.get('department')
		patient_name = request.POST.get('patient_name')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')
		dob = request.POST.get('dob')
		note = request.POST.get('note')
		try:
			apid = appointment_id()
			appointed = Appointment(appointment_id=apid, department=department, patient_name=patient_name,email=email,mobile=mobile,dob=dob,note=note)
			filtered_patient_by_email = Appointment.objects.filter(email=email)
			if filtered_patient_by_email.exists():
				return HttpResponse("Email already exist!")
			else:
				appointed.save()
			#ap = appointed_patient(patient_number,appointment_id) 
		except:
			print("error")	
		# ap_data = None
		# ap_data = Appointment.objects.filter(added_date=datetime.datetime.now())
		# print(ap_data,9999)	
	return render(request, 'accounts/appointment.html', {'department':DEPARTMENT})

# voicetherepy start

def voicetherepy(request):
	return render(request, 'facility/voice_therapy/voice_therepy.html')

# speechtherepy start

def speechtherepy(request):
	return render(request, 'facility/speech_therapy/speech_therepy.html')

def speechclasses(request):
	return render(request, 'facility/speech_therapy/speech_classes.html')

def speechbenefits(request):
	return render(request, 'facility/speech_therapy/speech_benefits.html')

# hearingtest start
def hearingtest(request):
	return render(request, 'facility/hearing_test/hearing_test.html')

def pta_hearingtest(request):
	return render(request, 'facility/hearing_test/pta.html')

def oae_hearingtest(request):
	return render(request, 'facility/hearing_test/oae.html')

def bera_hearingtest(request):
	return render(request, 'facility/hearing_test/bera.html')

def assr_hearingtest(request):
	return render(request, 'facility/hearing_test/assr.html')

#fluency therepy

def fluency(request):
	return render(request, 'facility/fluency.html')

#language therapy
def language(request):
	return render(request, 'facility/language.html')


def baha(request):
	return render(request, 'product/baha.html')

def wireless(request):
	return render(request, 'product/wireless.html')


