from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Course(models.Model):
    courses = models.CharField(max_length=255)


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    group_type = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_type


class Student(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    registered_date = models.DateField(auto_now_add=True)
    parent_name = models.CharField(max_length=255)
    city_address = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='students/')
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=255)
    password = models.CharField(max_length=16)
    login_username = models.CharField(max_length=255)
    parent_phone = models.CharField(max_length=14)
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    education_place = models.CharField(max_length=255)
    is_educated = models.BooleanField(default=False)
    education_started = models.DateField()
    education_ending = models.DateField()
    edu_place_address = models.CharField(max_length=255)

