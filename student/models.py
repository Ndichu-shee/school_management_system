from django.db import models
from django.db.models.fields import CharField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
GENDERS_CHOICES= (
        ("m", "male"),
        ("f", "female")
    )
class Student(models.Model):
    
    first_name = models.CharField(max_length=15,help_text="Stores first name of student")
    last_name = models.CharField(max_length=15)
    age = models.PositiveSmallIntegerField()
    nationality = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    class_name = models.CharField(max_length=20)
    nationality_id = models.CharField(max_length=15)
    email = models.EmailField()
    admission_date = models.DateField()
    academic_year = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    guardians_contact = PhoneNumberField(unique = True, null = False, blank = False)
    student_contact = PhoneNumberField(unique = True, null = False, blank = False)
    room = models.CharField(max_length=20)
    gender =models.CharField(max_length=10,choices=GENDERS_CHOICES,default='female')
  
    

    def __str__(self):
        return self.first_name

