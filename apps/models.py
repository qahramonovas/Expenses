from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db import models
from django.db.models import Model, CharField, EmailField, ForeignKey, CASCADE, ImageField, DecimalField, TextField, \
    DateField, PositiveIntegerField, SET_NULL
from django.db.models.enums import TextChoices
from django.apps import apps


class CustomUserManager(UserManager):

    def _create_user(self, phone_number, email, password, **extra_fields):

        if not phone_number:
            raise ValueError("The given phone_number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, email, password, **extra_fields)

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", 'admin')


        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, email, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    class UserRole(TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    username = None
    full_name = CharField(max_length=255)
    phone_number = CharField(max_length=12, unique=True)
    role = CharField(max_length=55, choices=UserRole.choices, default=UserRole.USER)  # noqa


class Category(Model):
    class Type(TextChoices):
        INCOME = 'income', 'Income'
        EXPENSES = 'expenses', 'Expenses'

    name = CharField(max_length=255, unique=True)
    type = CharField(max_length=55, choices=Type.choices)
    icon = ImageField(upload_to='media/category')


class Expenses(Model):
    class Type(TextChoices):
        INCOME = 'income', 'Income'
        EXPENSES = 'expenses', 'Expenses'

    type = CharField(max_length=55, choices=Type.choices)
    category = ForeignKey('apps.Category', on_delete=CASCADE)
    user = ForeignKey('apps.User', on_delete=CASCADE)
    amount = DecimalField(max_digits=8, decimal_places=2)
    description = TextField()
    created_at = DateField(auto_now_add=True)
