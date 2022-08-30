from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password=None, ):
        """
        Creates and saves a User with the given first_name, last_name, email, username, password1, password2.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            # id=id,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password=None):
        """
        Creates and saves a superuser with the given first_name, last_name, email, username, password1, password2.
        """
        user = self.create_user(
            # id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name='email address', max_length=100, unique=True, )
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=8)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'password', ]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Car(models.Model):
    companyname = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=20)
    fueltype = models.CharField(max_length=50)
    seating_capacity = models.IntegerField()
    rent_per_day = models.IntegerField()
    availability = models.BooleanField(null=True)

    def __str__(self):
        return self.model


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return str(self.customer) + "- " + str(self.car)
