from django.db import models
from django.db.models import QuerySet


class ProductManager(models.Manager):
    def available_products(self) -> QuerySet:
        return self.filter(is_available=True)

    # We use __name on category because it's a fk -> we get it's name from the main category model
    def available_products_in_category(self, category_name: str) -> QuerySet:
        return self.filter(
            is_available=True,
            category__name=category_name
        )


