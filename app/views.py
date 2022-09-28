from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response
from .serializers import *
from rest_framework import mixins, status, generics
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .utils import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class Registration(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = Customer.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        # relativeLink = reverse('user:email-verify')
        absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
        email_body = 'Hi ' + user.username + ' Use link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}
        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass


class CustomerList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerRegisterSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UpdateCustomer(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerRegisterSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteCustomer(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerRegisterSerializer
    permission_classes = (DjangoModelPermissions,)
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CreateCar(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (DjangoModelPermissions,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CarList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UpdateCar(mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (DjangoModelPermissions,)
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteCar(mixins.ListModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (DjangoModelPermissions,)
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CarReservation(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CarReservationList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UpdateCarReservation(mixins.ListModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (DjangoModelPermissions,)
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteCarReservation(mixins.ListModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (DjangoModelPermissions,)
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
