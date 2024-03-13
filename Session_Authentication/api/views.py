from .models import Studnet
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly

# Model View Set 
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Studnet.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes  = [AllowAny]
    # permission_classes  = [IsAdminUser]
    permission_classes  = [IsAuthenticatedOrReadOnly]

