from django.urls import path
from .models import Course
from .views import CoursesFormView, CoursesList, delete_course, edit_course, view_course
app_name = "course"
urlpatterns = [
    path('', CoursesList.as_view(),name ="course"),
    path ('add_course', CoursesFormView.as_view(),name='add_course'),
    path('<id>/delete',delete_course, name='delete_student'),
    path('<id>/edit',edit_course, name='edit_course'),
    path('<id>/view',view_course, name='view_profile' )
]