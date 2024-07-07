from django.contrib import admin
from booking.models import User, Booking, Room
# Register your models here.
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Booking)