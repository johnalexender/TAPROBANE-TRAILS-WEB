from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Destination,
    Highlight,
    TripDay,
    DestinationPhoto,
    TravelService,
    Review,
    TripBooking,
    Guide,
    Vehicle,
)


# =========================================================
# DESTINATION PHOTO / GALLERY
# =========================================================

@admin.register(DestinationPhoto)
class DestinationPhotoAdmin(admin.ModelAdmin):

    list_display = (
        "thumbnail",
        "destination",
        "caption",
        "order",
    )

    list_filter = (
        "destination",
    )

    search_fields = (
        "destination__name",
        "caption",
    )

    ordering = (
        "destination",
        "order",
    )

    list_editable = (
        "order",
    )

    readonly_fields = (
        "preview",
    )

    fields = (
        "destination",
        "image",
        "preview",
        "caption",
        "order",
    )

    # -----------------------------------------------------
    # Small thumbnail in admin list
    # -----------------------------------------------------

    @admin.display(description="Photo")
    def thumbnail(self, obj):

        if obj.image:

            return format_html(
                '<img src="{}" width="100" height="70" '
                'style="object-fit:cover; border-radius:8px;" />',
                obj.image.url
            )

        return "No Image"

    # -----------------------------------------------------
    # Large image preview
    # -----------------------------------------------------

    @admin.display(description="Preview")
    def preview(self, obj):

        if obj.image:

            return format_html(
                '<img src="{}" width="500" '
                'style="max-height:350px; '
                'object-fit:cover; '
                'border-radius:12px;" />',
                obj.image.url
            )

        return "No Image"


# =========================================================
# DESTINATION
# =========================================================

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "region",
        "duration",
        "travel_type",
        "is_active",
    )

    list_filter = (
        "is_active",
        "region",
    )

    search_fields = (
        "name",
        "region",
    )


# =========================================================
# HIGHLIGHT
# =========================================================

@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):

    list_display = (
        "destination",
        "title",
        "order",
        "video",
    )

    list_filter = (
        "destination",
    )

    search_fields = (
        "title",
        "destination__name",
    )

    ordering = (
        "destination",
        "order",
    )


# =========================================================
# TRIP DAY
# =========================================================

@admin.register(TripDay)
class TripDayAdmin(admin.ModelAdmin):

    list_display = (
        "destination",
        "day_number",
        "title",
    )

    list_filter = (
        "destination",
    )

    search_fields = (
        "title",
        "destination__name",
    )

    ordering = (
        "destination",
        "day_number",
    )


# =========================================================
# TRAVEL SERVICE
# =========================================================

@admin.register(TravelService)
class TravelServiceAdmin(admin.ModelAdmin):

    list_display = (
        "destination",
        "number",
        "title",
    )

    list_filter = (
        "destination",
    )

    search_fields = (
        "title",
        "destination__name",
    )

    ordering = (
        "destination",
        "number",
    )


# =========================================================
# REVIEW
# =========================================================

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "customer_name",
        "destination",
        "country",
        "rating",
        "is_published",
    )

    list_filter = (
        "destination",
        "rating",
        "is_published",
    )

    search_fields = (
        "customer_name",
        "country",
        "review_text",
    )
# =========================================================
# TRIP BOOKING
# =========================================================

@admin.register(TripBooking)
class TripBookingAdmin(admin.ModelAdmin):

    list_display = (
        "booking_reference",
        "name",
        "destination",
        "travel_date",
        "duration",
        "adults",
        "children",
        "phone",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "destination",
        "travel_date",
        "created_at",
    )

    search_fields = (
        "booking_reference",
        "name",
        "phone",
        "email",
        "destination__name",
    )

    readonly_fields = (
        "booking_reference",
        "created_at",
        "updated_at",
    )

    ordering = (
        "-created_at",
    )

    list_editable = (
        "status",
    )

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "title",
        "location",
        "experience",
        "is_featured",
        "is_active",
    )

    list_filter = (
        "is_featured",
        "is_active",
    )

    search_fields = (
        "name",
        "location",
        "languages",
        "description",
    )

    list_editable = (
        "is_featured",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Guide Profile",
            {
                "fields": (
                    "name",
                    "title",
                    "location",
                    "experience",
                    "languages",
                    "description",
                )
            }
        ),

        (
            "Images",
            {
                "fields": (
                    "profile_image",
                    "vehicle_image",
                )
            }
        ),

        (
            "Contact",
            {
                "fields": (
                    "phone",
                    "whatsapp",
                    "email",
                )
            }
        ),

        (
            "Website Visibility",
            {
                "fields": (
                    "is_featured",
                    "is_active",
                )
            }
        ),

        (
            "System",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            }
        ),

    )
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "vehicle_type",
        "passenger_capacity",
        "luggage_capacity",
        "is_featured",
        "is_active",
        "display_order",
    )

    list_filter = (
        "vehicle_type",
        "is_featured",
        "is_active",
        "air_conditioned",
        "private_vehicle",
    )

    search_fields = (
        "name",
        "vehicle_type",
        "short_description",
        "description",
    )

    list_editable = (
        "is_featured",
        "is_active",
        "display_order",
    )

    ordering = (
        "display_order",
        "-is_featured",
        "name",
    )