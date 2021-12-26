from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=20)
    course_code = models.CharField(max_length=10)
    trainer_id =models.CharField(max_length=5)
    description = models.TextField()
    syllabus = models.FileField()
    
    def __str__(self):
        return self.course_name