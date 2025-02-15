from django.urls import path
from . views import (
    PatientListView, PatientCreateView, PatientDetailView,PatientUpdateView,
    TreatmentCreateView,PatientDeleteView, AppointmentCreateView
                     )

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
    path('create/', PatientCreateView.as_view(), name='patient_create'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('<int:pk>/update/', PatientUpdateView.as_view(), name='patient_update'),
    path('<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
    # URL to add treatment
    path('patient/<int:patient_id>/add_treatment/', TreatmentCreateView.as_view(), name='add_treatment'),
    # URL to add appointment
    path('patient/<int:patient_id>/add_appointment/', AppointmentCreateView.as_view(), name='add_appointment'),
    ]