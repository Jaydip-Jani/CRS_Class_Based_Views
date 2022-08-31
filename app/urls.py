from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )
from rest_framework_simplejwt.views import TokenVerifyView
from .views import *

urlpatterns = [
    path('registercustomer/', RegisterCustomerDetails.as_view()),
    path('customerlist/', CustomerList.as_view()),
    path('updatecustomer/<int:id>/', UpdateCustomer.as_view()),
    path('deletecustomer/<int:id>/', DeleteCustomer.as_view()),
    path('login/', TokenObtainPairView.as_view(), ),
    path('refresh/', TokenRefreshView.as_view(), ),
    path('verify/', TokenVerifyView.as_view(), ),
    path('createcar/', CreateCar.as_view()),
    path('carlist/', CarList.as_view()),
    path('updatecar/<int:id>/', UpdateCar.as_view()),
    path('deletecar/<int:id>/', DeleteCar.as_view()),
    path('carreservation/', CarReservation.as_view()),
    path('carreservationlist/', CarReservationList.as_view()),
    path('updatecarreservation/', UpdateCarReservation.as_view()),
    path('deletecarreservation/', DeleteCarReservation.as_view()),
]
