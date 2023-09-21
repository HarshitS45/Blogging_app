from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        """Creates and saves a user with the given details"""
        if not email:
            raise ValueError("User must provide an email address")
        if not username:
            raise ValueError("User must provide a username")
        if not first_name:
            raise ValueError("User must provide a firstname")
        if not last_name:
            raise ValueError("User must provide a lastname")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        """Creates and saves a superuser with the given details"""
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password,
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)


class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name='email address', max_length=50, unique=True)
    username        = models.CharField(unique=True, max_length=25)
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return f"Username: {self.username} Email: {self.email}"

    def has_perm(self, perm, obj=None):
        """Checks if the user has any permissions"""
        return self.is_admin

    def has_module_perms(self, app_label):
        """Checks if the user has permission to view the app 'app_label'"""
        return True