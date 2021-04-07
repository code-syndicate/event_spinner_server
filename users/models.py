from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager )


# Custom User Manager for the user class 
class CustomUserManager( BaseUserManager):

    # creates an ordinary user with no superuser privileges 
    def create_user( self, firstname, lastname, email, password):
        user = self.model( firstname = firstname, lastname = lastname, email = self.normalize_email(email) )
        user.save( using = self._db )
        user.set_password( password )
        return user

    # creates a new user with superuser privileges 
    def create_superuser( self, firstname , lastname, email ,password ):
        user = self.create_user( firstname = firstname, lastname = lastname, email = email, password = password )
        user.is_admin = True
        user.save()
        return user




# The main user model ; custom user model 
class User( AbstractBaseUser):
    firstname = models.CharField( max_length= 25, blank= False )
    lastname = models.CharField( max_length = 25, blank = False)
    email  = models.EmailField( max_length = 255, unique= True , primary_key= True)
    is_active = models.BooleanField( default= True)
    is_admin = models.BooleanField( default = False )
    is_host = models.BooleanField( default = False )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname','password']
    objects = CustomUserManager()


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        if self.is_host:
            return "Host " + self.get_full_name()

        return self.email
    
    @property
    def is_staff( self):
        return self.is_active

    def get_full_name(self):
        return self.firstname + ' ' + self.lastname

    def get_short_name(self):
        return self.firstname

    def has_perm( self, app):
        return True

    def has_module_perms( self, app_label = None):
        return True

    

