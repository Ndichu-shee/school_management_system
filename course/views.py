from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy 
from django.views.generic.list import ListView
from .models import Course
from django.views.generic import CreateView
from .forms import CourseForm

# Create your views here.

class CoursesList(ListView):
    model = Course
    template_name = 'courses_list.html'

    def get_queryset(self, *args, **kwargs):
        all_courses = super(CoursesList, self).get_queryset(*args, **kwargs)
        return all_courses
       
class CoursesFormView(CreateView):
    form_class = CourseForm
    model = Course
    template_name = 'add_course.html'
    success_url = reverse_lazy('course:course')

def delete_course(request, id):
    course = Course.objects.get(id =id)

    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect('/courses/')
        
    return render(request,'delete_course.html',{'course': course})

def edit_course(request, id):
    context = {}

    course= Course.objects.get( id = id)
    form =CourseForm(request.POST or None, instance = course)


    if form.is_valid():
        form.save()
        return redirect("/courses/")
    context["form"] = form

    return render(request, "edit_course.html", context)

def view_course(request, id):
    course = Course.objects.get(id =id)
    return render (request, 'view_profile.html', {'course': course})




