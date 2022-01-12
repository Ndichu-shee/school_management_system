from rest_framework import serializers
from student.models import Student
from course.models import Course
from trainer.views import Trainer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name','last_name','age','nationality','date_of_birth','class_name','nationality_id','email','admission_date','academic_year','guardians_contact','student_contact','room')

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ('first_name','second_name','company','course_name','course','email','joining_date','salary','city','image','resume','contract','phone_number')
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_name','course_code','trainer_id','description','syllabus')