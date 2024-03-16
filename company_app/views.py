from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from .models import Company
from .forms import CompanyForm
from django.urls import reverse_lazy

class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company_app/add.html'
    success_url = reverse_lazy('company_app:company_list') 


class CompanyListView(ListView):
    model = Company
    template_name = 'company_app/all.html'
    context_object_name = 'companies'

class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'company_app/view.html'
    success_url = reverse_lazy('company_app:company_list_view') 
    
class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company_app/view.html'
    context_object_name = 'company'

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company_app/company_app_confirm_delete.html'
    success_url = reverse_lazy('company_app:company_list')
