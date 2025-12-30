from django.shortcuts import render,redirect
from hospital.models import Doctor,patient,Appointment

def home(request):
    return render(request,'home.html')

def appointment_list(request):
    appointments = Appointment.objects.select_related('patient', 'doctor')
    return render(request, 'appointment_list.html', {
        'appointments': appointments
    })

def add_appointment(request):
    patients = patient.objects.all()
    doctors = Doctor.objects.all()

    if request.method == "POST":
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')

        Appointment.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date=date,
            time=time
        )

        return redirect('appointment_list')

    return render(request, 'add_appointment.html', {
        'patients': patients,
        'doctors': doctors
    })

def delete_appointment(request, id):
    appointment = Appointment.objects.filter(id=id).first()

    if appointment and request.method == "POST":
        appointment.delete()

    return redirect('appointment_list')







def add_patient(request):
    doctors = Doctor.objects.all()
    if request.method=='POST':
        doctor_id = request.POST.get('doctor')   
        doctor_obj = Doctor.objects.get(id=doctor_id)
        patient.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            disease=request.POST.get('disease'),
            doctor=doctor_obj 
        )
        return redirect('patient_list')
    return render(request, 'add_patient.html', {'doctors': doctors})

def patient_list(request):
    patients= patient.objects.all()
    return render(request,'patient_list.html',{'patients': patients})

def delete_patient(request, id):
    patients = patient.objects.filter(id=id).first()

    if patients and request.method == "POST":
        patients.delete()

    return redirect('patient_list')



def add_doctor(request):
    if request.method == 'POST':
        Doctor.objects.create(
            name=request.POST['name'],
            department=request.POST['department'],
            phone=request.POST['phone']
        )
        return redirect('doctor_list')
    return render(request,'add_doctor.html')

def doctor_list(request):
    doctors= Doctor.objects.all()
    return render(request,'doctor_list.html',{'doctors': doctors})


def delete_doctor(request, id):
    doctor = Doctor.objects.filter(id=id).first()

    if doctor and request.method == "POST":
        doctor.delete()

    return redirect('doctor_list')






