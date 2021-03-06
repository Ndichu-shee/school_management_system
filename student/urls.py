from django.urls import path
from . import views
from .views import StudentList, StudentFormView, delete_student, edit_student, student_profile,home
app_name = "student"

urlpatterns = [
    path('', home, name='home'),
    path('students',StudentList.as_view() , name='student'),
    path('add_student/',StudentFormView.as_view(), name='add_students'),
    path('<id>/delete',delete_student,name='delete_student'),
    path('<id>/edit',edit_student,name='edit_student'),
    path('<id>/view',student_profile, name='student_profile'),

]
