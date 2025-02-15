from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Patient, Treatment, Appointment


# ===========================
# View for Patient model
# ===========================
class PatientListView(ListView):
    """Display the patients list"""
    model = Patient
    # context_object_name = 'patient_list'
    paginate_by = 4
    ordering = ['-id']


class PatientDetailView(DetailView):
    """Display patient detail."""
    model = Patient


class PatientCreateView(CreateView):
    """Allows to create a new patient."""
    model = Patient
    fields = ['name', 'email', 'phone', 'gender', 'address', 'age', 'weight', 'photo']
    success_url = reverse_lazy('patient_list')  # Redirect after creation


class PatientUpdateView(UpdateView):
    """Allows to update an existing patient."""
    model = Patient
    fields = ['name', 'email', 'phone', 'gender', 'address', 'age', 'weight', 'photo', 'last_visit_date']
    success_url = reverse_lazy('patient_list')  # Redirect after update


class PatientDeleteView(DeleteView):
    """Allows to delete a patient."""
    model = Patient
    template_name = 'patient_medication/patient_confirm_delete.html'  # Name of the template to confirm deletion
    success_url = reverse_lazy('patient_list')  # Redirect after deletion


# ===========================
# View for Treatment model
# ===========================
class TreatmentCreateView(CreateView):
    # Specifies the model associated with this view
    model = Treatment

    # Defines the fields that will be included in the form
    fields = ['disease', 'medical_treatment']

    # Defines the URL to redirect to upon successful form submission
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        # Retrieves the 'patient_id' from the URL parameters
        patient_id = self.kwargs.get('patient_id')

        # Fetches the Patient instance with the given ID
        patient = Patient.objects.get(id=patient_id)

        # Associates the new Treatment instance with the retrieved Patient
        form.instance.patient = patient

        # Calls the parent class's form_valid() method to complete the process
        return super().form_valid(form)


# =================================
# View for creating an Appointment
# =================================
class AppointmentCreateView(CreateView):
    # Specifies the model associated with this view
    model = Appointment

    # Defines the fields to include in the form
    fields = ['appointment',]

    # Defines the URL to redirect to after a successful form submission
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        # Retrieve the 'patient_id' from the URL parameters
        patient_id = self.kwargs.get('patient_id')

        # Fetch the corresponding Patient instance using the retrieved ID
        patient = Patient.objects.get(id=patient_id)

        # Associate the new Appointment instance with the retrieved Patient
        form.instance.patient = patient

        # Call the parent class's form_valid() method to process the form submission
        return super().form_valid(form)
