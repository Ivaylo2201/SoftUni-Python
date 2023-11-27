# Generated by Django 4.2.4 on 2023-10-23 15:37

from django.db import migrations


def create_unique_brands(apps, schema_editor) -> None:
    # Schema editor is required by RunPython but not here
    shoe = apps.get_model('main_app', 'Shoe')
    unique_brands = apps.get_model('main_app', 'UniqueBrands')

    # Getting the brand of all shoes [("brand1",), ("brand2",)]
    # Flat = True -> ["brand1", "brand2"] (Multidimensional list -> One dimensional list)
    # distinct() -> Getting unique elements only
    unique_brand_names = shoe.objects.values_list('brand', flat=True).distinct()

    # Creates a bunch of instances of UniqueBrands
    unique_brands_to_create = [
        unique_brands(brand_name=brand_name) for brand_name in unique_brand_names
    ]
    # Saves all instances at once instead of saving them one by one
    unique_brands.objects.bulk_create(unique_brands_to_create)


# It's a good practise to have a reverse function
def delete_unique_brands(apps, schema_editor) -> None:
    unique_brands = apps.get_model('main_app', 'UniqueBrands')

    # Same as TRUNCATE TABLE
    unique_brands.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0002_uniquebrands'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands, reverse_code=delete_unique_brands)
    ]
