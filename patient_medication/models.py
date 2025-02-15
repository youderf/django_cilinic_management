from django.db import models
from django.db import models
from datetime import date
from django.contrib import admin


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=250)
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    photo = models.ImageField(upload_to='patients/photos/', null=True, blank=True)
    first_visit_date = models.DateField(null=True, blank=True, editable=False)  # Not editable in admin
    last_visit_date = models.DateField(default=date.today)  # Auto-updates on every save

    def save(self):
        # Set first_visit_date only if it's not already set
        if not self.first_visit_date:
            self.first_visit_date = date.today()
        super().save()

    def __str__(self):
        return self.name


# Treatment model
class Treatment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.CharField(max_length=255)
    medical_treatment = models.TextField()
    treatment_date = models.DateField(null=True, blank=True, editable=False)

    def save(self):
        # Set treatment_date only if it's not already set
        if not self.treatment_date:
            self.treatment_date = date.today()
        super().save()

    def __str__(self):
        return f"{self.disease} ({self.patient.name})"


# Appointment Model
class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.CharField(max_length=50)

    def __str__(self):
        return f"Appointment for {self.patient.name} on {self.appointment}"


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address',)
