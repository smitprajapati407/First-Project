from django.urls import path
from hospital import views

urlpatterns = [
    path('',views.home,name='home'),
    path('patients/',views.patient_list,name='patient_list'),
    path('add_patients/',views.add_patient,name='add_patient'),
    path('doctors/',views.doctor_list,name='doctor_list'),
    path('add_doctors/',views.add_doctor,name='add_doctor'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('delete_patient/<int:id>/', views.delete_patient, name='delete_patient'),
    path('delete_doctor/<int:id>/', views.delete_doctor, name='delete_doctor'),
    path('delete_appointment/<int:id>/', views.delete_appointment, name='delete_appointment'),



   

]
