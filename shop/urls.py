from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="aboutus"),
    path("contact/", views.contact, name="contactus"),
    path("tracker/", views.tracker, name="trackingstatus"),
    path("search/", views.search, name="search"),
    path("products/<int:id>", views.productview, name="product"),
    path("checkout/", views.checkout, name="checkout"),
    path("basic/", views.basic, name="basic"),
]
