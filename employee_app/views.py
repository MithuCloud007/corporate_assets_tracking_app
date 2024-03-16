from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from .models import Employee
from .forms import EmployeeForm
from django.urls import reverse_lazy

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_app/add.html'
    success_url = reverse_lazy('employee_app:employee_list') 


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_app/all.html'
    context_object_name = 'employees'

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_app/add.html'
    success_url = reverse_lazy('employee_app:employee_list') 
    
class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_app/view.html'
    context_object_name = 'employee'

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_app/employee_app_confirm_delete.html'
    success_url = reverse_lazy('employee_app:employee_list')
