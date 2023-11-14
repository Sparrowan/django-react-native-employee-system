from django.contrib import admin
from .models import EmployeeGeneralDetails, EmployeeOtherDetails


@admin.register(EmployeeGeneralDetails)
class EmployeeGeneralDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'date_of_birth', 'id_no', 'gender', 'date_created', 'created_by')
    # Add other configurations or fields to display in the list view

@admin.register(EmployeeOtherDetails)
class EmployeeOtherDetailsAdmin(admin.ModelAdmin):
    list_display = ('general_details', 'nationality', 'ethnicity', 'home_county', 'email', 'has_disability')
    # Add other configurations or fields to display in the list view
