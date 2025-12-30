from django.db import models

class Doctor(models.Model):
    name= models.CharField( max_length=100)
    department=models.CharField(max_length=100)
    phone=models.CharField( max_length=50)


    def __str__(self):
        return self.name


class patient(models.Model):
    name=models.CharField( max_length=150)
    age=models.IntegerField()
    disease=models.CharField( max_length=100)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(
        patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    date = models.DateField()
    time = models.TimeField()

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} → Dr. {self.doctor.name} ({self.date})"