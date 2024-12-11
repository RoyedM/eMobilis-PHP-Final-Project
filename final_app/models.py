from django.db import models

# Create your models here.
class Seat (models.Model):
    """Bookings table"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateField()
    people = models.CharField(max_length=4)
    time = models.CharField(max_length=20)
    travel_class = models.CharField(max_length=20)
    route = models.CharField(max_length=20)
    message = models.TextField()

    # To return the values in human readable format
    def __str__(self):
        return self.name