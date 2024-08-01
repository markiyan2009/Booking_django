from django.urls import path
from booking import views

urlpatterns=[
    path("",views.index,name = "home"),
    path("rooms/",views.get_rooms,name = "rooms"),
    path("bookings/", views.get_booking, name="bookings"),
    
    path("delete_user/",views.delete_user,name="delete_user"),
    path("add_room/",views.add_room,name="add_room"),
    path("book_room", views.book_room, name="book_room"),
   
]