from django.db import models


class Services(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    verbose_name = 'Service'


class Staff(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} ({self.title})"


class Appointment(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Staff, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{self.email} || ({self.appointment_date}:{self.appointment_time})"
