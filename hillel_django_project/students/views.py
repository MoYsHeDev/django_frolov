from django.http import HttpResponse
from faker import Faker

from .models import Student


def make_student():
    """Generate student and added him in DataBase"""
    fake = Faker()
    student = Student.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(),
                                     age=fake.random_int(16, 45))
    return student


def home(request) -> HttpResponse:
    return HttpResponse('<h1 align=center>Welcome to "Hillel Homework Django Project"</h1>'
                        '<p align=center>by Michail Frolov</p>')


def generate_student(request) -> str:
    student = make_student()
    output = ''.join(f"<p>Created 1 student with id: {student.id}</p>"
                     f"<p>{student.first_name} {student.last_name}, {student.age};</p>")
    return HttpResponse(output)
