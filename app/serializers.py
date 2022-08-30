from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        # fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password',)
        # ('id', 'first_name', 'last_name', 'email', 'username', 'password',)
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['first_name'], last_name=validated_data['last_name'],
                                        email=validated_data['email'], password=validated_data['password'], )
        return user


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
