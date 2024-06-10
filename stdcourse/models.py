from django.db import models

# Create your models here.

class Course(models.Model):
    course_code = models.CharField(max_length=30)
    course_name = models.CharField(max_length=30)
    course_credit = models.IntegerField()

class Student(models.Model):
    student_name = models.CharField(max_length=30)
    student_usn = models.CharField(max_length=30)
    student_sem = models.IntegerField()
    enrollment = models.ManyToManyField(Course)

