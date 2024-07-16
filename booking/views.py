from django.shortcuts import render, redirect
from booking.models import User, Room, Booking 
from django.http import HttpResponse
# Create your views here.
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
        user = User(name = name, email=email,password=password)
        user.save()

        return redirect("rooms")
    else:
        return render(request, template_name='booking/register_user.html')
    
def delete_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(email=email).first()
        user.delete()

        return redirect("rooms")
    else:
        return render(request,template_name="booking/delete_user.html")

def add_room(request):
    if request.method == "POST":
        number = request.POST.get("number")
        price = request.POST.get("price")
        people_in = request.POST.get("people_in")
        type_room = request.POST.get("type_room")
        avaible = request.POST.get("avaible")
        print(avaible)
        if avaible == "on":
            avaible = True
        else:
            avaible=False
        room = Room(number=number,price=price,people_in=people_in,type_room=type_room,avaible=avaible)
        room.save()
        return redirect("rooms")
    else:
        return render(request,template_name="booking/add_room.html")