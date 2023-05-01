from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from users.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=63, unique=True)
    first_name = models.CharField(max_length=63,  blank=True)
    last_name = models.CharField(max_length=63, blank=True)
    bio = models.CharField(max_length=255,  blank=True)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    subscribed_to = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="subscribers",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
