import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import Student

# Returns all records from the students table
print(Student.objects.all)

# Prints only the first records from the students table
print(Student.objects.first())

# Gets the student with id of 0001 and prints it
# print(Student.objects.get(student_id='0001'))

# Adds a record to the database
# Student.objects.create(first_name='name', last_name='name')

# Returns a QuerySet of all objects that have a first_name = name
print(Student.objects.filter(first_name='name'))

# Returns a QuerySet of all objects that DO NOT have a first_name = name
print(Student.objects.exclude(first_name='name'))

# order_by('<attribute>') - Sort by that attribute by asc order
# order_by('-<attribute>') - Sort by that attribute by desc order
print(Student.objects.all().order_by('-first_name'))
print(Student.objects.all().order_by('birth_date'))


def add_students() -> None:
    Student.objects.create(
        student_id='FC5204', first_name='John', last_name='Doe',
        birth_date='1995-05-15', email='john.doe@university.com'
    )

    Student.objects.create(
        student_id='FE0054', first_name='Jane', last_name='Smith',
        birth_date=None, email='jane.smith@university.com'
    )

    Student.objects.create(
        student_id='FH2014', first_name='Alice', last_name='Johnson',
        birth_date='1998-02-10', email='alice.johnson@university.com'
    )

    Student.objects.create(
        student_id='FH2015', first_name='Bob', last_name='Wilson',
        birth_date='1996-11-25', email='bob.wilson@university.com'
    )


def get_students_info() -> str:
    return '\n'.join([
        f"Student №{student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}"
        for student in Student.objects.all()
    ])


def update_students_emails() -> None:
    for student in Student.objects.all():
        new_email = student.email.replace('university.com', 'uni-students.com')
        student.email = new_email
        student.save()


def truncate_students() -> None:
    Student.objects.all().delete()
