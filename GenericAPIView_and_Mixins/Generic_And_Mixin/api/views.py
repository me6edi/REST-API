# GenericAPIView and Model Mixin

from .models import Student
from .serializers import StudnetSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

class StudnetList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudnetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    
