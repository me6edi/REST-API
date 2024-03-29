from .models import Studnet
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

# Model View Set 
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Studnet.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]


    # permission_classes = [IsAuthenticated]
    # permission_classes  = [AllowAny]


    permission_classes  = [IsAdminUser]

