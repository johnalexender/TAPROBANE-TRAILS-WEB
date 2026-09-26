from django.db import models

# Create your models here.
class Destination(models.Model):

    name = models.CharField(max_length=100, unique=True)

    region = models.CharField(max_length=150)

    description = models.TextField()

    intro = models.TextField()

    duration = models.CharField(
        max_length=100,
        blank=True
    )

    travel_type = models.CharField(
        max_length=100,
        blank=True
    )

    best_for = models.CharField(
        max_length=200,
        blank=True
    )

    hero_image = models.ImageField(
        upload_to="destinations/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Highlight(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="highlights"
    )

    title = models.CharField(max_length=200)

    video = models.FileField(
        upload_to="highlights/videos/",
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["destination", "order"]

    def __str__(self):
        return self.title

class TripDay(models.Model):

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="trip_days"
    )

    day_number = models.PositiveIntegerField()

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    class Meta:
        ordering = ["day_number"]

    def __str__(self):
        return f"{self.destination.name} - Day {self.day_number}"

class DestinationPhoto(models.Model):

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="photos"
    )

    image = models.ImageField(
        upload_to="destinations/gallery/"
    )

    caption = models.CharField(
        max_length=200,
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.destination.name} Photo"


class TravelService(models.Model):

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="services"
    )

    number = models.PositiveIntegerField(
        default=1
    )

    title = models.CharField(
        max_length=150
    )

    description = models.TextField()

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return f"{self.destination.name} - {self.title}"


class Review(models.Model):

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    customer_name = models.CharField(
        max_length=100
    )

    country = models.CharField(
        max_length=100,
        blank=True
    )

    rating = models.PositiveIntegerField(
        default=5
    )

    review_text = models.TextField()

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.customer_name} - {self.destination.name}"

class TripBooking(models.Model):

    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    booking_reference = models.CharField(
        max_length=30,
        unique=True
    )

    name = models.CharField(
        max_length=150
    )

    phone = models.CharField(
        max_length=30
    )

    email = models.EmailField(
        blank=True
    )

    vehicle = models.CharField(
        max_length=100,
        default="Private Van"
    )

    destination = models.ForeignKey(
        Destination,
        on_delete=models.PROTECT,
        related_name="trip_bookings"
    )

    places = models.TextField(
        blank=True
    )

    duration = models.PositiveIntegerField()

    travel_date = models.DateField()

    end_date = models.DateField(
    null=True,
    blank=True
    )
    pickup = models.CharField(
        max_length=255
    )

    dropoff = models.CharField(
        max_length=255,
        blank=True
    )

    adults = models.PositiveIntegerField(
        default=1
    )

    children = models.PositiveIntegerField(
        default=0
    )

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.booking_reference} - {self.name}"

class Guide(models.Model):

    name = models.CharField(
        max_length=150
    )

    title = models.CharField(
        max_length=150,
        default="Private Driver & Local Guide"
    )

    location = models.CharField(
        max_length=150,
        blank=True
    )

    experience = models.CharField(
        max_length=100,
        blank=True
    )

    languages = models.CharField(
        max_length=200,
        blank=True
    )

    description = models.TextField()

    profile_image = models.ImageField(
        upload_to="guides/profiles/",
        blank=True,
        null=True
    )

    vehicle_image = models.ImageField(
        upload_to="guides/vehicles/",
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    whatsapp = models.CharField(
        max_length=50,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-is_featured", "name"]

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ("car", "Car"),
        ("van", "Van"),
        ("suv", "SUV"),
        ("minivan", "Mini Van"),
    ]

    name = models.CharField(max_length=150)
    vehicle_type = models.CharField(
        max_length=30,
        choices=VEHICLE_TYPES,
        default="car"
    )

    image = models.ImageField(
        upload_to="vehicles/"
    )

    short_description = models.CharField(
        max_length=250,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    passenger_capacity = models.PositiveIntegerField(
        default=3
    )

    luggage_capacity = models.PositiveIntegerField(
        default=2
    )

    air_conditioned = models.BooleanField(
        default=True
    )

    comfortable = models.BooleanField(
        default=True
    )

    private_vehicle = models.BooleanField(
        default=True
    )

    price_note = models.CharField(
        max_length=150,
        blank=True,
        help_text="Example: Starting from USD 45/day"
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["display_order", "-is_featured", "name"]
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __str__(self):
        return self.name