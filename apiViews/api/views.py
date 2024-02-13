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
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudnetSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudnetSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudnetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created!'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = StudnetSerializer(stu, data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated!!'})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted!!'})
        