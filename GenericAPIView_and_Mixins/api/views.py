# GenericAPIView and Model Mixin

from .models import Studnet
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Studnet.objects.all()
#     serializer_class = StudentSerializer


#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Studnet.objects.all()
#     serializer_class = StudentSerializer


#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    


# class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
#     queryset = Studnet.objects.all()
#     serializer_class = StudentSerializer


#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
# class StudentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Studnet.objects.all()
#     serializer_class = StudentSerializer


#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    

# class StudentDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = Studnet.objects.all()
#     serializer_class = StudentSerializer


#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)







# List and Create - PK Not Required


class LCStudentListAPI(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset = Studnet.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



# Retrieve Updae and Destroy - PK required
    

class RUDStudentAPI(GenericAPIView, UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset = Studnet.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)