from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.utils import timezone


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, country, address1, postcode, phone_number, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            country=country,
            address1=address1,
            postcode=postcode,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, country, address1, postcode, phone_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            country=country,
            address1=address1,
            postcode=postcode,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email")
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.CharField(max_length=40, verbose_name='date joined', default=timezone.now)
    last_login = models.DateTimeField(max_length=40, verbose_name='last joined', default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    postcode = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'country', 'address1', 'postcode', 'phone_number']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
