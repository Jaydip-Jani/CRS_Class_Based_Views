from rest_framework.response import Response
from .serializers import *
from rest_framework import mixins, status
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated, AllowAny


class RegisterCustomerDetails(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateCustomer(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteCustomer(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (DjangoModelPermissions,)

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

    def update(self, request, id):
        user = self.get_object()
        serializers = self.get_serializer(user, data=request.data, partial=True)
        serializers.is_valid(raise_exception=True)
        self.perform_update(serializers)
        return Response(serializers.data)


class DeleteCar(mixins.ListModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (DjangoModelPermissions,)
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def delete_car(self, request, id):
        user = self.get_object()
        serializers = self.get_serializer(user, data=request.data, partial=True)
        serializers.is_valid(raise_exception=True)
        self.delete(serializers)
        return Response(serializers.data)
