from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

ROLES = (
    ("HR" , "HR"),
    ("CANDIDATE" , "CANDIDATE" ),
    ("INTERVIEWER" , "INTERVIEWER"),
    ("Admin", "Admin")
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, role='CANDIDATE'):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
                email=self.normalize_email(email)
                )
        user.set_password(password)
        user.name = name
        user.role = role
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """creates and saves a new superuser with given details"""
        user = self.create_user(email,"super user", password)
        user.role = 'Admin'
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255,default='username')
    active = models.BooleanField(default=True)
    role = models.CharField(max_length=255, choices=ROLES, default='CANDIDATE')
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin()

    def is_admin(self):
        return self.role == 'Admin'

class Availablity(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    available_date = models.DateField()
    available_from = models.IntegerField()
    available_to = models.IntegerField()


    def __str__(self):
        return self.user.email