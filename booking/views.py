from django.shortcuts import render, redirect
from booking.models import  Room, Booking 
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from hotel_system import settings
from django.contrib.auth import get_user_model
# Create your views here
def index(request):
    return render(request, template_name="booking/index.html")
def get_rooms(request):
    rooms = Room.objects.all()
    context = {
        "rooms" : rooms
    }

    return render(request, template_name="booking/rooms.html", context = context)

def get_booking(request):
    bookings = Booking.objects.all()
    context = {
        "bookings" : bookings,
    }

    return render(request,template_name="booking/bookings.html", context=context)

def add_user(request):
    if request.method == "POST":
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = settings.AUTH_USER_MODEL(name = name, email=email,password=password)
        user.save()

        return redirect("rooms")
    else:
        return render(request, template_name='booking/register_user.html')
    
def delete_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user = get_user_model().objects.filter(username=username).first()
        if user is not None:
            user.delete()

            return redirect("rooms")
        else:
            messages.error(request,message="User not found")
    else:
        return render(request,template_name="booking/delete_user.html")

def add_room(request):
    if request.method == "POST":
        number = request.POST.get("number")
        price = request.POST.get("price")
        people_in = request.POST.get("people_in")
        max_people = request.POST.get("max_people")
        type_room = request.POST.get("type_room")
        avaible = request.POST.get("avaible")
        print(avaible)
        if avaible == "on":
            avaible = True
        else:
            avaible=False
        room = Room(number=number,price=price,people_in=people_in,type_room=type_room,avaible=avaible,max_people=max_people)
        room.save()
        return redirect("rooms")
    else:
        return render(request,template_name="booking/add_room.html")
def book_room(request):
    if request.method == "POST":
        room = Room.objects.filter(number = request.POST.get("room_number")).first()
        user = get_user_model().objects.filter(email = request.POST.get("email_user")).first()

        start_date = request.POST.get("start_date")
        print(start_date)
        start_date_processing = start_date.replace('T', '-').replace(':', '-').split('-')
        start_date_processing = [int(v) for v in start_date_processing]
        start_date = datetime(*start_date_processing)

        end_date = request.POST.get("end_date")
        print(end_date)
        end_date_processing = end_date.replace('T', '-').replace(':', '-').split('-')
        end_date_processing = [int(v) for v in end_date_processing]
        end_date = datetime(*end_date_processing)
        
        booking = Booking(room = room, start_date=start_date, end_date=end_date)
        
        booking.save()
        booking.user.add(user)


        return redirect("rooms")
    else:
        return render(request, template_name="booking/book_room.html")

def get_room(request, room_number):
    room = Room.objects.filter(number = room_number).first()
    return render(
        request,
        template_name="booking/room.html",
        context={"room":room}
    )