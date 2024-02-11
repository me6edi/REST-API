# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# Create your views here.

# @api_view()
# def hello_world(request):
#     return Response({'msg':"Hello World"})

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':"Hello World"})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':"This is post request!!"})


# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method == "GET":
#         return Response({'msg':"This is get request!!"})
#     if request.method == "POST":
#         print(request.data)
#         return Response({'msg':"This is post request!!",'data':request.data})


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudnetSerializer


"""========== Start function-based CRUD API =========="""
@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get(id)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudnetSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudnetSerializer(stu, many=True)
        return Response(serializer.data)