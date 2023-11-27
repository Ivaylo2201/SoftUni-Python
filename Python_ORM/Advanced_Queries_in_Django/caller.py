import os
import django
from django.db.models import Sum, Q, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct


def product_quantity_ordered() -> str:
    # SELECT SUM(orderproduct__quantity) AS total_ordered_quantity FROM ... GROUP BY product.name
    # annotate() = aggregation
    total_quantity_ordered_products = (
        Product.objects.annotate(
            total_ordered_quantity=Sum('orderproduct__quantity')
        ).exclude(total_ordered_quantity=None).order_by('-total_ordered_quantity')
    )

    return '\n'.join([
        f"Quantity ordered of {product.name}: {product.total_ordered_quantity}" for product in total_quantity_ordered_products
    ])

def ordered_products_per_customer() -> str:
    orders = Order.objects.all().order_by('id')
    result = []

    # M2M -> prefetch_related
    # O2M -> select_related

    for order in orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")
        for product in order.products.all():
            result.append(f"- Product: {product.name}, Category: {product.category.name}")

    return '\n'.join(result)


def filter_products() -> str:
    # We use the Q object to create OR queries (filter is always AND)
    query = Q(is_available=True) & Q(price__gt=3.00)
    products = Product.objects.filter(query)

    return '\n'.join([f"{p.name}: {p.price}lv" for p in products])

def give_discount() -> str:
    reduction = F('price') * 0.7  # Otkude go vzima?
    query = Q(is_available=True) & Q(price__gt=3)

    Product.objects.filter(query).update(price=reduction)

    return '\n'.join([f"{p.name}: {p.price}lv." for p in Product.objects.filter(is_available=True).order_by('-price', 'name')])
