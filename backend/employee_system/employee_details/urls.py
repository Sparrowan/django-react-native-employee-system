from django.urls import path
from .views import *

app_name = 'employee_details'
urlpatterns = [
    # Other URL patterns...
    path('list/', ListCombinedEmployeeDetailsView.as_view(), name='employee-list'),
    path('create/', CreateEmployeeDetailsView.as_view(), name='create-employee-details'),
]
