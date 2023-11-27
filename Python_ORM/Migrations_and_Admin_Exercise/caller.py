import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Shoe

# Getting the brand of the Shoes and converting the QuerySet to
print(Shoe.objects.values_list('brand', flat=True).distinct())
