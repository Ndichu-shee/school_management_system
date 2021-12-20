from django.db import models

# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    company = models.CharField(max_length=25)
    course_name = models.CharField(max_length=20)
    course = models.IntegerField()
    gender = (
        ('m','male')
        ('f','female')
    )
    email = models.EmailField()
    joining_date = models.Datefield()
    salary = models.BigIntegerField()
    city = models.CharField()
    image = models.ImageField()
    resume = models.FileField()
    contract = models.FileField()
    phone_number = models.PhoneNumberField()