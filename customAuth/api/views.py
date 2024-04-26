from .models import Studnet
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.customAuth import CustomAuthentication
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Studnet.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]




