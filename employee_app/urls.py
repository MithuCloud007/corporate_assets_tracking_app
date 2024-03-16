from django.urls import path
from .views import EmployeeCreateView,EmployeeListView,EmployeeUpdateView,EmployeeDetailView,EmployeeDeleteView
app_name='employee_app'

urlpatterns = [
    path('employee-add', EmployeeCreateView.as_view(), name="employee_add"),
    path('employee-list', EmployeeListView.as_view(), name="employee_list"),
    path('employee-list-update/<int:pk>', EmployeeUpdateView.as_view(), name="employee_list_update"),
    path('employee-list-view/<int:pk>', EmployeeDetailView.as_view(), name="employee_list_view"),
    path('employee-list-delete/<int:pk>', EmployeeDeleteView.as_view(), name="employee_list_delete"),
]