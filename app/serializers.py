from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password',)
        # ('id', 'first_name', 'last_name', 'email', 'username', 'password',)
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True},
        }


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'companyname', 'model', 'vehicle_number', 'fueltype', 'seating_capacity', 'rent_per_day',
                  'availability']


class AvailableCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'companyname', 'model', 'vehicle_number', 'fueltype', 'seating_capacity', 'rent_per_day',
                  'availability']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['customer', 'car', 'issue_date', 'return_date']


class CarDetailReservationSerializer(serializers.Serializer):
    car = CarSerializer()
    current_active_bookings = ReservationSerializer(many=True)
