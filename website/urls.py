from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("gallery/", views.gallery, name="gallery"),
    path("vehicles/", views.vehicles, name="vehicles"),
    path("guides/",views.guides,name="guides"),
    path("guides/<int:guide_id>/",views.guide_detail,name="guide_detail"),
    path("planner/", views.planner, name="planner"),
    path("planner/success/", views.planner_success, name="planner_success"),
]