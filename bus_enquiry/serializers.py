from rest_framework import serializers
from .models import TransportCompany, Bus, Stop, Route, RouteStop, Schedule

class TransportCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportCompany
        fields = '__all__'

class TransportCompanySerializer1(serializers.ModelSerializer):
    class Meta:
        model = TransportCompany
        fields = ('name', 'contact_information')

class BusSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=TransportCompany.objects.all())

    class Meta:
        model = Bus
        fields = '__all__'

class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stop
        fields = '__all__'

class RouteStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteStop
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    starting_stop = serializers.PrimaryKeyRelatedField(queryset=Stop.objects.all())
    destination_stop = serializers.PrimaryKeyRelatedField(queryset=Stop.objects.all())
    stops = StopSerializer(many=True)

    class Meta:
        model = Route
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    bus = BusSerializer(read_only=True)
    route = RouteSerializer(read_only=True)
    bus_id = serializers.PrimaryKeyRelatedField(queryset=Bus.objects.all(), source='bus', write_only=True)
    route_id = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all(), source='route', write_only=True)

    class Meta:
        model = Schedule
        fields = '__all__'

    def create(self, validated_data):
        bus = validated_data.pop('bus')
        route = validated_data.pop('route')

        schedule = Schedule.objects.create(bus=bus, route=route, **validated_data)
        return schedule
