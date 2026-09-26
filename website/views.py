
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.utils import timezone

from urllib.parse import quote

from .models import Destination, TripBooking ,Guide , Vehicle

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def gallery(request):
    return render(request, "gallery.html")


def vehicles(request):
    vehicle_list = Vehicle.objects.filter(
        is_active=True
    ).order_by(
        "display_order",
        "-is_featured",
        "name"
    )

    return render(
        request,
        "vehicle.html",
        {
            "vehicles": vehicle_list
        }
    )

def guide(request):
    return render(request, "guide.html")

def planner(request):
    return render(request, "planner.html")

def planner_success(request):
    return render(request, "planner_success.html")

def services(request):
    return render(request, "services.html")


def services(request):

    destination_name = request.GET.get(
        "destination"
    )

    destination = get_object_or_404(
        Destination,
        name__iexact=destination_name,
        is_active=True
    )

    return render(
        request,
        "services.html",
        {
            "destination": destination
        }
    )

def planner(request):

    # =====================================================
    # GET SELECTED VEHICLE FROM URL
    # Example:
    # /planner/?vehicle=3
    # =====================================================

    vehicle_id = request.GET.get("vehicle")

    selected_vehicle = None

    if vehicle_id:

        selected_vehicle = get_object_or_404(
            Vehicle,
            id=vehicle_id,
            is_active=True
        )


    # =====================================================
    # POST - CREATE BOOKING
    # =====================================================

    if request.method == "POST":

        name = request.POST.get(
            "name",
            ""
        ).strip()

        phone = request.POST.get(
            "phone",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip()


        # -------------------------------------------------
        # VEHICLE
        # -------------------------------------------------

        vehicle_id = request.POST.get("vehicle")

        selected_vehicle = get_object_or_404(
            Vehicle,
            id=vehicle_id,
            is_active=True
        )


        # -------------------------------------------------
        # DESTINATION
        # -------------------------------------------------

        destination_id = request.POST.get(
            "destination"
        )

        destination = get_object_or_404(
            Destination,
            id=destination_id,
            is_active=True
        )


        # -------------------------------------------------
        # OTHER FORM DATA
        # -------------------------------------------------

        places = request.POST.get(
            "places",
            ""
        ).strip()

        duration = request.POST.get(
            "duration"
        )

        travel_date = request.POST.get(
            "travel_date"
        )

        end_date = request.POST.get(
            "end_date"
        )

        pickup = request.POST.get(
            "pickup",
            ""
        ).strip()

        dropoff = request.POST.get(
            "dropoff",
            ""
        ).strip()

        adults = request.POST.get(
            "adults",
            "1"
        )

        children = request.POST.get(
            "children",
            "0"
        )

        message = request.POST.get(
            "message",
            ""
        ).strip()


        # =================================================
        # BOOKING REFERENCE
        # =================================================

        timestamp = timezone.now().strftime(
            "%Y%m%d%H%M%S"
        )

        booking_reference = f"EL-{timestamp}"


        # =================================================
        # SAVE BOOKING
        # =================================================

        booking = TripBooking.objects.create(

            booking_reference=booking_reference,

            name=name,

            phone=phone,

            email=email,

            # Save vehicle NAME to your existing database
            vehicle=selected_vehicle.name,

            destination=destination,

            places=places,

            duration=int(duration),

            travel_date=travel_date,

            end_date=end_date,

            pickup=pickup,

            dropoff=dropoff,

            adults=int(adults),

            children=int(children),

            message=message,
        )


        # =================================================
        # WHATSAPP MESSAGE
        # =================================================

        whatsapp_message = f"""
Hello Explore Lanka,

I would like to plan a private journey.

BOOKING REQUEST
----------------------------

Booking Reference:
{booking.booking_reference}

Name:
{name}

WhatsApp:
{phone}

Email:
{email or "Not provided"}

Vehicle:
{selected_vehicle.name}

Destination:
{destination.name}

Region:
{destination.region}

Trip Duration:
{duration} Days

Start Date:
{travel_date}

End Date:
{end_date}

Pickup:
{pickup}

Drop-off:
{dropoff or "Not specified"}

Travellers:
{adults} Adults
{children} Children

Places I would like to visit:
{places or "Not specified"}

Special Requests:
{message or "None"}

Thank you.
""".strip()


        encoded_message = quote(
            whatsapp_message
        )


        owner_whatsapp = getattr(
            settings,
            "OWNER_WHATSAPP",
            "947XXXXXXXX"
        )


        whatsapp_url = (
            f"https://wa.me/"
            f"{owner_whatsapp}"
            f"?text={encoded_message}"
        )


        return render(
            request,
            "planner_success.html",
            {
                "booking": booking,
                "whatsapp_url": whatsapp_url,
            }
        )


    # =====================================================
    # GET - LOAD PLANNER DATA
    # =====================================================

    destinations = Destination.objects.filter(
        is_active=True
    ).order_by("name")


    vehicles = Vehicle.objects.filter(
        is_active=True
    ).order_by(
        "display_order",
        "-is_featured",
        "name"
    )


    # =====================================================
    # MOVE SELECTED VEHICLE TO FIRST POSITION
    # =====================================================

    if selected_vehicle:

        vehicles = list(vehicles)

        vehicles = [
            selected_vehicle
        ] + [
            vehicle
            for vehicle in vehicles
            if vehicle.id != selected_vehicle.id
        ]


    # =====================================================
    # CONTEXT
    # =====================================================

    context = {

        "destinations": destinations,

        "vehicles": vehicles,

        "selected_vehicle": selected_vehicle,

        "durations": range(1, 15),

        "adult_numbers": range(1, 7),

        "child_numbers": range(0, 7),

    }


    return render(
        request,
        "planner.html",
        context
    )

def guides(request):

    guide_list = Guide.objects.filter(
        is_active=True
    ).order_by(
        "-is_featured",
        "name"
    )

    return render(
        request,
        "guides.html",
        {
            "guides": guide_list
        }
    )


def guide_detail(request, guide_id):

    guide = get_object_or_404(
        Guide,
        id=guide_id,
        is_active=True
    )

    return render(
        request,
        "guide_detail.html",
        {
            "guide": guide
        }
    )