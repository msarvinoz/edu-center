from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializer import *
from django.contrib import messages


#1 task
@api_view(['POST'])
def login_page(request):
    try:
        email = request.POST.get('email')
        password = request.POST.get('password')
        registered_user = User.objects.get(password=password)
        if User.objects.filter(email=email, password=password).exists():
            if password == registered_user.password:
                messages.success(request, "You are now logged in!")
            return Response("successfully signed up")
        else:
            messages.error(request, "Invalid email or email password.")
            return Response("can not login!")
    except Exception as err:
        return Response({'error': f'{err}'})


# 2 task
@api_view(['GET'])
def students_list(request):
    try:
        student_list = Student.objects.filter(is_active=True)
        ser = StudentSerializer(student_list, many=True)
        return Response(ser.data)
    except Exception as err:
        return Response({'error': f'{err}'})


# 3 task
# crud api(modelviewset)
class StudentView(viewsets.ModelViewSet):
    serializer_class = AllStudentInfoSerializer
    queryset = Student.objects.all()

    def list(self, request):  # -------> get
        student = Student.objects.all()
        ser = AllStudentInfoSerializer(student, many=True)
        return Response(ser.data)

    def create(self, request):  # -------> post
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        registered_date = request.POST.get('registered_date')
        parent_name = request.POST.get('parent_name')
        city_address = request.POST.get('city_address')
        address = request.POST.get('address')
        birth_date = request.POST.get('birth_date')
        birth_place = request.POST.get('birth_place')
        password = request.POST.get('password')
        login_username = request.POST.get('login_username')
        parent_phone = request.POST.get('parent_phone')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        photo = request.POST.get('photo')
        group = request.POST.get('group')
        is_active = request.POST.get('is_active')
        education_place = request.POST.get('education_place')
        is_educated = request.POST.get('is_educated')
        education_started = request.POST.get('education_started')
        education_ending = request.POST.get('education_ending')
        edu_place_address = request.POST.get('edu_place_address')
        c = Student.objects.create(
            f_name=f_name,
            l_name=l_name,
            registered_date=registered_date,
            parent_name=parent_name,
            city_address=city_address,
            address=address,
            photo=photo,
            birth_date=birth_date,
            birth_place=birth_place,
            password=password,
            login_username=login_username,
            parent_phone=parent_phone,
            phone_number=phone_number,
            email=email,
            group_id=group,
            is_active=is_active,
            education_place=education_place,
            is_educated=is_educated,
            education_started=education_started,
            education_ending=education_ending,
            edu_place_address=edu_place_address,
        )
        return Response(AllStudentInfoSerializer(c).data)

    def retrieve(self, request, pk=None):  # -------> get
        student = Student.objects.get(pk=pk)
        ser = AllStudentInfoSerializer(student)
        return Response(ser.data)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

