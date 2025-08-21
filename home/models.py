from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .choices import *

class Appointment(models.Model):
	# user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userdetail")
	department = models.IntegerField(choices=DEPARTMENT)
	patient_name = models.CharField(max_length=250)
	email	= models.EmailField(null=True, blank=True)
	mobile = models.BigIntegerField()
	dob		= models.DateField()
	note	= models.TextField(null=True, blank=True)
	added_date = models.DateTimeField(auto_now_add=True)

	appointment_id = models.CharField(max_length=50)

	def __str__(self):
		return str(self.patient_name)