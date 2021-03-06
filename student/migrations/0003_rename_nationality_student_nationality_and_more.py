# Generated by Django 4.0 on 2021-12-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Nationality',
            new_name='nationality',
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default='female', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='academic_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
