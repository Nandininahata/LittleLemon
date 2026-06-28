from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    menu_item_description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_time = models.DateTimeField(auto_now=False)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name