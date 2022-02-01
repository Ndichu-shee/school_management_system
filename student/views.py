
from django.http import request
from django.shortcuts import redirect, render
from .models import Student
from .forms import StudentForm
from django.views.generic.list import ListView 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import (get_list_or_404,HttpResponseRedirect)
from django.views.generic.edit import UpdateView
from trainer.models import Trainer
from course.models import Course


def home(request):
    data = []
    total_students = Student.objects.all().count()
    total_trainers =Trainer.objects.all().count() 
    total_courses = Course.objects.all().count()
    data.append([total_students,total_trainers, total_courses])
    
    return render (request, 'navbar.html', {'top_data':data})




#viewing all the students
class StudentList(ListView):
    model = Student
    template_name = 'students_list.html'

    def get_queryset(self, *args, **kwargs):
        all_students = super(StudentList, self).get_queryset(*args, **kwargs)
        return all_students
       
#registering a new student
class StudentFormView(CreateView):
    template_name = 'add_student.html'
    form_class = StudentForm
    model = Student
    success_url = reverse_lazy('student:student')

  #deleting a student
def delete_student(request, id):
    student= Student.objects.get( id = id)
   
    if request.method =="POST":
       student.delete()
       return HttpResponseRedirect("/students")
    return render(request, 'delete_student.html', {'student':student})

#editing student details
def edit_student(request, id):
    context = {}

    student= Student.objects.get( id = id)
    form =StudentForm(request.POST or None, instance = student)


    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form

    return render(request, "edit_student.html", context)

def student_profile(request, id):
    student = Student.objects.get(id=id)
    return render(request,'student_profile.html',{'student':student})


