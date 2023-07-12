from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.db import models


class CustomerUserManager(UserManager):
    def create_user(self, phone, last_name=None, email=None, user_type=0, password=None, is_staff=False, is_superuser=False, is_active=True, **extra_fields):
        user = self.model(phone=phone, password=password, is_staff=is_staff, is_superuser=is_superuser,
                          is_active=is_active, user_type=user_type, last_name=last_name, email=email, **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone=None, user_type=None, password=None, **extra_fields):
        return self.create_user(phone=phone, password=password, is_staff=True, is_superuser=True, is_active=True, user_type=user_type,
                                **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=128, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=128, unique=True, blank=True, null=True)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128)

    user_type = models.SmallIntegerField(default=0)

    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = CustomerUserManager()

    USERNAME_FIELD = 'email'


class OTP(models.Model):
    email = models.CharField(max_length=1024)
    key = models.CharField(max_length=512)

    is_conf = models.BooleanField(default=False)
    is_expire = models.BooleanField(default=False)
    tries = models.SmallIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.tries >= 3:
            self.is_expire = True

        super(OTP, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.phone}'
