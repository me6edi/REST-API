from .models import Studnet
from .serializers import StudentSerializer
from rest_framework import viewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Studnet.objects.all()
    serializer_class = StudentSerializer



