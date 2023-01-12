import uuid
from django.contrib.gis.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.conf import settings

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email,)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email,  password):
        user = self.create_user(email,  password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# from chat.models import ChatList


class User(AbstractBaseUser, PermissionsMixin):
    """User Model"""


    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserAccountManager()
    def __str__(self):
        return self.email
    
    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "Verify Job Portal Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return


class UserDeviceInfo(models.Model):
    user_ip = models.CharField(max_length=155,null=True,blank=True)
    device_type = models.CharField(max_length=155,null=True,blank=True)