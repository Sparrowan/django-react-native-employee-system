from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.permissions import IsAuthenticated


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class CreateEmployeeDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        general_data = request.data.get('general_details', {})
        general_serializer = EmployeeGeneralDetailsSerializer(data=general_data)
        general_data['created_by'] = request.user.id

        if general_serializer.is_valid():
            general_instance = general_serializer.save()

            other_data = request.data.get('other_details', {})
            other_data['general_details'] = general_instance.id  # Associate with EmployeeGeneralDetails

            other_serializer = EmployeeOtherDetailsSerializer(data=other_data)

            if other_serializer.is_valid():
                other_instance = other_serializer.save()
                return Response({
                    'general_details': general_serializer.data,
                    'other_details': other_serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                general_instance.delete()  # Roll back creation of EmployeeGeneralDetails if other_details failed
                return Response({'other_errors': other_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'general_errors': general_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class ListCombinedEmployeeDetailsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CombinedEmployeeDetailsSerializer

    def get_queryset(self):
        return EmployeeOtherDetails.objects.select_related('general_details').all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)