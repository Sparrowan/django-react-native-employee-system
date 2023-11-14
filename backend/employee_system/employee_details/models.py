from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

ETHNICITY_CHOICES = (
    ('ASIAN', 'Asian'),
    ('BLACK', 'Black'),
    ('HISPANIC', 'Hispanic'),
    ('WHITE', 'White'),
    ('OTHER', 'Other'),
)

class EmployeeGeneralDetails(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    id_no = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employees')

    class Meta:
        ordering = ('date_created',)

    def __str__(self):
        return self.name

class EmployeeOtherDetails(models.Model):
    general_details = models.OneToOneField(EmployeeGeneralDetails, on_delete=models.CASCADE, related_name='other_details')
    nationality = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=10, choices=ETHNICITY_CHOICES)
    home_county = models.CharField(max_length=100)
    postal_address = models.TextField()
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    alternative_person_name = models.CharField(max_length=200)
    alternative_person_telephone_number = models.CharField(max_length=20)
    has_disability = models.BooleanField(default=False)
    disability_details = models.TextField(blank=True, null=True)
    reg_details = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('general_details__date_created',)

    def __str__(self):
        return self.other_details.name
        
