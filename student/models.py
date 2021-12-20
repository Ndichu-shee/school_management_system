from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.PositiveSmallIntegerField()
    Nationality = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    class_name = models.CharField(max_length=20)
    nationality_id = models.CharField(max_length=15)
    email = models.EmailField()
    admission_date = models.DateField()
    academic_year = models.ImageField()
    image = models.ImageField()
    guardians_contact = models.PhoneNumberField()
    student_contact = models.PhoneNumberField()
    room = models.CharField(max_length=20)
    gender = (
        ('m', 'male'),
        ('f', 'female')
    )

