from .models import Studnet
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveAPIView, UpdateAPIView, DestroyAPIView

class studentList(ListAPIView):
    queryset = Studnet.objects.all()
    serializer_class = StudentSerializer
    throttle_scope = 'viewstu' 

class studentCreate(CreateAPIView):
    queryset = Studnet.objects.all()
    serializer_class = StudentSerializer

class studentRetrieve(RetrieveAPIView):
    queryset = Studnet.objects.all()
    serializer_class = StudentSerializer
    throttle_scope = 'viewstu' 

class studentUpdate(UpdateAPIView):
    queryset = Studnet.objects.all()
    serializer_class = StudentSerializer
    throttle_scope = 'modifystu' 

class DestroyApiview(DestroyAPIView):
    queryset = Studnet.objects.all()
    serializer_class = StudentSerializer
    throttle_scope = 'modifystu'