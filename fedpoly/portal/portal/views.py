from django.shortcuts import render
from headlines.models import Headline
from teachers.models import Teacher
from course.models import Course
from library.models import Book



def index(request):
    Content = Headline.objects.all()
    return render(request, 'index.html', {'Content': Content})

def blog(request):
    books = Book.objects.all()
    teachers = Teacher.objects.all()
    courses = Course.objects.all()

    return render(request, 'blog.html', {'Books': books, 'Teachers': teachers, 'Courses': courses})
