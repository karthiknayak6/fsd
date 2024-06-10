from django.http import HttpResponse
from django.shortcuts import render

from stdcourse.models import Course, Student


# Create your views here.


def add_data(request):
    s = Student(student_name="Karthik", student_usn="075", student_sem=6 )
    s.save()
    s = Student(student_name="Preetham", student_usn="068", student_sem=6 )
    s.save()
    s = Student(student_name="Shailesh", student_usn="097", student_sem=6 )
    s.save()
    c = Course(course_code="CS62", course_name="fullstack", course_credit=4)
    c.save()
    c = Course(course_code="CS61", course_name="software", course_credit=3)
    c.save()
    c = Course(course_code="CS63", course_name="data science", course_credit=3)
    c.save()
    return HttpResponse("Data insertion success!!")

def render_form(request):
    if request.method == "GET":
        students = Student.objects.all()
        courses = Course.objects.all()
        return render(request, "form.html", {"students": students, "courses": courses})
    elif request.method == "POST":
        s = request.POST.get("sel_student")
        c = request.POST.get("sel_course")
        sel_student = Student.objects.get(student_usn=s)
        sel_course = Course.objects.get(course_code=c)
        res = sel_student.enrollment.filter(id=sel_course.id)
        if res:
            return HttpResponse("Student already registered")
        sel_student.enrollment.add(sel_course)
       
        return HttpResponse("Success")


        
        
        
