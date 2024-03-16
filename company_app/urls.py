from django.urls import path
from .views import CompanyCreateView,CompanyListView,CompanyUpdateView,CompanyDeleteView,CompanyDetailView
app_name='company_app'

urlpatterns = [
    path('company-add', CompanyCreateView.as_view(), name="company_add"),
    path('company-list', CompanyListView.as_view(), name="company_list"),
    path('company-list-update/<int:pk>', CompanyUpdateView.as_view(), name="company_list_update"),
    path('company-list-view/<int:pk>', CompanyDetailView.as_view(), name="company_list_view"),
    path('company-list-delete/<int:pk>', CompanyDeleteView.as_view(), name="company_list_delete"),
]