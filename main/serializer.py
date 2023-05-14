from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['address', 'photo', 'birth_date', 'birth_place', 'password', 'login_username', 'parent_phone', 'education_place', 'is_educated', 'education_started', 'education_ending', 'edu_place_address']


class AllStudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        depth=2
        model = Student
        fields = '__all__'
