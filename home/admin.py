from django.contrib import admin
from .models import *

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'department', 'patient_name', 'email', 'mobile', 'dob', 'note', 'added_date')


admin.site.register(Appointment, AppointmentAdmin)    