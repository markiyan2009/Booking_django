from django.db import models

# Create your models here.
class Room(models.Model):
    number = models.IntegerField(null=True)
    price = models.IntegerField()
    people_in = models.IntegerField(default=0)
    max_people = models.IntegerField()
    type_room = models.CharField(max_length=150)
    avaible = models.BooleanField()

    def __str__(self):
        return str(self.number)
    class Meta:
        ordering = ["avaible"]
    
class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Meta:
        ordering = ["name"]

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.start_date
    class Meta:
        ordering = ["room"]