import os
import django
from django.core.exceptions import ValidationError

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import Person

try:
    invalid_person = Person(
        name="dgdfg",
        age=233
    )
    invalid_person.full_clean()
except ValidationError as e:
    print(e)
