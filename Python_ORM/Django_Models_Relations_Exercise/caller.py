import os
import django
from django.db.models import QuerySet
from datetime import timedelta, date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here


from main_app.models import Author, Book, Artist, Song, Product, Review, Driver, DrivingLicense, Owner, Registration, Car


# Create queries within functions

def show_all_authors_with_their_books() -> str:
    authors = Author.objects.all().order_by('id')
    data = []

    for author in authors:
        books = Book.objects.filter(author=author)

        if not books:
            continue
        else:
            data.append(f"{author.name} has written - {', '.join([book.title for book in books])}!")

    return '\n'.join(data)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(
        book__isnull=True  # Means no relation
    ).delete()


def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)


def get_songs_by_artist(artist_name: str) -> QuerySet[Song]:
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str) -> float:
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    return sum([r.rating for r in reviews]) / len(reviews)


def get_reviews_with_high_ratings(threshold: int) -> QuerySet[Review]:
    return (Review.objects
            .filter(rating__gte=threshold))


def get_products_with_no_reviews() -> QuerySet[Product]:
    return (Product.objects
            .filter(reviews__isnull=True)
            .order_by('-name'))


def delete_products_without_reviews() -> None:
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates() -> str:
    licenses = DrivingLicense.objects.order_by('-license_number')

    return '\n'.join(
        f"License with id: {lic.license_number} expires on {lic.issue_date + timedelta(days=365)}!"
        for lic in licenses
    )

def get_drivers_with_expired_licenses(due_date) -> list[Driver]:
    drivers = Driver.objects.all()
    expired_drivers = []

    for d in drivers:
        expiration_date = d.drivinglicense.issue_date + timedelta(days=365)

        if expiration_date > due_date:
            expired_drivers.append(d)

    return expired_drivers


def register_car_by_owner(owner: Owner) -> str:
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True, owner=owner).first()

    car.owner = owner
    car.registration = registration

    car.save()

    registration.registration_date = date.today()
    registration.car = car

    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."


# Create instances of the Owner model
owner1 = Owner.objects.create(name='Ivelhjghinjj Milchev')
owner2 = Owner.objects.create(name='Alijjghjghjjce Smith')

# Create instances of the Car model and associate them with owners
car1 = Car.objects.create(model='Citroenghjghjj C5', year=2004)
car2 = Car.objects.create(model='Hondajjghjj Civic', year=2021)

# Create instances of the Registration model for the cars
registration1 = Registration.objects.create(registration_number='TjXA')
registration2 = Registration.objects.create(registration_number='XZ789')

print(register_car_by_owner(owner1))
