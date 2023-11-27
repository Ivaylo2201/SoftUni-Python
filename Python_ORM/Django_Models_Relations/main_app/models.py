from datetime import date

from django.db import models


# Create your models here

class Lecturer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    lecturer = models.ForeignKey(to='Lecturer', on_delete=models.SET_NULL, null=True)  # M -> 1

    # A collection subject_set is created to every Lecturer instance - Reverse Selection
    # Contains the subjects that every Lecturer teaches

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    subjects = models.ManyToManyField(to='Subject', through='StudentEnrollment')

#   ManyToManyField creates a default junction table
#   through -> Don't use the default junction table, instead use the one I created.
#   We use through when we need to extend the junction table


# Custom junction table (Raises an error if the default M2M junction table exists)
class StudentEnrollment(models.Model):
    class Grades(models.TextChoices):
        A = 'A'
        B = 'B'
        C = 'C'
        D = 'D'
        E = 'E'
        F = 'F'

    student = models.ForeignKey(to='Student', on_delete=models.CASCADE)
    subject = models.ForeignKey(to='Subject', on_delete=models.CASCADE)
    enrollment_date = models.DateField(default=date.today)
    grade = models.CharField(max_length=1, choices=Grades.choices)


class LecturerProfile(models.Model):
    lecturer = models.OneToOneField(to='Lecturer', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    office_location = models.CharField(max_length=100, null=True, blank=True)