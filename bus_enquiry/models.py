from django.db import models

class TransportCompany(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)

class Bus(models.Model):
    number = models.CharField(max_length=20)
    model = models.CharField(max_length=100)
    capacity = models.IntegerField()
    company = models.ForeignKey(TransportCompany, on_delete=models.CASCADE)

class Stop(models.Model):
    name = models.CharField(max_length=100)
    # Add any additional fields for the stop

class Route(models.Model):
    starting_stop = models.ForeignKey(Stop, related_name='starting_routes', on_delete=models.CASCADE)
    destination_stop = models.ForeignKey(Stop, related_name='destination_routes', on_delete=models.CASCADE)
    stops = models.ManyToManyField(Stop, through='RouteStop')
    # Add any additional fields for the route

class RouteStop(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)

class Schedule(models.Model):
    TIME_CHOICES = (
    ('12:00 AM', '12:00 AM'),
    ('01:00 AM', '01:00 AM'),
    ('02:00 AM', '02:00 AM'),
    ('03:00 AM', '03:00 AM'),
    ('04:00 AM', '04:00 AM'),
    ('05:00 AM', '05:00 AM'),
    ('06:00 AM', '06:00 AM'),
    ('07:00 AM', '07:00 AM'),
    ('08:00 AM', '08:00 AM'),
    ('09:00 AM', '09:00 AM'),
    ('10:00 AM', '10:00 AM'),
    ('11:00 AM', '11:00 AM'),
    ('12:00 PM', '12:00 PM'),
    ('01:00 PM', '01:00 PM'),
    ('02:00 PM', '02:00 PM'),
    ('03:00 PM', '03:00 PM'),
    ('04:00 PM', '04:00 PM'),
    ('05:00 PM', '05:00 PM'),
    ('06:00 PM', '06:00 PM'),
    ('07:00 PM', '07:00 PM'),
    ('08:00 PM', '08:00 PM'),
    ('09:00 PM', '09:00 PM'),
    ('10:00 PM', '10:00 PM'),
    ('11:00 PM', '11:00 PM'),
)


    arrival_time = models.CharField(max_length=10, choices=TIME_CHOICES)
    departure_time = models.CharField(max_length=10, choices=TIME_CHOICES)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

