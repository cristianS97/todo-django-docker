from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('m', 'Masculino'),
        ('f', 'Femenino'),
        ('o', 'Otros')
    )

    email = models.EmailField(verbose_name='Correo', unique=True)
    names = models.CharField(verbose_name='Nombres', max_length=50, blank=True)
    last_name = models.CharField(verbose_name='Apellidos', max_length=50, blank=True)
    gender = models.CharField(verbose_name='Género', max_length=1, choices=GENDER_CHOICES, blank=True)
    image = models.ImageField(verbose_name='Imagen', blank=True, upload_to='static/img/user')
    ocupation = models.CharField(verbose_name='Ocupacion', max_length=30, blank=True)
    birth_date = models.DateField(verbose_name='Fecha de nacimiento', blank=True, null=True)
    is_staff = models.BooleanField(verbose_name='Staff', default=False)
    is_active = models.BooleanField(verbose_name='Activo', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Última actualización')

    # Campo a usar como nombre de usuario
    USERNAME_FIELD = 'email'
    # Campos extra que pedira en la consola
    REQUIRED_FIELDS = ['names']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return f"{self.names} {self.last_name}"
