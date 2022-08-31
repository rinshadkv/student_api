from django.shortcuts import render

# Create your views here.
from urllib import request
from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Student
from api.serializers import ApiSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
# from rest_framework import permissions
# Create your views here.


@csrf_exempt
@api_view(["GET"])
def view_student(request):
   
    if request.method=="GET":
        student=Student.objects.all()
        student_serlizer=ApiSerializer(student,many='True')
    
        return JsonResponse(student_serlizer.data,safe=False)


@api_view(["POST"])
def add_student(request):
   if request.method=="POST":
        studentdata = JSONParser().parse(request)
        serializer = ApiSerializer(data=studentdata)
        if serializer.is_valid():
            serializer.save()

        return JsonResponse('Data inserted Successfully..!',safe=False)




@api_view(["PUT"])
def update_student(request):
    if request.method=="PUT":
        studentdata = JSONParser().parse(request)
        student = Student.objects.get(id=studentdata['id'])
        student_serializer = ApiSerializer(student,studentdata)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse('Data updated Successfully..!',safe=False)
    return JsonResponse('Failed to update..!',safe=False)

@api_view(["DELETE"])
def delete_student(request):
    if request.method=='DELETE':
        student = Student.objects.get(id=id)
        student.delete()
        return JsonResponse('Data deleted Successfully..!',safe=False)



