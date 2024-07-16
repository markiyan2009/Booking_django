from django.urls import path
from booking import views

urlpatterns=[
    path("rooms/",views.get_rooms,name = "rooms"),
    path("bookings/", views.get_booking, name="booking"),
    path("register/",views.add_user,name="register_user"),
    path("delete_user/",views.delete_user,name="delete_user"),
    path("add_room/",views.add_room,name="add_room"),
]