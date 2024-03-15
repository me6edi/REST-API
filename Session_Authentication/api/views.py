from .models import Studnet
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .Custompermission import Mypermission 
# Model View Set 
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Studnet.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes  = [AllowAny]
    # permission_classes  = [IsAdminUser]
    # permission_classes  = [IsAuthenticatedOrReadOnly]
    # permission_classes  = [DjangoModelPermissions]
    # permission_classes  = [DjangoModelPermissionsOrAnonReadOnly]




# Custom Permission 
    permission_classes = [Mypermission]


