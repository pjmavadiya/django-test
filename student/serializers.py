from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 's_id', 'first_name', 'last_name', 'school', 'age', 'nationality']
        extra_kwargs = {
            's_id': {'required': False},
            's_id': {'read_only': True},
        }
        
    def validate(self, data):
        """
        Check for the max student in call before creating an objct
        """
        school = data['school']
        print (Student.objects.filter(school=school).count())
        print (school.max_student)
        if Student.objects.filter(school=school).count() >= school.max_student:
            raise serializers.ValidationError("This school is full.")
        return data
        
        
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'max_student', 'state', 'city']




