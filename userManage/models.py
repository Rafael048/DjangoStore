from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        
        if not username:
            raise ValueError('El username es obligatorio')
        
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100,unique=True) 
    rol = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    
    objects = CustomUserManager()

    def __str__(self):
        return self.username
# Create your models here.
