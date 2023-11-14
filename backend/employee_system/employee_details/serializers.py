from rest_framework import serializers
from .models import EmployeeGeneralDetails, EmployeeOtherDetails

class EmployeeGeneralDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeGeneralDetails
        fields = '__all__'

class EmployeeOtherDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeOtherDetails
        fields = '__all__'

class CombinedEmployeeDetailsSerializer(serializers.Serializer):
    general_details = EmployeeGeneralDetailsSerializer()
    other_details = EmployeeOtherDetailsSerializer(source='general_details')  # Using the source parameter to refer to the same serializer

    def to_representation(self, instance):
        return {
            'general_details': EmployeeGeneralDetailsSerializer(instance.general_details).data,
            'other_details': EmployeeOtherDetailsSerializer(instance).data
        }
