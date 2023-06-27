from rest_framework import viewsets, pagination
from .models import TransportCompany, Bus, Stop, Route, Schedule, RouteStop
from .serializers import (
    TransportCompanySerializer,
    BusSerializer,
    StopSerializer,
    RouteSerializer,
    ScheduleSerializer,
    RouteStopSerializer,
    TransportCompanySerializer1,
)

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class TransportCompanyViewSet(viewsets.ModelViewSet):
    queryset = TransportCompany.objects.all()
    serializer_class = TransportCompanySerializer
    pagination_class = CustomPagination

class TransportCompanyViewSet1(viewsets.ModelViewSet):
    queryset = TransportCompany.objects.all()
    serializer_class = TransportCompanySerializer1
    pagination_class = CustomPagination

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    pagination_class = CustomPagination

class StopViewSet(viewsets.ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
    pagination_class = CustomPagination

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    pagination_class = CustomPagination

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    pagination_class = CustomPagination
    

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get the search parameters from query parameters
        arrival_time = self.request.query_params.get('arrival_time')
        departure_time = self.request.query_params.get('departure_time')

        # Apply filtering based on arrival time and/or departure time
        if arrival_time:
            queryset = queryset.filter(arrival_time__icontains=arrival_time)

        if departure_time:
            queryset = queryset.filter(departure_time__icontains=departure_time)

        return queryset

class RouteStopViewSet(viewsets.ModelViewSet):
    queryset = RouteStop.objects.all()
    serializer_class = RouteStopSerializer
    pagination_class = CustomPagination
