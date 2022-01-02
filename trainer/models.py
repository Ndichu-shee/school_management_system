from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    company = models.CharField(max_length=25)
    course_name = models.CharField(max_length=20)
    course = models.IntegerField()
    email = models.EmailField()
    joining_date = models.DateField()
    salary = models.BigIntegerField()
    city = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    resume = models.FileField()
    contract = models.FileField()
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)
    gender = (
        ('m', 'male'),
        ('f', 'female')
    )

    def __str__(self):
        return self.first_name