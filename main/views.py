from django.shortcuts import render

from .models import *


def home_view(request):
    services = Services.objects.all()
    staff = Staff.objects.all()
    if request.method == 'POST':
        print('POSTED')
        service = request.POST.get('service')
        doctor = request.POST.get('doctor')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        Appointment.objects.create(
            service_id=service, doctor_id=doctor, full_name=full_name, email=email,
            appointment_date=appointment_date, appointment_time=appointment_time
        )
    context = {'services': services, 'staff': staff}

    return render(request, 'index.html', context)
