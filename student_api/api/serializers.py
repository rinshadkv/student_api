from rest_framework import serializers  
from api.models import *

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','name','email','username','password')
