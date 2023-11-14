# Generated by Django 4.2.7 on 2023-11-14 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeGeneralDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('id_no', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='EmployeeOtherDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nationality', models.CharField(max_length=100)),
                ('ethnicity', models.CharField(choices=[('ASIAN', 'Asian'), ('BLACK', 'Black'), ('HISPANIC', 'Hispanic'), ('WHITE', 'White'), ('OTHER', 'Other')], max_length=10)),
                ('home_county', models.CharField(max_length=100)),
                ('postal_address', models.TextField()),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('telephone_number', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('alternative_person_name', models.CharField(max_length=200)),
                ('alternative_person_telephone_number', models.CharField(max_length=20)),
                ('has_disability', models.BooleanField(default=False)),
                ('disability_details', models.TextField(blank=True, null=True)),
                ('reg_details', models.TextField(blank=True, null=True)),
                ('general_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='other_details', to='employee_details.employeegeneraldetails')),
            ],
            options={
                'ordering': ('general_details__date_created',),
            },
        ),
    ]
